import mysql.connector

def inventory_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="KwaViVa123.",
        database="inventory"
    )