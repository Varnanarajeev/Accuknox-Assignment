"""CSV Data Import to a Database: Write a Python script that reads data from a
CSV file containing user information (e.g., name, email) and inserts it into a SQLite database.
"""

import pandas as pd
import sqlite3

conn = sqlite3.connect("people.db")
data = pd.read_csv('sample-data.csv')

data.to_sql('info',conn,if_exists='replace',index=False)
c = conn.cursor()
for row in c.execute('SELECT * FROM info'):
    print(row)

conn.close()