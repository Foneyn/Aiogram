from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
], resize_keyboard=True)

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Видио", url="https://www.youtube.com/"),
    InlineKeyboardButton(text="Музыка", url="https://www.shazam.com/ru-ru"),
    InlineKeyboardButton(text="Новости", url="https://iz.ru/")

    ]])
inline_keyboard2 = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='info'),
    ]])
inline_keyboard3 = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Опция 1", url="https://www.vesti.ru/"),
    InlineKeyboardButton(text="Опция 2", url="https://ria.ru/"),

    ]])

test = ["Кнопка  1", "Кнопка 2","Кнопка  3", "Кнопка  3",]

async def test_keyboard():
   keyboard = ReplyKeyboardBuilder()
   for key in test:
       keyboard.add(KeyboardButton(text=key, url="https://iz.ru/"))
   return keyboard.adjust(2).as_markup()

