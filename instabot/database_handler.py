import os
import sqlite3
import datetime

# create sqlite connection and updates/deletes/gets
SQL_CREATE_USERNAMES_TABLE = """
    CREATE TABLE IF NOT EXISTS `usernames` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `username` TEXT NOT NULL,
        `followers` INTEGER,
        `following` INTEGER,
        `f2f_ratio` FLOAT,
        `status` TEXT NOT NULL,
        `cal_date` DATETIME NOT NULL);"""

SQL_CREATE_ACCOUNT_PROGRESS_TABLE = """
    CREATE TABLE IF NOT EXISTS `accountProgress` (
        `cal_date` DATETIME NOT NULL,
        `followers` INTEGER NOT NULL,
        `following` INTEGER NOT NULL,
        `f2f_ratio` FLOAT);"""

SQL_CREATE_ACTIVITY_RECORD_TABLE = """
    CREATE TABLE IF NOT EXISTS 'activityRecord' (
        `cal_date` DATE NOT NULL,
        `time_elapsed` DATETIME NOT NULL,
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
                    "accountProgress",
                    "activityRecord"
                ],
            )

            connection.commit()

    except Exception as exc:
            print("Wah! Error occurred while getting a DB for '{}':\n\t{}".format(
                name, str(exc)))

    finally:
        if connection:
            # close the open connection
            connection.close()

def select_usernames_for_date(address, date):
    names = []

    conn = sqlite3.connect(address)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usernames WHERE cal_date=:cal_date", {"cal_date":date})
    
    rows = cursor.fetchall()

    if conn:
        conn.close()

    for r in rows:
        names.append(r[1]) 

    return(names)

def select_usernames_for_date_range(address, date_range):
    date_range = list(map(str, date_range))

    usernames = []

    for date in date_range:
        names = select_usernames_for_date(address, date)
        usernames.append(names)

    return(usernames)

def select_blacklist_from_usernames(address, ratio_limit):
    blacklist = []

    conn = sqlite3.connect(address)
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM usernames WHERE f2f_ratio>:ratio_limit", {"ratio_limit":ratio_limit})

    rows = cursor.fetchall()

    for row in rows:
        blacklist.append(row[0])

    conn.close()

    return(blacklist)

def select_username_from_table(address, username):
    date_range = list(map(str, date_range))

    conn = sqlite3.connect(address)
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM usernames WHERE username=:username", {"username":username})
    records = cursor.fetchall()

    return(records)

def create_tables(cursor, tables):
    if "usernames" in tables:
        cursor.execute(SQL_CREATE_USERNAMES_TABLE)

    if "recordActivity" in tables:
        cursor.execute(SQL_CREATE_ACTIVITY_RECORD_TABLE)

    if "accountProgress" in tables:
        cursor.execute(SQL_CREATE_ACCOUNT_PROGRESS_TABLE)

def add_data(address, table, data):

    conn = sqlite3.connect(address)
    cursor = conn.cursor()

    try:
        if table == "usernames":
            task = "INSERT INTO usernames(username,followers,following,f2f_ratio,status,cal_date) VALUES (?,?,?,?,?,?)"

        elif table == 'accountProgress':
            task = "INSERT INTO accountProgress(cal_date,followers,following,f2f_ratio) VALUES (?,?,?,?)"

        elif table == 'activityRecord':
            task = "INSERT INTO activityRecord(cal_date,time_elapsed,profiles_engaged,comments,likes) VALUES (?,?,?,?,?)"
    except:
        print('ProgrammingError occurred')

    cursor.execute(task, data)

    conn.commit()

def update_username_record(address, username, data):

    conn = sqlite3.connect(address)
    cursor = conn.cursor()

    task = "INSERT OR REPLACE INTO usernames(username, followers, following, f2f_ratio,status,cal_date) VALUES (?,?,?,?,?,?)"

    cursor.execute(task, data)

    conn.commit()
    conn.close()

def delete_username(address, username):

    conn = sqlite3.connect(address)
    cursor = conn.cursor

    task = "DELETE from usernames WHERE username=:username"

