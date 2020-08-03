
# Size of local Cache
LOCAL_CACHE_SIZE = 1000

# Minimum Size of Cache
MIN_LOCAL_CACHE_SIZE = 250

# Batch Size to be inserted in db
INSERT_BATCH_SIZE = 2000

# Fetch Batch Size
FETCH_BATCH_SIZE = LOCAL_CACHE_SIZE

# Maximum Keys Allowed in database
MAX_AVAILABLE_KEYS_DB = 100000

MIN_AVAILABLE_KEYS_DB = 2000

MYSQL = {
    'engine': 'mysql+pymysql',
    'pool_size': 100,
    'debug': False,
    'username': "root",
    'password': "Villa#25",
    'host': "0.0.0.0",
    'db_name': "shortener"
}