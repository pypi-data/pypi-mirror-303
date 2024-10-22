# ####################################################################################################
# api.py
#
# APIServer, APIWorker, APISyncWorker
#
# This version assumes that input data (payloads) and output data (responses) are very short.
# Large inputs/outputs must be implemented with urls pointing to payloads/results. The runner callback must
# download the inputs from a payload url, upload the results and return the result url.
#
# Both API Server and Worker Server requires configuration defined by the cfg dict of this form:
# cfg = {
#   'apiserver': {'servive':<service>, 'wkey':<wkey>}
#   'gcloud': {'gs_key':<gs_key_struct>}}
#   }
# If cfg is passed as argument it is used, otherwise cfg is loaded from the yaml file (secret)
# trough config_load(<service>).
#
# Responses are allwways JSON, both for GET/POST of the form {status_code:<int>, message:<str>, result:<dict>}
#
# Example APIServer:
#   apis = APIServer('kardio')
#   api.run()
#
# Example APIWorker:
#   def proc(task, start_cb, done_cb, error_cb):
#       eta = 3
#       start_cb(task['req_uid'], eta)
#       time.sleep(eta)
#       done_cb(task['req_uid'], {'ml':42}, used_credits=1.)
#       return 0
#   ws = APIWorker('kardio', url='http://ju:9000')
#   ws.run(proc)
#
# Example APIClient:
#   api_cli = APIClient(key=key, url='http://ju:9000')
#   res = api_cli.req({'url':'www.xxx.com'})
#   req_uid = res['result']['req_uid']
#   api_cli.check(req_uid)
#
# ####################################################################################################
import sys
import time
import datetime
import secrets
import string
from pathlib import Path
import json
import sqlite3
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from dl2050utils.core import oget, now, date_to_srt, str_to_date, is_numeric_str, get_uid
from dl2050utils.env import config_load
from dl2050utils.log import AppLog
from dl2050utils.fs import json_dumps, json_loads
from dl2050utils.sqlite import Sqlite
from dl2050utils.restutils import sync_request
from dl2050utils.gs import GS

TASK_STATUS = ['REQUESTED', 'DISPATCHED', 'START', 'DONE', 'ERROR']

# ####################################################################################################
# REST
# ####################################################################################################

def raise_error(status_code=500, msg='', LOG=None):
    """Generic function to raise HTTPException and optionally log the error (used in the API)"""
    if LOG is not None: LOG(4, 0, label='HTTPException', msg=msg)
    raise HTTPException(status_code=status_code, detail=msg)

def rest_ok(result=None, message=''):
    return JSONResponse(status_code=200, content={'status':200, 'message':message, 'result':result})

async def http_exception(request, exc):
    return JSONResponse(status_code=exc.status_code,
                        content={'status':exc.status_code, 'message': exc.detail or "HTTP error"})
    # 'error_code': exc.__class__.__name__

async def server_error_exception(request, exc):
    return JSONResponse(status_code=500, content={'status': 500, 'message': "Internal server error",})

def get_param(request, param_name, param_type, max_length=None, required=True, data=None, LOG=None):
    """Get and sanitize param, from query_params for GET or from json data for POST requests"""
    param = request.query_params.get(param_name) if request.method=='GET' else oget(data,[param_name])
    if required and param is None:
        raise_error(400, f'Missing required param {param_name} on {request.url.path}', LOG)
    if param_type==str:
        if max_length and len(param)>max_length:
            raise_error(400, f'Invalid param {param_name} on {request.url.path}', LOG)
        return param.strip()
    elif param_type==int or param_type==float:
        if type(param)==int or type(param)==float: return param_type(param)
        if type(param)==str and is_numeric_str(param): return param_type(param)
        raise_error(400, f'Invalid number format for param {param_name} on {request.url.path}', LOG)
    elif param_type==dict or param_type==bytes:
        if max_length is not None and sys.getsizeof(param)>max_length:
            raise_error(400, f'Invalid param {param_name} on {request.url.path}', LOG)
        return param
    raise_error(400, f'Invalid param type: {param_name} on {request.url.path}', LOG)

# ####################################################################################################
# Utility functions
# ####################################################################################################

def db_create(db):
    Q1 = '''
        CREATE TABLE IF NOT EXISTS api_keys (
            key CHAR(256) PRIMARY KEY,
            email VARCHAR(128),
            name VARCHAR(128),
            created_at DATETIME,
            reset_calls_at DATETIME,
            active BOOLEAN,
            rate_limit INTEGER,
            calls INTEGER DEFAULT 0,
            calls_total INTEGER DEFAULT 0,
            credits REAL DEFAULT 0 -- current credits total
        )
    '''
    Q2 = '''
        CREATE TABLE IF NOT EXISTS api_tasks (
            req_uid CHAR(32) PRIMARY KEY,
            created_at DATETIME,
            key CHAR(256),
            status CHAR(32),
            payload TEXT,
            result TEXT,
            eta DATETIME,
            credits REAL DEFAULT 0 -- credits used by task
        );
    '''
    db.execute(Q1)
    db.execute(Q2)

def get_new_key(n=256): return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(n))
def get_reset_time(): return date_to_srt(now()+datetime.timedelta(hours=1))

# ####################################################################################################
# Transactions
# ####################################################################################################

def grab_task(db):
    """Gets the oldest task with status REQUESTED and updates the status to PROCESSING with atomiticity"""
    tbl = 'api_tasks'
    d = None
    try:
        # Begin a transaction to lock the row and ensure atomicity
        db.conn.execute('BEGIN IMMEDIATE')
        cursor = db.conn.cursor()
        Q = f"SELECT * FROM {tbl} WHERE status == 'REQUESTED' ORDER BY req_uid LIMIT 1"
        cursor.execute(Q)
        task = cursor.fetchone()
        if not task:
            db.conn.rollback()
            return None
        # Fetch the column names and convert the row to a dictionary
        column_names = [description[0] for description in cursor.description]
        d = dict(zip(column_names, task))
        cursor.execute(f"UPDATE {tbl} SET status = ? WHERE req_uid = ?", ('PROCESSING', d['req_uid']))
        db.conn.commit()
        return d
    except sqlite3.DatabaseError as exc:
        print(f'grab_task EXCEPTION: {exc}')
        db.conn.rollback()
    
def update_credits(db, key, value):
    """DB transaction to update key credits value"""
    try:
        db.conn.execute('BEGIN IMMEDIATE')
        cursor = db.conn.cursor()
        cursor.execute("""UPDATE api_keys SET credits = credits + ? WHERE key = ?""", (value, key))
        db.conn.commit()
    except Exception as exc:
        print(f'update_credits EXCEPTION: {exc}')
        db.conn.rollback()
        raise exc

# ####################################################################################################
# APIServer
# ####################################################################################################

class APIServer:
    def __init__(self, service, sync_worker_url=None, cfg=None):
        if service is None: raise Exception('service must be defined')
        if cfg is None: cfg = config_load('kardio')
        p0 = Path(f'/data/{service}/apiserver')
        (p0/'workfiles').mkdir(parents=True, exist_ok=True)
        self.db = Sqlite(p0/'/api-db')
        self.skey,self.wkey = oget(cfg,['apiserver','skey']),oget(cfg,['apiserver','wkey'])
        if self.wkey is None: raise Exception('Worker key not defined')
        self.fs = GS(service) if oget(cfg,['gcloud','gs_key']) is not None else None
        self.sync_worker_url = sync_worker_url
        self.port = 9000
        self.LOG = AppLog(cfg, service=f'{service}-apis')
        self.LOG(2, 0, label='READY')
    
    # ####################################################################################################
    # Admin
    # ####################################################################################################

    def new_key(self, email, rate_limit=100):
        key = get_new_key()
        self.add_key(key, email, rate_limit=rate_limit)
        return key
    def add_key(self, key, email, rate_limit=100):
        self.db.insert('api_keys',{'key':key, 'email':email, 'active':True, 'rate_limit':rate_limit,
                                   'reset_calls_at':get_reset_time()})
    def revoke_key(self, key): return self.select_and_update('api_keys', 'key', {'key':key, 'active':False})
    def get_key(self, key): return self.db.select_one('api_keys', 'key', key)
    def get_keys(self): return self.db.select('api_keys')
    def get_tasks(self): return self.db.select('api_tasks')
    def get_task(self, req_uid): return self.db.select_one('api_tasks', 'req_uid', req_uid)
    def remove_all_tasks(self): self.db.delete_all('api_tasks')
    def add_credits(self, key, value): update_credits(self.db, key, value)
    def remove_credits(self, key, value): update_credits(self.db, key, -value)
    def db_create(self): db_create(self.db)
    
    # ####################################################################################################
    # Access control
    # ####################################################################################################

    def check_access(self, key, enforce_credits=True):
        """Enforces valid client key for access. Returns 0 is access is granted, raises HTTP error otherwise."""
        # Service key skey has inconditional access
        if key==self.skey: return 0
        # Check key existance and status
        d = self.db.select_one('api_keys', 'key', key)
        if d is None: raise_error(403, 'Invalid API key', self.LOG)
        if d['active']==0: raise_error(403, 'Inactive API key', self.LOG)
        # Check rate limits and credits
        if d['calls'] > d['rate_limit']: raise_error(403, 'Rate limit exceded', self.LOG)
        if enforce_credits and d['credits'] < 0: raise_error(403, 'Out of credits', self.LOG)
        # Update statistics and time window limit
        for c in ['calls','calls_total']: d[c] += 1
        ts1,ts2 = now(),str_to_date(d['reset_calls_at'])
        if ts1 > ts2: d['calls'],d['reset_calls_at'] = 0,ts2+datetime.timedelta(hours=1)
        self.db.update( 'api_keys', 'key', d)
        return 0
    
    def check_worker_access(self, key):
        """Enforces valid worker key for access."""
        if len(key)>256: raise_error(400, 'Invalid Worker key', self.LOG)
        if key!=self.wkey: raise_error(403, 'Unauthorized Worker key', self.LOG)
    
    def reset_rate_limit(self, key):
        ts = now()+datetime.timedelta(hours=1)
        return self.db.select_and_update('api_keys', 'key', {'key':key, 'calls':0, 'reset_calls_at':ts})
    
    # ####################################################################################################
    # API Entrypoints
    # ####################################################################################################
    
    async def req(self, request):
        """Request for async proc. payload only has blob url."""
        data = await request.json()
        key = get_param(request, 'key', str, max_length=256, data=data, LOG=self.LOG) # POST
        payload = get_param(request, 'payload', dict, max_length=256, data=data, LOG=self.LOG)
        self.check_access(key)
        req_uid = get_uid()
        task = {'req_uid':req_uid, 'created_at':now(), 'key':key, 'status':'REQUESTED', 'payload':json_dumps(payload)}
        self.db.insert('api_tasks', task)
        self.LOG(2, 0, label='API', label2='/apiserver/req', msg=f"req_uid={req_uid}")
        return rest_ok(result={'req_uid':req_uid})
    
    async def check(self, request):
        """Check async proc. response only has respose url. GET request."""
        key = get_param(request, 'key', str, max_length=256, LOG=self.LOG)
        req_uid = get_param(request, 'req_uid', str, max_length=32, LOG=self.LOG)
        self.check_access(key, enforce_credits=False)
        task = self.db.select_one('api_tasks', 'req_uid', req_uid)
        if task is None: raise_error(400, 'Request not found', self.LOG)
        res = {'status':task['status']}
        if res['status']!='DONE':
            res['eta'] = task['eta']
        else:
            res['result'],res['credits'] = json_loads(task['result']),task['credits']
        return rest_ok(result=res)
    
    async def get_upload_url(self, request):
        """Provides signed url for upload link to be used in req. GET request."""
        key = get_param(request, 'key', str, max_length=256, LOG=self.LOG)
        self.check_access(key)
        if self.fs is None: raise_error(400, 'Upload links not available', self.LOG)
        bucket = 'kardio'
        fname = f'EXT-{get_uid()}'
        upload_url,download_url = self.fs.urls(bucket, fname)
        return rest_ok(result={'upload_url':upload_url, 'download_url':download_url})
    
    async def proc(self, request):
        """Request for sync proc. payload has data blob and response all the proc output."""
        if self.sync_worker_url is None: raise_error(400, 'Sync Worker not found', self.LOG)
        data = await request.json()
        key = get_param(request, 'key', str, max_length=256, data=data, LOG=self.LOG)
        payload = get_param(request, 'payload', bytes, max_length=8192, data=data, LOG=self.LOG)
        self.check_access(key)
        # Call sync worker
        payload2 = {'key':self.wkey, 'payload':payload}
        result = sync_request(f'{self.sync_worker_url}/proc', method='POST', payload=payload2, LOG=self.LOG)
        self.LOG(2, 0, label='API', label2='/apiserver/proc', msg=f"")
        return rest_ok(result=result)
    
    # ####################################################################################################
    # Worker Entrypoints
    # ####################################################################################################
    
    async def grab(self, request):
        data = await request.json()
        key = get_param(request, 'key', str, max_length=256, data=data, LOG=self.LOG)
        self.check_worker_access(key)
        task = grab_task(self.db)
        if task is not None: self.db.select_and_update('api_tasks', 'req_uid',{'req_uid':task['req_uid'], 'status':'DISPATCHED'})
        if task is not None: self.LOG(2, 0, label='API', label2='/worker/grab', msg=f"req_uid={task['req_uid']}")
        return rest_ok(result=task)

    async def start(self, request):
        data = await request.json()
        key = get_param(request, 'key', str, max_length=256, data=data, LOG=self.LOG)
        req_uid = get_param(request, 'req_uid', str, max_length=32, data=data, LOG=self.LOG)
        eta = get_param(request, 'eta', int, data=data, LOG=self.LOG)
        self.check_worker_access(key)
        self.db.select_and_update('api_tasks', 'req_uid', {'req_uid':req_uid, 'status':'START', 'eta':eta})
        return rest_ok()

    async def done(self, request):
        data = await request.json()
        key = get_param(request, 'key', str, max_length=256, data=data, LOG=self.LOG)
        req_uid = get_param(request, 'req_uid', str, max_length=32, data=data, LOG=self.LOG)
        result = json_dumps(get_param(request, 'result', dict, data=data, LOG=self.LOG))
        used_credits = get_param(request, 'credits', float, data=data, LOG=self.LOG)
        self.check_worker_access(key)
        self.db.select_and_update('api_tasks', 'req_uid',
            {'req_uid':req_uid, 'status':'DONE', 'result':result, 'credits':used_credits, 'eta':None})
        task = self.get_task(req_uid)
        self.remove_credits(task['key'], used_credits)
        return rest_ok()

    async def error(self, request):
        data = await request.json()
        key = get_param(request, 'key', str, max_length=256, data=data, LOG=self.LOG)
        req_uid = get_param(request, 'req_uid', str, max_length=32, LOG=self.LOG)
        self.check_worker_access(key)
        self.db.select_and_update('api_tasks', 'req_uid', {'req_uid':req_uid, 'status':'ERROR', 'eta':None})
        return rest_ok()

    # ####################################################################################################
    # Run
    # ####################################################################################################
    
    def run(self, port=None):
        port = port or self.port
        self.LOG(2, 0, label='RUN', msg=f'Listening in port {port}')
        routes = [
            # Client async routes
            Route('/apiserver/req', endpoint=self.req, methods=['POST']),
            Route('/apiserver/check', endpoint=self.check, methods=['GET']),
            Route('/apiserver/get_upload_url', endpoint=self.get_upload_url, methods=['GET']),
            # Client sync routes
            Route('/apiserver/proc', endpoint=self.proc, methods=['POST']),
            # Worker routes
            Route('/worker/grab', endpoint=self.grab, methods=['POST']),
            Route('/worker/start', endpoint=self.start, methods=['POST']),
            Route('/worker/done', endpoint=self.done, methods=['POST']),
            Route('/worker/error', endpoint=self.error, methods=['POST']),
        ]
        exception_handlers = {
            HTTPException: http_exception,
            Exception: server_error_exception,
        }
        app = Starlette(
            debug=True,
            routes=routes,
            exception_handlers=exception_handlers,
            # middleware=self.middleware,
        )
        uvicorn.run(app, port=port, host='0.0.0.0', log_level='critical')

# ####################################################################################################
# APIClient
# ####################################################################################################

class APIClient:
    def __init__(self, key, url):
        self.key,self.url = key,url
    def do_request(self, route, payload):
        method = 'GET' if route in ['/apiserver/check','/apiserver/get_upload_url'] else 'POST'
        print(route)
        return sync_request(f'{self.url}{route}', method=method, payload=payload)
    def check(self, req_uid):
        return self.do_request('/apiserver/check', {'key':self.key, 'req_uid':req_uid})
    def req(self, payload):
        return self.do_request('/apiserver/req',  {'key':self.key, 'payload':payload})
    def get_upload_url(self):
        return self.do_request('/apiserver/get_upload_url',  {'key':self.key})
    def proc(self, payload):
        return self.do_request('/apiserver/proc',  {'key':self.key, 'payload':payload})

# ####################################################################################################
# class APIWorker:
# ####################################################################################################

class APIWorker:

    def __init__(self, service, cfg=None, api_server_url=None):
        if service is None: raise Exception('service must be defined')
        if cfg is None: cfg = config_load('kardio')
        self.wkey = oget(cfg,['apiserver','wkey'])
        if self.wkey is None: raise Exception('worker key not defined')
        self.api_server_url = api_server_url or 'http://localhost:9000'
        self.LOG = AppLog(cfg, service=f'{service}-apiw')
        self.LOG(2, 0, label='READY', label2='START', msg=f'API Server at {self.api_server_url}')

    def request(self, path, payload):
        res = sync_request(f'{self.api_server_url}/{path}', method='POST', payload=payload, LOG=self.LOG)
        if oget(res,['status']!=200):
            self.LOG(4, 0, label='APIWorker', label2=path)
            return None
        return res

    def grab(self):
        res = self.request('worker/grab', {'key':self.wkey})
        return oget(res,['result'])

    def start_cb(self, req_uid, eta=None):
        return self.request('worker/start', {'key':self.wkey, 'req_uid':req_uid, 'eta':eta})

    def done_cb(self, req_uid, result, used_credits=0.):
        return self.request('worker/done', {'key':self.wkey, 'req_uid':req_uid, 'result':result, 'credits':used_credits})

    def error_cb(self, req_uid):
        return self.request('worker/error', {'key':self.wkey, 'req_uid':req_uid})
    
    def run(self, cb):
        self.LOG(2, 0, label='RUN', msg=f'Fetching tasks from {self.api_server_url}')
        try:
            while True:
                task = self.grab()
                if task is None:
                    time.sleep(1)
                    continue
                try:
                    req_uid = task['req_uid']
                    if not cb(task, self.start_cb, self.done_cb, self.error_cb):
                        self.LOG(2, 0, label='APIWorker', label2='DONE', msg=f"{req_uid}")
                    else:
                        self.LOG(3, 0, label='APIWorker', label2='ABORTED', msg=f"{req_uid}")
                except Exception as exc:
                    self.error_cb(req_uid)
                    self.LOG(4, 0, label='APIWorker', label2='Callback EXCEPTION', msg=f"{req_uid}, exc={exc}")
        except KeyboardInterrupt:
            self.LOG(2, 0, label='APIWorker', label2='SHUTDOWN')
        except Exception as exc:
            self.error_cb(req_uid)
            self.LOG(4, 0, label='APIWorker', label2='Server EXCEPTION', msg=f'exc={exc}')

# ####################################################################################################
# APISyncWorker
# ####################################################################################################

class APISyncWorker:

    def __init__(self, service, cb, cfg=None):
        if service is None: raise Exception('service must be defined')
        if cfg is None: cfg = config_load('kardio')
        self.wkey = oget(cfg,['apiserver','wkey'])
        if self.wkey is None: raise Exception('worker key not defined')
        self.cb = cb
        self.port = 9500
        self.LOG = AppLog(cfg, service=f'{service}-apiws')
        self.LOG(2, 0, label='READY', label2='START')

    def check_worker_access(self, key):
        """Enforces valid worker key for access."""
        if len(key)>256: raise_error(400, 'Invalid Worker key', self.LOG)
        if key!=self.wkey: raise_error(403, 'Unauthorized Worker key', self.LOG)

    async def proc(self, request):
        data = await request.json()
        key = get_param(request, 'key', str, max_length=256, data=data, LOG=self.LOG)
        payload = get_param(request, 'payload', dict, max_length=8192, data=data, LOG=self.LOG)
        self.check_worker_access(key)
        result = self.cb(payload)
        self.LOG(2, 0, label='APISyncWorker', label2='/apiserver/proc')
        return rest_ok(result)

    def run(self, port=None):
        port = port or self.port
        self.LOG(2, 0, label='RUN', msg=f'Listening in port {port}')
        routes = [
            Route('/proc', endpoint=self.proc, methods=['POST']),
        ]
        exception_handlers = {
            HTTPException: http_exception,
            Exception: server_error_exception,
        }
        app = Starlette(
            debug=True,
            routes=routes,
            exception_handlers=exception_handlers,
            # middleware=self.middleware,
        )
        uvicorn.run(app, port=port, host='0.0.0.0', log_level='critical')
