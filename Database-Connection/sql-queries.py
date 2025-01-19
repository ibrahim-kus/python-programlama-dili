
import sqlite3

conn = sqlite3.connect("chinook.db")

cursor = conn.cursor()

#cursor.execute("Select * from customers")

sql = "INSERT INTO genres(name) VALUES('MACERA')"

cursor.execute(sql)

conn.commit()

#customers = cursor.fetchall() #all

# result = cursor.fetchone() # one 
# print(result)
# print("********************************************")
# for customer in customers:
#     #print(customer)
#     print(customer[1]+ " " +customer[2])

conn.close()