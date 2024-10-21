import hashlib
import yaml
from apify import Actor
from .constants import *
from .utils import elapsed, prompt_template_yaml

# -----------------------------------------------------------------------------------
# - version: 1
#   name: 'bts'
#   fix: ''
#   query: '방탄소년단 | bts'
#   prompt: |
#     bts
#   keywords:
#     - '방탄소년단'
#     - 'bts'
# -----------------------------------------------------------------------------------
# opt 종류
QUERY = 'query'
FIX = 'fix'
PROMPT = 'prompt'
KEYWORDS = 'keywords'
def get(_name, _opt):
    datadict = prompt_template_yaml(SX_SCRAPER)
    for entry in datadict:
        if entry.get('name') == _name:
            if _opt == FIX:
                return fix_query(entry[QUERY])
            return entry[_opt]
    return None

# 'Hello | World + 한글 - "Test"'
def fix_query(_naver_query):
    hash_bytes = hashlib.sha256(_naver_query.encode()).digest()
    out =  bytes(a ^ b ^ c ^ d for a, b, c, d in zip(hash_bytes[:8], hash_bytes[8:16], hash_bytes[16:24], hash_bytes[24:]))
    return out.hex()

async def getkv(_name, _opt):
    kv_store = await Actor.open_key_value_store(name=SX_KV_CONFIG)
    begintrx = await kv_store.get_value(f'{SX_SCRAPER}{SX_EXT_YAML}') or None
    if not begintrx:
        return get(_name, _opt)
    datadict = yaml.load(begintrx, Loader=yaml.FullLoader)
    for entry in datadict:
        if entry.get('name') == _name:
            if _opt == FIX:
                return fix_query(entry[QUERY])
            return entry[_opt]
    return None
