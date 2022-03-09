import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password= "PokiYoki17283964"


)


mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_rest")