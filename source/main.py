from sqlDatabase import *

# Instantiating a database interaction object.
# This object will be used to connect, set up a cursor for and alter the content of the SQL localhost server.
db = sqlDatabase()

# This is used to connect to the sql localhost server.
db.connect()

# This sets up a Cursor that will point and execute SQL Queries
db.setCursor()

# SQL Query - Creates a database called "QFinance"
db.createDatabase("QFinance")

# SQL Query - Point to a database to be altered by further actions
db.useDatabase("QFinance")