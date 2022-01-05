from sqlDatabase import *
from gui import *

# Instantiating a database interaction object.
# This object will be used to connect, set up a cursor for and alter the content of the SQL localhost server.
db = sqlDatabase()

db.connect() # This is used to connect to the sql localhost server.
db.setCursor() # This sets up a Cursor that will point and execute SQL Queries
db.createDatabase("QFinance") # SQL Query - Creates a database called "QFinance"
db.useDatabase("QFinance")# SQL Query - Point to a database to be altered by further actions
db.createTables()

'''To Change when SQL Database has methods to be modified'''
class tableObj():
    def __init__(self, n, id):
        self.name = n
        self.t_id = id


global addGUI
mainGUI = mainGUI()
addGUI = infoGatherer()


mainGUI.loopThrough(addGUI)

# Uncomment to debug
# anObj = oneObj("Barclays", 1)
# twoObj = oneObj("Kujawiak", 3)
# threeObj = oneObj("Barclays", 2)# Uncomment to debug
# for i in (anObj, twoObj, threeObj):
#     mainGUI.appendObj(i)
