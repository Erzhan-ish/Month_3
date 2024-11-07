import asyncio
import logging

from bot_config import bot, dp
from handlers.other_messages import other_messages_router
from handlers.picture import picture_router
from handlers.start import start_router


# запуск бота
async def main():
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(other_messages_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # логирование
    asyncio.run(main())