import sqlite3
from random import *

#####
# 1. Pull latest changes from github
#    git pull
#
# 2. Look at github history to see changes that were made in the past
#   - app.py is last week's code
#   - app1.py is this week's code
#
# 3. Convert raw code into classes
#   - constructor
#   - dependencies
#   - self
#   - class properties
#   - class functions
#   - code that is dynamic vs static
#
# 4. Moving towards abstract classes for better code re-use
#####


def showError(error, statement):
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(error).__name__, error.args)
    print(message, statement, "\n")


class DB:
    def __init__(self, location):
        self.location = location

    def execute(self, statement):
        try:
            connection = sqlite3.connect(self.location)
            cursor = connection.cursor()
            cursor.execute(statement)
            connection.commit()
        except Exception as error:
            showError(error, statement)
        finally:
            connection.close()

    def fetchAll(self, statement):
        result = None
        try:
            connection = sqlite3.connect(self.location)
            cursor = connection.cursor()
            result = cursor.execute(statement).fetchall()
        except Exception as error:
            showError(error, statement)
        finally:
            connection.close()

        return result

    def fetchOne(self, statement):
        result = None
        try:
            connection = sqlite3.connect(self.location)
            cursor = connection.cursor()
            result = cursor.execute(statement).fetchone()
        except Exception as error:
            showError(error, statement)
        finally:
            connection.close()

        return result


class UserTable:
    tableName = "user"
    tableColumnDefinitions = [
        "email TEXT NOT NULL",
        "name TEXT NOT NULL",
        "pk TEXT NOT NULL PRIMARY KEY",
    ]

    def __init__(self, db):
        self.db = db
        self.createTable()

    def getTableColumns(self):
        cols = filter(lambda col: self.isTableColumn(col), self.tableColumnDefinitions)
        cols = list(map(lambda col: col.split(" ")[0], cols))
        return cols

    def getColumnNames(self):
        return ",".join(self.getTableColumns())

    def isTableColumn(self, col):
        return not col.startswith("PRIMARY KEY") and not col.startswith("FOREIGN KEY")

    def createTable(self):
        stmt = f"CREATE TABLE IF NOT EXISTS {self.tableName} ({', '.join(self.tableColumnDefinitions)});"
        self.db.execute(stmt)

    def getAll(self):
        cols = self.getColumnNames()
        stmt = f"SELECT {cols} FROM {self.tableName}"
        result = self.db.fetchAll(stmt)
        return result

    def get(self, pk):
        cols = self.getColumnNames()
        stmt = f"SELECT {cols} FROM {self.tableName} WHERE pk = '{pk}'"
        result = self.db.fetchOne(stmt)
        return result

    def delete(self, pk):
        stmt = f"DELETE FROM {self.tableName} WHERE pk = '{pk}'"
        self.db.execute(stmt)

    def create(self, item):
        item["pk"] = str(randint(10000, 99999))
        cols = self.getColumnNames()
        vals = self.getItemValues(item)
        stmt = f"INSERT INTO {self.tableName} ({cols}) VALUES ({vals})"
        self.db.execute(stmt)
        return self.get(item["pk"])

    def getItemValues(self, item):
        if isinstance(item, dict):
            d = item
        else:
            d = item.__dict__

        values = []
        for col in self.getTableColumns():
            try:
                values.append(d[col])
            except (KeyError):
                values.append(None)

        vals = ", ".join(f"'{v}'".replace("'None'", "null") for v in values)
        return vals

    def update(self, item):
        setters = self.getUpdateSetters(item)
        stmt = f"UPDATE {self.tableName} SET {setters} WHERE pk = '{item['pk']}'"
        self.db.execute(stmt)
        return self.get(item["pk"])

    def getUpdateSetters(self, item):
        cols = self.getTableColumns()
        vals = self.getItemValues(item).split(", ")
        setters = []
        for c, v in zip(cols, vals):
            setters.append(f"{c} = {v}")
        setters = filter(lambda setter: not setter.startswith("pk = "), setters)
        return ", ".join(setters)


# Now that we have classes, this is how we use them

databaseLocation = "python-app.db"  # specify the database file location
db = DB(databaseLocation)  # create an instance of the database class
userTable = UserTable(db)  # create an instance of the user table class

# user = {"email": "my-email@example.com", "name": "jonny"}
# userTable.create(user)

# user2 = {
#     "email": "different-email@example.com",
#     "name": "different-jonny",
#     "pk": "51722",
# }
# userTable.update(user2)

# userTable.delete("51722")

# one = userTable.get("42221")
# print(f"one: {one}")

# all = userTable.getAll()
# print(f"all: {all}")


###
# Next we will learn how to create an abstract class to share code between classes that have things in common
###
