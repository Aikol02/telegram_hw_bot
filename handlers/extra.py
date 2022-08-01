import asyncio
from aiogram import types, Dispatcher
from config import bot


async def echo(message: types.Message):
    x = message.text
    try:
        x = int(x)
        c = 1
    except:
        pass
        c = 0
    if c == 1:
        await bot.send_message(message.chat.id, f"{x * x}")
    elif c == 0:
        await bot.send_message(message.chat.id, x)
    else:
        pass
# второе задание
    if message.text.startswith('!pin'):
        if not message.reply_to_message:
            await bot.send_message(message.chat.id, f'Specify a message to pin (reply to that)')
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    #
    # if message.text.lower() == "dice":
    #     v = await bot.send_dice(message.chat.id, emoji='🎲')
    #     await bot.send_message(message.chat.id, "Your throw")
    #     d = v.dice.value
    #     print(d)
    #     k = await bot.send_dice(message.chat.id, emoji='🎲')
    #     await bot.send_message(message.chat.id, "My throw")
    #     f = k.dice.value
    #     print(f)
    #     await asyncio.sleep(5)
    #     if d > f:
    #         await bot.send_message(message.chat.id, "You won")
    #     elif d < f:
    #         await bot.send_message(message.chat.id, "I won")
    #     else:
    #         await bot.send_message(message.chat.id, "Leg and leg")
    #


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
