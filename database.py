import sqlite3



def update():
    pass

def insert(insert_info):
    with sqlite3.connect('identifier.sqlite') as db:
        cursor = db.cursor()
        query1 = """ CREATE TABLE IF NOT EXISTS files(name TEXT PRIMARY KEY, id INTEGER) """
        query2 = """ INSERT INTO files (id, name) VALUES(?,?); """
        cursor.execute(query1)
        cursor.executemany(query2, insert_info)
        db.commit()

def get_id(name):
    with sqlite3.connect('identifier.sqlite')as db:
        cursor = db.cursor()
        query1 = """ CREATE TABLE IF NOT EXISTS files(name TEXT PRIMARY KEY, id INTEGER) """
        cursor.execute(query1)
        cursor.execute("SELECT id FROM files WHERE name = ?", (name,))
        data = cursor.fetchall()
        db.commit()
        if len(data) == 0:
            return 0
        return data[0][0]


def get_folder_id(name):
    with sqlite3.connect('identifier.sqlite')as db:
        cursor = db.cursor()
        query1 = """ CREATE TABLE IF NOT EXISTS folders(name TEXT PRIMARY KEY, id INTEGER) """
        cursor.execute(query1)
        cursor.execute("SELECT id FROM folders WHERE name = ?", (name,))
        data = cursor.fetchall()
        db.commit()
        if len(data) == 0:
            return 0
        return data[0][0]

def add_folder_id(idd, name):
    with sqlite3.connect('identifier.sqlite')as db:
        cursor = db.cursor()
        query1 = """ CREATE TABLE IF NOT EXISTS folders(name TEXT PRIMARY KEY, id INTEGER)"""
        query2 = f""" INSERT INTO folders (id, name) VALUES(?,?); """
        cursor.execute(query1)
        cursor.executemany(query2, [(idd, name)])
        db.commit()

def is_exists(name):
    with sqlite3.connect('identifier.sqlite')as db:
        cursor = db.cursor()
        query1 = """ CREATE TABLE IF NOT EXISTS folders(name TEXT PRIMARY KEY, id INTEGER) """
        cursor.execute(query1)
        cursor.execute("SELECT rowid FROM folders WHERE name = ?", (name,))
        data = cursor.fetchall()
        if len(data) == 0:
            return False
        else:
            return True
        db.commit()


