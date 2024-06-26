import sqlite3 as sql

import requests
from typing import Literal


# hi
# hi, i'm ROSTGG (Rostislav)
def create_row_userinfo(tg_id: int, user_name: str, black_list: list, event_datatime: str):
    bd = sql.connect("Telegram/data/second_user_info.SQLite")

    cursor = bd.cursor()
    try:
        black_list = '.'.join(black_list)
    except:
        black_list = 'NOT'

    cursor.execute('''
CREATE TABLE IF NOT EXISTS Clients (
id INTEGER PRIMARY KEY,
tg_id INTEGER NOT NULL,
user_name TEXT NOT NULL,
black_list TEXT NOT NULL,        
event_datatime TEXT NOT NULL)''')

    bd.commit()

    cursor.execute('INSERT INTO Clients (tg_id, user_name, black_list, event_datatime) VALUES (?, ?, ?, ?)',
                   (tg_id, user_name,black_list,event_datatime))

    bd.commit()
    bd.close()

    return 'All Upload'


OperatorFilter = Literal["=", ">", "<", "!=", "<=", ">="]



# res = get_data_from_hole('tg_id', '=', 34252345, *['name', 'city'])

# print(res)
def isRegisterUser_userinfo(TgId: int):
    bd = sql.connect('Telegram/data/second_user_info.SQLite')
    cursor = bd.cursor()
    cursor.execute('SELECT tg_id FROM Clients WHERE tg_id = ?', (TgId,))
    data = cursor.fetchall()
    bd.close()
    if len(data) == 0:
        return False
    else:
        return True


def get_line_userinfo(TgId: int):
    bd = sql.connect('Telegram/data/second_user_info.SQLite')
    cursor = bd.cursor()
    cursor.execute('SELECT * FROM Clients WHERE tg_id = ?', (TgId,))
    data = cursor.fetchall()
    bd.close()
    try:
        return data[0]
    except:
        return data
def get_line_userinfo_username(username: str):
    bd = sql.connect('Telegram/data/second_user_info.SQLite')
    cursor = bd.cursor()
    cursor.execute('SELECT * FROM Clients WHERE user_name = ?', (username,))
    data = cursor.fetchall()
    bd.close()
    return data[0]


def update_line_userinfo(tg_id: int, user_name: str, black_list: list, event_datatime: str):
    bd = sql.connect('Telegram/data/second_user_info.SQLite')
    try:
        black_list = '.'.join(black_list)
    except:
        black_list = 'NOT'
    cursor = bd.cursor()
    cursor.execute("SELECT user_name FROM Clients WHERE tg_id = ?", (tg_id,))
    data = cursor.fetchall()
    if len(data) == 0:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clients (
        id INTEGER PRIMARY KEY,
        tg_id INTEGER NOT NULL,
        user_name TEXT NOT NULL,
        black_list TEXT NOT NULL,
        event_datatime TEXT NOT NULL,
        )''')
        cursor.execute('INSERT INTO Clients (tg_id, user_name, black_list, event_datatime) VALUES (?, ?, ?, ?)',
                       (tg_id, user_name, black_list, event_datatime))
    else:
        cursor.execute(
            'UPDATE Clients SET user_name = ?,  black_list = ?, event_datatime = ?  WHERE tg_id = ?',
            (user_name, black_list, event_datatime, tg_id))
    # cursor.execute(
    #     'UPDATE Clients SET user_name = ?,  black_list = ?  WHERE tg_id = ?',
    #     (user_name, black_list, tg_id))
    bd.commit()
    bd.close()
def delete_line_userinfo(tg_id: int):
    print("Delete temp sql metod")
    bd = sql.connect('Telegram/data/second_user_info.SQLite')
    cursor = bd.cursor()
    cursor.execute('DELETE FROM Clients WHERE tg_id = ?', (tg_id,))
    bd.commit()
    bd.close()







