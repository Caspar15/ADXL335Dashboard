import pandas as pd
from sqlalchemy import create_engine
from cachetools import cached, TTLCache

# 創建 SQLAlchemy 引擎
db_engine = create_engine('mysql+mysqlconnector://root:920216@127.0.0.1/ADXL335')

# 創建緩存，資料存活時間 180 秒
cache = TTLCache(maxsize=100, ttl=180)

# 數據提取函數
@cached(cache)
def fetch_data(query):
    try:
        df = pd.read_sql(query, db_engine)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()  # 返回空數據框

    return df

def fetch_filtered_data(start_date, end_date, table_name):
    query = f"SELECT * FROM {table_name} WHERE RECORDED_TIME BETWEEN '{start_date}' AND '{end_date}' ORDER BY RECORDED_TIME DESC"
    df = fetch_data(query)
    if df.empty:
        print(f"No data fetched for table: {table_name} between {start_date} and {end_date}")
    else:
        print(f"Fetched data for table: {table_name} between {start_date} and {end_date}")
        print(df.head())
    return df

def clear_cache():
    cache.clear()
