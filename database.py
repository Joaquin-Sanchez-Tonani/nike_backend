import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="autorack.proxy.rlwy.net",
        user="root",
        password="gUwUGiXhDyajFXyMPEVyOduaMMeMlAYg",
        database="railway"
    )



