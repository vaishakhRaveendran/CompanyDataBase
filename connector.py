import mysql.connector
mydb=connect(host='localhost',user='root',password='########')
dbCursor=mydb.cursor()
dbCursor.execute('show databases')
for i in dbCursor:
    print(i)
