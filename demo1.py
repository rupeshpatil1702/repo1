import mysql.connector


db = mysql.connector.connect(
        host="localhost",
  user="root",
  password="Pass@123",
  database="rupesh"
    )

mycursor = db.cursor()

query = "select * from emp limit 3"

mycursor.execute(query)

result = mycursor.fetchall()
for x in result:
    print(x)

