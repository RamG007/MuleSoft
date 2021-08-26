import sqlite3

# define connection and cursor

connection = sqlite3.connect('movies_database.db')
cursor = connection.cursor()

# create movies table

command = """CREATE TABLE IF NOT EXISTS movies( id INTEGER PRIMARY KEY, 
                                                movie_name TEXT,
                                                actor TEXT,
                                                actress TEXT,
                                                director TEXT,
                                                release_year INTEGER)"""
cursor.execute(command)


# Insert data into movies table

cursor.execute("INSERT INTO movies VALUES( 1, 'Avatar', 'Sam Worthington', 'Zoe Saldana', 'James Cameron', 2009)")
cursor.execute("INSERT INTO movies VALUES( 2, 'Sherlock Holmes', 'Robert Downey Jr.', 'Rachel McAdams', 'Guy Ritchie', 2009)")
cursor.execute("INSERT INTO movies VALUES( 3, 'Flipped', 'Callan McAuliffe', 'Madeline Carroll', 'Rob Reiner', 2010)")

# get movies

print('All Movies : ')
cursor.execute("SELECT * FROM movies")
print(cursor.fetchall())

print('---------')

print('Movies of Robert Downey Jr.')
cursor.execute("SELECT * FROM movies WHERE actor='Robert Downey Jr.'")
print(cursor.fetchall())
