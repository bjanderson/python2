import sqlite3

print()  # just adding a new line in the terminal output

# set the name of the database file
dbLocation = "python-app.db"

# this is the table definition
tableName = "user"

# Try to create the table, or handle the error
# and remember to close the connection when you're done
print("### Create the table ###")
stmt = f"""CREATE TABLE IF NOT EXISTS {tableName} (
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    pk TEXT NOT NULL PRIMARY KEY
);"""
try:
    connection = sqlite3.connect(dbLocation)
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    print()
except Exception as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print(message, "\n")
finally:
    connection.close()

# Add rows to the table
print("### Insert a row into the table ###")
stmt = f"INSERT INTO {tableName} (email, name, pk) VALUES ('user1@example.com', 'User One', 'userpk1')"
try:
    connection = sqlite3.connect(dbLocation)
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    print()
except Exception as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print(message, stmt, "\n")
finally:
    connection.close()

# fetch all rows from the table
print("### Fetch all rows from the table ###")
stmt = f"SELECT email, name, pk FROM {tableName}"
try:
    connection = sqlite3.connect(dbLocation)
    cursor = connection.cursor()
    result = cursor.execute(stmt).fetchall()
    print(result, "\n")
except Exception as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print(message, stmt, "\n")
finally:
    connection.close()


# fetch one row from the table
print("### Fetch one row from the table ###")
stmt = f"SELECT email, name, pk FROM {tableName} WHERE pk = 'userpk1'"
try:
    connection = sqlite3.connect(dbLocation)
    cursor = connection.cursor()
    result = cursor.execute(stmt).fetchone()
    print(result, "\n")
except Exception as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print(message, stmt, "\n")
finally:
    connection.close()

# delete a row from the table
print("### Delete a row from the table ###")
stmt = f"DELETE FROM {tableName} WHERE pk = 'userpk1'"
try:
    connection = sqlite3.connect(dbLocation)
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    print()
except Exception as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print(message, stmt, "\n")
finally:
    connection.close()
