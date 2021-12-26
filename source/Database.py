import mysql.connector
import sqlite3

class Database():
    def __init__(self):
        self.mydb = None
        self.cursor = None
    
    # Establish a connection to a local database
    def connect(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "admin",
            autocommit = True
            )

    # Setting up a cursor pointing in the database to make changes.
    def setCursor(self):
        self.cursor = self.mydb.cursor()
    
    # Creating a Database to include data.
    def createDatabase(self):
        self.cursor.execute(
            """CREATE
            DATABASE
            IF NOT EXISTS
            QFinance""")

    # Tell pointer to make any further changes in specified Database
    def useDatabase(self):
        self.cursor.execute(
            """USE QFinance"""
        )

    # Creating Tables inside Pointing Database
    def createTables(self):
        # Create transactions 
        self.cursor.execute(
            """CREATE
            TABLE
            IF NOT EXISTS
            transactions
            (
                t_id int NOT NULL AUTO_INCREMENT,
                to varchar(255),
                from varchar(255),
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
    