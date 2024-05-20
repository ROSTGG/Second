from Telegram.bot_dialogs.data import *

@dataclass
class Ibdstr:
    id: str
    info: str
    info_but: str
import sqlite3

def search(instrument: str, tg_id: int) -> list:

    #Connection
    conn = sqlite3.connect('../data/second.SQLite')
    cur = conn.cursor()

    #Get City
    cur.execute("SELECT city, genre FROM Clients WHERE tg_id = ?", (tg_id,))
    data = cur.fetchall()[0]
    city, genre = data[0], data[1]

    #Get Nearby City
    # cur.execute("SELECT nearby_cities FROM Cities WHERE city = ?", (city,))
    # nearby_cities = cur.fetchall()[0]
    nearby_cities = ['Москва', 'Игумново']



    #Search DATA By City
    data = []
    cur.execute("SELECT main_inst, choice_inst, genre, tg_id FROM Clients WHERE city = ? and tg_id != ?", (city, tg_id, ))
    try:
        for i in cur.fetchall():
            data.append(i)
    except:
        return False

    points = [3 for _ in range(len(data))]

    count = 0

    for n_city in nearby_cities:
        cur.execute("SELECT main_inst, choice_inst, genre, tg_id FROM Clients WHERE city = ?", (n_city,))
        try:
            data.append(cur.fetchall()[0])
            count += 1
        except:
            pass

    points += [2 for _ in range(count)]




    for i in data:
        if i[0] == instrument:
            points[data.index(i)] += 2
        elif i[1] == instrument:
            points[data.index(i)] += 1

        if i[2] == genre:
            points[data.index(i)] += 1

    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if points[j] < points[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                points[j], points[j + 1] = points[j + 1], points[j]

    ans = []
    for i in data:
        print(i, points[data.index(i)])
        cur.execute("SELECT * FROM Clients WHERE tg_id = ?", (i[3],))
        ans.append(form(cur.fetchall()[0]))

    return ans




def form(card):
    # trans = trans or Translator(from_lang='en', to_lang='ru')
    data = getter_data_dict
    card = list(card)
    for i in data[genre_KEY]:
        if i.id == card[4]:
            card[4] = i.name
    for i in data[Instrument_KEY]:
        if i.id == card[5]:
            card[5] = i.name
    for i in data[Instrument_KEY]:
        if i.id == card[6]:
            card[6] = i.name
    card = tuple(card)
    data = Ibdstr(card[1],f'''{card[2]} - {card[3]}
Основной инструмент - {card[5]}
Дополнительный инструмент - {card[6]}
Стаж -  годов - {card[8].split(".")[0]},  месяцев - {card[8].split(".")[1]}
Жанр - {str(card[4] + " music")}
О себе - "{card[9]}"
Ссылка на публичную страницу - {card[10]}
''', f"{card[2]}")
    return data


# for i in search('An_electro-pediatrician', int(input('Enter TG id: '))):
#     print(i.info)