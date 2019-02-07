# import_csv.py

import cx_Oracle
import csv

con = cx_Oracle.connect('user/password@hostIP/database')

print("Connected to Oracle")

reader = csv.reader(open("yourfile.csv", "r"))
next(reader)
columns = []
for line in reader:
    columns.append(line)

cur = con.cursor()
for line in columns:
    print("Inserting data")
    insrt_stmt = "insert into TABLE (COLUMN1,COLUMN2,COLUMN3) values (:1, :2, :3)"
    cur.execute(insrt_stmt, line)
con.commit()
cur.close()
print("completed")
