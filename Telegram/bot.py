import asyncio
import logging

from aiogram import Bot, Dispatcher, F, Router
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from aiogram.filters import ExceptionTypeFilter
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ErrorEvent, Message, ReplyKeyboardRemove, CallbackQuery

from aiogram_dialog import DialogManager, setup_dialogs, ShowMode, StartMode, Dialog, LaunchMode
from aiogram_dialog.api.exceptions import UnknownIntent

# from Telegram.bot_dialogs import search_dialog
from Telegram.bot_dialogs.common import dialog_dont_work, send_notification
from Telegram.bot_dialogs.data import isAlredyRegister, tg_id_user, Data_update_list, FINISHED_KEY, bot_main, \
    bot_for_test, bot_notification
from Telegram.bot_dialogs.edit_account import EditAccount_dialog
from Telegram.bot_dialogs.help import dialog_help
from Telegram.bot_dialogs.menu import menu
from Telegram.bot_dialogs.search_dialog import window_one, window_view
from Telegram.bot_dialogs.states import Menu, Register
from Telegram.bot_dialogs.register import gregister_dialog_228
from Telegram.bd import isRegisterUser, get_line_user
from Telegram.db_user_info import update_line_userinfo
from Telegram.enter_bot_value import bot



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

async def start(callback: CallbackQuery, dialog_manager: DialogManager):
    # it is important to reset stack because user wants to restart everything
    # await dialog_manager.start(Menu.MAIN, mode=StartMode.RESET_STACK)
    print(callback.from_user.id)
    # await send_notification(dialog_manager.event.from_user.id, "dd")
    try:
        # if request_
        if isRegisterUser(callback.from_user.id):
            await clear_chat(callback, dialog_manager)
            update_line_userinfo(dialog_manager.event.from_user.id, dialog_manager.event.from_user.username)
            await dialog_manager.start(Menu.MAIN, mode=StartMode.RESET_STACK)
        else:
            await clear_chat(callback, dialog_manager)
            await dialog_manager.start(Register.notif_bot, mode=StartMode.RESET_STACK)
    except:
        await clear_chat(callback, dialog_manager)
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
    await dialog_manager.start(
        Register.name,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.SEND,
    )


dialog_router = Router()
dialog_router.include_routers(
    menu,
    gregister_dialog_228,
    EditAccount_dialog,
    dialog_dont_work,
    dialog_help,
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
    setup_dialogs(dp)
    return dp


async def main():
    # real main
    # logging.getLogger().setLevel(logging.DEBUG)
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.DEBUG)

    dp = setup_dp()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
