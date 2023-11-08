import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database='employeemanagement',
    password='l@xmi2421'
)

dbCursor = mydb.cursor()
dbCursor.execute('SELECT pr.stackId, sk.employeeSsn ' 
                'FROM skills AS sk ' 
                'RIGHT JOIN projectrequirements AS pr ON pr.stackId = sk.stackId ' 
                'WHERE pr.pnumber = 2;')

for row in dbCursor:
    print(row)
