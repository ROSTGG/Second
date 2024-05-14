from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Button, Column, Select, NextPage, PrevPage, Row

from Telegram.bot import send_notification
from Telegram.enter_bot_value import bot
from Telegram.bd import Session, get_line_user
from Telegram.bot_dialogs.common import MAIN_MENU_BUTTON
from Telegram.bot_dialogs.data import *
from Telegram.bot_dialogs.getter import getter_profil
from Telegram.bot_dialogs.states import Search_m
from Telegram.db_user_info import get_line_userinfo
# from Telegram.bd import create_row, get_line_user, update_line_user
from Telegram.logic.search_function import search, Ibdstr
from aiogram_dialog.widgets.text import Const, Format, List

bot = bot
temp_instrument = {}
temp_id = {}
temp_id_user_info = None
# bot = Bot(token="6752526100:AAFCSA3zE7LTV88AP68ozKPd90DxJ14Upks")
def id_getter(istr: Ibdstr) -> str:
    return istr.id
# json_file_path = "temp_instrument.json"
# Функция для записи данных в JSON файл
# def load_json(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             data = json.load(file)
#     except FileNotFoundError:
#         data = []  # Если файл не существует, создаем пустой список для начала
#     return data
# def read_from_json():
#     with open(json_file_path, 'r') as file:
#         data = json.load(file)
#         return data
#
# def write_to_json(id, data):
#     existing_data = read_from_json()
#
#     # Добавление новых данных к загруженным
#     set_data = {id: data}
#     existing_data.append(set_data)
#     with open(json_file_path, 'w') as file:
#         json.dump(set_data, file, indent=4)
# write_to_json(1151515111, "good bye")
# print(read_from_json())

# Функция для чтения данных из JSON файла
async def step_set_instrument(event, widget, dialog_manager: DialogManager, item_id: str, *_):
    # dialog_manager.dialog_data[t_data_genre] = item_id
    # data = get_line_user_temp(dialog_manager.event.from_user.id)
    temp_instrument[dialog_manager.event.from_user.id] = item_id
    await dialog_manager.switch_to(Search_m.MAIN)


session = Session('Telegram/data')
async def getter_one(dialog_manager: DialogManager, **kwargs):
    data = search(temp_instrument[dialog_manager.event.from_user.id], dialog_manager.event.from_user.id,session)
    temp = []
    for i in data:
        temp.append(i.id)
        # id_t, text = i.id, i.info
        # print(text)
    temp_id[dialog_manager.event.from_user.id] = temp

    return {
        find_user_KEY:
            # Ibdstr("132121351", "dfiogjdiojsgi"),
            # Ibdstr("132121351", "dfiogjdiojsgi"),
            # Ibdstr("132121351", "dfiogjdiojsgi"),
            # Ibdstr("132121351", "dfiogjdiojsgi")

            data
    }
async def enter_user(event, widget, manager: DialogManager, **kwargs):
    widget = manager.find('scroll_no_pager')
    # print(await widget.get_page())
    data = temp_id[manager.event.from_user.id][await widget.get_page()]
    # print(data)
    # print(manager.event.from_user)
    info = get_line_userinfo(data)
    # info = get_line_userinfo(manager.event.from_user.id)
    # await manager.answer_callback()

    info_me = get_line_userinfo(manager.event.from_user.id)
    card = get_line_user(data)
    await send_notification(False, manager.event.from_user.id, f'''Вы выбрали @{info[2]}
    {card[2]} - {card[3]}
Основной инструмент - {card[5]}
Дополнительный инструмент - {card[6]}
Стаж -  годов - {card[8].split(".")[0]},  месяцев - {card[8].split(".")[1]}
Жанр - {str(card[4] + " music")}
О себе - "{card[9]}"
Ссылка на публичную страницу - {card[10]}''')

    datas = getter_data_dict
    card = get_line_user(manager.event.from_user.id)
    card = list(card)
    for i in datas[genre_KEY]:
        if i.id == card[4]:
            card[4] = i.name
    for i in datas[Instrument_KEY]:
        if i.id == card[5]:
            card[5] = i.name
    for i in datas[Instrument_KEY]:
        if i.id == card[6]:
            card[6] = i.name
    card = tuple(card)

    await send_notification(True, data, f'''Вас выбрал @{info_me[2]}
{card[2]} - {card[3]}
Основной инструмент - {card[5]}
Дополнительный инструмент - {card[6]}
Стаж -  годов - {card[8].split(".")[0]},  месяцев - {card[8].split(".")[1]}
Жанр - {str(card[4] + " music")}
О себе - "{card[9]}"
Ссылка на публичную страницу - {card[10]}
    ''')


window_one = Window(
    Const("Выберете инcтрумент:"),
    Column(
    Select(
        text=Format("{item.emoji} {item.name}"),
        id="first_instrument",
        items=Instrument_KEY,
        # Alternatives:
        # items=lambda d: d[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        # items=F[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        item_id_getter=id_getter,
        on_click=step_set_instrument,
    )),
    MAIN_MENU_BUTTON,
    getter=getter_profil,
    preview_data=getter_profil,
    state=Search_m.EnterInstrument,
)
window_view = Window(
    Const("See:"),
    # Const("Scrolling group with default pager (legacy mode)"),
    List(
        Format("{item.info}"),
        items=find_user_KEY,
        id="scroll_no_pager",
        page_size=1,
        # item_id_getter=id_getter
    ),
    # Row(
    #
    #     FirstPage(
    #         scroll="scroll_no_pager", text=Format("⏮️ {target_page1}"),
    #     ),
    #     PrevPage(
    #         scroll="scroll_no_pager", text=Format("◀️"),
    #     ),
    #     CurrentPage(
    #         scroll="scroll_no_pager", text=Format("{current_page1}"),
    #     ),
    #     NextPage(
    #         scroll="scroll_no_pager", text=Format("▶️"),
    #     ),
    #     LastPage(
    #         scroll="scroll_no_pager", text=Format("{target_page1} ⏭️"),
    #     ),
    # ),
    # NumberedPager(
    #     scroll="scroll_no_pager",
    # ),

    Row(
        PrevPage(scroll="scroll_no_pager"),
        Button(Const("выбрать"), id="next_page", on_click=enter_user),
        NextPage(scroll="scroll_no_pager"),
    ),
    MAIN_MENU_BUTTON,
    getter=getter_one,
    preview_data=getter_one,
    state=Search_m.MAIN,
)
# window_preview = Window(
#     Format("{item}"),
# #     Format("{item.info}"),
# #     items=find_user_KEY,
# #     id="view_musiciants",
# #     item_id_getter=id_getter,
# #     on_click=step_view_user,
# # ),
#     # Const("Scrolling group with default pager (legacy mode)"),
#     MAIN_MENU_BUTTON,
#     getter=getter_two,
#     state=Search_m.MAIN,
# )
# dialog_search = Dialog(window_one,window_view, launch_mode=LaunchMode.ROOT)