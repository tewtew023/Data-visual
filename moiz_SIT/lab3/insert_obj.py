from db_util import Db_util
class Insert_obj:

    def __init__(self):
        print('### inserting###')

    def insert(self,sql,type,data,c):
        data = type,data,c
        db_util = Db_util()
        db_util.execute_sql(sql, data)