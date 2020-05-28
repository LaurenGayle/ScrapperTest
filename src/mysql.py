"""
This Module is For Connecting My mysql server to python for dumping scraped data to

"""
import os
import mysql.connector
import logging
  
host= os.environ.get("MYSQL_HOST")
user= os.environment.get("MYSQL_USER")
passwd= os.environment.get("MYSQL_PASS")
database=os.environment.get("MYSQL_DATA")

 
databasesql = mysql.connector.connect(
    host,
    user,
    passwd,
    database
)

mycursor = databasesql.cursor()

# Connects to Mysql Database
def mysqlConnect():
   try:
        databasesql.connect()
        
        db_Info = databasesql.get_server_info()
        
        if databasesql.is_connected():
            logging.warning("Database is Connected!"+db_Info)
        else:
            logging.error("Database not connected!")
            
    
def mysqlPush():

    name = ("John")
    grade = ("10")
    sql = "INSERT INTO "+database+" ("+name+", "+grade+") VALUES (%s, %s)"

    mycursor.execute(sql, name, grade)
    databasesql.commit()

print(mycursor.rowcount, "record inserted.")

