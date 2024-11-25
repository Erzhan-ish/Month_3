from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    print(F'Message chat type: {message.chat.type}')
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
            ],
            [
                types.InlineKeyboardButton(
                    text="О нас",
                    callback_data="about_us"
                )
            ]
        ]
    )
    await message.answer(msg, reply_markup=kb)
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text=msg,
    #

#@start_router.callback_query(lambda cb: cb.data == "about")
@start_router.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.message.answer("О нас")