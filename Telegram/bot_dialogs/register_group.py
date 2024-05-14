import requests
from aiogram import F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, LaunchMode, Window, DialogManager, StartMode
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, SwitchTo, Column, Select, Url
from aiogram_dialog.widgets.text import Const, Format

# from Telegram.bot import bot
from Telegram.bot_dialogs.data import FINISHED_KEY, choice_KEY, genre_KEY, main_instrument_KEY, choice_instrument_KEY, \
    Instrument_KEY, Choice_group_KEY, isAlredyRegister, Data_update_list, tg_id_user, Istr
from Telegram.bot_dialogs.getter import getter_profil
from Telegram.bot_dialogs.states import Register, Menu
from Telegram.bd import create_row
from Telegram.db_user_info import create_row_userinfo

bot = Bot(token="6752526100:AAFCSA3zE7LTV88AP68ozKPd90DxJ14Upks")


def id_getter(istr: Istr) -> str:
    return istr.id

CANCEL_EDIT = SwitchTo(
    Const("Отменить редактирование"),
    when=F["dialog_data"][FINISHED_KEY],
    id="cnl_edt",
    state=Register.preview,
)

async def get_call_data(dialog_manager: DialogManager, **kwargs):
    return dialog_manager.dialog_data
# async def Choice_button(event, widget, dialog_manager: DialogManager, *_):
#     # await dialog_manager
#     t = dialog_manager.dialog_data..get("")
#     t = dialog_manager.load_data()

# async def next_or_end(event_from_user: CallbackQuery, widget, dialog_manager: DialogManager, *_):
#     # print(event_from_user.from_user.id)
#     # print(event_from_user.u)
#     # id_user = dialog_manager.dialog_data["user_id"]

# async def step_choice(event, widget, dialog_manager: DialogManager,item_id: str, *_):
#     dialog_manager.dialog_data[choice_KEY] = item_id
#     if dialog_manager.dialog_data.get(FINISHED_KEY):
#         await dialog_manager.switch_to(Wizard.preview)
#     else:
#         await dialog_manager.switch_to(Wizard.name)

# async def step_go_edit_akkount(callback: CallbackQuery, dialog_manager: DialogManager,*_):
#     dialog_manager.dialog_data[isAlredyRegister] = True
#     # dialog_manager.dialog_data[choice_KEY] = item_id
#     data = get_line_user(callback.from_user.id)
#     dialog_manager.dialog_data[Data_update_list] = data
#     await dialog_manager.start(Register.preview)
async def step_name(callback: CallbackQuery, widget, dialog_manager: DialogManager,item_id: str, *_):
    # dialog_manager.dialog_data[choice_KEY] = item_id
    if len(item_id) <= 30:
        create_row_userinfo(dialog_manager.event.from_user.id, dialog_manager.event.from_user.username)
        try:
            dialog_manager.dialog_data[Data_update_list][1] = item_id
        except Exception as e:
            print(e)
        try:
            if dialog_manager.dialog_data[FINISHED_KEY]:
                await dialog_manager.switch_to(Register.preview)
            else:
                dialog_manager.dialog_data[FINISHED_KEY] = False
                await dialog_manager.switch_to(Register.city)
        except:
            dialog_manager.dialog_data[FINISHED_KEY] = False
            await dialog_manager.switch_to(Register.city)
    else:
        await callback.answer("Введите имя по короче меньше 30 сиволов включая побелы")
        await dialog_manager.switch_to(Register.name)

async def step_city(callback: CallbackQuery, widget, dialog_manager: DialogManager,item_id: str, *_):
    if len(item_id) <= 60:
        if dialog_manager.dialog_data[FINISHED_KEY]:
            await dialog_manager.switch_to(Register.preview)
        else:
            await dialog_manager.switch_to(Register.genre)
    else:
        await callback.answer("Введите город по короче меньше 60 сиволов включая побелы")
        await dialog_manager.switch_to(Register.city)
async def step_genre(event, widget, dialog_manager: DialogManager, item_id: str, *_):
    dialog_manager.dialog_data[genre_KEY] = item_id
    if dialog_manager.dialog_data[FINISHED_KEY]:
        await dialog_manager.switch_to(Register.preview)
    else:
        await dialog_manager.switch_to(Register.first_instrument)

async def step_first_instrument(event, widget, dialog_manager: DialogManager, item_id: str, *_):
    dialog_manager.dialog_data[main_instrument_KEY] = item_id
    if dialog_manager.dialog_data[FINISHED_KEY]:
        await dialog_manager.switch_to(Register.preview)
    else:
        await dialog_manager.switch_to(Register.choice_instrument)
async def step_choice_instrument(event, widget, dialog_manager: DialogManager, item_id: str, *_):
    dialog_manager.dialog_data[choice_instrument_KEY] = item_id
    if dialog_manager.dialog_data[FINISHED_KEY]:
        await dialog_manager.switch_to(Register.preview)
    else:
        await dialog_manager.switch_to(Register.choice)
async def step_choice(event, widget, dialog_manager: DialogManager, item_id: str, *_):
    dialog_manager.dialog_data[choice_KEY] = item_id
    if dialog_manager.dialog_data[FINISHED_KEY]:
        await dialog_manager.switch_to(Register.preview)
    else:
        await dialog_manager.switch_to(Register.experience)
async def step_experience(callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str, *_):
    try:
        if item_id.split(".")[0].isdigit() == False:
            raise Exception
        elif item_id.split(".")[1].isdigit() == False:
            raise Exception
        elif int(item_id.split(".")[1]) > 12:
            await callback.answer("дед у нас 12 месяцев https://www.youtube.com/watch?v=MxEc7YWJCvk")
            await dialog_manager.switch_to(Register.experience)
        elif int(item_id.split(".")[0]) >= 90:
            await callback.answer("прости дед у нас максимум 90 лет")
            await dialog_manager.switch_to(Register.experience)
        else:
            if dialog_manager.dialog_data[FINISHED_KEY]:
                await dialog_manager.switch_to(Register.preview)
            else:
                await dialog_manager.switch_to(Register.description)
            # data = get_line_user_temp(dialog_manager.event.from_user.id)
            # update_line_user_temp(dialog_manager.event.from_user.id, data[2], data[3], data[4], data[5], data[6], data[7],
            #                       item_id, data[9], data[10])
            # await dialog_manager.switch_to(Register.preview)
    except:
        await callback.answer("Вы ввели данное значение не правильно, пожалуйста внимателенее прочитайте пример!")
        await dialog_manager.switch_to(Register.experience)
async def step_description(callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str, *_):
    if len(item_id) <= 300:
        if dialog_manager.dialog_data[FINISHED_KEY]:
            await dialog_manager.switch_to(Register.preview)
        else:
            await dialog_manager.switch_to(Register.link)
    else:
        await callback.answer("Введите описание по короче меньше 300 сиволов включая побелы")
        await dialog_manager.switch_to(Register.description)
async def step_link(callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str, *_):
    try:
        check = requests.get(item_id).status_code
        if check == 404:
            await callback.answer("НЕ КОРЕКТНАЯ ССЫЛКА небыло получено ответа от сайта")
            await dialog_manager.switch_to(Register.link)
        else:
            dialog_manager.dialog_data[isAlredyRegister] = True
            await dialog_manager.switch_to(Register.preview)
    except:
        await callback.answer("НЕ КОРЕКТНАЯ ССЫЛКА пример:https://github.com/ROSTGG")
        await dialog_manager.switch_to(Register.link)

    # await next_or_end(event, widget, dialog_manager, *_)
# async def finaly_link(event, widget, dialog_manager: DialogManager, item_id: str, *_):
#     dialog_manager.dialog_data[FINISHED_KEY] = True
#     await dialog_manager.switch_to(Wizard.preview)
    # await next_or_end(event, widget, dialog_manager, *_)
# async def step_Ffind(event, widget, dialog_manager: DialogManager,item_id: str, *_):
#     dialog_manager.dialog_data["Ffind_id"] = item_id
#     await next_or_end(event, widget, dialog_manager, *_)

async def result_getter(dialog_manager: DialogManager, **kwargs):
    dialog_manager.dialog_data[FINISHED_KEY] = True
    genre, first_instrument, choice_instrument, choice = None, None, None, None
    try:
        genre = dialog_manager.dialog_data[genre_KEY]
        first_instrument = dialog_manager.dialog_data[main_instrument_KEY]
        choice_instrument = dialog_manager.dialog_data[choice_instrument_KEY]
        choice = dialog_manager.dialog_data[choice_KEY]
    except:
        pass
    data = await getter_profil()
    for i in data[genre_KEY]:
        if i.id == genre:
            genre = i.name
    for i in data[Instrument_KEY]:
        if i.id == first_instrument:
            first_instrument = i.name
    for i in data[Instrument_KEY]:
        if i.id == choice_instrument:
            choice_instrument = i.name
    for i in data[Choice_group_KEY]:
        if i.id == choice:
            choice = i.name

    return {
        "name": dialog_manager.find("name").get_value(),
        "city": dialog_manager.find("city").get_value(),
        "genre": genre,
        "first_instrument": first_instrument,
        "choice_instrument": choice_instrument,
        "choice": choice,
        "experience": dialog_manager.find("experience").get_value(),
        "description": dialog_manager.find("description").get_value(),
        "link": dialog_manager.find("link").get_value(),
    }

async def clear_chat(callback: CallbackQuery, dialog_manager: DialogManager):
    try:
        # Все сообщения, начиная с текущего и до первого (message_id = 0)
        for i in range(dialog_manager.event.message_id, 0, -1):
            # loop = asyncio.get_event_loop()
            # forecast = loop.run_until_complete(bot.delete_message(dialog_manager.event.from_user.id, i))
            # loop.close()
            await bot.delete_message(dialog_manager.event.from_user.id, i)
    except TelegramBadRequest as ex:
        # Если сообщение не найдено (уже удалено или не существует),
        # код ошибки будет "Bad Request: message to delete not found"
        if ex.message == "Bad Request: message to delete not found":
            print("Все сообщения удалены")
        else:
            print(ex.message)
async def register_user(callback: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    # find_text = str(dialog_manager.find("find").get_checked()).replace("]", "").replace("'", "").replace("[", "")
    # if dialog_manager.dialog_data[isFind_KEY] == "yes":
    #     TisFind = True
    # else:
    #     TisFind = False
    # if dialog_manager.dialog_data[choice_KEY] == "person":
    #     choice = 1301150
    # else:
    #     choice = 1301151
    # await callback.answer("Регистрация начилась")
    # r = new_str(tg_id=str(callback.from_user.id),
    #         name=dialog_manager.find("name").get_value(),
    #         city=dialog_manager.find("city").get_value(),
    #         find=find_text,
    #         isFind=TisFind,
    #         status=choice,
    #         description=dialog_manager.find("description").get_value(),
    #         link=dialog_manager.find("link").get_value(),)
    # print("Exit code from data base"+str(r))
    # await dialog_manager.start(Menu_st.menu_s, mode=StartMode.NEW_STACK)
    # if dialog_manager.dialog_data[choice_KEY] == "person":
    #     choice = "Музыкант 🎶"
    # else:
    #     choice = "Группа 🧾"
    # if dialog_manager.dialog_data[isFind_KEY] == "yes":
    #     TisFind = "Вы пытетесь найти группу"
    # else:
    #     TisFind = "Вы НЕ пытетесь найти группу"
    # first_instrument = str(dialog_manager.find("first_instrument").get_value()).replace("]", "").replace("'", "").replace("[", "")
    # choice_instrument = str(dialog_manager.find("choice_instrument").get_value()).replace("]", "").replace("'", "").replace("[", "")
    # if dialog_manager.dialog_data[isFind_KEY] == "piano":
    #     TFind = "Пианино"
    # elif dialog_manager.dialog_data[isFind_KEY] == "guitar":
    #     TFind = "Гитара"
    # elif dialog_manager.dialog_data[isFind_KEY] == "bass_guitar":
    #     TFind = "Басс гитара"
    # else:
    #     TFind = "Флейта"
    # data = await getter_profil()
    # for i in data[Instrument_KEY]:
    #     if data[Instrument_KEY][i].id == main_instrument:
    #         main_instrument = data[Instrument_KEY][i].name
    # for i in data[Instrument_KEY]:
    #     if data[Instrument_KEY][i].id == choice_instrument:
    #         choice_instrument = data[Instrument_KEY][i].name
    genre, main_instrument, choice_instrument, choice = None, None, None, None
    try:
        genre = dialog_manager.dialog_data[genre_KEY]
        main_instrument = dialog_manager.dialog_data[main_instrument_KEY]
        choice_instrument = dialog_manager.dialog_data[choice_instrument_KEY]
        choice = dialog_manager.dialog_data[choice_KEY]
    except:
        pass

    print("TG_ID: " + str(callback.from_user.id))
    print(f"name: {dialog_manager.find('name').get_value()}\n",
        f"city: {dialog_manager.find('city').get_value()}\n",
        f"genre: {genre}\n",
        f"first_instrument: {main_instrument}\n",
        f"choice_instrument: {choice_instrument}\n",
        f"choice: {choice}\n",
        f"experience: {dialog_manager.find('experience').get_value()}\n",
        f"description: {dialog_manager.find('description').get_value()}\n",
        f"link: {dialog_manager.find('link').get_value()}\n")
    data = create_row(tg_id=callback.from_user.id,
               name=dialog_manager.find('name').get_value(),
               city=dialog_manager.find('city').get_value(),
               genre = genre,
               main_inst = main_instrument,
               choice_inst = choice_instrument,
               choice = choice,
               exp = dialog_manager.find('experience').get_value(),
               des = dialog_manager.find('description').get_value(),
               link = dialog_manager.find('link').get_value())
    await callback.answer("Регистрация завершена")
    # await clear_chat(callback, dialog_manager)
    await dialog_manager.start(Menu.MAIN, mode=StartMode.NEW_STACK)


info_bot_window = Window(
    Const("Пожалуйста, запустите бота @notif_second_bot для уведомлений, туда вам будут высылать второстепенную информацию что-бы не засорять основной бот"),
    Url(Const("БОТ"), Const("https://t.me/notif_second_bot")),
    SwitchTo(text=Const("Я запустил(а) бота, начать дегистрацию"), id="to_next_name_from_info", state=Register.name),
    CANCEL_EDIT,
    state=Register.notif_bot,
)

name_window = Window(
    Const("Введите ваше имя:"),
    TextInput(id="name", on_success=step_name),
    CANCEL_EDIT,
    state=Register.name,
)
city_window = Window(
    Const("Введите ваш город(город в котором вы проживаете):"),
    TextInput(id="city", on_success=step_city),
    CANCEL_EDIT,
    state=Register.city,
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
    )),
    CANCEL_EDIT,
    state=Register.genre,
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
    )),
    CANCEL_EDIT,
    state=Register.first_instrument,
    getter=getter_profil,
    preview_data=getter_profil,
)
choice_instrument_window = Window(
    Const("Выберите дополнительный музыкальный инструмент:"),
    Column(
    Select(
        text=Format("{item.emoji} {item.name}"),
        id="choice_instrument",
        items=Instrument_KEY,
        # Alternatives:
        # items=lambda d: d[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        # items=F[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        item_id_getter=id_getter,
        on_click=step_choice_instrument,
    )),
    CANCEL_EDIT,
    state=Register.choice_instrument,
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
        state=Register.choice,
        getter=getter_profil,
        preview_data=getter_profil,
        )
experience_window = Window(
    Const("Введите стаж пример(пять лет и одинадцать месяцев): 5.11:"),
    TextInput(id="experience", on_success=step_experience),
    CANCEL_EDIT,
    state=Register.experience,
)
description_window = Window(
    Const("Введите описание:"),
    TextInput(id="description", on_success=step_description),
    CANCEL_EDIT,
    state=Register.description,
)
link_window = Window(
    Const("Введите ссылку на публичную страницу:"),
    TextInput(id="link", on_success=step_link),
    CANCEL_EDIT,
    state=Register.link,
)
exit_window = Window(
    Const("Пожалуйста, проверте введённые данные"),
    Format("Имя: {name}"),
    Format("Город: {city}"),
    Format("Жанр: {genre}"),
    Format("Основной музыкальный инструмент: {first_instrument}"),
    Format("Дополнительный музыкальный инструмент: {choice_instrument}"),
    Format("Состоите ли вы в группе: {choice}"),
    Format("Стаж: {experience}"),
    Format("Описание: {description}"),
    Format("Ссылка: {link}"),
    SwitchTo(
        Const("Изменить название"),
        state=Register.name, id="to_name",
    ),
    SwitchTo(
        Const("Изменить город"),
        state=Register.city, id="to_city",
    ),
    SwitchTo(
        Const("Изменить жанр"),
        state=Register.genre, id="to_genre",
    ),
    SwitchTo(
        Const("Изменить основной музыкальный инструмент"),
        state=Register.first_instrument, id="to_first_instrument",
    ),
    SwitchTo(
        Const("Изменить дополнительный музыкальный инструмент"),
        state=Register.choice_instrument, id="to_choise_instrument",
    ),
    SwitchTo(
        Const("Изменить статус"),
        state=Register.choice, id="to_choice",
    ),
    SwitchTo(
        Const("Изменить стаж"),
        state=Register.experience, id="to_isFind",
    ),
    SwitchTo(
        Const("Изменить описание"),
        state=Register.description, id="to_description",
    ),
    SwitchTo(
        Const("Изменить ссылку на публичную страницу"),
        state=Register.link,
        id="to_link",
    ),
    Button(
        Const("Сохранить"),
        id="to_save",
        on_click=register_user,
    ),
    state=Register.preview,
    getter=result_getter,
    # getter=get_call_data,
    parse_mode="html",
    )

register_group = Dialog(
                info_bot_window,
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

