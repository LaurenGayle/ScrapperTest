"""
This Module is For Connecting My mysql server to python for dumping scraped data to

"""
import os
import yaml
import logging
import mysql.connector

logging.basicConfig(filename='example.log',level=logging.DEBUG)

with open(r'assets/config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    
host= config['MYSQL_HOST']
user= config['MYSQL_USER']
passwd= config['MYSQL_PASS']
database= config['MYSQL_DATA']

 
databasesql = mysql.connector.connect(
   host= config['MYSQL_HOST'],
    user= config['MYSQL_USER'],
    passwd= config['MYSQL_PASS'],
    database= config['MYSQL_DATA']
)

mycursor = databasesql.cursor()


# Connects to Mysql Database
def mysqlConnect():
   try:
        databasesql.connect()
        
        db_Info = databasesql.get_server_info()
        
        if databasesql.is_connected():
            logging.warning("Database is Connected!"+db_Info)
   except:
        logging.error("Database not connected!")
            
def mysqlPush():
    name = ("John")
    grade = ("10")
    sql = "INSERT INTO "+database+" ("+name+", "+grade+") VALUES (%s, %s)"

    mycursor.execute(sql, name, grade)
    databasesql.commit()
    print(mycursor.rowcount, "record inserted.")

