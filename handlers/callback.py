from aiogram import types, Dispatcher
from config import bot
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_2',
    )
    markup.add(button_call_2)
    question = 'Кто эти люди?'
    answers = [
        'никто', 'Не знаю их', 'Оснаватели Google', 'Оснаватели Однакласников'
    ]
    photo = open('media/brinla.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_3',
    )
    markup.add(button_call_3)
    questions = 'Кто придумал наушники'
    answer = [
        'кто ни будь...', 'Билл Гейтс', 'Человек', 'Натаниэль Болдуин', 'кто-то умнее нас'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=questions,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):
    questions_ = 'Когда отмечается день программиста?'
    answer_ = [
        'не знаю совсем', '14-октября', '11-апреля', '13-сентября'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=questions_,
        options=answer_,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Если ты программист, то, за считанные секунды можешь отгадать",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')
    dp.register_callback_query_handler(quiz_4, lambda call: call.data == 'button_call_3')
