from dataclasses import dataclass

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row, Start, Url
from aiogram_dialog.widgets.text import Const

from Telegram.bot_dialogs import states
from Telegram.bot_dialogs.data import tg_id_user
from Telegram.bot_dialogs.edit_account import step_go_edit_akkount
from Telegram.bot_dialogs.states import Menu, My_profile, Movement_musicians, \
    Search_m, Event, My_Group, Project, Help, DontWorked
from Telegram.bot_dialogs.all import Register
FRUITS_KEY = "fruits"
OTHER_KEY = "others"
@dataclass
class Fruit:
    id: str
    name: str
    emoji: str
async def getter(**_kwargs):
    return {
        FRUITS_KEY: [
            Fruit("apple_a", "Apple", "🍏"),
            Fruit("banana_b", "Banana", "🍌"),
            Fruit("orange_o", "Orange", "🍊"),
            Fruit("pear_p", "Pear", "🍐"),
        ],
        OTHER_KEY: {
            FRUITS_KEY: [
                Fruit("mango_m", "Mango", "🥭"),
                Fruit("pineapple_p", "Pineapple", "🍍"),
                Fruit("kiwi_k", "Kiwi", "🥝"),
            ],
        },
    }
MAIN_MENU_BUTTON = Start(
    text=Const("☰ Main menu"),
    id="__main__",
    state=states.Menu.MAIN,
)
async def my_profile(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    await step_go_edit_akkount(event_from_user, widj, dialog_manager)
async def my_group(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    # await dialog_manager.start(My_Group.MAIN)
    await dialog_manager.start(DontWorked.MAIN)
async def search_m(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    # await dialog_manager.start(DontWorked.MAIN)
    await dialog_manager.start(Search_m.EnterInstrument)

async def event(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    await dialog_manager.start(DontWorked.MAIN)
    # await dialog_manager.start(Event.MAIN)
async def project(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    await dialog_manager.start(DontWorked.MAIN)
    # await dialog_manager.start(Project.MAIN)
async def help(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    await dialog_manager.start(Help.MAIN)
    # await dialog_manager.start(Help.MAIN)


# async def movement_musicians(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
#     await dialog_manager.start()


async def CancelEdit(event_from_user: CallbackQuery, widj, dialog_manager: DialogManager, **kwargs):
    await event_from_user.answer("notification")
menu = Dialog(
    Window(
        Const("Выберите из меню:"),
        Row(
                Button(Const("Мой аккаунт"),
                id="my_akkount",
                on_click=step_go_edit_akkount),
                Button(Const("Моя группа"),
                id="my_group",
                on_click=my_group),
                Button(Const("Поиск"),
                id="search_m",
                on_click=search_m),),
        Row(
                Button(Const("События"),
                id="event",
                on_click=event),
                Button(Const("Проекты"),
                id="project",
                on_click=project),

                Button(Const("Справка"),
                id="help",
                on_click=help),),
        Row(
                Url(Const("Движение музыкантов"),
                    Const('t.me/musicwgo'))),

        # Select(
        #     text=Format("{item.emoji} {item.name}"),
        #     id="choice",
        #     items=Choice_KEY,
        #     # Alternatives:
        #     # items=lambda d: d[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        #     # items=F[OTHER_KEY][FRUITS_KEY],  # noqa: E800
        #     item_id_getter=id_getter,
        #     on_click=step_choice,
        # ),
        # CANCEL_EDIT,
        # MAIN_MENU_BUTTON,
        state=Menu.MAIN,
        # parse_mode="html",
        # getter=getter,
        # preview_data=getter,
        # getter=getter,
        # parse_mode="html",
        # preview_data=getter,
))


#
# Row(
#     Start(Const("Мой профиль"),
#           id="my_profile",
#           state=My_profile.MAIN),
#     Start(Const("События"),
#           id="event",
#           state=Event.MAIN),
#     Start(Const("Изменение аккаунта"),
#           id="changing_profile",
#           state=Changing_profile.MAIN), ),
# Row(
#     Start(Const("Создать событие"),
#           id="create_event",
#           state=Create_event.MAIN),
#     Start(Const("Поиск"),
#           id="search_m",
#           state=Search_m.MAIN),
#     Start(Const("Движение музыкантов"),
#           id="movement_musicians",
#           state=Movement_musicians.MAIN), ),
# Row(
#     Start(Const("Создать проект"),
#           id="create_project",
#           state=Create_project.MAIN),
#     Start(Const("Мои события"),
#           id="my_event",
#           state=My_event.MAIN),
#     Start(Const("Мои проекты"),
#           id="my_project",
#           state=My_project.MAIN)),