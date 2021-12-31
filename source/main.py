from sqlDatabase import *
from gui import *

# Instantiating a database interaction object.
# This object will be used to connect, set up a cursor for and alter the content of the SQL localhost server.
db = sqlDatabase()

db.connect() # This is used to connect to the sql localhost server.
db.setCursor() # This sets up a Cursor that will point and execute SQL Queries
db.createDatabase("QFinance") # SQL Query - Creates a database called "QFinance"
db.useDatabase("QFinance")# SQL Query - Point to a database to be altered by further actions

mainGUI = GUI()
mainGUI.loopThrough()
