import asyncio
import shutil
import math
from pathlib import Path
import subprocess
from py7zr import unpack_7zarchive
import orjson
import pickle
import numpy as np
import pandas as pd
import requests
import aiofiles
import io
from tqdm.notebook import tqdm
from dl2050utils.core import oget, listify, xre

Path.ls = lambda x: list(x.iterdir())

# ################################################################################
# pickle_save (pickle_dump), pickle_load
# np_save, np_load, np_load_async
# df_save, df_load
# json_load (json_parse), json_dump, read_json
# json_saves, json_loads
# ################################################################################

def pickle_save(p, d):
    p = Path(p)
    p = p.with_suffix('.pickle')
    try:
        with open(p, 'wb') as f:
            pickle.dump(d, f)
        return 0
    except Exception as exc:
        print(str(exc))
        return 1

# Deprecated
def pickle_dump(p, d): return pickle_save(p, d)
    
def pickle_load(p):
    p = Path(p)
    p = p.with_suffix('.pickle')
    if not p.is_file():
        return None
    try:
        with open(p, 'rb') as f:
            d = pickle.load(f)
        return d
    except Exception as exc:
        print(str(exc))
        return 1
    
def np_save(p, d, allow_pickle=True):
    p = Path(p)
    p = p.with_suffix('.npy')
    try:
        np.save(p, d, allow_pickle=allow_pickle)
        return 0
    except Exception as exc:
        print(str(exc))
        return 1
    
def np_load(p, allow_pickle=True):
    p = Path(p)
    p = p.with_suffix('.npy')
    if not p.is_file():
        return None
    try:
        if allow_pickle:
            d = np.load(p, allow_pickle=allow_pickle)
            if d is None: return None
            return d.item()
        else:
            return np.load(p)
    except Exception as exc:
        print(str(exc))
        return 1
    
async def np_load_async(p, allow_pickle=False):
    p = Path(p)
    p = p.with_suffix('.npy')
    if not p.is_file():
        return None
    try:
        async with aiofiles.open(p, mode='rb') as f:
            buffer = await f.read()
        f = io.BytesIO(buffer)
        if allow_pickle:
            d = np.load(f, allow_pickle=allow_pickle)
            if d is None: return None
            return d.item()
        else:
            return np.load(f, allow_pickle=allow_pickle)
    except Exception:
        return None
    
def df_save(p, df):
    p = Path(p)
    p = p.with_suffix('.feather')
    try:
        df.to_feather(p)
        return 0
    except Exception:
        return 1
    
def df_load(p):
    p = Path(p)
    p = p.with_suffix('.feather')
    if not p.is_file():
        return None
    try:
        df = pd.read_feather(p)
        return df
    except Exception:
        return None

def json_save(p, d):
    p = Path(p).with_suffix('.json')
    try:
        with open(p, 'wb') as f:
            f.write(orjson.dumps(d, option=orjson.OPT_NON_STR_KEYS))
        return 0
    except Exception as exc:
        print(f'json_save: file={p}, Exception: {exc}')
        return 1
    
def json_load(p):
    p = Path(p).with_suffix('.json')
    if not p.is_file():
        print(f'json_load: file {p} not found')
        return None
    try:
        with open(p, 'rb') as f:
            return orjson.loads(f.read())
    except Exception as exc:
        print(f'json_load: file={p}, Exception: {exc}')
        return None

def json_dumps(o):
    if o is None: return None
    try:
        return orjson.dumps(o, option=orjson.OPT_SERIALIZE_NUMPY).decode()
    except:
        return None

def json_loads(s):
    if s is None or s=='': return None
    try:
        o = orjson.loads(s)
        if o=={}: return None
        return o
    except:
        return None

# To be reviwed (used in PW) and renamed to json_load
def read_json(p): return json_load(p)

# ################################################################################
# Shell commands: cp, rm, sh_run, run_asyc
# ################################################################################

def cp(p1, p2):
    """Copies p1 to p2 with overwrite. If p1 is a directory, copies recursively."""
    p1,p2 = Path(p1),Path(p2)
    if not p1.exists():
        print(f'File {p1} not found')
        return 1
    try:
        if p1.is_file():
            shutil.copyfile(p1, p2)
            return 0
        if p2.is_dir():
            shutil.rmtree(p2)
        shutil.copytree(p1, p2)
    except Exception:
        return 1
    
def rm(p):
    " Removes file or directory p. If p is a directory, removes recursively. "
    try: 
        p = Path(p)
        if p.is_file():
            p.unlink()
            return 0
        if p.is_dir():
            return shutil.rmtree(p)
    except Exception:
        return 1

def sh_run(cmd):
    """ Executas a shell command and return a tuple with exit code and stdout. """
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdout, stderr) = proc.communicate()
    stdout, stderr = stdout.decode("utf-8"), stderr.decode("utf-8")
    if proc.returncode!=0: raise RuntimeError(f'sh_run command \n{cmd}\n exit with error code {proc.returncode}:\n{stderr}')
    return (proc.returncode, stdout)

async def run_asyc(*args):
    try:
        process = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return process.returncode, stdout.decode(), stderr.decode()
    except:
        return -1, '', 'Command not found'
    
# ################################################################################
# get_all_files, split_files_into_subfolders, get_dir_files, get_dir_dirs
# ################################################################################

def get_all_files(p, filetypes=None):
    p = Path(p)
    filetypes = [e.lower() for e in listify(filetypes)]
    filetypes = [f'.{e}' if e[0]!='.' else e for e in filetypes]
    files = [p1 for p1 in p.rglob('*')]
    files = [e for e in files if xre('(DS_Store)',str(e)) is None and xre('(__MACOSX)',str(e)) is None]
    if len(filetypes): files = [f for f in files if f.suffix.lower() in filetypes]
    return files

def split_files_into_subfolders(p, suffix=None, n=1000):
    """
    Splits the files in a folder into subfolders with n files each
    """
    p0 = Path(p)
    print('Collecting all files')
    ps = get_all_files('/nas/kardio/exams/ecgs/con/json', suffix)
    print(f'Found {len(ps)} files')
    n = math.ceil(len(ps)/1000)
    for k in tqdm(range(n)):
        (p0/f'{k}').mkdir(parents=True, exist_ok=True, mode=0o755)
        for i in range(k*1000,max((k+1)*1000,len(ps))):
            p1 = ps[i]
            p2 = p0/f'{k}'/p1.name
            _ = p1.rename(p2)

# Draft
def get_dir_files(path, types=None):
    return [f for f in path.glob('**/*') if f.is_file() and (types==None or f.suffix[1:] in types)]

# Draft
def get_dir_dirs(path):
    return [d for d in path.glob('**/*') if d.is_dir()]
    
# ###################################################################################
# zip_get_registered_formats, zip_register_formats, iszip, dozip, unzip, unzip_tree
# ###################################################################################

def zip_get_registered_formats():
    return sum([e[1] for e in shutil.get_unpack_formats()], [])
    
def zip_register_formats():
    zips = zip_get_registered_formats()
    if '.7z' not in zips and '.hsz' not in zips:
        print('Registering [.7z,.hsz]')
        shutil.register_unpack_format('7zip', ['.7z','.hsz'], unpack_7zarchive)

def dozip(p, remove=False):
    p = Path(p)
    if not p.exists():
        print(f'dozip: file not found: {p}')
        return 1
    try: 
        shutil.make_archive(p, 'zip', p)
        if remove:
            if rm(p): return 1
        return 0
    except Exception:
        return 1
    
def iszip(p):
    zipext = zip_get_registered_formats()
    archext = ['.rar']
    return (Path(p)).suffix in zipext+archext
    
def unzip(p, remove=False):
    """ Unzip or untar a file. If it is not an archive does nothing. """
    p = Path(p)
    if not p.exists():
        print(f'unzip: file not found: {p}')
        return 1
    if p.is_dir():
        return 0
    if not iszip(p):
        return 0
    if p.suffix in ['.rar']:
        code,stdout = sh_run(f'unrar x {p} {p.parent}')
        if code!=0:
            print(f'unrar error: {stdout}')
            return 1
        if remove:
            if rm(p): return 1
        print(f'File {p} extracted from archive')
        return 0
    p_dir = p.with_suffix('')
    try: 
        shutil.unpack_archive(p, p_dir)
        if remove:
            if rm(p): return 1
        return 0
    except Exception as exc:
        print(f'Exception: {exc}')
        return 1
    
def unzip_tree(p):
    """ Get all subfolders and files from and unzip/untar if needed. """
    for p1 in [p1 for p1 in get_all_files(p)]:
        if unzip(p1, remove=True):
            print(f'unzip_tree: error unzipping {p1}')

# ##############################################################################################################
# upload_file, download_file
# ##############################################################################################################

def upload_file(url, p):
    """
    Uploads a file to the given pre-signed URL.
    Args:
        url (str): The pre-signed URL for the upload.
        p (str): The local path to the file to be uploaded.
    Returns 0 if upload is successful, 1 otherwise.
    """
    headers = {'Content-Type': 'application/octet-stream'}
    try:
        with open(p, 'rb') as f:
            res = requests.put(url, data=f, headers=headers)
            if res.status_code == 200: return 0
            print(f'upload_file ERROR: {res.status_code}:{res.text}')
            return 1
    except Exception as exc:
        print(f'upload_file EXCEPTION: {exc}')
        return 1
    
def download_file(url, p):
    """
    Downloads a file to the given pre-signed URL.
    Args:
        url (str): The pre-signed URL for the upload.
        p (str): The local path to the file to be uploaded.
    Returns 0 if upload is successful, 1 otherwise.
    """
    headers = {'Content-Type': 'application/octet-stream'}
    try:
        res = requests.get(url, headers=headers)
        if res.status_code==200:
            with open(p, 'wb') as f:
                f.write(res.content)
            return 0
        print(f'download_file ERROR: {res.status_code}:{res.text}')
        return 1
    except Exception as exc:
        print(f'download_file EXCEPTION: {exc}')
        return 1
