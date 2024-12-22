import mysql.connector

def get_db_connection():
    try:
        return mysql.connector.connect(
            host="autorack.proxy.rlwy.net",  
            user="root",                   
            password="gUwUGiXhDyajFXyMPEVyOduaMMeMlAYg",  
            database="railway",            
            port=47280                      
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
