import sqlite3



def update():
    pass

def insert(insert_info):
    with sqlite3.connect('identifier.sqlite') as db:
        cursor = db.cursor()
        query1 = """ CREATE TABLE IF NOT EXISTS filesMatan(name TEXT PRIMARY KEY, id INTEGER) """
        query2 = """ INSERT INTO filesMatan (id, name) VALUES(?,?); """
        cursor.execute(query1)
        cursor.executemany(query2, insert_info)
        db.commit()

def get_id(name):
    with sqlite3.connect('identifier.sqlite')as db:
        cursor = db.cursor()
        query1 = """ CREATE TABLE IF NOT EXISTS filesMatan(name TEXT PRIMARY KEY, id INTEGER) """
        cursor.execute(query1)
        cursor.execute("SELECT id FROM filesMatan WHERE name = ?", (name,))
        data = cursor.fetchall()
        db.commit()
        if len(data) == 0:
            return 0
        return data[0][0]


def get_folder_id(name):
    with sqlite3.connect('identifier.sqlite')as db:
        cursor = db.cursor()
        query1 = """ CREATE TABLE IF NOT EXISTS foldersMatan(name TEXT PRIMARY KEY, id INTEGER) """
        cursor.execute(query1)
        cursor.execute("SELECT id FROM foldersMatan WHERE name = ?", (name,))
        data = cursor.fetchall()
        db.commit()
        if len(data) == 0:
            return 0
        return data[0][0]

def add_folder_id(idd, name):
    with sqlite3.connect('identifier.sqlite')as db:
        cursor = db.cursor()
        query1 = """ CREATE TABLE IF NOT EXISTS foldersMatan(name TEXT PRIMARY KEY, id INTEGER)"""
        query2 = f""" INSERT INTO foldersMatan (id, name) VALUES(?,?); """
        cursor.execute(query1)
        cursor.executemany(query2, [(idd, name)])
        db.commit()

def is_exists(name):
    with sqlite3.connect('identifier.sqlite')as db:
        cursor = db.cursor()
        query1 = """ CREATE TABLE IF NOT EXISTS foldersMatan(name TEXT PRIMARY KEY, id INTEGER) """
        cursor.execute(query1)
        cursor.execute("SELECT rowid FROM foldersMatan WHERE name = ?", (name,))
        data = cursor.fetchall()
        if len(data) == 0:
            return False
        else:
            return True
        db.commit()


