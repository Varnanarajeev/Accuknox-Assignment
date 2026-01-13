"""API Data Retrieval and Storage: You are tasked with fetching data from an 
external REST API, storing it in a local SQLite database, and displaying the 
retrieved data. The API provides a list of books in JSON format with attributes like 
title, author, and publication year.
i"""

import requests
import sqlite3

url="https://openlibrary.org/search.json"
params={"q":"Self Love"}
response=requests.get(url,params=params)
response_json=response.json()


for book in response_json["docs"]:
    title=book.get("title","No Title")
    author= ",".join(book.get("author_name",["Unknown"]))
    year=book.get("first_publish_year","N/A")
   


conn=sqlite3.connect('books.db')
c=conn.cursor()


c.execute("""
          create table if not exists books(
          id integer primary key autoincrement,
            title text,
            author text,
            year date)
            
            """)
conn.commit()


for book in response_json["docs"][:50]:
    title = book.get("title","No Title")
    author = ", ".join(book.get("author_name",["Unknown"]))
    year = book.get("first_publish_year",None)

    c.execute(
        "insert into books (title, author, year) VALUES (?, ?, ?)",
        (title, author, year)
    )

conn.commit()

c.execute("select * from books")
rows = c.fetchall()
print("\nBOOK DETAILS:\n")

for row in rows:
    print(row)

conn.close()