import csv
import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Person')
cur.execute('''CREATE TABLE IF NOT EXISTS Person
(id INTEGER PRIMARY KEY, year INTEGER, earnings REAL,
degree TEXT, gender TEXT, age INTEGER)''')

with open("CPSSW9204.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:

        cur.execute('INSERT INTO Person (year,earnings,degree,gender,age) VALUES (?,?,?,?,?)',(row[1],row[2],row[3],row[4],row[5]))
        #rows.append(row)
conn.commit()
print('Columns Of Csv File',header[1:6])
print('Retrieved and Stored all data...')
