import mysql.connector
mydb=connect(host='localhost',user='root',password='l@xmi2421')
dbCursor=mydb.cursor()
dbCursor.execute('show databases')
for i in dbCursor:
    print(i)