import os
from dotenv import load_dotenv
from uuid import uuid4
from apify import Actor
from .constants import *

def env(_opt, _name, _task, _storage, _start=None, _end=None, _gpt=None):
    try:
        load_dotenv()
        global input_name
        global task_count
        global input_start
        global input_end
        global openai_api_key
        global storage_name
        input_name = _name
        # _gpt
        task_count = _task
        storage_name = _storage
        if _opt == AF_CATALOG:
            input_start = _start
            input_end = _end
        if _opt == AF_GOLD_S01:
            openai_api_key = os.environ['OPENAI_API_KEY']
        if _opt == AF_GOLD_S02:
            openai_api_key = os.environ['OPENAI_API_KEY']
            # print(f"[API KEY]\n{os.environ['OPENAI_API_KEY'][:-25]}" + "*" * 25)
    except Exception as err:
        # raise InternalLlmError(err)
        raise

async def check_input(_opt):
    try:
        global input_name
        global input_start
        global input_end
        global task_count
        global openai_api_key
        actor_input = await Actor.get_input()
        cmd = actor_input.get(AF_CMD)
        if cmd == AF_CMD_INPUT:
            input_name = actor_input.get('name')
            task_count = actor_input.get('task')
            if _opt == AF_CATALOG:
                input_start = actor_input.get('start')
                input_end = actor_input.get('end')
            if _opt == AF_GOLD_S01:
                openai_api_key = actor_input.get('openai-api')
                # print(f"[API KEY]\n{os.environ['OPENAI_API_KEY'][:-25]}" + "*" * 25)
            if _opt == AF_GOLD_S02:
                openai_api_key = actor_input.get('openai-api')
            return True
        elif cmd == AF_CMD_UPDATE:
            if _opt == AF_CATALOG:
                scraperdata = actor_input.get('scraper')
                kv_store = await Actor.open_key_value_store(name=SX_KV_CONFIG)
                await kv_store.set_value(f'{SX_SCRAPER}{SX_EXT_YAML}', scraperdata)
            return False
    except Exception as err:
        # raise InternalLlmError(err)
        raise