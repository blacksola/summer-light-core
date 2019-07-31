import psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SqlUtils:
    def connect(self):
        engine = create_engine(self.dbUrl, echo=False,pool_size=30, pool_recycle=5, pool_timeout=30, max_overflow=0)
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def getArrResult(self, sql, autoClose=False):
        queryList = self.session.execute(sql)
        res = queryList.fetchall()
        if autoClose:
            self.closeConnect()
        return res

    # 包装getArrResult
    def getArrResultWrapper(self, querySql,logger=None, pyFileName='', methodName=''):
        rsData = []
        try:
            rsData = self.getArrResult(querySql)
        except Exception as error:
            if logger:
                logger.error('---error---file:%s;method:%s;error=%s' % (pyFileName, methodName, error))
            raise error
        finally:
            self.closeConnect()
        return rsData

    def getTableStructure(self, tableName):
        tableStructure = []
        if tableName:
            sql = f"""SELECT table_schema, table_name, column_name, data_type, column_default, is_nullable
                            FROM information_schema.columns WHERE table_name = '{tableName}'"""
            result = self.getArrResult(sql)
            for row in result:
                structure = {}
                structure['table_schema'] = row[0]
                structure['table_name'] = row[1]
                structure['column_name'] = row[2]
                structure['data_type'] = row[3]
                structure['column_default'] = row[4]
                structure['is_nullable'] = row[5]
                tableStructure.append(structure)
        return tableStructure

    def getDictResult(self, sql):
        list = self.session.execute(sql)
        cols = list.cursor.description#对于oracle，sql里是有小写的字段，但这一步就将所有的字段转大写了，
        columnNames = []
        for col in cols:
            try:
                # columnNames.append(col.name)#因数据库不同而导致查询的col可能是对象也可能是数组，所以需要捕捉异常处理
                colName = col.name
            except Exception as error:
                # columnNames.append(col[0])
                colName = col[0]
            columnNames.append(colName.lower())

        columnNames = tuple(columnNames)#需要转tuple
        res = list.fetchall()
        resArr = []
        for row in res:
            resArr.append(dict(zip(columnNames,row)))
        return resArr

    def getTotal(self, sql):
        sql = "select count(*) as total from (" + sql + ") a"
        tb = self.session.execute(sql)
        b = tb.fetchall()
        tbs = []
        for u in b:
            tbs.append(dict(zip(u.keys(), u.values())))
        return tbs[0]

    def executeUpdateSql(self, sql):#执行插入或修改语句，需要回滚，多次执行后需要调用closeConnect手动关闭连接
        try :
            self.session.execute(sql)#不关闭异常，可能多次调用执行sql，最后让用户执行commit和连接的关闭
        except Exception as error:
            raise error    #需要将异常抛出到调用的函数，让其进行处理

    # 增删改 SQL操作 type增删改  table对应的表  id操作的id  **kwargs传入 字段=值 例:name='张三'
    def executeSql(self,type,table,id,**kwargs):
        state = ''
        try:
            if type == "insert":
                field = ''
                fieldvalue = ''
                for i,j in kwargs.items():
                    field += ''' "{}",'''.format(i)
                    fieldvalue += ''' '{}','''.format(j)
                sql = r'''INSERT INTO {}({}"id") VALUES ({}'{}')'''.format(table,field,fieldvalue,id)
                # print(sql)
            elif type == "update":
                field = ''
                for i,j in kwargs.items():
                    field += '''"{}" = '{}','''.format(i,j)
                sql = r'''UPDATE {0} SET {1} WHERE "id" = '{2}' '''.format(table,field[:-1],id)
            elif type == "delete":
                sql = r'''DELETE FROM {0} WHERE "id" = {1}'''.format(table,id)
            else:
                raise Exception('type类型错误')
            self.excuteSqlByBulkParams(sql)
        except Exception as e:
            state = e
        finally:
            self.closeConnect()
        return state

    # 执行增删改sql
    def excuteSqlByBulkParams(self, sql, paremeters=None, logger=None):
        try:
            effCount = self.session.execute(sql, paremeters)
        except Exception as error:
            self.rollBack()
            if logger:
                logger.error('---error---file:utils.py;method:excuteSqlByBulkParams;error=%s' % error.args)
            raise error
        finally:
            self.closeConnect()#只执行一次就关闭连接
        return effCount

    def closeConnect(self):
        self.session.commit()
        self.session.close()

    def rollBack(self):
        self.session.rollback()
        self.session.close()

    def __init__(self, dbType='default', dbId='', connInfo={}):
        self.kind = 'pgsql'
        self.dbUrl = 'postgresql://sola:a@123456B@pgm-bp1kyk50ab84p141eo.pg.rds.aliyuncs.com:3432/summerlight'
        if dbType == 'mysql':
            self.dbUrl = 'mysql+pymysql://sola:a@123456B@129.204.88.98:3306/incontrol'
        self.connect()


