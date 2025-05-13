from db_connection import kon, cursor 


query = "SELECT * FROM pesanan"
cursor.execute(query)


for row in cursor.fetchall():
    print(row)


cursor.close()
kon.close()
 