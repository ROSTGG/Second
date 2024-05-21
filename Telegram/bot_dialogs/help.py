from aiogram_dialog import Dialog, LaunchMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Column, Select, Start, NumberedPager
from aiogram_dialog.widgets.text import Const, Format, ScrollingText

from Telegram.bot_dialogs.common import MAIN_MENU_BUTTON
from Telegram.bot_dialogs.states import EditAccount, Help

VERY_LONG_TEXT = """\
Тут будет справка)

По вопросам, предложениям,  @RM1238g @stassmol
"""

window_one = Window(
        Const("Справка:\n"),
        ScrollingText(
            text=Const(VERY_LONG_TEXT),
            id="text_scroll",
            page_size=1000,
        ),
        NumberedPager(
            scroll="text_scroll",
        ),
        MAIN_MENU_BUTTON,
        state=Help.MAIN,
)


dialog_help = Dialog(window_one, launch_mode=LaunchMode.ROOT)