from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, LaunchMode, Window, DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Column, Select, Start, NumberedPager, Button
from aiogram_dialog.widgets.text import Const, Format, ScrollingText

from Telegram.bot_dialogs.common import MAIN_MENU_BUTTON
from Telegram.bot_dialogs.states import EditAccount, Help, Settings
from Telegram.logic import black_list_logic
from Telegram.logic.black_list_logic import is_username_in_list


async def step_name(callback: CallbackQuery, widget, dialog_manager: DialogManager,item_id: str, *_):
    # dialog_manager.dialog_data[choice_KEY] = item_id
    # dialog_manager.dialog_data[t_data_name] = item_id
    if is_username_in_list(item_id):
        black_list_logic.add_users(dialog_manager.event.from_user.id, black_list_logic.get_tgid(item_id))
        await dialog_manager.event.update.callback_query.answer(f"Пользователь {item_id} был добавлен в чёрный список!")
        await dialog_manager.switch_to(Settings.Enter)
    else:
        await dialog_manager.event.update.callback_query.answer("Такого пользователя не существует!")
        await dialog_manager.switch_to(Settings.Enter)


async def add(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    await dialog_manager.start(Help.MAIN)
async def remove(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    await dialog_manager.start(Help.MAIN)
window_one = Window(
        Const("Функции ченого списка:"),
        Button(Const("Добавить"),
               id="add",
               on_click=add),
        Button(Const("Удалить"),
               id="remove",
               on_click=remove),
        MAIN_MENU_BUTTON,
        state=Settings.MAIN,
)
window_two = Window(
        Const("Введите username без @ Пример: nick"),
        TextInput(id="name", on_success=step_name),
        MAIN_MENU_BUTTON,
        state=Settings.Enter,
)

dialog_setting = Dialog(window_one, launch_mode=LaunchMode.ROOT)