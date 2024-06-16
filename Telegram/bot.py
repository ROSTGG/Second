import asyncio
import logging
import os

import requests
from aiogram import Bot, Dispatcher, F, Router
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from aiogram.filters import ExceptionTypeFilter
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ErrorEvent, Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.utils.formatting import BotCommand

from aiogram_dialog import DialogManager, setup_dialogs, ShowMode, StartMode, Dialog, LaunchMode
from aiogram_dialog.api.exceptions import UnknownIntent

from Telegram.bot_dialogs.black_list_dialog import dialog_black_list
from Telegram.bot_dialogs.common import dialog_dont_work, send_notification
from Telegram.bot_dialogs.edit_account import EditAccount_dialog
from Telegram.bot_dialogs.help import dialog_help
from Telegram.bot_dialogs.menu import menu
from Telegram.bot_dialogs.search_dialog import window_one, window_view
from Telegram.bot_dialogs.settings import dialog_setting
from Telegram.bot_dialogs.states import Menu, Register
from Telegram.bot_dialogs.register import gregister_dialog_228
from Telegram.bd_functions.bd import isRegisterUser, get_line_user
from Telegram.bd_functions.db_user_info import update_line_userinfo
from Telegram.enter_bot_value import bot



async def clear_chat(dialog_manager: DialogManager):
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

async def start(callback: CallbackQuery, dialog_manager: DialogManager):
    # it is important to reset stack because user wants to restart everything
    # await dialog_manager.start(Menu.MAIN, mode=StartMode.RESET_STACK)
    print(callback.from_user.id)
    # await send_notification(dialog_manager.event.from_user.id, "dd")
    try:
        # if request_
        if isRegisterUser(callback.from_user.id):
            await clear_chat(dialog_manager)
            print("isRegisterUser = True")
            update_line_userinfo(tg_id=dialog_manager.event.from_user.id,
                                 user_name=dialog_manager.event.from_user.username, black_list=[0])
            await dialog_manager.start(Menu.MAIN, mode=StartMode.RESET_STACK)
        else:
            await clear_chat(dialog_manager)
            await dialog_manager.done()
            print("isRegisterUser = False")
            update_line_userinfo(tg_id=dialog_manager.event.from_user.id,
                                 user_name=dialog_manager.event.from_user.username, black_list=[0])
            await dialog_manager.start(Register.notif_bot, mode=StartMode.RESET_STACK)
    except Exception as e:
        print(e)
        await clear_chat(dialog_manager)
        await dialog_manager.start(Register.notif_bot, mode=StartMode.RESET_STACK)


async def on_unknown_intent(event: ErrorEvent, dialog_manager: DialogManager):
    # Example of handling UnknownIntent Error and starting new dialog.
    logging.error("Restarting dialog: %s", event.exception)
    if event.update.callback_query:
        await event.update.callback_query.answer(
            "Bot process was restarted due to maintenance.\n"
            "Redirecting to main menu.",
        )
        if event.update.callback_query.message:
            try:
                await event.update.callback_query.message.delete()
            except TelegramBadRequest:
                pass  # whatever
    elif event.update.message:
        await event.update.message.answer(
            "Bot process was restarted due to maintenance.\n"
            "Redirecting to main menu.",
            reply_markup=ReplyKeyboardRemove(),
        )
    # print(dialog_manager.event.from_user.id)
    # print(dialog_manager.dialog_data)
    # print(dialog_manager.start_data)
    # print(dialog_manager.event.callback_query.from_user.id)
    # print(dialog_manager.event.update.from_user.id)
    # print(event.update.from_user.id)
    print(event.update.callback_query.from_user.id)
    try:
        if isRegisterUser(event.update.callback_query.from_user.id):
            update_line_userinfo(tg_id=event.update.callback_query.from_user.id,
                                 user_name=event.update.callback_query.from_user.username,
                                 black_list=[0])
            await dialog_manager.start(Menu.MAIN, mode=StartMode.RESET_STACK)
        else:
            await dialog_manager.start(Register.notif_bot, mode=StartMode.RESET_STACK)
    except Exception as e:
        print(e)
        await dialog_manager.start(Register.notif_bot, mode=StartMode.RESET_STACK)
    # await dialog_manager.start(
    #     Register.name,
    #     mode=StartMode.RESET_STACK,
    #     show_mode=ShowMode.SEND,
    # )


dialog_router = Router()
dialog_router.include_routers(
    menu,
    gregister_dialog_228,
    EditAccount_dialog,
    dialog_dont_work,
    dialog_help,
    dialog_setting,
    dialog_black_list,
    Dialog(window_one,window_view, launch_mode=LaunchMode.ROOT))


def setup_dp():
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.message.register(start, F.text == "/start")
    dp.errors.register(
        on_unknown_intent,
        ExceptionTypeFilter(UnknownIntent),
    )
    dp.include_router(dialog_router)
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        # BotCommand(command="/find", description="Найти музыкальных сообщников"),
    ]
    bot.set_my_commands(commands)
    setup_dialogs(dp)
    return dp

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        # BotCommand(command="/find", description="Найти музыкальных сообщников"),
    ]
    await bot.set_my_commands(commands)

async def on_startup(dp):
    await set_commands(bot)
class TelegramHandler(logging.Handler):
    """Handler для отправки логов в телеграм."""

    def __init__(self, token, chat_id):
        super().__init__()

        self.token = token
        self.chat_id = chat_id

    def send_message_to_telegram(self, message: str) -> None:
        """Отправляет сообщение в телеграм."""
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        data = {
            'chat_id': self.chat_id,
            'text': message
        }
        requests.post(url=url, json=data)

    def emit(self, record: logging.LogRecord) -> None:
        """
        Зарегистрировать запись лога.

        Данный метод защищён от возможных ошибок, чтобы ошибка при логировании не повлияла на работу кода.
        """
        try:
            message = self.format(record)
            self.send_message_to_telegram(message)
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)

def create_tg_logger(name: str) -> logging.Logger:
    """Создать telegram Logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.DEBUG)
    handler = TelegramHandler("6862759280:AAHZjS4WURkLzk812ELzwUSQS6522x5FST4", "1041354811")
    handler.formatter = logging.Formatter('%(levelname)s: LOGGER: %(name)s TIME: %(asctime)s: MESSAGE: %(message)s')
    logger.addHandler(handler)

    return logger


# def main() -> None:
#     """Тестовое логирование."""
#     logger = create_tg_logger('test-logger')
#
#     print('До')
#     logger.critical('qweqwe, ой беда все сюда')
#     print('После')

async def main():
    # os.environ["TOKEN_BOT_MAIN"] = "6752526100:AAFCSA3zE7LTV88AP68ozKPd90DxJ14Upks"
    # spis = os.environ

    # Итерируем по каждой паре ключ-значение
    # for key, value in spis.items():
    #     print(f"{key} = {value}")
    # print(os.environ["TOKEN_BOT_MAIN"])
    # real main
    # logging.getLogger().setLevel(logging.DEBUG)
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.DEBUG)
    logger = create_tg_logger('logger')
    logger.info('Bot Started')
    # logger.basicConfig(level=logging.DEBUG)
    dp = setup_dp()
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == '__main__':
    asyncio.run(main())
