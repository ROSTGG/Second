from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from aiogram_dialog import (
    Dialog, DialogManager, setup_dialogs, StartMode, Window,
)
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from aiogram.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery

from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button, Back
from aiogram_dialog.widgets.text import Const, Format


class MySG(StatesGroup):
    main = State()
    window1 = State()
    window2 = State()


main_window = Window(
    Const("Hello, unknown person"),
    Button(Const("Useless button"), id="nothing"),
    state=MySG.main,
)
dialog = Dialog(main_window)

storage = MemoryStorage()
bot = Bot(token='6752526100:AAFCSA3zE7LTV88AP68ozKPd90DxJ14Upks')
dp = Dispatcher(storage=storage)
dp.include_router(dialog)
setup_dialogs(dp)


async def window1_get_data(**kwargs):
    return {
        "something": "data from Window1 getter",
    }


async def window2_get_data(**kwargs):
    return {
        "something": "data from Window2 getter",
    }


async def dialog_get_data(**kwargs):
    return {
        "name": "Tishka17",
    }


async def button1_clicked(callback: CallbackQuery, button: Button, manager: DialogManager):
    """ Add data to `dialog_data` and switch to the next window of current dialog """
    manager.dialog_data['user_input'] = 'some data from user, stored in `dialog_data`'
    await manager.next()


dialog = Dialog(
    Window(
        Format("Hello, {name}!"),
        Format("Something: {something}"),
        Button(Const("Next window"), id="button1", on_click=button1_clicked),
        state=MySG.window1,
        getter=window1_get_data,  # here we specify data getter for window1
    ),
    Window(
        Format("Hello, {name}!"),
        Format("Something: {something}"),
        Format("User input: {dialog_data[user_input]}"),
        Back(text=Const("Back")),
        state=MySG.window2,
        getter=window2_get_data,  # here we specify data getter for window2
    ),
    getter=dialog_get_data  # here we specify data getter for dialog
)

@dp.message(Command("start"))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.window1, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    dp.run_polling(bot, skip_updates=True)