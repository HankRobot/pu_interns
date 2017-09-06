#Python sample for writing to database
import pyodbc
#Enter all your connection info here.
#You can get all these from azure portal
server = 'vainos-iot.database.windows.net'
database = 'VainOS_IoT'
username = 'vainos'
password = 'Asdf1234'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

#Take note, I create a table, then assign column, then get data
cursor = cnxn.cursor()
#Creates a new table in the SQL database
cursor.execute("CREATE TABLE IOT_DATA2 (DataID int, Label varchar(255), Value int);")
#Insert some random data into database
cursor.execute("INSERT INTO IOT_DATA2 (DataID,Label,Value) VALUES (1, 'test', 255);")
cursor.execute("INSERT INTO IOT_DATA2 (DataID,Label,Value) VALUES (2, 'test', 1024);")

#Get the data out as strings...
cursor.execute("SELECT DataID, Value as ID, Value FROM IOT_DATA2;")

#Note that I've named it IOT_DATA2 because if you create a table with same name, you might overwrite it.
#You would want to create table once, then delete the create table code (Or comment it out).


row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()
