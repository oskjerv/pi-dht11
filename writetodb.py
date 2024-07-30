
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """create a database conenction to the SQlite database
        specified by db_file
    :param db_file: database file
    :return: connection object or None
    """
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

def create_datarow(conn, dht11):
    """
    Create a new data entry from dht11 into temp_hum-table
    :param conn:
    :param temperatures:
    """
    
    sql = ''' INSERT INTO temp_hum(pin, temp_c, temp_f, humidity, location)
              VALUES(?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, dht11)
    conn.commit()


def write_from_dht11(pin, temp_c, temp_f, humidity, location):
    database = r"/home/pi/Documents/temperature_and_humidity/temp_humidity.db"
    
    # create a db connection
    conn = create_connection(database)
    
    with conn:
        #create a datarow 
        write = (pin, temp_c, temp_f, humidity, location)
        
        create_datarow(conn, write)
        
