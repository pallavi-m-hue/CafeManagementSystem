import mysql.connector

def connect_database():
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="pallavi",
        database="cafemanegementsystem"
    )
    return db

def fetch_data(query,params=None):
    connection=connect_database()
    cursor=connection.cursor()
    try:
        cursor.execute(query,params)
        data = cursor.fetchall()
        return data
    finally:
        cursor.close()
        connection.close()
    

def execute_query(query,params=None,return_cursor=False):
    connection=connect_database()
    cursor=connection.cursor()
    try:
        cursor.execute(query,params)
        connection.commit()
        if return_cursor:
            return cursor
        
    finally:
        cursor.close()
        connection.close()

