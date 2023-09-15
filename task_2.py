#Name: Kuldip Savaliya
#UTA_ID: 1001832000
# DB1_Project1_Task2


import mysql.connector
import csv

mydb = mysql.connector.connect(host="acadmysqldb001p", user="kxs2000", password="Kd8490001906#", database="kxs2000")
mycursor = mydb.cursor()
print(mydb)
print(mycursor)

csv_data3 = csv.reader(open("EMPLOYEE.csv"),delimiter=',')
print("table1-------------------------------------------------------------------------------------------------------------")
for rows in csv_data3:
    print(rows)
    mycursor.execute("INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rows[8], rows[9]])


csv_data2 = csv.reader(open("DEPENDENT.csv"),delimiter=',')
print("table2-------------------------------------------------------------------------------------------------------------")
for rows in csv_data2:
    print(rows)
    mycursor.execute("INSERT INTO dependent VALUES(%s,%s,%s,%s,%s)", [rows[0], rows[1], rows[2], rows[3], rows[4]])


csv_data4 = csv.reader(open("DEPARTMENT.csv"),delimiter=',')
print("table3-------------------------------------------------------------------------------------------------------------")
for rows in csv_data4:
    print(rows)
    mycursor.execute("INSERT INTO department VALUES (%s,%s,%s,%s,%s)", [rows[0], rows[1], rows[2], rows[3]], rows[4])


csv_data1 = csv.reader(open("DEPT_LOCATIONS.csv"),delimiter=',')
print("table4-------------------------------------------------------------------------------------------------------------")
for rows in csv_data1:
    print(rows)
    mycursor.execute("INSERT INTO dept_locations VALUES (%s,%s)", [rows[0], rows[1]])


csv_data5 = csv.reader(open("PROJECT.csv"),delimiter=',')
print("table5-------------------------------------------------------------------------------------------------------------")
for rows in csv_data5:
    print(rows)
    mycursor.execute("INSERT INTO project VALUES (%s,%s,%s,%s)", [rows[0], rows[1], rows[2], rows[3]])


csv_data6 = csv.reader(open("WORKS_ON.csv"),delimiter=',')
print("table6-------------------------------------------------------------------------------------------------------------")
for rows in csv_data6:
    print(rows)
    mycursor.execute("INSERT INTO works_on VALUES(%s,%s,%s)", [rows[0], rows[1], rows[2]])



mydb.commit()
