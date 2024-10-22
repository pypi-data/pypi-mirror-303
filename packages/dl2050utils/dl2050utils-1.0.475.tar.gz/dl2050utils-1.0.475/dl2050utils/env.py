from pathlib import Path
from dotenv import load_dotenv
import yaml

# ################################################################################
# config_load
# ################################################################################

def find_yml(name):
    ps = [Path(f'./{name}'), Path(f'/run/secrets/{name}')]
    for p in ps:
        if p.exists(): return p
    return None

def config_load(name=None):
    """
        Load config yml file.
        File name is f'config-{name}.yml', or config.yml by default.
        Checks for file first in the current folder then in /run/secrets folder.
    """
    load_dotenv()
    name = 'config.yml' if name is None else f'config-{name}.yml'
    fname = find_yml(name)
    if fname is None:
        raise RuntimeError('Unable to find config file')
    with open(str(fname),'r') as f:
        try:
            cfg = yaml.safe_load(f)
        except yaml.YAMLError as err:
            raise RuntimeError(f'Unable to load config file: {str(err)}')
    return cfg
