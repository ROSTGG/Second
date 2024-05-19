import asyncio
import logging
import sqlite3
import sys
from os import getenv
from random import randint
from aiogram import F, types, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, StateFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.handlers import callback_query
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.utils.markdown import hbold
from aiogram import Bot, Dispatcher
# from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.filters.command import Command

# from botlogic.handlers.events import start_bot, stop_bot
# from aiogram.filters import Command
# from botlogic.handlers import send_file, simple
# from botlogic.settings import bot, bot_report
# from botlogic.units.private_message import private_message, get_number_of_users, for_data_base
from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.storage.base import StorageKey
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
import asyncio
import logging
import sys

import classes
from baserow import *
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    CallbackQuery,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from classes import *
from old_data import *

TOKEN = ("6752526100:AAFCSA3zE7LTV88AP68ozKPd90DxJ14Upks")
TOKEN_REPORT = ("6862759280:AAHZjS4WURkLzk812ELzwUSQS6522x5FST4")
form_router = Router()
bot = Bot(token=TOKEN, parse_mode='HTML')
bot_report = Bot(token=TOKEN_REPORT, parse_mode='HTML')


class MyClass:
    location = None


class StateUser(StatesGroup):
    base = State()
    choice = State()
    name = State()
    find = State()
    isFind = State()
    city = State()
    link = State()
    description = State()


async def builder_button_inline(list, num=1):
    keyboard = InlineKeyboardBuilder()
    for i in range(len(list)):
        keyboard.add(types.InlineKeyboardButton(text=f"{list[i]}",
                                                # keyboard.add(types.InlineKeyboardButton(text=f"Name: {list_of_users[i][1]}, Surname: {list_of_users[i][2]}, Tag: {list_of_users[i][3]}",
                                                callback_data=str(list[i])))
    keyboard.adjust(num)
    return keyboard


# for i in range(list["count"]):
#     print(f"ID: {list['results'][i]['id']}, chat_id: {list['results'][i]['chat_id']}, first_name: {list['results'][i]['first_name']}, last_name: {list['results'][i]['last_name']}, username: {list['results'][i]['username']}")
async def isFind_click(message: Message, state: FSMContext):
    f, list = get_all_str(str(message.chat.id))
    if f:
        print(list['isFind'])
        list["isFind"] = not list["isFind"]
        print(list['isFind'])

        update_row(**list)
        await message.answer("Статус обновлён")
    else:
        await message.answer("Вас не сущесчтвует в наших базах")


async def del_r(message: Message, state: FSMContext):
    # TODO function del №1
    isRegistr, id, white_list = is_id_bool(message.chat.id)
    if isRegistr:
        del_str(id)
        await message.answer("Информация о вас была успешно удалена")
    else:
        await message.answer("Вас уже нету в наших базах")


async def restart(message: Message, state: FSMContext):
    # TODO function restart
    await state.update_data(isRestart=True)
    await start(message, state)


async def start(message: Message, state: FSMContext):
    # TODO start function №1 start
    data = await state.get_data()
    isRegistr, id, white_list = is_id_bool(message.chat.id)
    await state.update_data(id=id)
    client = Client(**white_list)
    await state.update_data(white_list=white_list)
    isRes = True
    try:
        if data['isRestart']:
            isRes = False
    except:
        pass

    if isRegistr and isRes:
        # await message.answer(start_message_text_t)
        button = builder_button_inline(button_menu, 3)
        mes = await message.answer(f"{info} Меню", reply_markup=button.as_markup())
        await state.update_data(state_user="choise_menu")
        await state.update_data(mes=mes)
    else:
        try:
            if data['isRestart']:
                mes = await message.answer("Введите обновлённые данные")
            else:
                mes = await message.answer(start_message_text)  # hello
        except:
            mes = await message.answer(start_message_text)  # hello
        await state.set_state(StateUser.choice)
        await state.update_data(mes=mes)
        await state.update_data(id_tg=message.from_user.id)

        keyboard = await builder_button_inline(dbt["person"]["choice"]["list"], 2)
        await state.update_data(state_user="choice")
        mes = await message.answer(enter_choice_text, reply_markup=keyboard.as_markup())
        await state.update_data(mes2=mes)


# data = await state.get_data()
# await state.set_state(StateUser.base)
# await state.update_data(city=message.text)
# await message.delete()
# await bot.delete_message(chat_id=data["id_tg"], message_id=data["mes"].message_id)
# await message.answer(f"{exit_city_text}{message.text}") # city stop

# keyboard = await builder_button_inline(enter_isFind_list, 2)
# await state.update_data(state_user="isFind")
# mes = await message.answer(enter_isFind_text, reply_markup=keyboard.as_markup())
# await state.update_data(mes=mes)
async def choice(message: Message, state: FSMContext):
    global data, rightanswer, choicen
    await state.set_state(StateUser.name)
    if message.text.lower() in rightanswer[0]:

        data['id_tg'] = message.chat.id
        data['type'] = message.text.lower()
        if message.text.lower() == rightanswer[0][0]:
            choicen = 'person'
        else:
            choicen = 'band'
        await message.answer(mess[choicen][0])
    else:
        await state.set_state(StateUser.choice)
        await message.answer("Не правльно введено значение, попробуйте еще раз: ")


async def register_comm(message: Message, state: FSMContext):
    await state.set_state(StateUser.name)
    mes = await message.answer(dbt[data['choices']]['name']['enter'])
    await state.update_data(mes=mes)
    await state.update_data(id_tg=message.from_user.id)


# async def name(message: Message, state: FSMContext):
#     global data
#     await state.set_state(StateUser.find)
#     if len(message.text) > 30:
#         await state.set_state(StateUser.name)
#         await message.answer(mess[choicen][1])
#     else:
#         data['name'] = message.text
#         await message.answer(mess[choicen][2], )
async def name(message: Message, state: FSMContext):
    # TODO start function №3 name
    data = await state.get_data()
    if len(message.text) >= 40:
        await state.set_state(StateUser.name)
        await message.delete()
        await bot.delete_message(chat_id=data["id_tg"], message_id=data["mes"].message_id)
        mes = await message.answer(dbt[data['choices']]['name']['reset'])
        await state.update_data(mes=mes)
    else:
        await state.set_state(StateUser.city)
        await message.delete()
        await bot.delete_message(chat_id=data["id_tg"], message_id=data["mes"].message_id)
        await message.answer(f"{dbt[data['choices']]['name']['exit']}{message.text}")
        await state.update_data(name=message.text)  # city start
        mes = await message.answer(dbt[data['choices']]['city']['enter'])
        await state.update_data(mes=mes)


async def city(message: Message, state: FSMContext):
    # TODO start function №4 city
    data = await state.get_data()
    if len(message.text) >= 60:
        await state.set_state(StateUser.city)
        await message.delete()
        await bot.delete_message(chat_id=data["id_tg"], message_id=data["mes"].message_id)
        mes = await message.answer(dbt[data['choices']]['city']['reset'])
        await state.update_data(mes=mes)
    else:
        await state.set_state(StateUser.base)
        await state.update_data(city=message.text)
        await message.delete()
        await bot.delete_message(chat_id=data["id_tg"], message_id=data["mes"].message_id)
        await message.answer(f"{dbt[data['choices']]['city']['exit']}{message.text}")  # city stop

        keyboard = await builder_button_inline(dbt[data['choices']]['isFind']['list'], 2)
        await state.update_data(state_user="isFind")
        await state.update_data(state_user_st="base")
        mes = await message.answer(dbt[data['choices']]['isFind']['enter'], reply_markup=keyboard.as_markup())
        await state.update_data(mes=mes)


async def description(message: Message, state: FSMContext):
    # TODO start function №7 description
    # \B: dsdsd
    data = await state.get_data()
    if len(message.text) >= 300:
        await state.set_state(StateUser.description)
        await message.delete()
        await bot.delete_message(chat_id=data["id_tg"], message_id=data["mes"].message_id)
        mes = await message.answer(dbt[data['choices']]['description']['reset'])
        await state.update_data(mes=mes)
    else:
        await state.set_state(StateUser.link)
        await message.delete()
        await bot.delete_message(chat_id=data["id_tg"], message_id=data["mes"].message_id)
        await message.answer(f"{dbt[data['choices']]['description']['exit']}{message.text}")
        await state.update_data(description=message.text)  # city start

        mes = await message.answer(dbt[data['choices']]['link']['enter'])
        await state.update_data(mes=mes)

    # dlu = white_list["results"][int(number_user_BR)]
    # # dlu = get_all_str("250967")["count"]["results"][number_user_BR]
    # await message.answer("Вы уже существуете в наших базах вот информация о вас:")
    # ax = already_exists_in_the_database
    # await message.answer("%s %s \n%s %s \n%s %s \n%s %s \n%s %s \n%s %s \n%s %s \n" % (
    # ax[0], dlu['tg_id'], ax[1], dlu['name'], ax[2], dlu['city'], ax[3], dlu['isFind'], ax[4], dlu['find'], ax[5],
    # dlu['link'], ax[6], dlu['description'],))


async def link(message: Message, state: FSMContext):
    # TODO start function №8 link
    data = await state.get_data()
    if len(message.text) >= 80:
        await state.set_state(StateUser.description)
        await message.delete()
        await bot.delete_message(chat_id=data["id_tg"], message_id=data["mes"].message_id)
        mes = await message.answer(dbt[data['choices']]['link']['reset'])
        await state.update_data(mes=mes)
    else:
        await state.set_state(StateUser.base)
        await message.delete()
        await bot.delete_message(chat_id=data["id_tg"], message_id=data["mes"].message_id)
        await message.answer(f"{dbt[data['choices']]['link']['exit']}: {message.text}")
        await state.update_data(link=message.text)  # city start
        await state.update_data(id=data["white_list"]["id"])
        status = None
        if data['choices'] == "person":
            status = 1301150
        elif data['choices'] == "band":
            status = 1301151
        await state.update_data(status_id=status)
        data = await state.get_data()
        try:
            if data['isRestart']:
                print("ddddd")
                print(data)
                print(update_row(**data))
                print("data up date")
                mes = await message.answer("Данные обновлены")
            else:
                print("else_5538")
                new_str(data['id_tg'], data['name'], data['find'], data['city'], data["isFind"], data["description"],
                        data["link"], status)
                mes = await message.answer(registration_exit_text)  # hello
        except Exception as e:
            mes = await message.answer(registration_exit_text)  # hello
            print("exept_110")
            print(e)
            new_str(data['id_tg'], data['name'], data['find'], data['city'], data["isFind"], data["description"],
                    data["link"], status)
        await state.update_data(isRestart=False)
        print(
            f"choice {data['choice']} id {data['id_tg']} name = {data['name']} city = {data['city']} isFind = {data['isFind']} find = {data['find']} link = {data['link']} description = {data['description']}")


async def search(message: Message, state: FSMContext):
    # TODO Поиск музыкантов, групп №1
    data = await state.get_data()
    isRegistr, number_user_BR, white_list = is_id_bool(message.chat.id)
    await message.delete()
    try:
        f = data["client"]
    except:
        client = Client(**white_list)
        await state.update_data(client=client)
    if str(white_list['status']['id']) == str(1301150):  # musikant
        await state.update_data(choices="person")
    elif str(white_list['status']['id']) == str(1301151):  # admin:
        await state.update_data(choices="band")
    data = await state.get_data()
    list = dbt[data['choices']]['find']['list']
    list.insert(len(dbt[data['choices']]['find']['list']), white_list['find'])
    print(dbt[data['choices']]['find']['list'])
    print(white_list['find'])
    print(list)
    keyboard = await builder_button_inline(list, 2)
    await state.update_data(state_user="search_find")
    await state.update_data(id_tg=message.chat.id)
    mes = await message.answer("На каком инструменте он должен играть",
                               reply_markup=keyboard.as_markup())  # dbt[data['choices']]['isFind']['enter']
    await state.update_data(mes=mes)


# await state.update_data(state_user="find")
# mes = await message.answer(enter_find_text, reply_markup=keyboard.as_markup())
# await state.update_data(mes=mes)
# await state.update_data(message_object=message)
async def all_callback(call: CallbackQuery, state: FSMContext):
    global button_menu
    data = await state.get_data()
    call_data = call.data
    if data["state_user"] == "choice":
        # TODO start function №2 choice
        await state.set_state(StateUser.name)
        if call_data == dbt["person"]["choice"]["list"][0]:  # musikant
            await state.update_data(choices="person")
        elif call_data == dbt["person"]["choice"]["list"][1]:  # admin:
            await state.update_data(choices="band")
        await state.update_data(choice=call_data)
        data = await state.get_data()
        await bot.send_message(data["id_tg"], f"{exit_choice_text}{call_data}")
        await bot.delete_message(data["id_tg"], data["mes"].message_id)
        await bot.delete_message(data["id_tg"], data["mes2"].message_id)
        mes = await bot.send_message(data["id_tg"], dbt[data['choices']]['name']['enter'])
        await state.update_data(mes=mes)
    elif data["state_user"] == "isFind":
        # TODO start function №5 isFind
        await state.update_data(isFind=call_data)
        if call_data == "Yes":
            await state.set_state(StateUser.base)
            keyboard = await builder_button_inline(dbt[data["choices"]]['find']["list"], 2)
            await bot.send_message(data["id_tg"], f"{dbt[data['choices']]['isFind']['exit'][0]}")
            await state.update_data(isFind=call_data)
            await bot.delete_message(data["id_tg"], data["mes"].message_id)

            await state.update_data(state_user="find")
            mes = await bot.send_message(data["id_tg"], dbt[data['choices']]['find']['enter'],
                                         reply_markup=keyboard.as_markup())
            await state.update_data(mes=mes)
        elif call_data == "No":
            await state.set_state(StateUser.description)
            await bot.send_message(data["id_tg"], f"{dbt[data['choices']]['isFind']['exit'][1]}")
            await state.update_data(find="None")
            await state.update_data(isFind=call_data)
            await bot.delete_message(data["id_tg"], data["mes"].message_id)

            mes = await bot.send_message(data["id_tg"], dbt[data['choices']]['description']['enter'])
            await state.update_data(mes=mes)
    elif data["state_user"] == "find":
        # TODO start function №6 find
        # if data["state_user"] == ""
        await state.set_state(StateUser.description)
        await state.update_data(find=call_data)
        await bot.send_message(data["id_tg"], f"{dbt[data['choices']]['find']['exit']}{call_data}")
        await bot.delete_message(data["id_tg"], data["mes"].message_id)

        await state.update_data(state_user="base")
        mes = await bot.send_message(data["id_tg"], dbt[data['choices']]['description']['enter'])
        await state.update_data(mes=mes)
    elif data["state_user"] == "search_find":
        # TODO Поиск музыкантов, групп №2
        data = await state.get_data()
        cliend = data["client"]
        er, l, list = cliend.search(call_data)
        print("fffff")
        print(list)
        for i in list:
            if er == '200':
                await bot.send_message(data["id_tg"], f"{i['name']} - {i['city']} - {i['link']} - {i['description']}")
            elif er == '404':
                await bot.send_message(data["id_tg"], l)
        await bot.delete_message(data["id_tg"], data["mes"].message_id)
        await state.update_data(state_user="base")
        # mes = await bot.send_message(data["id_tg"], dbt[data['choices']]['description']['enter'])
        # await state.update_data(mes=mes)
    elif data['state_user'] == "choise_menu":
        # TODO Меню Выбор CallBack
        if call_data == button_menu[0]:
            mes = await bot.send_message(data["id_tg"], classes.get_info())
            await state.update_data(mes=mes)
        elif call_data == button_menu[1]:
            mes = await bot.send_message(data["id_tg"], "pass")
            await state.update_data(mes=mes)
        elif call_data == button_menu[2]:
            pass
        elif call_data == button_menu[3]:
            pass
        elif call_data == button_menu[4]:
            pass
        elif call_data == button_menu[5]:
            pass
        elif call_data == button_menu[6]:
            pass
        elif call_data == button_menu[7]:
            pass
        elif call_data == button_menu[8]:
            pass
    # button_menu = ["Мой профиль", "События города", "Настройки аккаунта", "Создать событие", "Мои события",
    #                "Создать проект", "Мои проекты", "Поиск и движение музыкантов", "движение музыкантов"]

    else:
        await bot.send_message(data["id_tg"], call_data)


async def send_bot_error(text_e):
    await bot_report.send_message(1041354811, text_e)


async def start_bot():
    print('bot started')


async def stop_bot():
    print('bot stopped')


async def main():
    # TODO register command
    logging.basicConfig(
        level=logging.INFO, stream=sys.stdout,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(filename)s(%(lineno)d) - %(message)s)")
    dp = Dispatcher()
    dp.include_router(form_router)

    # dp.message.register(start_command, Command(commands='start'))  # State(state="base")
    # dp.message.register(register_comm, Command(commands='register'))  # State(state="base")
    dp.message.register(name, StateUser.name)
    dp.message.register(city, StateUser.city)
    dp.message.register(description, StateUser.description)
    dp.callback_query.register(all_callback, lambda call: True)
    dp.message.register(start, Command(commands='start'))  # State(state="base")
    dp.message.register(isFind_click, Command(commands='isfind'))  # State(state="base")
    dp.message.register(search, Command(commands='search'))  # State(state="base")
    dp.message.register(restart, Command(commands='restart'))  # State(state="base")
    dp.message.register(del_r, Command(commands='del'))  # State(state="base")
    dp.message.register(del_r, F.data == "find")  # State(state="base")
    dp.message.register(link, StateUser.link)
    dp.message.register(choice, StateUser.choice)
    dp.message.register(name, StateUser.name)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)


url_button = 'https://mastergroosha.github.io/aiogram-3-guide/buttons/'
if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
