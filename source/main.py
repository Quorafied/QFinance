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
    def __str__(self):
        return f"Name: {self.name} and ID: {self.t_id}"
# Initiating the GUI windows.
mainGUI = mainGUI()
addGUI = infoGatherer()

# Uncomment to debug
# anObj = tableObj("Barclays", 1)
# twoObj = tableObj("Kujawiak", 3)
# mainGUI.appendObj(anObj)
# mainGUI.appendObj(twoObj)

# Start the GUI up via the main Graphical User interface.
mainGUI.loopThrough(addGUI)







# threeObj = oneObj("Barclays", 2)# Uncomment to debug
# for i in (anObj, twoObj, threeObj):
#     mainGUI.appendObj(i)

# print(anObj)

