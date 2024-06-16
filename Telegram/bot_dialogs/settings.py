from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, LaunchMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Column, Select, Start, NumberedPager, Button
from aiogram_dialog.widgets.text import Const, Format, ScrollingText

from Telegram.bot_dialogs.common import MAIN_MENU_BUTTON
from Telegram.bot_dialogs.states import EditAccount, Help, Settings, Black_list

VERY_LONG_TEXT = """\
Тут будет справка)

По вопросам, предложениям,  @RM1238g @stassmol
"""
async def help(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    await dialog_manager.start(Help.MAIN)
async def black_list(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    await dialog_manager.start(Black_list.MAIN)
    # await dialog_manager.start(Help.MAIN)
window_one = Window(
        Const("Настройки:\n"),
        Button(Const("Черный список"),
           id="black_list",
           on_click=black_list),
        Button(Const("Справка"),
           id="help",
           on_click=help),
        MAIN_MENU_BUTTON,
        state=Settings.MAIN,
)

dialog_setting = Dialog(window_one, launch_mode=LaunchMode.ROOT)
