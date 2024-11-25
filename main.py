import asyncio
import logging

from bot_config import bot, dp, database

from handlers import private_router
from handlers.group import group_router


async def on_startup(bot):
    database.create_tables()
    await bot.send_message(chat_id=5747517813,text="Я онлайн")

# запуск бота
async def main():
    dp.include_router(private_router)
    dp.include_router(group_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # логирование
    asyncio.run(main())