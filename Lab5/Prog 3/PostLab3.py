'''
***********LABORATORY 5 - POST LAB - PROGRAMMING PROBLEM 3 ***********
CPE106L B2 Group 5

Members:
Claros, Angelica
Facal, Ma. Catherina
Santos, Angelica Anne

'''

import sqlite3

con = sqlite3.connect("PostLab3.db")

cur = con.cursor()

print("\n\nShowing the table 'GUIDE'\n")
for row in cur.execute('SELECT * FROM GUIDE;'):
    print(row)


print("\n\nShowing the table 'TRIP'\n")
for row in cur.execute('SELECT * FROM TRIP;'):
    print(row)

print("\n\nShowing the table 'CUSTOMER'\n")
for row in cur.execute('SELECT * FROM CUSTOMER;'):
    print(row)

print("\n\nShowing the table 'RESERVATION'\n")
for row in cur.execute('SELECT * FROM RESERVATION;'):
    print(row)


con.close()
