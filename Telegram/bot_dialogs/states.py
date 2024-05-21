from aiogram.fsm.state import StatesGroup, State

class Register(StatesGroup):
    notif_bot = State()
    name = State()
    city = State()
    genre = State()
    first_instrument = State()
    choice_instrument = State()
    choice = State()
    experience = State()
    description = State()
    link = State()
    preview = State()
    options = State()
    isFind = State()
    find = State()
    menu_state = State()
    menu_state2 = State()
    menu_state_button1 = State()
    menu_state_button2 = State()
    title = State()
class EditAccount(StatesGroup):
    name = State()
    city = State()
    genre = State()
    first_instrument = State()
    choice_instrument = State()
    choice = State()
    experience = State()
    description = State()
    link = State()
    preview = State()
    options = State()
    isFind = State()
    find = State()
    menu_state = State()
    menu_state2 = State()
    menu_state_button1 = State()
    menu_state_button2 = State()
    title = State()
class RegisterGroup(StatesGroup):
    name = State()
    link = State()
    description = State()
    user = State()
    instrument = State()
class Menu(StatesGroup):
    MAIN = State()
    Test = State()
class My_profile(StatesGroup):
    MAIN = State()
class My_Group(StatesGroup):
    MAIN = State()
class Search_m(StatesGroup):
    EnterInstrument = State()
    MAIN = State()
class Event(StatesGroup):
    MAIN = State()
class Project(StatesGroup):
    MAIN = State()
class Help(StatesGroup):
    MAIN = State()
class Settings(StatesGroup):
    MAIN = State()
    Enter = State()
class Movement_musicians(StatesGroup):
    MAIN = State()
class DontWorked(StatesGroup):
    MAIN = State()

