from datetime import datetime 
from operator import itemgetter
from itertools import groupby
from apify import Actor
from .constants import *

# -----------------------------------------------------------------------------------------------------------------
# job_list() 보다 먼저 수행됨
async def diff_stage(_pathm, _opt: str):
    option_map = {
        AF_BRONZE: (AF_BRONZE, AF_CATALOG),
        AF_SILVER: (AF_SILVER, AF_BRONZE),
        AF_GOLD_S01: (AF_GOLD_S01, AF_SILVER),
        AF_GOLD_S02: (AF_GOLD_S02, AF_GOLD_S01),
        AF_MART_S01: (AF_MART_S01, AF_GOLD_S02)
    }
    if _opt not in option_map:
        raise ValueError(f'Invalid option provided: {_opt}')
    idx_a, idx_b = option_map[_opt]
    async def load_res(_index):
        trx, kv_store = await kv_get_index(_pathm, _index)
        return await _kv_complete_pair(_pathm, trx, kv_store, _index)
    res_a = await load_res(idx_a)
    res_b = await load_res(idx_b)
    partial, job, complete = _compare_index(res_b, res_a)
    # print(f'partial:{partial} / job:{job} / complete:{complete}')
    # return partial, job, complete
    return partial, job

# -----------------------------------------------------------------------------------------------------------------
# _resume_month 이후의 값을 이전단계에서 아래와 같은형식으로 가져옴
# [ {
#     'job': '2024-10',
#     'complete': True / False
#   } ... ]
async def job_list(_pathm, _resume_month, _opt: str):
    option_map = {
        AF_BRONZE: AF_CATALOG,
        AF_SILVER: AF_BRONZE,
        AF_GOLD_S01: AF_SILVER,
        AF_GOLD_S02: AF_GOLD_S01,
        AF_MART_S01: AF_GOLD_S02
    }
    target_index = option_map.get(_opt)
    if not target_index:
        raise ValueError(f'Invalid option provided: {_opt}')
    trx, kv_store = await kv_get_index(_pathm, target_index)
    res_item = await _kv_complete_pair(_pathm, trx, kv_store, target_index)
    result = [job_item for job_item in res_item if job_item['job'] >= _resume_month]
    return result

# -----------------------------------------------------------------------------------------------------------------
# kv index 의 내용을 업데이트 함
async def do_index(_pathm, _kv_store, _month, _opt: str):
    index_map = {
        AF_CATALOG: _pathm.query_catalog_index,
        AF_BRONZE: _pathm.query_bronze_index,
        AF_SILVER: _pathm.query_silver_index,
        AF_GOLD_S01: _pathm.query_gold01_index,
        AF_GOLD_S02: _pathm.query_gold02_index,
        AF_MART_S01: _pathm.query_mart01_index
    }
    query_func = index_map.get(_opt)
    if not query_func:
        raise ValueError(f'Invalid option provided: {_opt}')
    _name = query_func()
    begintrx = await _kv_store.get_value(_name) or None
    if not begintrx:
        raise ValueError(f'do_index error')
    _add_or_update_job(begintrx, _month)
    await _kv_store.set_value(_name, begintrx)

# -----------------------------------------------------------------------------------------------------------------
# kv 에 완료file 생성
async def do_complete(_pathm, _month, _opt: str):
    option_map = {
        AF_CATALOG: (_pathm.kv_catalog, _pathm.query_catalog_yearmonth),
        AF_BRONZE: (_pathm.kv_bronze, _pathm.query_bronze_yearmonth),
        AF_SILVER: (_pathm.kv_silver, _pathm.query_silver_yearmonth),
        AF_GOLD_S01: (_pathm.kv_gold01, _pathm.query_gold01_yearmonth),
        AF_GOLD_S02: (_pathm.kv_gold02, _pathm.query_gold02_yearmonth),
        AF_MART_S01: (_pathm.kv_mart01, _pathm.query_mart01_yearmonth)
    }
    base_func, yearmonth_func = option_map.get(_opt, (None, None))
    if not base_func or not yearmonth_func:
        raise ValueError(f'Invalid option provided: {_opt}')
    _name = base_func()
    tmp_dataset = yearmonth_func(_month)
    kv_store = await Actor.open_key_value_store(name=_name)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    await kv_store.set_value(tmp_dataset, {'updatedAt': current_time, 'complete': True})

# -----------------------------------------------------------------------------------------------------------------
# 작업해야할 데이터를 가져옴
async def month_task_data(_pathm, _idxmonth: str, _opt: str):
    query_map = {
        AF_BRONZE: _pathm.query_catalog,
        AF_SILVER: _pathm.query_bronze_yearmonth,
        AF_GOLD_S01: _pathm.query_silver_yearmonth,
        AF_GOLD_S02: _pathm.query_gold01_yearmonth,
        AF_MART_S01: _pathm.query_gold02_yearmonth
    }
    query_func = query_map.get(_opt)
    if not query_func:
        raise ValueError(f'Invalid option provided: {_opt}')
    if _opt == AF_BRONZE:
        yearmonth = query_func()
    else:
        yearmonth = query_func(_idxmonth)
    dataset = await Actor.open_dataset(name=yearmonth)
    result = await dataset.get_data()
    sorted_data = sorted(result.items, key=itemgetter('target', 'createdAt'), reverse=False)
    # 'target'으로 그룹핑하고 최신 항목만 선택
    unique_data = [max(group, key=itemgetter('createdAt')) for _, group in groupby(sorted_data, key=itemgetter('target'))]
    def _find_by_target(data, target_value):
        # 입력된 target_value와 동일한 target을 가진 객체를 찾음
        for item in data:
            if item['target'] == target_value:
                return item
    if _opt == AF_BRONZE:
        catalog_item = _find_by_target(unique_data, _idxmonth)
        return catalog_item['catalog']
    return unique_data

# -----------------------------------------------------------------------------------------------------------------
# 이건 현재 stage 를 파악하여, target 값만 반환
async def job_task_exists(_pathm, _idxmonth: str, _opt: str):
    query_map = {
        AF_BRONZE: _pathm.query_bronze_yearmonth,
        AF_SILVER: _pathm.query_silver_yearmonth,
        AF_GOLD_S01: _pathm.query_gold01_yearmonth,
        AF_GOLD_S02: _pathm.query_gold02_yearmonth,
        AF_MART_S01: _pathm.query_mart01_yearmonth
    }
    query_func = query_map.get(_opt)
    if not query_func:
        raise ValueError(f'Invalid option provided: {_opt}')
    yearmonth = query_func(_idxmonth)
    dataset = await Actor.open_dataset(name=yearmonth)
    result = await dataset.get_data()
    def _unique_job(_result):
        target_dict = {}
        for item in _result:
            target = item['target']
            created_at = datetime.strptime(item['createdAt'], '%Y-%m-%d %H:%M:%S.%f')
            if target not in target_dict or created_at > target_dict[target]['createdAt']:
                target_dict[target] = {'target': target, 'createdAt': created_at}
        latest_targets = [item['target'] for item in target_dict.values()]
        latest_targets.sort()
        return latest_targets
    return _unique_job(result.items)

# -----------------------------------------------------------------------------------------------------------------
async def kv_get_index(_pathm, _opt: str):
    option_map = {
        AF_CATALOG: (_pathm.kv_catalog, _pathm.query_catalog_index),
        AF_BRONZE: (_pathm.kv_bronze, _pathm.query_bronze_index),
        AF_SILVER: (_pathm.kv_silver, _pathm.query_silver_index),
        AF_GOLD_S01: (_pathm.kv_gold01, _pathm.query_gold01_index),
        AF_GOLD_S02: (_pathm.kv_gold02, _pathm.query_gold02_index),
        AF_MART_S01: (_pathm.kv_mart01, _pathm.query_mart01_index)
    }
    base_func, index_func = option_map.get(_opt, (None, None))
    if not base_func or not index_func:
        raise ValueError(f'Invalid option provided: {_opt}')
    kv_store = await Actor.open_key_value_store(name=base_func())
    idx_name = index_func()
    begintrx = await kv_store.get_value(idx_name) or None
    if not begintrx:
        manager_job = {
            'version': SX_VER,
            'name': _pathm.getname(),
            'fix': _pathm.getfixname(),
            'naver': _pathm.getnaver(),
            'jobs': []
        }
        await kv_store.set_value(idx_name, manager_job)
        begintrx = manager_job
    return begintrx, kv_store

# -----------------------------------------------------------------------------------------------------------------
# 지정한 달의 데이터 가져옴
async def year_month_data(_pathm, _idxmonth: str, _opt: str):
    query_map = {
        AF_BRONZE: _pathm.query_bronze_yearmonth,
        AF_SILVER: _pathm.query_silver_yearmonth,
        AF_GOLD_S01: _pathm.query_gold01_yearmonth,
        AF_GOLD_S02: _pathm.query_gold02_yearmonth,
        AF_MART_S01: _pathm.query_mart01_yearmonth
    }
    query_func = query_map.get(_opt)
    if not query_func:
        raise ValueError(f'Invalid option provided: {_opt}')
    yearmonth = query_func(_idxmonth)
    dataset = await Actor.open_dataset(name=yearmonth)
    result = await dataset.get_data()
    sorted_data = sorted(result.items, key=itemgetter('target', 'createdAt'), reverse=False)
    # 'target'으로 그룹핑하고 최신 항목만 선택
    unique_data = [max(group, key=itemgetter('createdAt')) for _, group in groupby(sorted_data, key=itemgetter('target'))]
    return unique_data

# -----------------------------------------------------------------------------------------------------------------
def _add_or_update_job(_manager_job, _month):
    idxjob = {
        'updatedAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
        'job': _month
    }
    for _job in _manager_job['jobs']:
        if _job['job'] == _month:
            if _job['updatedAt'] != idxjob['updatedAt']:
                _job['updatedAt'] = idxjob['updatedAt']
            return
    # 동일한 'job'이 없으면 새로운 job 추가
    _manager_job['jobs'].append(idxjob)
    _manager_job['jobs'].sort(key=lambda x: x['job'])

# -----------------------------------------------------------------------------------------------------------------
# partial, job, complete
def _compare_index(_baseA, _currB):
    # B 배열의 job 값을 딕셔너리로 만들어 빠르게 접근할 수 있게 함
    B_dict = {item['job']: item for item in _currB}
    for a_item in _baseA:
        a_job = a_item['job']
        a_complete = a_item['complete']
        # A의 job에 해당하는 것이 B에 없다면 처리
        if a_job not in B_dict:
            if a_complete:
                # return f'noPartial : {a_job}'
                return False, a_job, True
            else:
                # return f'noPartial and B에서 complete 기록 안함 : {a_job}'
                return False, a_job, False
        # B 배열에서 해당 job 찾기
        b_item = B_dict[a_job]
        b_complete = b_item['complete']
        # A의 complete 이 True 고 B의 complete 이 False 면 'partial' 리턴
        if a_complete and not b_complete:
            # return f'partialA : {a_job} / {a_complete}'
            return True, a_job, True
        # A의 complete 이 False 고 B의 complete 이 False 면 'partial' 리턴
        if not a_complete and not b_complete:
            # return f'partialB : {a_job} / {a_complete}'
            return True, a_job, True
    # 모든 조건을 통과하면 None 리턴
    return None, None, None

# -----------------------------------------------------------------------------------------------------------------
# index 와 매칭되는 완료file 이 있는지 확인하여 아래 형태로 반환
# [ {
#     'job': '2024-10',
#     'complete': True / False
#   } ... ]
async def _kv_complete_pair(_pathm, _trx, _kv, _opt: str):
    query_map = {
        AF_CATALOG: _pathm.query_catalog_yearmonth,
        AF_BRONZE: _pathm.query_bronze_yearmonth,
        AF_SILVER: _pathm.query_silver_yearmonth,
        AF_GOLD_S01: _pathm.query_gold01_yearmonth,
        AF_GOLD_S02: _pathm.query_gold02_yearmonth,
        AF_MART_S01: _pathm.query_mart01_yearmonth
    }
    query_func = query_map.get(_opt)
    if not query_func:
        raise ValueError(f'Invalid option provided: {_opt}')
    res_catalog = []
    for _idx in _trx['jobs']:
        tmp_dataset = query_func(_idx['job'])
        value = await _kv.get_value(tmp_dataset) or None
        res_catalog.append({
            'job': _idx['job'],
            'complete': bool(value)
        })
    return res_catalog

# -----------------------------------------------------------------------------------------------------------------
# def init_storge(_pathm) -> None:
#     # datalake
#     os.makedirs(_pathm.PATH, exist_ok=True)
#     # catalog
#     os.makedirs(_pathm.CATALOG_PATH, exist_ok=True)
#     os.makedirs(_pathm.CATALOG_NEWS, exist_ok=True)
#     # bronze
#     os.makedirs(_pathm.BRONZE_PATH, exist_ok=True)
#     os.makedirs(_pathm.BRONZE_RAW_PATH, exist_ok=True)
#     os.makedirs(_pathm.BRONZE_RAW_NEWS, exist_ok=True)
#     os.makedirs(_pathm.BRONZE_FILTER_PATH, exist_ok=True)
#     os.makedirs(_pathm.BRONZE_FILTER_NEWS, exist_ok=True)
#     # silver
#     os.makedirs(_pathm.SILVER_PATH, exist_ok=True)
#     os.makedirs(_pathm.SILVER_NEWS, exist_ok=True)
#     # gold
#     os.makedirs(_pathm.GOLD_PATH, exist_ok=True)
#     os.makedirs(_pathm.GOLD_STEP01_PATH, exist_ok=True)
#     os.makedirs(_pathm.GOLD_STEP01_NEWS, exist_ok=True)
#     # # status files
#     # files = {
#     #     os.path.join(SX_CATALOG_PATH, SX_CATALOG_STAT): '{}',
#     #     os.path.join(SX_BRONZE_PATH, SX_BRONZE_STAT): '{}',
#     #     os.path.join(SX_SILVER_PATH, SX_SILVER_STAT): '{}',
#     #     os.path.join(SX_GOLD_PATH, SX_GOLD_STAT): '{}'
#     # }
#     # for file_path, content in files.items():
#     #     if not os.path.exists(file_path):
#     #         with open(file_path, 'w') as f:
#     #             f.write(content)

# -----------------------------------------------------------------------------------------------------------------
# def clean_tmpdir(_path: str):
#     if os.path.exists(_path) and os.path.isdir(_path):
#         shutil.rmtree(_path)
#     else:
#         print(f'폴더 {_path}가 존재하지 않습니다.')

# eof