#Librarys
import mysql.connector


def get_connection():
    conn = mysql.connector.connect(
        host= "localhost",
        user = "root",
        password = "",
        database = "kava_database"
    )
    return conn