import requests
from aiogram import F
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, LaunchMode, Window, DialogManager, StartMode
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, SwitchTo, Column, Select
from aiogram_dialog.widgets.text import Const, Format

from Telegram.bot_dialogs.data import FINISHED_KEY, choice_KEY, genre_KEY, main_instrument_KEY, choice_instrument_KEY, \
    Instrument_KEY, Choice_group_KEY, isAlredyRegister, Data_update_list, tg_id_user
from Telegram.bot_dialogs.getter import Istr, getter
from Telegram.bot_dialogs.states import Register, Menu
from Telegram.bd import create_row, get_line_user








# register_dialog = Dialog(
#                 ,
#                 launch_mode=LaunchMode.ROOT,)
