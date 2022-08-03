import random
from aiogram import types, Dispatcher
from config import bot
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from config import ADMIN
from database.bot_db import sql_command_random
from parser import dorama

from keyboards import client_kb


async def start(message: types.Message):
    await bot.send_message(message.chat.id, f'Поздравляю вы запустили меня',
                           reply_markup=client_kb.start_markup)


async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1',
    )
    markup.add(button_call_1)

    question = 'Чему равно число пи?'
    answers = [
        '3.15', '4.35', '3.14', '3.13'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def mem(message: types.Message):
    photo2 = open('media/mem.png', 'rb')
    photo3 = open('media/mem2.png', 'rb')
    await bot.send_photo(message.chat.id, photo=photo2)
    await bot.send_photo(message.chat.id, photo=photo3)


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply("Надо ответить на сообщение🙄")


async def game(message: types.Message):
    if message.text.startswith('game'.lower()):
        if message.from_user.id in ADMIN:
            emojies = ['🎯', '🎳', '🎰', '🎲', '⚽', '️🏀']
            rand_game = random.choice(emojies)
            await bot.send_dice(message.chat.id, emoji=rand_game)
    else:
        try:
            k = int(message.text)
            await bot.send_message(message.chat.id, k * k)
        except:
            await bot.send_message(message.chat.id, message.text)


async def show_random_food(message: types.Message):
    await sql_command_random(message)


async def parser_dorama(message: types.Message):
    data = dorama.parser()
    for dorams in data:
        await bot.send_message(
            message.from_user.id,
            f"{dorams['title']}\n\n"
            f"{dorams['desc']}\n"
            f"{dorams['year']}\n\n"
            f"{dorams['link']}")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(parser_dorama, commands=["doramy"])
    dp.register_message_handler(game)
