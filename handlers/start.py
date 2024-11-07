from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    msg = f"Привет, {name}"
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Наш инстаграм",
                    url="https://instagram.com/geeks"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Наш сайт",
                    url="https://geeks.kg"
                )
            ]
        ]
    )
    await message.answer(msg, reply_markup=kb)
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text=msg,
    # )