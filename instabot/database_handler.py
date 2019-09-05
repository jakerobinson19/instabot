import os
import sqlite3

# create sqlite connection and updates/deletes/gets
SQL_CREATE_USERNAMES_TABLE = """
    CREATE TABLE IF NOT EXISTS `usernames` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `username` TEXT NOT NULL,
        `followers` INTEGER,
        `following` INTEGER,
        `f2f ratio` FLOAT,
        `status` TEXT NOT NULL,
        `date` DATETIME NOT NULL);"""

SQL_CREATE_BLACKLIST_TABLE = """
    CREATE TABLE IF NOT EXISTS `profiles` (
        `username` TEXT NOT NULL,
        'f2f ratio', FLOAT);"""

SQL_CREATE_ACCOUNT_PROGRESS_TABLE = """
    CREATE TABLE IF NOT EXISTS `accountProgress` (
        `date` DATETIME NOT NULL,
        `followers` INTEGER NOT NULL,
        `following` INTEGER NOT NULL,
        `f2f ratio` FLOAT);"""

SQL_CREATE_RECORD_ACTIVITY_TABLE = """
    CREATE TABLE IF NOT EXISTS 'activityRecord' (
        `date` DATE NOT NULL,
        `time_elapse` DATETIME NOT NULL,
        `profiles_engaged` INTEGER,
        `comments` INTEGER,
        `likes` INTEGER);"""

def create_database(address, name):
    try:
        connection = sqlite3.connect(address)
        with connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            create_tables(
                cursor,
                [
                    "usernames",
                    "blacklist",
                    "accountProgress",
                    "activityRecord"
                ],
            )

            connection.commit()

    except Exception as exc:
            print("Wah! Error occurred while getting a DB for '{}':\n\t{}".format(
                name, str(exc))

    finally:
        if connection:
            # close the open connection
            connection.close()
