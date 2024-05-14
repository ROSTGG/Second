from aiogram.exceptions import TelegramForbiddenError
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import Dialog, LaunchMode, Window, DialogManager, StartMode
from Telegram.bot_dialogs import states
from Telegram.bot_dialogs.data import bot_notification
from Telegram.bot_dialogs.states import DontWorked
from Telegram.enter_bot_value import bot


async def send_notification(is_another_user: bool, id: int, mes: str):
    try:
        await bot_notification.send_message(id, mes)
    except TelegramForbiddenError as err:
        if is_another_user:
            pass
        else:
            await bot.send_message(id, "Для продолжения запустите или разблокируйте бота https://t.me/notif_second_bot")

MAIN_MENU_BUTTON = Start(
    text=Const("☰ Main menu"),
    id="__main__",
    state=states.Menu.MAIN,
)
window_one = Window(
    Const("Данная функция не работает"),
    MAIN_MENU_BUTTON,
    state=DontWorked.MAIN,
)
dialog_dont_work = Dialog(window_one, launch_mode=LaunchMode.ROOT)