from config import dp
from aiogram.utils import executor
import logging


from handlers import client, callback, admin, extra, fsmAdminMenu, notification
from database.bot_db import sql_create


async def on_startup(_):
    sql_create()

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminMenu.register_handlers_fsmAdminMenu(dp)
notification.register_handlers_notifications(dp)

extra.register_handlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
