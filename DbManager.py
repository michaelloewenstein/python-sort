import psycopg2

MYSQL_SECTION = "target_db_postgresql"

class DbManager(object):
	
	def __init__(self, config):
			connectionConfig = {
                'user' : config.get(MYSQL_SECTION, 'user', True),
                'db' : config.get(MYSQL_SECTION, 'db', True)
            }
		        conn = psycopg2.connect("dbname="+connectionConfig['db'] +" user="+connectionConfig['user'])
		        cur = conn.cursor()
	        	self._db = cur
	        	self._connection = conn

	def insert(self,input,output,sortType):
			r = self._db.execute("INSERT INTO sort VALUES(%s,%s,%s)",(input,output,sortType))
			print(r)
			res = self._db.execute("SELECT * FROM sort WHERE sortname = 'quicksort2' ")
		    	print(self._db.fetchone())
		    	self._connection.commit()





      
