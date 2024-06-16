from aiogram.exceptions import TelegramForbiddenError
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import Dialog, LaunchMode, Window, DialogManager, StartMode
from Telegram.bot_dialogs import states
from Telegram.bot_dialogs.data import bot_notification
from Telegram.bot_dialogs.states import DontWorked
from Telegram.enter_bot_value import bot
from Telegram.logic.black_list_logic import is_check_user_BL


async def send_notification(is_another_user: bool, id: int, operating_id: int, sent_id_id: int,  mes: str):
    """
    is_another_user: bool, - Работает ли НЕ с собой
    id: int - Передавать id кому отправить
    operating_id: int - ID с пользователем кто отправляет
    sent_id_id: int - ID кому собираеться отправлять
    mes: str - Сообщение
    """
    # проверка на регистрацию в боте увдомлений
    if is_check_user_BL:
        try:
            await bot_notification.send_message(id, mes)
        except TelegramForbiddenError as err:
            if is_another_user:
                pass
            else:
                await bot.send_message(id, "Для продолжения запустите или разблокируйте бота https://t.me/notif_second_bot")
    else:
        await bot.send_message(id, "Вас заблокировали! ⛔️")

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