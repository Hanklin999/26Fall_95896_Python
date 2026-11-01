
# 95896-A, 2026 Fall
# Student Name: Hank Lin
# Andrew ID: hanklin

#%%
'''1. 
The name of the database is dogsdb.sqlite3, but that’s not the name of the table(s) it contains.
Initially, it has one table, dogs (in addition to the bookkeeping table sqlite_master). You can check that by running the following:
cursor = connection.cursor()
query='select name from sqlite_master where type="table"'
cursor.execute(query)
table = cursor.fetchall()
print(table)'''

# Problem 1

import sqlite3

try:
    connection = sqlite3.connect("dogsdb.sqlite3")
    cursor = connection.cursor()

    query = 'SELECT name FROM sqlite_master WHERE type="table"'
    cursor.execute(query)

    table = cursor.fetchall()
    print(table)

except sqlite3.Error as e:
    print("Database error:", e)
    raise

#%%
# Problem 2

query = "SELECT * FROM dogs"

cursor.execute(query)

table = cursor.fetchall()

print(table)
print(type(table))

for row in table:
    print(row)

#%%
# Problem 3

print(cursor.description)

for item in cursor.description:
    print(item[0])

colnames = []

for item in cursor.description:
    colnames.append(item[0])

print(colnames)

#%%
# Problem 4

import pandas as pd

dogsDF = pd.DataFrame(table, columns=colnames)

print(dogsDF)

#%%
# Problem 5

from breeds import breeds

print(breeds)



#%%
# Problem 6

create_query = """
CREATE TABLE IF NOT EXISTS Breeds (
    Breed VARCHAR(20),
    Description VARCHAR(40)
)
"""

cursor.execute(create_query)

insert_query = """
INSERT INTO Breeds
VALUES (?, ?)
"""

cursor.executemany(insert_query, breeds)

connection.commit()




#%%

# 7. Query the table Breeds from dogdb and display it (i.e., as proof that it was stored)

query_breeds = "SELECT * FROM Breeds"

cursor.execute(query_breeds)
 
breeds_table = cursor.fetchall()

# print(breeds_table)

for row in breeds_table:
    print(row)


#%%

# 8.Write a JOIN query to join dogs with Breeds on the Breed field, but limited to the Name, Breed, and Description fields.

query_breeds_field = """
 SELECT dogs.Name, dogs.Breed, Breeds.Description
 FROM dogs
 JOIN Breeds
 ON dogs.Breed = Breeds.Breed
 """

cursor.execute(query_breeds_field)
 
breeds_field_table = cursor.fetchall()

for row in breeds_field_table:
    print(row)



#%%

# 9 
query = """
SELECT Name, Age
FROM dogs
WHERE Age >= 5
"""

cursor.execute(query)

table = cursor.fetchall()

for row in table:
    print(row)


#%%

# 10
query = """
SELECT AVG(dogs.Age)
FROM dogs
"""

cursor.execute(query)

result = cursor.fetchone()
average_age = result[0]

print(f"Average age: {average_age:.2f}")

#%%

# 11

lines = []
with open('testdata.txt','r') as f:
    for item in f:
        lines.append(item.strip())

print(lines)
        
import re

patterns = [
    r"\d",                 # any digit
    r"[A-Za-z]",           # any letter, either case
    r"\d+",                # integer = one or more digits
    r"^a",                 # begins with a
    r"s$",                 # ends with s
    r"\(",                 # contains (
    r"a.*e|e.*a",          # contains a and e, either order
    r"aeiou",              # lowercase vowels adjacent, in order
    r"a.*e.*i.*o.*u"       # lowercase vowels in order, not necessarily adjacent
]
    

for pattern in patterns:
    print("Pattern:", pattern)

    for line in lines:
        if re.search(pattern, line) is not None:
            print("Matched:", line)
    






