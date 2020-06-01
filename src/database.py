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

table = config['MYSQL_TABLE']

name ="nick"
address = "1"
 
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
    
    
    #DataTable Create should only be ran once
def mysqlcreate():
    try:
        logging.debug("creating users"+user+"in table"+table+" on Database"+database)
        mycursor.execute("CREATE TABLE "+table+" (name VARCHAR(255), address VARCHAR(255))")
        logging.debug("created succefully")
    except:
        logging.error("TABLE WAS NOT CREATED")
            
            
    # data is written to Mysql server via the Student Database Table 
def mysqlPush():
    mysqlConnect()
    sql ="INSERT INTO "+table+" (name, address) VALUES (%s, %s) "
    values = (name,address)
    
    mycursor.execute(sql.format(table = table), values)
    databasesql.commit()
    
    print(mycursor.rowcount, "record inserted.")
    logging.warn("INSERTED DATA ")
    databasesql.close()
    logging.warning("database connection closed")
    
def mysqlRead():
    sql_select_Query = "select names from"+table+""
    
    cursor = databasesql.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
    logging.debug(records)
    