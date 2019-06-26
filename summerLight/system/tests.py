import pandas as pd
from sqlalchemy import create_engine
def importpostgr():
    # 连接两个数据库
    orengine = create_engine("oracle://JINGNENG:123456@129.204.88.98/orcl", encoding='utf-8', echo=True)
    pgengine = create_engine('postgresql://postgres:!@#QWE123@106.12.75.246:5432/datax_extension')
    # 查询 department_attendance
    department_sql = '''SELECT * FROM department_attendance '''
    department_df = pd.read_sql(department_sql,orengine)
    # 查询 personal_approval
    personal_sql = '''SELECT * FROM personal_approval '''
    personal_df = pd.read_sql(personal_sql,orengine)
    # 查询 personal_approval
    process_sql = '''SELECT * FROM process_signed '''
    process_df = pd.read_sql(process_sql,orengine)
    # 写入pg数据库
    department_df.to_sql('oa_department_attendance',pgengine,index=True,if_exists='replace')
    personal_df.to_sql('oa_personal_approval',pgengine,index=True,if_exists='replace')
    process_df.to_sql('oa_process_signed',pgengine,index=True,if_exists='replace')
importpostgr()