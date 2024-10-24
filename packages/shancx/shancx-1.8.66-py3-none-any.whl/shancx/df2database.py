import pandas as pd
from sqlalchemy import create_engine 
import datetime
"""
enginestr = 'postgresql://postgres:{}@{}:{}/exam_data'.format(passwd,ip,port)

"""
def get_create_engine(enginestr):
    engine = create_engine(enginestr)
    return engine
# engine = get_create_engine(enginestr)
# 创建一个示例 DataFrame
def data_column_lower(exam_data):
    exam_data.columns = [col.lower() for col in exam_data.columns]
    return exam_data
def data_column_upper(exam_data):
    exam_data.columns = [col.upper() for col in exam_data.columns]
    return exam_data
def get_current_time_format():
    now = datetime.datetime.now()
    formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')    
    return formatted_now  
def write_to_postgresql(df):        
    # 将 DataFrame 写入 PostgreSQL 表中
    df.to_sql('weather_data_test', if_exists='replace', index=False,con=engine)
