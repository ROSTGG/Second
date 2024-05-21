import sqlite3 as sql

import requests
from typing import Literal

class Session:
    def __init__(self, path: str):
        self.path = path
        self.connection = sql.connect(self.path + "/second.SQLite")
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.commit()
        self.connection.close()

    def create_row(self, tg_id: int, name: str, city: str,
                   genre: str, main_inst: str, choice_inst: str,
                   choice: bool, exp: str, des: str, link: str):

        if choice:
            choice = 1
        else:
            choice = 0

        check = requests.get(link)
        if check.status_code == 404:
            return 'Failed link'

        self.cursor.execute('''
	CREATE TABLE IF NOT EXISTS Clients (
	id INTEGER PRIMARY KEY,
	tg_id INTEGER NOT NULL,
	name TEXT NOT NULL,
	city TEXT NOT NULL,
	genre TEXT NOT NULL, 
	main_inst TEXT NOT NULL,
	choice_inst TEXT NOT NULL,
	choice INTEGER NOT NULL,
	exp TEXT NOT NULL,
	des TEXT NOT NULL, 
	link TEXT NOT NULL
	)
	''')

        self.cursor.execute(
            'INSERT INTO Clients (tg_id, name, city, genre, main_inst, choice_inst, choice, exp, des, link) 	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (tg_id, name, city, genre, main_inst,
             choice_inst, choice, exp, des, link))
        self.connection.commit()

        return 'All Upload'

    OperatorFilter = Literal["=", ">", "<", "!=", "<=", ">="]

    def isRegisterUser(self, TgId: int):
        self.cursor.execute('SELECT tg_id FROM Clients WHERE tg_id = ?', (TgId,))
        data = self.cursor.fetchall()

        if len(data) == 0:
            return False
        else:
            return True

    def get_line_user(self, TgId: int):
        self.cursor.execute('SELECT * FROM Clients WHERE tg_id = ?', (TgId,))
        data = self.cursor.fetchall()
        return data[0]

    def update_line_user(self, tg_id: int, name: str, city: str,
                         genre: str, main_inst: str, choice_inst: str,
                         choice: bool, exp: str, des: str, link: str):
        if choice:
            choice = 1
        else:
            choice = 0
        self.cursor.execute(
            'DELETE FROM Clients WHERE tg_id = ?',
            (tg_id,))
        self.connection.commit()
        self.cursor.execute(
            'INSERT INTO Clients (tg_id, name, city, genre, main_inst, choice_inst, choice, exp, des, link) 	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (tg_id, name, city, genre, main_inst, choice_inst, choice, exp, des, link))
        self.connection.commit()


def create_row(tg_id: int, name: str, city: str,
               genre: str, main_inst: str, choice_inst: str,
               choice: str, exp: str, des: str, link: str):
    bd = sql.connect("Telegram/data/second.SQLite")
    if str(choice) == "True" or choice == True:
        choice = 1
    else:
        choice = 0
    cursor = bd.cursor()

    check = requests.get(link)
    if check.status_code == 404:
        return 'Failed link'

    cursor.execute('''
CREATE TABLE IF NOT EXISTS Clients (
id INTEGER PRIMARY KEY,
tg_id INTEGER NOT NULL,
name TEXT NOT NULL,
city TEXT NOT NULL,
genre TEXT NOT NULL, 
main_inst TEXT NOT NULL,
choice_inst TEXT NOT NULL,
choice INTEGER NOT NULL,
exp TEXT NOT NULL,
des TEXT NOT NULL, 
link TEXT NOT NULL
)
''')

    cursor.execute(
        'INSERT INTO Clients (tg_id, name, city, genre, main_inst, choice_inst, choice, exp, des, link) 	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (tg_id, name, city, genre, main_inst,
         choice_inst, choice, exp, des, link))

    bd.commit()
    bd.close()

    return 'All Upload'


OperatorFilter = Literal["=", ">", "<", "!=", "<=", ">="]


def get_data_from_hole(hole='tg_id', oper: OperatorFilter = '=', value_hole='None', *args):
    bd = sql.connect('Telegram/data/second.SQLite')

    cursor = bd.cursor()

    req = ', '.join(args)

    if oper == '=':
        cursor.execute('SELECT ? FROM Clients WHERE ? = ?', (req, hole, value_hole))
    elif oper == '>':
        cursor.execute('SELECT ? FROM Clients WHERE ? > ?', (req, hole, value_hole))
    elif oper == '<':
        cursor.execute('SELECT ? FROM Clients WHERE ? < ?', (req, hole, value_hole))
    elif oper == '!=':
        cursor.execute('SELECT ? FROM Clients WHERE ? != ?', (req, hole, value_hole))
    elif oper == '<=':
        cursor.execute('SELECT ? FROM Clients WHERE ? <= ?', (req, hole, value_hole))
    elif oper == '>=':
        cursor.execute('SELECT ? FROM Clients WHERE ? >= ?', (req, hole, value_hole))
    else:
        return 'Invalid operator'
    results = cursor.fetchall()

    return results


# res = get_data_from_hole('tg_id', '=', 34252345, *['name', 'city'])

# print(res)
def isRegisterUser(TgId: int):
    bd = sql.connect('Telegram/data/second.SQLite')
    cursor = bd.cursor()
    cursor.execute('SELECT tg_id FROM Clients WHERE tg_id = ?', (TgId,))
    data = cursor.fetchall()
    bd.close()
    if len(data) == 0:
        return False
    else:
        return True

def get_line_user(TgId: int):
    bd = sql.connect('Telegram/data/second.SQLite')
    cursor = bd.cursor()
    cursor.execute('SELECT * FROM Clients WHERE tg_id = ?', (TgId,))
    data = cursor.fetchall()
    bd.close()
    return data[0]


def get_base():
    bd = sql.connect('Telegram/data/second.SQLite')
    cursor = bd.cursor()
    cursor.execute('SELECT * FROM Clients ', )
    data = cursor.fetchall()
    bd.close()
    return data


# print(get_base())

def update_line_user(tg_id: int, name: str, city: str,
                     genre: str, main_inst: str, choice_inst: str,
                     choice: bool, exp: str, des: str, link: str):
    if choice:
        choice = 1
    else:
        choice = 0
    bd = sql.connect('Telegram/data/second.SQLite')
    cursor = bd.cursor()

    cursor.execute(
        'UPDATE Clients SET name = ?, city = ?, genre = ?, main_inst = ?, choice_inst = ?, choice = ?, exp = ?, des = ?, link = ? WHERE tg_id = ?',
        (name, city, genre, main_inst, choice_inst, choice, exp, des, link, tg_id))
    bd.commit()
    bd.close()

# print(create_row(1041354810, '<rm>', '<NAME
# print(create_row(1041354810, '<rm>', '<NAME>', '<NAME>', '<NAME>', '<NAME>', 0, '<NAME>', '<NAME>', 'https://stackoverflow.com/questions/8919481/how-to-select-only-1-row-from-oracle-sql'))
# print(get_line_user(1041354810))
# update_line_user(1041354810, '<NAME>', '<NAME>', '<NAME>', '<NAME>', '<NAME>', 0, '<NAME>', '<NAME>', 'https://stackoverflow.com/questions/8919481/how-to-select-only-1-row-from-oracle-sql')
# print(get_line_user(1041354810))


# print(isRegisterUser(1041354811))
# print(get_line_user(1041354811)[2])
#
# self.cursor.execute(
# 	'INSERT INTO Clients (tg_id, name, city, genre, main_inst, choice_inst, choice, exp, des, link) 	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
# 	(tg_id, name, city, genre, main_inst,
# 	 choice_inst, choice, exp, des, link))
# CREATE TABLE IF NOT EXISTS Clients (
# id INTEGER PRIMARY KEY,
# tg_id INTEGER NOT NULL,
# name TEXT NOT NULL,
# city TEXT NOT NULL,
# genre TEXT NOT NULL,
# main_inst TEXT NOT NULL,
# choice_inst TEXT NOT NULL,
# choice INTEGER NOT NULL,
# exp TEXT NOT NULL,
# des TEXT NOT NULL,
# link TEXT NOT NULL
