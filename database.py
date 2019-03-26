import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('LicensePlate.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS VehicleDetails (Serial REAL, Brand TEXT,  Vehicle_Number TEXT)')

def data_entry():
        c.execute("INSERT INTO VehicleDetails  VALUES(6 , 'Ford', '9090')")
        c.execute("INSERT INTO VehicleDetails  VALUES(1 , 'Ford', 'BA 1 PA 4453')")
        c.execute("INSERT INTO VehicleDetails  VALUES(2 , 'Hyundai', 'BA 2 PA 4553')")
        c.execute("INSERT INTO VehicleDetails  VALUES(3 , 'Nissan', 'BA 13 PA 4453')")
        c.execute("INSERT INTO VehicleDetails  VALUES(4 , 'Ford', 'BA 71 PA 303')")
        c.execute("INSERT INTO VehicleDetails  VALUES(5 , 'Ford', 'LU AA 1468')")
        c.execute("INSERT INTO VehicleDetails  VALUES(7 , 'Ford', '9090')")
        conn.commit()
        

def read_table():
    c.execute("SELECT * FROM VehicleDetails")
    data = c.fetchall()
    return data
    #print data



#create_table()
#data_entry()
read_table()
