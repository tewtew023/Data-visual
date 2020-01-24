import sys, traceback 
import pymysql.cursors

class Db_util:

	def __init__(self):
		print ('### Db_util is working ###')

	def connect(self):
		# Connect to the database
		connection = pymysql.connect(  	host='localhost',
			                            user='root',
			                            password='',
			                            db='dataViz',
			                            charset='utf8mb4',
			                            cursorclass=pymysql.cursors.DictCursor)
		                        
		return connection



	def execute_sql(self, sql, data):
		connection = self.connect()

		try:
			with connection.cursor() as cursor:

				cursor.execute(sql, data)
				connection.commit()
		except:
			 print (sys.exc_info())

		finally:
			connection.close()



	def select_data(self, sql):
		connection = self.connect()
		result = None

		try:
			with connection.cursor() as cursor:
				cursor.execute(sql)
				result = cursor.fetchall()
		except:
			 print (sys.exc_info())

		finally:
			connection.close()


		return result