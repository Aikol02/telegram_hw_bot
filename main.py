from config import dp
from aiogram.utils import executor
import logging
from database.bot_db import sql_create


async def on_startup(_):
    sql_create()

from handlers import client, callback, extra, fsmAdminMenu


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_extra(dp)
fsmAdminMenu.register_handlers_fsmAdminMenu(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
