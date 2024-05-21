# import asyncio
# import logging
# import os
# from dataclasses import dataclass
#
# from aiogram import Bot, Dispatcher, F, Router
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import Message, User, CallbackQuery
#
# from aiogram_dialog import (
#     Dialog, DialogManager, setup_dialogs, StartMode, Window, LaunchMode,
# )
# from aiogram_dialog.widgets.input import TextInput
# from aiogram_dialog.widgets.kbd import Checkbox, Next, SwitchTo, Radio, Button, Multiselect, Row, Column, Select
# from aiogram_dialog.widgets.text import Const, Jinja, Format, Case
#
# from Telegram.bot_dialogs.states import Register
# from baserow import new_str
#stasloh
# class Wizard(StatesGroup):
#     title = State()
#     city = State()
#     options = State()
#     preview = State()
#     name = State()
#     isFind = State()
#     find = State()
#     choice = State()
#     description = State()
#     link = State()
#     menu_state = State()
#     menu_state2 = State()
#     menu_state_button1 = State()
#     menu_state_button2 = State()
# class Menu_st(StatesGroup):
#     menu_s = State()
# Instrument_KEY = "instrument"
# isFind_KEY = "find_search"
# Choice_KEY = "choice_list"
# OTHER_KEY = "others"
# @dataclass
# class Istr:
#     id: str
#     name: str
#     emoji: str
#
# async def getter(**_kwargs):
#     return {
#         Instrument_KEY: [
#             Istr("piano", "piano", " "),
#             Istr("guitar", "guitar", " "),
#             Istr("bass_guitar", "bass_guitar", " "),
#             Istr("flueite", "flueite", " "),],
#         OTHER_KEY: {
#             Instrument_KEY: [
#                 Istr("guitar", "piano", " "),
#                 Istr("piano", "guitar", " "),
#                 Istr("bass_guitar", "bass_guitar", " "),
#                 Istr("flueite", "flueite", " "), ]
#         },
#         isFind_KEY: [
#             Istr("yes", "Я пытаюсь найти группу", "✔"),
#             Istr("no", "Я НЕ пытаюсь найти группу", "❌"),
#         ],
#         Choice_KEY: [
#             Istr("person", "Музыкант", "🎶"),
#             Istr("group", "Группа", "🧾"),
#         ]
#         }
# def id_getter(istr: Istr) -> str:
#     return istr.id
# FINISHED_KEY = "finished"
# FINISHED_KEY_REGISTER = "finished_reg"
# choice_KEY = "choice_id"
# isFind_KEY = "isFind_id"
# CANCEL_EDIT = SwitchTo(
#     Const("Отменить редактирование"),
#     when=F["dialog_data"][FINISHED_KEY],
#     id="cnl_edt",
#     state=Wizard.preview,
# )
# async def get_call_data(dialog_manager: DialogManager, **kwargs):
#     return dialog_manager.dialog_data
# # async def Choice_button(event, widget, dialog_manager: DialogManager, *_):
# #     # await dialog_manager
# #     t = dialog_manager.dialog_data..get("")
# #     t = dialog_manager.load_data()
#
# # async def next_or_end(event_from_user: CallbackQuery, widget, dialog_manager: DialogManager, *_):
# #     # print(event_from_user.from_user.id)
# #     # print(event_from_user.u)
# #     # id_user = dialog_manager.dialog_data["user_id"]
# #     if dialog_manager.dialog_data.get(FINISHED_KEY):
# #         await dialog_manager.switch_to(Wizard.preview)
# #     else:
# #         await dialog_manager.next()
# async def step_choice(event, widget, dialog_manager: DialogManager,item_id: str, *_):
#     dialog_manager.dialog_data[choice_KEY] = item_id
#     await dialog_manager.switch_to(Wizard.name)
#
# async def step_isFind(event, widget, dialog_manager: DialogManager, item_id: str, *_):
#     dialog_manager.dialog_data[isFind_KEY] = item_id
#     await dialog_manager.switch_to(Wizard.find)
#     # await next_or_end(event, widget, dialog_manager, *_)
# async def finaly_link(event, widget, dialog_manager: DialogManager, item_id: str, *_):
#     dialog_manager.dialog_data[FINISHED_KEY] = True
#     await dialog_manager.switch_to(Wizard.preview)
#     # await next_or_end(event, widget, dialog_manager, *_)
# # async def step_Ffind(event, widget, dialog_manager: DialogManager,item_id: str, *_):
# #     dialog_manager.dialog_data["Ffind_id"] = item_id
# #     await next_or_end(event, widget, dialog_manager, *_)
#
# async def result_getter(dialog_manager: DialogManager, **kwargs):
#     dialog_manager.dialog_data[FINISHED_KEY] = True
#     if dialog_manager.dialog_data[choice_KEY] == "person":
#         choice = "Музыкант 🎶"
#     else:
#         choice = "Группа 🧾"
#     if dialog_manager.dialog_data[isFind_KEY] == "yes":
#         TisFind = "Вы патетесь найти группу"
#     else:
#         TisFind = "Вы НЕ патетесь найти группу"
#     find_text = str(dialog_manager.find("find").get_checked()).replace("]", "").replace("'", "").replace("[", "")
#     # if dialog_manager.dialog_data[isFind_KEY] == "piano":
#     #     TFind = "Пианино"
#     # elif dialog_manager.dialog_data[isFind_KEY] == "guitar":
#     #     TFind = "Гитара"
#     # elif dialog_manager.dialog_data[isFind_KEY] == "bass_guitar":
#     #     TFind = "Басс гитара"
#     # else:
#     #     TFind = "Флейта"
#     return {
#         "choice": choice,
#         "name": dialog_manager.find("name").get_value(),
#         "city": dialog_manager.find("city").get_value(),
#         "isFind": TisFind,
#         "find": find_text,
#         "description": dialog_manager.find("description").get_value(),
#         "link": dialog_manager.find("link").get_value(),
#     }
# async def register_user(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
#     find_text = str(dialog_manager.find("find").get_checked()).replace("]", "").replace("'", "").replace("[", "")
#     if dialog_manager.dialog_data[isFind_KEY] == "yes":
#         TisFind = True
#     else:
#         TisFind = False
#     if dialog_manager.dialog_data[choice_KEY] == "person":
#         choice = 1301150
#     else:
#         choice = 1301151
#     new_str(tg_id=str(event_from_user.from_user.id),
#             name=dialog_manager.find("name").get_value(),
#             city=dialog_manager.find("city").get_value(),
#             find=find_text,
#             isFind=TisFind,
#             status=choice,
#             description=dialog_manager.find("description").get_value(),
#             link=dialog_manager.find("link").get_value(),)
#     # await dialog_manager.start(Menu_st.menu_s, mode=StartMode.NEW_STACK)
#     await dialog_manager.switch_to(Wizard.menu_state)

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
# name_window = Window(
#     Const("Введите название:"),
#     TextInput(id="name", on_success=Wizard.city),
#     CANCEL_EDIT,
#     state=Wizard.name,
# )
# city_window = Window(
#     Const("Введите город:"),
#     TextInput(id="city", on_success=Wizard.isFind),
#     CANCEL_EDIT,
#     state=Wizard.city,
# )
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
# choice_instrument_window = Window(
#     Const("Выберите инструменты:"),
#     Column(
#         Multiselect(
#         checked_text=Format("🔘 {item.emoji} {item.name}"),
#         unchecked_text=Format("⚪️ {item.emoji} {item.name}"),
#         id="find",
#         items=Instrument_KEY,
#         item_id_getter=id_getter,
#     )),
#     SwitchTo(
#         Const("Далее"),
#         state=Wizard.description, id="next_description",
#     ),
#     CANCEL_EDIT,
#     getter=getter,
#     state=Wizard.find,
# )
# description_window = Window(
#     Const("Введите описание:"),
#     TextInput(id="description", on_success=Wizard.link),
#     CANCEL_EDIT,
#     state=Wizard.description,
# )
# link_window = Window(
#     Const("Введите ссылку на публичную страницу:"),
#     TextInput(id="link", on_success=finaly_link),
#     CANCEL_EDIT,
#     state=Wizard.link,
# )
# exit_window = Window(
#     Const("Пожалуйста, проверте введённые данные"),
#     Format("Choice: {choice}"),
#     Format("Name: {name}"),
#     Format("City: {city}"),
#     Format("isFind: {isFind}"),
#     Format("Find: {find}"),
#     Format("Description: {description}"),
#     Format("Link: {link}"),
#     SwitchTo(
#         Const("Изменить статус"),
#         state=Wizard.choice, id="to_choice",
#     ),
#     SwitchTo(
#         Const("Изменить название"),
#         state=Wizard.name, id="to_title",
#     ),
#     SwitchTo(
#         Const("Изменить город"),
#         state=Wizard.city, id="to_city",
#     ),
#     SwitchTo(
#         Const("Изменить isFind"),
#         state=Wizard.isFind, id="to_isFind",
#     ),
#     SwitchTo(
#         Const("Изменить инструменты"),
#         state=Wizard.find, id="to_instr",
#     ),
#     SwitchTo(
#         Const("Изменить описание"),
#         state=Wizard.description, id="to_desc",
#     ),
#     SwitchTo(
#         Const("Изменить ссылку на публичную страницу"),
#         state=Wizard.link,
#         id="to_link",
#     ),
#     Button(
#         Const("Сохранить"),
#         id="to_save",
#         on_click=register_user,
#     ),
#     state=Wizard.preview,
#     getter=result_getter,
#     # getter=get_call_data,
#     parse_mode="html",
#     )

# register_dialog = Dialog(
#                 choice_window,
#                 name_window,
#                 city_window,
#                 choice_isFind_window,
#                 choice_instrument_window,
#                 description_window,
#                 link_window,
#                 exit_window,
#                 launch_mode=LaunchMode.ROOT,)


# menu_g = Dialog(
#     Window(Const("fffffffffff"),
#             SwitchTo(
#                 Const("dfgsfgfsd"),
#                 state=Wizard.menu_state_button1,
#                 id="to_menu_sss",
#             ),
#             state=Wizard.menu_state,),
#     Window(Const("ggggggggg"),
#             SwitchTo(
#                 Const("gdsfgfadfs"),
#                 state=Wizard.menu_state,
#                 id="to_menu_sss",
#             ),
#             state=Wizard.menu_state_button1,
#            ))


async def start(message: Message, dialog_manager: DialogManager):
    # it is important to reset stack because user wants to restart everything
    await dialog_manager.start(Register.choice, mode=StartMode.RESET_STACK)
    # pass
# dialog_router = Router()
# dialog_router.include_routers(
    # register,
    # menu,
    # menu_g
# )


async def main():
    # real main
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token="6752526100:AAFCSA3zE7LTV88AP68ozKPd90DxJ14Upks")
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router()
    dp.message.register(start, CommandStart())
    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
