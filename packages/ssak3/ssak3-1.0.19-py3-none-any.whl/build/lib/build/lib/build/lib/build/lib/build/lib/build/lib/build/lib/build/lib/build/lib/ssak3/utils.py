import os
import yaml
from datetime import datetime, timedelta
from . import sx_root_dir
from .constants import *

# ----------------------------------------------------------------------------------------
def elapsed(_start_time, _end_time):
    elapsed_time = _end_time - _start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time % 1) * 1000)
    return f'{hours:02d}h {minutes:02d}min {seconds:02d}s {milliseconds:03d}ms'

# -----------------------------------------------------------------------------------------------------------------
def prompt_template_yaml(_name):
    yamlfile = os.path.join(sx_root_dir, PROMPTS_DIR, f'{_name}{SX_EXT_YAML}')
    try:
        with open(yamlfile, 'r') as file:
            content = yaml.safe_load(file)
        return content
    except Exception as err:
        # raise InternalLlmError(err)
        raise

# -----------------------------------------------------------------------------------------------------------------
def name_map_yaml():
    yamlfile = os.path.join(sx_root_dir, PROMPTS_DIR, f'name_map{SX_EXT_YAML}')
    try:
        with open(yamlfile, 'r', encoding='utf-8') as file:
            sourcename_mapping = yaml.safe_load(file).get('sourcename_mapping', {})
        return sourcename_mapping
    except Exception as err:
        # raise InternalLlmError(err)
        raise

# -----------------------------------------------------------------------------------------------------------------
def get_month_range(start_month: str, end_month: str):
    # 시작과 끝 날짜를 datetime 객체로 변환
    start_date = datetime.strptime(start_month, "%Y-%m")
    end_date = datetime.strptime(end_month, "%Y-%m")
    
    # 결과를 담을 리스트
    months = []
    
    # 시작 날짜가 끝 날짜보다 작거나 같을 때까지 반복
    while start_date <= end_date:
        # 연도와 월을 "YYYY-MM" 형식으로 추가
        months.append(start_date.strftime("%Y-%m"))
        # 한 달 더하기
        start_date += timedelta(days=31)
        # 월의 정확한 시작일로 조정
        start_date = start_date.replace(day=1)
    
    return months