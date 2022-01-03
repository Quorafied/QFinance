import mysql.connector
from myDecorators import *

class sqlDatabase():
    def __init__(self):
        self.mydb = None
        self.cursor = None
    
    # Establish a connection to a local database
    @debug
    def connect(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "admin",
            autocommit = True
            )

    # Setting up a cursor pointing in the database to make changes.
    @debug
    def setCursor(self):
        self.cursor = self.mydb.cursor()
    
    # Creating a Database to include data.
    @debug
    def createDatabase(self, name):
        self.cursor.execute(
            """CREATE
            DATABASE
            IF NOT EXISTS
            {}""".format(name))

    # Tell pointer to make any further changes in specified Database
    @debug
    def useDatabase(self, name):
        self.cursor.execute(
            """USE {}""".format(name)
        )

    # Creating Tables inside Pointing Database
    @debug
    def createTables(self):
        # Create transactions 
        self.cursor.execute(
            """CREATE
            TABLE
            IF NOT EXISTS
            transactions
            (
                t_id int NOT NULL AUTO_INCREMENT,
                destination varchar(255),
                sender varchar(255),
                amount int,
                PRIMARY KEY(t_id)
            );
            """
        )

        # Creating a table containing details about transactions 
        self.cursor.execute(
            """CREATE
            TABLE
            IF NOT EXISTS
            transactionDetails
            (
                t_id int,
                method varchar(255),
                platform varchar(255),
                date varchar(255),
                reason varchar(255),
                PRIMARY KEY (t_id),
                FOREIGN KEY (t_id)
                    REFERENCES transactions (t_id)
            );"""
        )

        # Creating a table with information about debts.
        self.cursor.execute(
            """CREATE
            TABLE
            IF NOT EXISTS
            owes
            (
                owe_id int NOT NULL AUTO_INCREMENT,
                who varchar(255),
                owes varchar(255),
                amount int,
                method varchar(255),
                reason varchar(255),
                notes varchar(255),
                paid bit,
                PRIMARY KEY (owe_id) 
            );"""
        )
    @debug
    def removeTransaction(self):
        self.cursor.execute(
            """DELETE
            FROM 
            

            """)


