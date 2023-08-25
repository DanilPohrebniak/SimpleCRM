import mysql.connector

dateBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234qwer'
)

cursorObject = dateBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print('All Done!')