import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "password", database = "airlines_booking")
cur = mydb.cursor()
cur.execute(
    "create table if not exists flights (\
    s_no int primary key not null auto_increment,\
    AIRLINES_NAME VARCHAR(100),\
    DEPARTURE VARCHAR(100),\
    DESTINATION VARCHAR(100),\
    FLIGHT_NO varchar(50),\
    TIME_OF_DEPARTURE VARCHAR(50),\
    TIME_OF_ARRIVAL VARCHAR(50),\
    CHARGES INT );"
 )
