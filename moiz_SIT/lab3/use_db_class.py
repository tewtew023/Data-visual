from datetime import datetime
from db_util import Db_util
from insert_obj import Insert_obj
# from insert_log import Insert_log
insert_obj = Insert_obj()
db_util = Db_util()
# insert_log = Insert_log()


#[Select]
sql = 'select * from data_log' 
list_data = db_util.select_data(sql)
# print(list_data)
print('total data: '+str(len(list_data)))


#[Insert]
cdatetime = str(datetime.now())
sql = """INSERT INTO data_log (type, data, cdate) VALUES (%s,%s,%s)"""
data =('insert', 'Test insert log from object!', cdatetime)
# db_util.execute_sql(sql, data)
insert_obj.insert("""INSERT INTO data_log (type, data, cdate) VALUES (%s,%s,%s)""",'insert',"I ohm fatty",cdatetime)
insert_obj.insert("""INSERT INTO data_log (type, data, cdate) VALUES (%s,%s,%s)""",'insert',"I ohm fatty mak",cdatetime)
# insert_log.insert('insert','Test insert log')


sql = 'select * from data_log' 
list_data = db_util.select_data(sql)
print('total data: '+str(len(list_data)))
last_log_id = list_data[len(list_data)-1]['id']


#[Update]
# sql = "UPDATE data_log SET type=%s, data=%s, cdate=%s WHERE id=%s"
# update_data = ['update', 'Test Update log', cdatetime, last_log_id]
# db_util.execute_sql(sql, update_data)
# insert_log.insert('update','Test update log')



# #[Delete]
# sql = "DELETE FROM data_log WHERE id = %s"
# data = [last_log_id]
# db_util.execute_sql(sql, data)