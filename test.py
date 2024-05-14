from aiogram import Bot, types
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

# Задайте токен бота и инициализируйте бота и диспетчер
# Токен должен быть введен в формате "TOKEN"
token = "6752526100:AAFCSA3zE7LTV88AP68ozKPd90DxJ14Upks"
bot = Bot(token=token)
dp = Dispatcher()

# Функция, которая будет вызываться при нажатии на чекбокс
async def checkbox_callback(callback_query: types.CallbackQuery):
    selected_item = callback_query.data
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id, f"Вы выбрали: {selected_item}")

# Создайте чекбокс
checkbox_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Пункт 1", callback_data="item1"),
            InlineKeyboardButton(text="Пункт 2", callback_data="item2"),
            InlineKeyboardButton(text="Пункт 3", callback_data="item3"),
        ],
    ]
)

# Отправьте сообщение с чекбоксом
async def send_checkbox_message(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Выберите пункт:",
        reply_markup=checkbox_markup
    )

# Создайте обработчик для обратного вызова
@dp.callback_query_handler(lambda c: True)
async def callback_query_handler(callback_query: types.CallbackQuery):
    await checkbox_callback(callback_query)

# Создайте обработчик для сообщения
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await send_checkbox_message(message)

# Запустите бота
from aiogram import executor
executor.start_polling(dp, skip_updates=True)