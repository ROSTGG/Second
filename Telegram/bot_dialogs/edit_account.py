import requests
from aiogram.enums import ContentType
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, LaunchMode, Window, DialogManager
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button, SwitchTo, Column, Select, Start, RequestLocation, Row
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory, MarkupFactory
from aiogram_dialog.widgets.text import Const, Format
from aiogram import Bot, Dispatcher, types, Router, F
from Telegram.common_function import name_city

from Telegram.bot_dialogs.data import *
from Telegram.bot_dialogs.getter import getter_profil
from Telegram.bot_dialogs.states import EditAccount, Menu
from Telegram.bd_functions.bd import create_row, get_line_user, update_line_user
from Telegram.bd_functions.db_user_temp import create_row_temp, get_line_user_temp, update_line_user_temp, delete_line_user_temp

def id_getter(istr: Istr) -> str:
    return istr.id

CANCEL_EDIT = SwitchTo(
    Const("Отменить редактирование"),
    id="cnl_edt",
    state=EditAccount.preview,
)
# "name": dialog_manager.find("name").get_value(),
# "city": dialog_manager.find("city").get_value(),
# "genre": genre,
# "first_instrument": first_instrument,
# "choice_instrument": choice_instrument,
# "choice": choice,
# "experience": dialog_manager.find("experience").get_value(),
# "description": dialog_manager.find("description").get_value(),
# "link": dialog_manager.find("link").get_value(),

async def step_go_edit_akkount(callback: CallbackQuery, widget, dialog_manager: DialogManager):
    # global data.object_dialog_manager
    data_list = get_line_user(callback.from_user.id)
    create_row_temp(callback.from_user.id, data_list[2], data_list[3],
                    data_list[4], data_list[5], data_list[6], data_list[7],
                    data_list[8], data_list[9], data_list[10])

    # dialog_manager.dialog_data[Data_update_list] = data_list
    # print(data_list)
    # print(data_list[3])
    # dialog_manager.dialog_data[t_data_name] = data_list[2]
    # dialog_manager.dialog_data[t_data_city] = data_list[3]
    # dialog_manager.dialog_data[t_data_genre] = data_list[4]
    # dialog_manager.dialog_data[t_data_first_instrument] = data_list[5]
    # dialog_manager.dialog_data[t_data_choice_instrument] = data_list[6]
    # dialog_manager.dialog_data[t_data_choice] = data_list[7]
    # dialog_manager.dialog_data[t_data_experience] = data_list[8]
    # dialog_manager.dialog_data[t_data_description] = data_list[9]
    # dialog_manager.dialog_data[t_data_link] = data_list[10]
    # data.object_dialog_manager = dialog_manager
    #
    # print(dialog_manager.dialog_data.get(t_data_name))
    await dialog_manager.start(EditAccount.preview)

async def step_name(callback: CallbackQuery, widget, dialog_manager: DialogManager,item_id: str, *_):
    # dialog_manager.dialog_data[choice_KEY] = item_id
    # dialog_manager.dialog_data[t_data_name] = item_id
    if len(item_id) < 31:
        data = get_line_user_temp(dialog_manager.event.from_user.id)
        update_line_user_temp(dialog_manager.event.from_user.id, item_id, data[3], data[4], data[5], data[6], data[7],
                              data[8], data[9], data[10])
        await dialog_manager.switch_to(EditAccount.preview)
    else:
        await callback.answer("Введите имя по короче меньше 30 сиволов включая побелы")
        await dialog_manager.switch_to(EditAccount.name)

async def step_city(message: types.Message, dialog: Dialog, manager: DialogManager):
    # dialog_manager.dialog_data[t_data_city] = item_id
    if message.content_type == ContentType.LOCATION:
        location = message.location
        # user_data[message.from_user.id][LOCATION] = (location.latitude, location.longitude)
        # await message.answer(f"Вы отправили геопозицию:\nШирота: {location.latitude}\nДолгота: {location.longitude}")
        data = get_line_user_temp(manager.event.from_user.id)
        update_line_user_temp(manager.event.from_user.id, data[2], f"{location.latitude};{location.longitude}", data[4], data[5], data[6], data[7],
                                  data[8], data[9], data[10])
        # await manager.done()
        await manager.switch_to(EditAccount.preview)

    # if len(item_id) <= 100:
    #     data = get_line_user_temp(dialog_manager.event.from_user.id)
    #     update_line_user_temp(dialog_manager.event.from_user.id, data[2], item_id, data[4], data[5], data[6], data[7],
    #                           data[8], data[9], data[10])
    #     await dialog_manager.switch_to(EditAccount.preview)
    # else:
    #     await callback.answer("Введите город по короче меньше 100 сиволов включая побелы")
    #     await dialog_manager.switch_to(EditAccount.name)
async def step_genre(callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str, *_):
    # dialog_manager.dialog_data[t_data_genre] = item_id
    data = get_line_user_temp(dialog_manager.event.from_user.id)
    update_line_user_temp(dialog_manager.event.from_user.id, data[2], data[3], item_id, data[5], data[6], data[7], data[8], data[9], data[10])

    await dialog_manager.switch_to(EditAccount.preview)

async def step_first_instrument(callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str, *_):
    # dialog_manager.dialog_data[t_data_first_instrument] = item_id
    data = get_line_user_temp(dialog_manager.event.from_user.id)
    update_line_user_temp(dialog_manager.event.from_user.id, data[2], data[3], data[4], item_id, data[6], data[7], data[8], data[9], data[10])

    await dialog_manager.switch_to(EditAccount.preview)
async def step_choice_instrument(callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str, *_):
    # dialog_manager.dialog_data[t_data_choice_instrument] = item_id
    data = get_line_user_temp(dialog_manager.event.from_user.id)
    update_line_user_temp(dialog_manager.event.from_user.id, data[2], data[3], data[4], data[5], item_id, data[7], data[8], data[9], data[10])

    await dialog_manager.switch_to(EditAccount.preview)

async def step_choice(callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str, *_):
    # dialog_manager.dialog_data[t_data_choice] = item_id
    if item_id == "True": item_id = True
    elif item_id == "False": item_id = False
    data = get_line_user_temp(dialog_manager.event.from_user.id)
    update_line_user_temp(dialog_manager.event.from_user.id, data[2], data[3], data[4], data[5], data[6], item_id, data[8], data[9], data[10])

    await dialog_manager.switch_to(EditAccount.preview)
async def step_experience(callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str, *_):
    # dialog_manager.dialog_data[t_data_experience] = item_id
    try:
        if item_id.split(".")[0].isdigit() == False:
            raise Exception
        elif item_id.split(".")[1].isdigit() == False:
            raise Exception
        elif int(item_id.split(".")[1]) > 12:
            await callback.answer("дед у нас 12 месяцев https://www.youtube.com/watch?v=MxEc7YWJCvk")
            await dialog_manager.switch_to(EditAccount.experience)
        elif int(item_id.split(".")[0]) >= 90:
            await callback.answer("прости дед у нас максимум 90 лет")
            await dialog_manager.switch_to(EditAccount.experience)
        else:
            data = get_line_user_temp(dialog_manager.event.from_user.id)
            update_line_user_temp(dialog_manager.event.from_user.id, data[2], data[3], data[4], data[5], data[6], data[7],
                                  item_id, data[9], data[10])
            await dialog_manager.switch_to(EditAccount.preview)
    except:
        await callback.answer("Вы ввели данное значение не правильно, пожалуйста внимателенее прочитайте пример!")
        await dialog_manager.switch_to(EditAccount.experience)


async def step_description(callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str, *_):
    # dialog_manager.dialog_data[t_data_description] = item_id
    if len(item_id) < 300:
        data = get_line_user_temp(dialog_manager.event.from_user.id)
        update_line_user_temp(dialog_manager.event.from_user.id, data[2], data[3], data[4], data[5], data[6], data[7], data[8], item_id, data[10])
        await dialog_manager.switch_to(EditAccount.preview)
    else:
        await callback.answer("Введите описание по короче меньше 300 сиволов включая побелы")
        await dialog_manager.switch_to(EditAccount.description)


async def step_link(callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str, *_):
    try:
        check = requests.get(item_id).status_code
        if check == 404:
            await callback.answer("НЕ КОРЕКТНАЯ ССЫЛКА небыло получено ответа от сайта")
            await dialog_manager.switch_to(EditAccount.link)
        else:
            # dialog_manager.dialog_data[t_data_link] = item_id
            data = get_line_user_temp(dialog_manager.event.from_user.id)
            update_line_user_temp(dialog_manager.event.from_user.id, data[2], data[3], data[4], data[5], data[6],
                                  data[7], data[8], data[9], item_id)

            await dialog_manager.switch_to(EditAccount.preview)
    except:
        await callback.answer("НЕ КОРЕКТНАЯ ССЫЛКА пример:https://github.com/ROSTGG")
        await dialog_manager.switch_to(EditAccount.link)

    # await next_or_end(event, widget, dialog_manager, *_)
# async def finaly_link(event, widget, dialog_manager: DialogManager, item_id: str, *_):
#     dialog_manager.dialog_data[FINISHED_KEY] = True
#     await dialog_manager.switch_to(Wizard.preview)
    # await next_or_end(event, widget, dialog_manager, *_)
# async def step_Ffind(event, widget, dialog_manager: DialogManager,item_id: str, *_):
#     dialog_manager.dialog_data["Ffind_id"] = item_id
#     await next_or_end(event, widget, dialog_manager, *_)

async def result_getter(dialog_manager: DialogManager, **kwargs):
    print("from result_setter: " + str(dialog_manager.event.from_user.id))
    # print("result_getter: " + str(dialog_manager.dialog_data.get(t_data_name)))
    data = list(get_line_user_temp(dialog_manager.event.from_user.id))
    # data = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", ]
    getter_data = await getter_profil()
    for i in getter_data[genre_KEY]:
        if i.id == data[4]:
            data[4] = i.name
    for i in getter_data[Instrument_KEY]:
        if i.id == data[5]:
            data[5] = i.name
    for i in getter_data[Instrument_KEY]:
        if i.id == data[6]:
            data[6] = i.name
    if 1 == data[7]:
        data[7] = "Да"
    else:
        data[7] = "Нет"

    return {
        "name": data[2],
        "city": name_city(data[3]),
        "genre": data[4],
        "first_instrument": data[5],
        "choice_instrument": data[6],
        "choice": data[7],
        "experience": data[8],
        "description": data[9],
        "link": data[10],
    }


async def EditAccount_user(callback: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    print("Пользоваетль начал обновление")
    print("TG_ID" + str(callback.from_user.id))
    # print(f"name: {dialog_manager.dialog_data.get(t_data_name)}\n",
    #     f"city: {dialog_manager.dialog_data.get(t_data_city)}\n",
    #     f"genre: {dialog_manager.dialog_data.get(t_data_genre)}\n",
    #     f"first_instrument: {dialog_manager.dialog_data.get(t_data_first_instrument)}\n",
    #     f"choice_instrument: {dialog_manager.dialog_data.get(t_data_choice_instrument)}\n",
    #     f"choice: {dialog_manager.dialog_data.get(t_data_choice)}\n",
    #     f"experience: {dialog_manager.dialog_data.get(t_data_experience)}\n",
    #     f"description: {dialog_manager.dialog_data.get(t_data_description)}\n",
    #     f"link: {dialog_manager.dialog_data.get(t_data_link)}\n")
    data = get_line_user_temp(dialog_manager.event.from_user.id)

    update_line_user(dialog_manager.event.from_user.id, data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
    delete_line_user_temp(dialog_manager.event.from_user.id)
    # data = update_line_user(tg_id=callback.from_user.id,
    #            name=dialog_manager.dialog_data.get(t_data_name),
    #            city=dialog_manager.dialog_data.get(t_data_city),
    #            genre = dialog_manager.dialog_data.get(t_data_genre),
    #            main_inst = dialog_manager.dialog_data.get(t_data_first_instrument),
    #            choice_inst = dialog_manager.dialog_data.get(t_data_choice_instrument),
    #            choice = dialog_manager.dialog_data.get(t_data_choice),
    #            exp = dialog_manager.dialog_data.get(t_data_experience),
    #            des = dialog_manager.dialog_data.get(t_data_description),
    #            link = dialog_manager.dialog_data.get(t_data_link))
    await callback.answer("Обновление завершено")
    await dialog_manager.start(Menu.MAIN)
async def cancel_edit(callback: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    delete_line_user_temp(dialog_manager.event.from_user.id)
    await dialog_manager.start(Menu.MAIN)

# choice_window = Window(
# Const("Вы группа или музыкант?"),
#         Select(
#             text=Format("{item.emoji} {item.name}"),
#             id="choice",
#             items=Choice_KEY,
#             # Alternatives:
#             # items=lambda d: d[OTHER_KEY][FRUITS_KEY],  # noqa: E800
#             # items=F[OTHER_KEY][FRUITS_KEY],  # noqa: E800
#             item_id_getter=id_getter,
#             on_click=step_choice,
#         ),
#         CANCEL_EDIT,
#         state=Wizard.choice,
#         getter=getter,
#         preview_data=getter,
#         )
name_window = Window(
    Const("Введите своё имя:"),
    TextInput(id="name", on_success=step_name),
    CANCEL_EDIT,
    state=EditAccount.name,
)

user_data = {}
# async def get_location(message: types.Message, dialog: Dialog, manager: DialogManager):
#     if message.content_type == ContentType.LOCATION:
#         location = message.location
#         user_data[message.from_user.id] = (location.latitude, location.longitude)
#         await message.answer(f"Вы отправили геопозицию:\nШирота: {location.latitude}\nДолгота: {location.longitude}")
#         await manager.done()
city_window = Window(
    Const("Отправьте вашу геолокацию с помощью кнопки ниже!"),
    RequestLocation(Const("📍 Send location")),
    MessageInput(step_city, content_types=ContentType.LOCATION),
    # TextInput(id="city", on_success=step_city),
    CANCEL_EDIT,
    markup_factory=ReplyKeyboardFactory(
            input_field_placeholder=Format("{event.from_user.username}"),
            resize_keyboard=True,),
    state=EditAccount.city,
)



genre_window = Window(
    Const("Выберите любимый жанр:"),
    Column(
    Select(
        text=Format("{item.emoji} {item.name}"),
        id="genre",
        items=genre_KEY,
        # Alternatives:
        # items=lambda d: d[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        # items=F[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        item_id_getter=id_getter,
        on_click=step_genre,
    ),
CANCEL_EDIT
),
    state=EditAccount.genre,
    getter=getter_profil,
    preview_data=getter_profil,
)
first_instrument_window = Window(
    Const("Выберите основной музыкальный инструмент:"),
    Column(
    Select(
        text=Format("{item.emoji} {item.name}"),
        id="first_instrument",
        items=Instrument_KEY,
        # Alternatives:
        # items=lambda d: d[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        # items=F[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        item_id_getter=id_getter,
        on_click=step_first_instrument,
    ),
        CANCEL_EDIT),
    state=EditAccount.first_instrument,
    getter=getter_profil,
    preview_data=getter_profil,
)
choice_instrument_window = Window(
    Const("Выберите дополнительный музыкальный инструмент:"),
    Column(
    Select(
        text=Format("{item.emoji} {item.name} ("),
        id="choice_instrument",
        items=Instrument_KEY,
        # Alternatives:
        # items=lambda d: d[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        # items=F[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        item_id_getter=id_getter,
        on_click=step_choice_instrument,
    ),
        CANCEL_EDIT),
    state=EditAccount.choice_instrument,
    getter=getter_profil,
    preview_data=getter_profil,
)
# choice_isFind_window = Window(
#     Const("Выберите :"),
#     Select(
#         text=Format("{item.emoji} {item.name} ("),
#         id=isFind_KEY,
#         items=isFind_KEY,
#         # Alternatives:
#         # items=lambda d: d[OTHER_KEY][FRUITS_KEY],  # noqa: E800
#         # items=F[OTHER_KEY][FRUITS_KEY],  # noqa: E800
#         item_id_getter=id_getter,
#         on_click=step_isFind,
#     ),
#     CANCEL_EDIT,
#     state=Wizard.isFind,
#     getter=getter,
#     preview_data=getter,
# )
choice_window = Window(
Const("Вы состоите в группе?"),
            Select(
            text=Format("{item.emoji} {item.name}"),
            id="choice",
            items=Choice_group_KEY,
            # Alternatives:
            # items=lambda d: d[OTHER_KEY][FRUITS_KEY],  # noqa: E800
            # items=F[OTHER_KEY][FRUITS_KEY],  # noqa: E800
            item_id_getter=id_getter,
            on_click=step_choice,
            ),
        CANCEL_EDIT,
        state=EditAccount.choice,
        getter=getter_profil,
        preview_data=getter_profil,
        )
experience_window = Window(
    Const("Введите стаж пример(пять лет и одинадцать месяцев): 5.11:"),
    TextInput(id="experience", on_success=step_experience),
    CANCEL_EDIT,
    state=EditAccount.experience,
)
description_window = Window(
    Const("Введите описание:"),
    TextInput(id="description", on_success=step_description),
    CANCEL_EDIT,
    state=EditAccount.description,
)
link_window = Window(
    Const("Введите ссылку на публичную страницу:"),
    TextInput(id="link", on_success=step_link),
    CANCEL_EDIT,
    state=EditAccount.link,
)
exit_window = Window(
    Const("Пожалуйста, проверте введённые данные"),
    Format("Name: {name}"),
    Format("City: {city}"),
    Format("Жанр: {genre}"),
    Format("Основной музыкальный инструмент: {first_instrument}"),
    Format("Дополнительный музыкальный инструмент: {choice_instrument}"),
    Format("isFind: {choice}"),
    Format("Стаж: {experience}"),
    Format("Description: {description}"),
    Format("Link: {link}"),
    SwitchTo(
        Const("Изменить название"),
        state=EditAccount.name, id="to_name",
    ),
    SwitchTo(
        Const("Изменить город"),
        state=EditAccount.city, id="to_city",
    ),
    SwitchTo(
        Const("Изменить жанр"),
        state=EditAccount.genre, id="to_genre",
    ),
    SwitchTo(
        Const("Изменить основной музыкальный инструмент"),
        state=EditAccount.first_instrument, id="to_first_instrument",
    ),
    SwitchTo(
        Const("Изменить дополнительный музыкальный инструмент"),
        state=EditAccount.choice_instrument, id="to_choise_instrument",
    ),
    SwitchTo(
        Const("Изменить статус"),
        state=EditAccount.choice, id="to_choice",
    ),
    SwitchTo(
        Const("Изменить стаж"),
        state=EditAccount.experience, id="to_isFind",
    ),
    SwitchTo(
        Const("Изменить описание"),
        state=EditAccount.description, id="to_description",
    ),
    SwitchTo(
        Const("Изменить ссылку на публичную страницу"),
        state=EditAccount.link,
        id="to_link",
    ),
    Button(
        Const("Сохранить"),
        id="to_save",
        on_click=EditAccount_user,
    ),
    Button(
        Const("Отмена"),
        on_click=cancel_edit,
        id="to_cancel_main"),
    state=EditAccount.preview,
    getter=result_getter,
    # getter=get_call_data,
    parse_mode="html",
    )

EditAccount_dialog = Dialog(
                name_window,
                city_window,
                genre_window,
                first_instrument_window,
                choice_instrument_window,
                choice_window,
                experience_window,
                description_window,
                link_window,
                exit_window,
                launch_mode=LaunchMode.ROOT,)

