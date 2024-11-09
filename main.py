import asyncio
from aiogram import Bot, Dispatcher,F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN
from translate  import Translator
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

ru_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
en_letters = 'abcdefghijklmnopqrstuvwxyz'

@dp.message()
async def echo(message: Message):
    text = message.text
    if text[0].lower() in ru_letters:
        translation = Translator(from_lang ='russian', to_lang='english')
    elif text[0].lower() in en_letters:
        translation = Translator(from_lang ='english', to_lang='russian')
    else:
        await message.answer("�� не понимаю языка этого сообщения.")
        return
    translation = translation.translate(text)
    await message.answer(translation)





@dp.message(Command('voice'))
async def voice(message: Message):
     voice = FSInputFile('Tenor.ogg')
     await message.answer_voice(voice)


@dp.message(F.photo)
async def aiphoto(message: Message):
    list=["Ого какая фотка!","Не могу понять что на фото!", "НЕ присылай мне фото такого содержания я приличная девочка!"]
    await message.answer(random.choice(list))
    await bot.download(message.photo[-1],destination=f'img/{message.photo[-1].file_id}.jpg')


@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer("Искусственный интеллект (ИИ) — это не инструмент или программа, а отдельное направление компьютерных наук. Специалисты по ИИ разрабатывают системы, которые анализируют информацию и решают задачи аналогично тому, как это делает человек.")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name} ! Я бот!")


@dp.message()
async def start(message: Message):
    await message.send_copy(chat_id=message.chat.id)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())