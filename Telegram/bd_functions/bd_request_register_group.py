import sqlite3 as sql

def get_group_from_id(id):
    conn = sql.connect('../data/second.SQLite')
    cur = conn.cursor()

    cur.execute('SELECT * FROM request_register_group WHERE id = ?', (id,))

    ans = cur.fetchall()
    ans[5] = ans[5].split('.')
    ans[6] = ans[6].split('.')

    return ans

# def get_card_from_id(id):
#     conn = sql.connect('../data/second.SQLite')
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM request_register_group WHERE id = ?', (id,))
#     group = cur.fetchall()[0]
#     users = ''
#     print(group)
#
#     for i in range(len(group[5].split("."))):
#         print(group[5].split(".")[i])
#         cur.execute('SELECT name FROM Clients WHERE tg_id = ?', (group[5].split(".")[i],))
#         users += f'\n           {cur.fetchall()[0][0]} - {group[6].split(".")[i]}'
#
#     cur.execute('SELECT name FROM Clients WHERE tg_id = ?', (group[4],))
#
#     admin = cur.fetchall()[0][0]
#
#     return f"""
# Название - {group[1]}
# Описание - {group[3]}
# Админ - {admin}
# Ссылка - {group[2]}
# Участники - {users}
# """

def  create_group(name: str, des: str, admin: int, link: str, users: list, inst: list):
    conn = sql.connect('../data/second.SQLite')

    cur = conn.cursor()

    cur.execute('''
CREATE TABLE IF NOT EXISTS request_register_group (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
link TEXT NOT NULL, 
des TEXT NOT NULL,
admin INTEGER NOT NULL,
users TEXT NOT NULL,
inst TEXT NOT NULL
)
''')

    us = '.'.join(users)
    ins = '.'.join(inst)

    cur.execute(
        'INSERT INTO request_register_group (name, link, des, admin, users, inst) 	VALUES (?, ?, ?, ?, ?, ?)',
        (name, link, des, admin, us, ins))
    conn.commit()
    conn.close()

def update_line_user(id, name: str, des: str, admin: int, link: str, users: list, inst: list):
    bd = sql.connect('../data/second.SQLite')
    cursor = bd.cursor()
    users = '.'.join(users)
    inst = '.'.join(inst)
    cursor.execute(
        'UPDATE request_register_group SET name = ?, link = ?, des = ?, admin = ?, users = ?, inst = ? WHERE id = ?',
        (name, link, des, admin, users, inst, id))
    bd.commit()
    bd.close()

