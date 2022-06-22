"""
    This is a small python script, which creates a database for taltech diners.


    After database creation there are 2 queries which tests database:
     1) query for canteens which are open 16.15-18.00
    2) query for canteens which are serviced by Rahva Toit. 

    Run the script with:

        python3 task_a.py


"""

import sqlite3


def opendb():
    """
    1) Create SQLite database DINERS, with two related tables CANTEEN and PROVIDER
    """
    global conn
    conn = sqlite3.connect('diners_a.db')
    


def create_table_providers():
    """
    Table Provider fields: ID, ProviderName.
    """
    conn.execute('''CREATE TABLE IF NOT EXISTS PROVIDER
             (
             ID             INTEGER PRIMARY KEY     AUTOINCREMENT,
            ProviderName          CHAR(50)                NOT NULL 
             );''')
   


def create_table_canteen():
    """
   Table CANTEEN fields: ID, ProviderID, Name, Location,  time_open, time_closed (weekday doesn't matter).
    """
    conn.execute('''CREATE TABLE IF NOT EXISTS CANTEEN
             (
             ID             INTEGER PRIMARY KEY     AUTOINCREMENT,
             ProviderID    INTEGER                 NOT NULL,
             Name          CHAR(100)               NOT NULL,
             Location      CHAR(100)               NOT NULL,
             time_open      TIME                    NOT NULL,
             time_closed    TIME                    NOT NULL
             );''')



def add_records_providers():
    """
    add provider records in the PROVIDER table
    """
    conn.execute("INSERT INTO PROVIDER (ProviderName) \
                 VALUES ('Rahva Toit')");

    conn.execute("INSERT INTO PROVIDER (ProviderName) \
                 VALUES ('Baltic Restaurants Estonia AS')");

    conn.execute("INSERT INTO PROVIDER (ProviderName) \
                 VALUES ('TTÜ Sport OÜ')");

    conn.commit()
    


def add_records_canteen():
    """
    create canteen records in the CANTEEN table
    """
    conn.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) \
                 VALUES (1,'Economics - and social science building canteen', 'Akadeemia tee 3, SOC - building', '09:00:00 AM', '18:30:00 PM')");

    conn.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) \
                 VALUES (1,'Library canteen', 'Akadeemia tee 1/ Ehitajate tee 7', '08:30:00 AM', '19:00:00 PM')");

    conn.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) \
                 VALUES (2,'Main building Deli cafe', 'Ehitajate tee 5, U01 building', '09:00:00 AM', '16:30:00 PM')");

    conn.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) \
                 VALUES (2,'Main building Daily lunch restaurant', 'Ehitajate tee 5, U01 building', '09:00:00 AM', '16:30:00 PM')");

    conn.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) \
                 VALUES (1,'U06 building canteen', 'Ehitajate tee 5, U06 building', '09:00:00 AM', '16:00:00 PM')");

    conn.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) \
                 VALUES (2,'Natural Science building canteen', 'Akadeemia tee 15, SCI building', '09:00:00 AM', '16:00:00 PM')");

    conn.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) \
                 VALUES (2,'ICT building canteen', 'Raja 15/Mäepealse 1', '09:00:00 AM', '16:00:00 PM')");

    conn.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) \
                 VALUES (3,'Sports building canteen', 'Männiliiva 7, S01 building', '11:00:00 AM', '20:00:00 PM')");

    conn.commit()
    


def insert_bitStop():
    """
    Insert IT College canteen data by separate statement
    """
    conn.execute("INSERT INTO PROVIDER (ProviderName) \
                 VALUES ('bitStop kohvik')")

    conn.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) \
                 VALUES (4,'bitStop Kohvik', 'IT College of TalTech, 1st Floor', '09:30:00 AM', '16:00:00 PM')");

    conn.commit()
    




def query1():
    """
    3) Create query for canteens which are open 16.15-18.00,
    """
    cursor = conn.execute("SELECT * FROM CANTEEN WHERE time_closed >= '18:00:00 PM'")
    for row in cursor:
        print("Name: ", row[2])
        print("Closing time: ", row[5], "\n")


def query2():
    """
    4) Create query for canteens which are serviced by Rahva Toit. NB! Create query by string "Rahva Toit" not by direct ID!.
    """
    cursor = conn.execute("SELECT * FROM CANTEEN WHERE ProviderID = (SELECT ID FROM PROVIDER WHERE ProviderName = 'Rahva Toit')")
    for row in cursor:
        print("Name: ", row[2], "\n")



def delete_records():
    """
    Drop tables 
    """
    conn.execute("DROP TABLE PROVIDERS;")
    conn.execute("DROP TABLE CANTEEN;")
    conn.commit()
    


def closeconn():
    """
    close connection
    """
    conn.close()
    


if __name__ == "__main__":
    """
    test everything!
    3) Create query for canteens which are open 16.15-18.00,
    4) Create query for canteens which are serviced by Rahva Toit. NB! Create query by string "Rahva Toit" not by direct ID!.
    """
    opendb()
    create_table_providers()
    create_table_canteen()
    add_records_providers()
    add_records_canteen()
    insert_bitStop()
    
   

    print("\nDiners which are open between 16:15-18:00:")
    query1()

    print("\nDiners serviced by Rahva Toit:")
    query2()

    
    closeconn()

