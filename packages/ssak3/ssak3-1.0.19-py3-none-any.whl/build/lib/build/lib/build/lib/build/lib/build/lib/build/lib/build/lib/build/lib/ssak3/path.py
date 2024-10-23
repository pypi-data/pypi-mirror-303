import os
import re
from datetime import datetime
from typing import List
from .constants import *
from .query import fix_query

class ApifyPathManager:
    def __init__(self, _name, _query, _storage, install=SX_STORAGE_BASE):
        self.name = _name
        self.query = self._gend(_query)
        self.naver = _query
        # self.query = 'q6b46da7dddaa4417'
        self.STORAGE = _storage
        self.INSTALL = install
        self._update()

    def _update(self):
        self.PATH = f'{self.INSTALL}-{self.STORAGE}'
        self.NEWS_PATH = f'{self.PATH}-{AF_SCRAPER_NEWS}'
        self.CATALOG_PATH = f'{self.NEWS_PATH}-{AF_CATALOG}'
        self.BRONZE_PATH = f'{self.NEWS_PATH}-{AF_BRONZE}'
        self.SILVER_PATH = f'{self.NEWS_PATH}-{AF_SILVER}'
        self.GOLD01_PATH = f'{self.NEWS_PATH}-{AF_GOLD_S01}'
        self.GOLD02_PATH = f'{self.NEWS_PATH}-{AF_GOLD_S02}'
        self.MART01_PATH = f'{self.NEWS_PATH}-{AF_MART_S01}'

    def getname(self) -> str:
        return self.name
    def getfixname(self) -> str:
        return self.query
    def getnaver(self) -> str:
        return self.naver

    def _gend(self, _query: str) -> str:
        return f'{AF_QRY_HDR}{fix_query(_query)}'

    def base_catalog(self) -> str:
        return self.CATALOG_PATH
    def base_bronze(self) -> str:
        return self.BRONZE_PATH
    def base_silver(self) -> str:
        return self.SILVER_PATH
    def base_gold01(self) -> str:
        return self.GOLD01_PATH
    def base_gold02(self) -> str:
        return self.GOLD02_PATH
    def base_mart01(self) -> str:
        return self.MART01_PATH

    def kv_catalog(self) -> str:
        return f'{self.CATALOG_PATH}-{self.query}'
    def kv_bronze(self) -> str:
        return f'{self.BRONZE_PATH}-{self.query}'
    def kv_silver(self) -> str:
        return f'{self.SILVER_PATH}-{self.query}'
    def kv_gold01(self) -> str:
        return f'{self.GOLD01_PATH}-{self.query}'
    def kv_gold02(self) -> str:
        return f'{self.GOLD02_PATH}-{self.query}'
    def kv_mart01(self) -> str:
        return f'{self.MART01_PATH}-{self.query}'

    def query_catalog(self) -> str:
        return f'{self.base_catalog()}-{self.query}'
    def query_catalog_index(self) -> str:
        return f'{self.base_catalog()}-{self.query}-{AF_INDEX}'
    def query_catalog_yearmonth(self, _date) -> str:
        if isinstance(_date, str):
            _date = datetime.strptime(_date, '%Y-%m')
        return f'{self.base_catalog()}-{self.query}-{_date.strftime("%Y-%m")}'
    #
    def query_bronze_index(self) -> str:
        return f'{self.base_bronze()}-{self.query}-{AF_INDEX}'
    def query_bronze_yearmonth(self, _date) -> str:
        if isinstance(_date, str):
            _date = datetime.strptime(_date, '%Y-%m')
        return f'{self.base_bronze()}-{self.query}-{_date.strftime("%Y-%m")}'
    #
    def query_silver_index(self) -> str:
        return f'{self.base_silver()}-{self.query}-{AF_INDEX}'
    def query_silver_yearmonth(self, _date) -> str:
        if isinstance(_date, str):
            _date = datetime.strptime(_date, '%Y-%m')
        return f'{self.base_silver()}-{self.query}-{_date.strftime("%Y-%m")}'
    #
    def query_gold01_index(self) -> str:
        return f'{self.base_gold01()}-{self.query}-{AF_INDEX}'
    def query_gold01_yearmonth(self, _date) -> str:
        if isinstance(_date, str):
            _date = datetime.strptime(_date, '%Y-%m')
        return f'{self.base_gold01()}-{self.query}-{_date.strftime("%Y-%m")}'
    #
    def query_gold02_index(self) -> str:
        return f'{self.base_gold02()}-{self.query}-{AF_INDEX}'
    def query_gold02_yearmonth(self, _date) -> str:
        if isinstance(_date, str):
            _date = datetime.strptime(_date, '%Y-%m')
        return f'{self.base_gold02()}-{self.query}-{_date.strftime("%Y-%m")}'
    #
    def query_mart01_index(self) -> str:
        return f'{self.base_mart01()}-{self.query}-{AF_INDEX}'
    def query_mart01_yearmonth(self, _date) -> str:
        if isinstance(_date, str):
            _date = datetime.strptime(_date, '%Y-%m')
        return f'{self.base_mart01()}-{self.query}-{_date.strftime("%Y-%m")}'

    # raw_04_00001_d83ca7c4e62e6241e8f1d825cf87802e1df975f1f3ef6866c44fe026d8e91204
    def bronze_data_name(self, _period_start, _num, _fingerprint) -> str:
        return f'{SX_RAW_HDR}{_period_start[-2:]}_{_num:05}_{_fingerprint}'

    def silver_data_name(self, _raw: str) -> str:
        base_name_with_ext = _raw[len(SX_RAW_HDR):]
        base_name, _ = os.path.splitext(base_name_with_ext)
        return f'{SX_PUR_HDR}{base_name}'

    def gold_step01_data_name(self, _pur: str) -> str:
        base_name_with_ext = _pur[len(SX_PUR_HDR):]
        base_name, _ = os.path.splitext(base_name_with_ext)
        return f'{SX_S01_HDR}{base_name}'

    def gold_step02_data_name(self, _s01: str) -> str:
        base_name_with_ext = _s01[len(SX_S01_HDR):]
        base_name, _ = os.path.splitext(base_name_with_ext)
        return f'{SX_S02_HDR}{base_name}'

    def mart_step01_data_name(self) -> str:
        return f'{SX_M01_HDR}stat01'

class FilePathManager:
    def __init__(self, _name, _query, _storage, install=SX_STORAGE_BASE):
        self.name = _name
        self.query = self._gend(_query)
        self.naver = _query
        # self.query = 'q6b46da7dddaa4417'
        self.STORAGE = _storage
        self.INSTALL = install
        self._update()

    def _update(self):
        self.PATH = os.path.join(self.INSTALL, self.STORAGE)
        self.CATALOG_PATH = os.path.join(self.PATH, SX_CATALOG)
        self.CATALOG_NEWS = os.path.join(self.CATALOG_PATH, SX_SCRAPER_NEWS)
        self.BRONZE_PATH = os.path.join(self.PATH, SX_BRONZE)
        self.BRONZE_RAW_PATH = os.path.join(self.BRONZE_PATH, SX_BRONZE_RAW)
        self.BRONZE_RAW_NEWS = os.path.join(self.BRONZE_RAW_PATH, SX_SCRAPER_NEWS)
        self.BRONZE_FILTER_PATH = os.path.join(self.BRONZE_PATH, SX_BRONZE_FILTER)
        self.BRONZE_FILTER_NEWS = os.path.join(self.BRONZE_FILTER_PATH, SX_SCRAPER_NEWS)
        self.SILVER_PATH = os.path.join(self.PATH, SX_SILVER)
        self.SILVER_NEWS = os.path.join(self.SILVER_PATH, SX_SCRAPER_NEWS)
        self.GOLD_PATH = os.path.join(self.PATH, SX_GOLD)
        self.GOLD_STEP01_PATH = os.path.join(self.GOLD_PATH, SX_GOLD_STEP01)
        self.GOLD_STEP01_NEWS = os.path.join(self.GOLD_STEP01_PATH, SX_SCRAPER_NEWS)
        self.GOLD_STEP02_PATH = os.path.join(self.GOLD_PATH, SX_GOLD_STEP02)
        self.GOLD_STEP02_NEWS = os.path.join(self.GOLD_STEP02_PATH, SX_SCRAPER_NEWS)

    def getname(self) -> str:
        return self.name
    def getfixname(self) -> str:
        return self.query
    def getnaver(self) -> str:
        return self.naver

    def _gend(self, _query: str) -> str:
        return f'{SX_QRY_HDR}{fix_query(_query)}'

    def storage_path(self, _path):
        marker = f'{self.STORAGE}/'
        index = _path.find(marker)
        if index != -1:
            return _path[index:]
        else:
            return 'not founded'

    # ----------------------------------------------------------------------------------------
    def catalog_query_dir(self) -> str:
        return os.path.join(self.CATALOG_NEWS, self.query)

    def catalog_tmp_dir(self, _date: datetime) -> str:
        return os.path.join(self.catalog_query_dir(), f'_{_date.strftime("%Y_%m")}')

    def catalog_tmp_name(self, _date: datetime) -> str:
        tmp_path = self.catalog_tmp_dir(_date)
        # return os.path.join(tmp_path, f'{SX_TMP_HDR}{SX_IDX_HDR}{_date.strftime("%Y_%m_%d")}{SX_EXT_YAML}')
        return os.path.join(tmp_path, f'{SX_TMP_HDR}{SX_IDX_HDR}{_date.strftime("%Y_%m_%d")}{SX_EXT_JSON}')

    def catalog_data_name(self, _date: datetime) -> str:
        # return os.path.join(self.catalog_query_dir(), f'{SX_IDX_HDR}{_date.strftime("%Y_%m")}{SX_EXT_YAML}')
        return os.path.join(self.catalog_query_dir(), f'{SX_IDX_HDR}{_date.strftime("%Y_%m")}{SX_EXT_JSON}')

    def catalog_data_list(self):
        # files = sorted(
        #     [f for f in os.listdir(self.catalog_query_dir()) if f.startswith(SX_IDX_HDR) and f.endswith(SX_EXT_YAML)],
        #     key=lambda x: datetime.strptime('_'.join(x.replace(SX_EXT_YAML, '').split('_')[2:4]), '%Y_%m')
        # )
        files = sorted(
            [f for f in os.listdir(self.catalog_query_dir()) if f.startswith(SX_IDX_HDR) and f.endswith(SX_EXT_JSON)],
            key=lambda x: datetime.strptime('_'.join(x.replace(SX_EXT_JSON, '').split('_')[2:4]), '%Y_%m')
        )
        return files

    # ----------------------------------------------------------------------------------------
    def bronze_query_raw_dir(self) -> str:
        return os.path.join(self.BRONZE_RAW_NEWS, self.query)

    def bronze_raw_year_dir(self, _indexfn: str) -> str:
        return os.path.join(self.bronze_query_raw_dir(), f'{SX_KEY_YEAR}{_indexfn.split("_")[2]}')
        
    def bronze_raw_data_dir(self, _indexfn: str) -> str:
        # return os.path.join(self.bronze_raw_year_dir(_indexfn), f'{SX_KEY_MONTH}{_indexfn.split("_")[3].replace(SX_EXT_YAML, "")}')
        return os.path.join(self.bronze_raw_year_dir(_indexfn), f'{SX_KEY_MONTH}{_indexfn.split("_")[3].replace(SX_EXT_JSON, "")}')

    # def bronze_raw_data_tmp_dir(self, _indexfn: str) -> str:
    #     return os.path.join(self.bronze_raw_year_dir(_indexfn), f'{SX_TMP_HDR}{_indexfn.split("_")[3].replace(SX_EXT_YAML, "")}')

    def bronze_raw_data_name(self, _indexfn: str, _period_start, _num, _fingerprint) -> str:
        return os.path.join(self.bronze_raw_data_dir(_indexfn), f'{SX_RAW_HDR}{_period_start[-2:]}_{_num:05}_{_fingerprint}{SX_EXT_JSON}')

    # def bronze_raw_data_tmp_name(self, _indexfn: str, _period_start, _num, _fingerprint) -> str:
    #     return os.path.join(self.bronze_raw_data_tmp_dir(_indexfn), f'{SX_RAW_HDR}{_period_start[-2:]}_{_num:05}_{_fingerprint}{SX_EXT_HTML}')

    # # ----------------------------------------------------------------------------------------
    def bronze_query_filter_dir(self) -> str:
        return os.path.join(self.BRONZE_FILTER_NEWS, self.query)

    def bronze_filter_year_dir(self, _indexfn: str) -> str:
        return os.path.join(self.bronze_query_filter_dir(), f'{SX_KEY_YEAR}{_indexfn.split("_")[2]}')

    def bronze_filter_data_dir(self, _indexfn: str) -> str:
        # return os.path.join(self.bronze_filter_year_dir(_indexfn), f'{SX_KEY_MONTH}{_indexfn.split("_")[3].replace(SX_EXT_YAML, "")}')
        return os.path.join(self.bronze_filter_year_dir(_indexfn), f'{SX_KEY_MONTH}{_indexfn.split("_")[3].replace(SX_EXT_JSON, "")}')

    # # def bronze_filter_data_tmp_dir(self, _indexfn: str) -> str:
    # #     return os.path.join(self.bronze_filter_year_dir(_indexfn), f'{SX_TMP_HDR}{_indexfn.split("_")[3].replace(SX_EXT_YAML, "")}')

    # def bronze_filter_data_name(self, _indexfn: str, _period_start, _num, _fingerprint) -> str:
    #     return os.path.join(self.bronze_filter_data_dir(_indexfn), f'{SX_FLT_HDR}{_period_start[-2:]}_{_num:05}_{_fingerprint}{SX_EXT_HTML}')

    # # def bronze_filter_data_tmp_name(self, _indexfn: str, _period_start, _num, _fingerprint) -> str:
    # #     return os.path.join(self.bronze_filter_data_tmp_dir(_indexfn), f'{SX_FLT_HDR}{_period_start[-2:]}_{_num:05}_{_fingerprint}{SX_EXT_HTML}')

    # ----------------------------------------------------------------------------------------
    def bronze_raw_year_dir_list(self) -> List:
        raw_dir = self.bronze_query_raw_dir()
        folders = sorted(
            [f.split('=')[1] for f in os.listdir(raw_dir) if os.path.isdir(os.path.join(raw_dir, f)) and re.match(rf'{SX_KEY_YEAR}\d{{4}}', f)],
            key=lambda x: datetime.strptime(x, '%Y')
        )
        # ['2022', '2023', '2024']
        return folders
   
    # '2024'
    def bronze_raw_data_dir_list(self, _year: str) -> List:
        data_dir = os.path.join(self.bronze_query_raw_dir(), f'{SX_KEY_YEAR}{_year}')
        folders = sorted(
            [f.split('=')[1] for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f)) and re.match(rf'{SX_KEY_MONTH}\d{{2}}', f)],
            key=lambda x: int(x)
        )
        # ['09', '10']
        return folders

    # raw_03_00003_126d6bd606088d7e9049789ab635a18de03322dffe11a2c3a63a76c5345eac2d.html
    def bronze_raw_data_list(self, _year: str, _month: str):
        data_dir = os.path.join(self.bronze_query_raw_dir(), f'{SX_KEY_YEAR}{_year}', f'{SX_KEY_MONTH}{_month}')
        files = sorted(
            [f for f in os.listdir(data_dir) if f.startswith(SX_RAW_HDR) and f.endswith(SX_EXT_JSON)],
            key=lambda x: (int(x.split('_')[1]), int(x.split('_')[2]))
        )
        return files

    # ----------------------------------------------------------------------------------------
    def silver_query_dir(self) -> str:
        return os.path.join(self.SILVER_NEWS, self.query)

    # /Users/eastjoo/works/scraper/x4t/03.silver/news/query_서태지/2024
    def silver_year_dir(self, _year: str) -> str:
        return os.path.join(self.silver_query_dir(), f'{SX_KEY_YEAR}{_year}')

    # /Users/eastjoo/works/scraper/x4t/03.silver/news/query_서태지/2024/07
    def silver_data_dir(self, _year: str, _month: str) -> str:
        return os.path.join(self.silver_year_dir(_year), f'{SX_KEY_MONTH}{_month}')

    def silver_data_name(self, _year: str, _month: str, _raw: str) -> str:
        base_name_with_ext = _raw[len('raw_'):]
        base_name, _ = os.path.splitext(base_name_with_ext)
        return os.path.join(self.silver_data_dir(_year, _month), f'{SX_PUR_HDR}{base_name}{SX_EXT_JSON}')

    # def silver_data_tmp_dir(self, _indexfn: str) -> str:
    #     return os.path.join(self.silver_year_dir(_indexfn), f'{SX_TMP_HDR}{_indexfn.split("_")[3].replace(SX_EXT_YAML, "")}')

    # def silver_data_tmp_name(self, _indexfn: str, _period_start, _num, _fingerprint) -> str:
    #     return os.path.join(self.silver_data_tmp_dir(_indexfn), f'{SX_PUR_HDR}{_period_start[-2:]}_{_num:05}_{_fingerprint}{SX_EXT_JSON}')

    def silver_year_dir_list(self) -> List:
        raw_dir = self.silver_query_dir()
        folders = sorted(
            [f.split('=')[1] for f in os.listdir(raw_dir) if os.path.isdir(os.path.join(raw_dir, f)) and re.match(rf'{SX_KEY_YEAR}\d{{4}}', f)],
            key=lambda x: datetime.strptime(x, '%Y')
        )
        # ['2022', '2023', '2024']
        return folders

    # '2024'
    def silver_data_dir_list(self, _year: str) -> List:
        data_dir = os.path.join(self.silver_query_dir(), f'{SX_KEY_YEAR}{_year}')
        folders = sorted(
            [f.split('=')[1] for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f)) and re.match(rf'{SX_KEY_MONTH}\d{{2}}', f)],
            key=lambda x: int(x)  # 추출한 숫자 부분을 정렬
        )
        # ['09', '10']
        return folders

    # pur_03_00003_126d6bd606088d7e9049789ab635a18de03322dffe11a2c3a63a76c5345eac2d.json
    def silver_data_list(self, _year: str, _month: str):
        data_dir = os.path.join(self.silver_query_dir(), f'{SX_KEY_YEAR}{_year}', f'{SX_KEY_MONTH}{_month}')
        files = sorted(
            [f for f in os.listdir(data_dir) if f.startswith(SX_PUR_HDR) and f.endswith(SX_EXT_JSON)],
            key=lambda x: (int(x.split('_')[1]), int(x.split('_')[2]))
        )
        return files

    # ----------------------------------------------------------------------------------------
    def gold_query_step01_dir(self) -> str:
        return os.path.join(self.GOLD_STEP01_NEWS, self.query)

    def gold_step01_year_dir(self, _year: str) -> str:
        return os.path.join(self.gold_query_step01_dir(), f'{SX_KEY_YEAR}{_year}')

    def gold_step01_data_dir(self, _year: str, _month: str) -> str:
        return os.path.join(self.gold_step01_year_dir(_year), f'{SX_KEY_MONTH}{_month}')

    def gold_step01_data_name(self, _year: str, _month: str, _raw: str) -> str:
        base_name_with_ext = _raw[len('pur_'):]
        base_name, _ = os.path.splitext(base_name_with_ext)
        return os.path.join(self.gold_step01_data_dir(_year, _month), f'{SX_S01_HDR}{base_name}{SX_EXT_JSON}')

    def gold_step01_year_dir_list(self) -> List:
        raw_dir = self.gold_query_step01_dir()
        folders = sorted(
            [f.split('=')[1] for f in os.listdir(raw_dir) if os.path.isdir(os.path.join(raw_dir, f)) and re.match(rf'{SX_KEY_YEAR}\d{{4}}', f)],
            key=lambda x: datetime.strptime(x, '%Y')
        )
        # ['2022', '2023', '2024']
        return folders

    # '2024'
    def gold_step01_data_dir_list(self, _year: str) -> List:
        data_dir = os.path.join(self.gold_query_step01_dir(), f'{SX_KEY_YEAR}{_year}')
        folders = sorted(
            [f.split('=')[1] for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f)) and re.match(rf'{SX_KEY_MONTH}\d{{2}}', f)],
            key=lambda x: int(x)  # 추출한 숫자 부분을 정렬
        )
        # ['09', '10']
        return folders

    # s01_03_00003_126d6bd606088d7e9049789ab635a18de03322dffe11a2c3a63a76c5345eac2d.json
    def gold_step01_data_list(self, _year: str, _month: str):
        data_dir = os.path.join(self.gold_query_step01_dir(), f'{SX_KEY_YEAR}{_year}', f'{SX_KEY_MONTH}{_month}')
        files = sorted(
            [f for f in os.listdir(data_dir) if f.startswith(SX_S01_HDR) and f.endswith(SX_EXT_JSON)],
            key=lambda x: (int(x.split('_')[1]), int(x.split('_')[2]))
        )
        return files

    # ----------------------------------------------------------------------------------------
    def gold_query_step02_dir(self) -> str:
        return os.path.join(self.GOLD_STEP02_NEWS, self.query)

    def gold_step02_year_dir(self, _year: str) -> str:
        return os.path.join(self.gold_query_step02_dir(), f'{SX_KEY_YEAR}{_year}')

    def gold_step02_data_dir(self, _year: str, _month: str) -> str:
        return os.path.join(self.gold_step02_year_dir(_year), f'{SX_KEY_MONTH}{_month}')

    def gold_step02_data_name(self, _year: str, _month: str, _raw: str) -> str:
        base_name_with_ext = _raw[len(SX_S01_HDR):]
        base_name, _ = os.path.splitext(base_name_with_ext)
        return os.path.join(self.gold_step02_data_dir(_year, _month), f'{SX_S02_HDR}{base_name}{SX_EXT_JSON}')

    def gold_step02_data_list(self, _year: str, _month: str):
        data_dir = os.path.join(self.gold_query_step02_dir(), f'{SX_KEY_YEAR}{_year}', f'{SX_KEY_MONTH}{_month}')
        files = sorted(
            [f for f in os.listdir(data_dir) if f.startswith(SX_S02_HDR) and f.endswith(SX_EXT_JSON)],
            key=lambda x: (int(x.split('_')[1]), int(x.split('_')[2]))
        )
        return files

# eof