import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    c = connection.cursor()
    #creating table
    c.execute("""CREATE TABLE task(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
    #inserting dummy data into table
    c.execute(
        'INSERT INTO task(name, due_date, priority, status)'
        'VALUES("Finish this shit", "25/02/2018", 10, 1)'

    )
    c.execute(
        'INSERT INTO task(name, due_date, priority, status)'
        'VALUES("Finish that shit", "28/02/2018", 10, 1)'
        
    )
