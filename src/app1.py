import sqlite3

print()  # just adding a new line in the terminal output

# set the name of the database file
databaseLocation = "python-app.db"


def showError(error, statement):
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(error).__name__, error.args)
    print(message, statement, "\n")


def executeStatement(statement):
    print(f"execute - statement: {statement}")
    try:
        connection = sqlite3.connect(databaseLocation)
        cursor = connection.cursor()
        cursor.execute(statement)
        connection.commit()
        print()
    except Exception as error:
        showError(error, statement)
    finally:
        connection.close()


def executeFetchAllStatment(statement):
    result = None
    try:
        connection = sqlite3.connect(databaseLocation)
        cursor = connection.cursor()
        result = cursor.execute(statement).fetchall()
        print(result, "\n")
    except Exception as error:
        showError(error, statement)
    finally:
        connection.close()

    return result


def executeFetchOneStatment(statement):
    result = None
    try:
        connection = sqlite3.connect(databaseLocation)
        cursor = connection.cursor()
        result = cursor.execute(statement).fetchone()
        print(result, "\n")
    except Exception as error:
        showError(error, statement)
    finally:
        connection.close()

    return result


tableName = "user"
statement = f"""CREATE TABLE IF NOT EXISTS {tableName} (
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    pk TEXT NOT NULL PRIMARY KEY
);"""
executeStatement(statement)

statement = f"INSERT INTO {tableName} (email, name, pk) VALUES ('user1@example.com', 'User One', 'userpk1')"
executeStatement(statement)

statement = f"SELECT email, name, pk FROM {tableName}"
executeFetchAllStatment(statement)

statement = f"SELECT email, name, pk FROM {tableName} WHERE pk = 'userpk1'"
executeFetchOneStatment(statement)

statement = f"DELETE FROM {tableName} WHERE pk = 'userpk1'"
executeStatement(statement)

#####################################################################################


# def createTable(tableName, tableDefinition):
#     statement = f"""CREATE TABLE IF NOT EXISTS {tableName} ({tableDefinition});"""
#     executeStatement(statement)


# tableName = "password"
# tableDefinition = """
# password TEXT NOT NULL,
# userPK TEXT NOT NULL,
# FOREIGN KEY(userPK) REFERENCES user(pk),
# PRIMARY KEY(password, userPK)
# """
# createTable(tableName, tableDefinition)

# # --------------------
# def createRow(tableName, fields, values):
#     fields = ", ".join(fields)
#     values = list(map(lambda value: f"'{value}'", values))
#     values = ", ".join(values)
#     statement = f"INSERT INTO {tableName} ({fields}) VALUES ({values})"
#     executeStatement(statement)


# tableName = "password"
# fields = ["password", "userPK"]
# values = ["Password_1", "userpk1"]
# createRow(tableName, fields, values)

# # --------------------
# def selectAll(tableName, fields):
#     fields = ", ".join(fields)
#     statement = f"SELECT {fields} FROM {tableName}"
#     return executeFetchAllStatment(statement)


# tableName = "password"
# fields = ["password", "userPK"]
# results = selectAll(tableName, fields)
# print("results: ", results)

# # --------------------
# def selectOne(tableName, fields, pk, pkField="pk"):
#     fields = ", ".join(fields)
#     statement = f"SELECT {fields} FROM {tableName} WHERE {pkField} = '{pk}'"
#     return executeFetchOneStatment(statement)


# tableName = "password"
# fields = ["password", "userPK"]
# result = selectOne(tableName, fields, "userpk1", "userPK")
# print("result: ", result)
