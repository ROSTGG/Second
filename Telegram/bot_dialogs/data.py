from dataclasses import dataclass

from aiogram import Bot

# from Telegram.bot_dialogs.getter import Istr

bot_main = Bot(token="6752526100:AAFCSA3zE7LTV88AP68ozKPd90DxJ14Upks")
bot_for_test = Bot(token="6952795171:AAEKXFIDlF8v0zdnKtWCSJrqnj9J26h9LMw")
bot_notification = Bot(token="7161720298:AAGJ9vqbd1upE9gerv-HHbas66woDOP_ExY")
Instrument_KEY = "instrument"
Choice_KEY = "choice_list"
Choice_group_KEY = "choice_group_list"
OTHER_KEY = "others"
genre_KEY = "genre_KEY"
instrument_KEY = "instrument_KEY"
main_instrument_KEY = "main_instrument_KEY"
choice_instrument_KEY = "choice_instrument_KEY"
second_instrument_KEY = "second_instrument_KEY"
FINISHED_KEY = "finished"
FINISHED_KEY_REGISTER = "finished_reg"
choice_KEY = "choice_id"
isFind_KEY = "isFind_id"
Data_update_list = "Data_update_list"
isAlredyRegister = "isAlredyRegister"
tg_id_user = "tg_id_user"
t_data_name = "t_name_data"
t_data_city = "t_data_city"
t_data_genre = "t_data_genre"
t_data_first_instrument = "t_data_first_instrument"
t_data_choice_instrument = "t_data_choice_instrument"
t_data_experience = "t_data_experience"
t_data_choice = "t_data_choice"
t_data_description = "t_data_description"
t_data_link = "t_data_link"
object_dialog_manager = None
find_user_KEY = "find_user_KEY"
@dataclass
class Istr:
    id: str
    name: str
    emoji: str
getter_data_dict = {
        Instrument_KEY: [
            Istr("Keyboards", "Клавишные", "🎹"),
            Istr("An_electro-pediatrician", "Электрогиатра", "🎸"),
            Istr("Acoustic_Guitar", "Акустическая Гитара", "🎸"),
            Istr("Bass_guitar", "Басс гитара", "🎸"),
            Istr("Drums", "Барабаны", "🥁"),
            Istr("Violin", "Скрипка", "🎶"),
            Istr("Brass_instruments", "Дўховные", "🎶"),
            Istr("Vokal", "Вокал", "🎶"),
            # Istr("Trumpet", "Труба", "🎺"),
            # Istr("Saxophone", "Саксофон", "🎷"),
            # Istr("Harpsichord", "Фортепиано", "🎹"),
            Istr("Cello", "Виолончель", "🎻"),
            # Istr("Clarinet", "Кларнет", "🎵"),
            Istr("None", "Нервы", "🎵"),
        ],

        # OTHER_KEY: {
        #     Instrument_KEY: [
        #         Istr("guitar", "piano", " "),
        #         Istr("piano", "guitar", " "),
        #         Istr("bass_guitar", "bass_guitar", " "),
        #         Istr("flueite", "flueite", " "), ]
        # },
        isFind_KEY: [
            Istr("yes", "Я пытаюсь найти группу", "✔"),
            Istr("no", "Я НЕ пытаюсь найти группу", "❌"),
        ],
        genre_KEY: [
            Istr("Rock", "Рок", "🎸"),
            Istr("Pop", "Поп", "🎤"),
            Istr("Metal", "Металл", "🔧"),
            Istr("Jazz", "Джаз", "🎺"),
            Istr("Classic", "Кассика", "🎻"),
            Istr("Electronic_music", "Электронная музыка", "🎹"),
            # Istr("Hip-hop", "Хип-хоп", "🎧"),
            # Istr("Rhythm_and_blues", "Ритм и блюз", "🎷"),
            # Istr("Country", "Кантри", "🤠"),
            # Istr("Gae", "Рэгги", "🇯🇲"),
            # Istr("Latin", "Латино", "💃🎶"),
        ],
        # Choice_KEY: [
        #     Istr("person", "Музыкант", "🎶"),
        #     Istr("group", "Группа", "🧾"),
        # ],
        Choice_group_KEY: [
            Istr("True", "Да", "✔"),
            Istr("False", "Нет", "❌"),
        ]
        }