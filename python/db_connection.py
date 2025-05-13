import mysql.connector


kon = mysql.connector.connect(
    host="localhost",      
    user="root",           
    password="mn174539",           
    database="orderall_shope" )

cursor = kon.cursor()
print("KONEKSI KE MYSQLNYA BERHASIL!!") 
