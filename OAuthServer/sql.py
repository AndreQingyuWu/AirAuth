import pymysql
 
db = pymysql.connect(host='23.99.190.56',user='root', password='wu1999916', port=3306,database='dj_client')
#db = pymysql.connect(host='23.99.190.56',user='root', password='wu1999916', port=3306,database='dj_auther')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()
