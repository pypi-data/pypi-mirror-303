#################################################################
# configure
#################################################################
SX_STORAGE_BASE = 'techlab'                 # '/Users/eastjoo/works/scraper'
SX_STORAGE_NAME = 'sx'

SX_FILE_SYTEM = 'file'
SX_APIFY_SYSTEM = 'apify'
SX_STORAGE_TYPE = SX_APIFY_SYSTEM

GPT_4o = 'gpt-4o-2024-08-06'                # 128,000 tokens / 16,384 tokens
GPT_4o_mini = 'gpt-4o-mini-2024-07-18'      # 128,000 tokens / 16,384 tokens
GPT_MODEL = GPT_4o_mini

SX_TASK_TIMEOUT = 180                       # task timeout
SX_MAX_AGENCY = 20                          # 신문사 length

SX_CATALOG_SIZE = 25
SX_BRONZE_SIZE = 20
SX_SILVER_SIZE = 30
SX_GOLD_SIZE = 30
SX_MART_01_SIZE = 10

SX_SQLDB_DIR = 'sqldb'

#################################################################
# constant
#################################################################
SX_VER = '1'

PROMPTS_DIR = 'prompts'                     # ssak3/prompt
PROMPT_GOLD_01 = 'gold_01'
PROMPT_GOLD_02 = 'gold_02'
PROMPT_GOLD_03 = 'gold_03'

# apify storage schema
AF_CATALOG = 'catalog'
AF_INDEX = 'index'
AF_BRONZE = 'bronze'
AF_SILVER = 'silver'
AF_GOLD_S01 = 'gold01'
AF_GOLD_S02 = 'gold02'
AF_MART_S01 = 'mart01'

# apify file name
AF_QRY_HDR = 'q'
AF_IDX_HDR = 'news-index-'
AF_TMP_HDR = '-'

# file storage schema
SX_CATALOG = '01.catalog'
SX_BRONZE = '02.bronze'
SX_BRONZE_RAW = '01.rawdata'
SX_BRONZE_FILTER = '02.filtereddata'
SX_SILVER = '03.silver'
SX_GOLD = '04.gold'
SX_GOLD_STEP01 = '01.step'
SX_GOLD_STEP02 = '02.step'

# file name
SX_QRY_HDR = 'query='
SX_IDX_HDR = 'news_index_'
SX_RAW_HDR = 'raw_'
SX_FLT_HDR = 'filter_'
SX_PUR_HDR = 'pur_'
SX_LLM_HDR = 'llm_'
SX_TMP_HDR = '_'
SX_S01_HDR = 's01_'
SX_S02_HDR = 's02_'
SX_M01_HDR = 'm01_'
SX_KEY_YEAR = 'year='
SX_KEY_MONTH = 'month='
SX_SCRAPER_NEWS = 'topic=news'
AF_SCRAPER_NEWS = 'news'

# logging
SX_LOGS = 'logs'
SX_LOG_CATALOG = 'sc'
SX_LOG_BRONZE = 'sb'
SX_LOG_SILVER = 'ss'
SX_LOG_GOLD_01 = 'sg01'
SX_LOG_GOLD_02 = 'sg02'
SX_LOG_MART_01 = 'sm01'

# internal
SX_SCRAPER = 'scraper'
SX_EXT_YAML = '.yaml'
SX_EXT_JSON = '.json'
SX_KV_CONFIG = f'{SX_STORAGE_BASE}-{SX_STORAGE_NAME}-{AF_SCRAPER_NEWS}-config'

AF_CMD = 'cmd'
AF_CMD_INPUT = 'input'
AF_CMD_UPDATE = 'update'

# __all__ = ['SX_GOLD_SIZE', SX_GOLD_SIZE]