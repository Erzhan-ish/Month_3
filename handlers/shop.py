from aiogram import F, Router, types
from aiogram.filters import Command

from bot_config import database

shop_router = Router()


@shop_router.message(Command("books"))
async def show_all_books(message: types.Message):
    all_genres = database.fetch("SELECT * FROM genres")
    if not all_genres:
        await message.answer("Нет ни одного жанра")
        return
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text=genre["name"]) for genre in all_genres]
        ]
    )
    await message.answer("Выберите жанр литературы", reply_markup=kb)

def chek_genre_filter(message: types.Message):
    print("inside genre filter")
    all_genres = database.fetch(
        query="SELECT name FROM genres WHERE name = ?",
        params=(message.text,)) # [{'name'} : 'Приключение'}]
    if all_genres:
        return True

    return False


@shop_router.message(chek_genre_filter)
async def show_books_by_genre(message: types.Message):
    all_books = database.fetch(
        query="SELECT * FROM books JOIN genres ON books.genre_id = genres.id WHERE genre = ?",
        params=(message.text, )
    )
    print(all_books)
    if not all_books:
        await message.answer("Извините книг данного жанра нет")
        return
    await message.answer("Книги из нашего каталога: ")
    for book in all_books:
        await message.answer(F"Название : {book['name']}\n"
                             F"Цена : {book['price']}")