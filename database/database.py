import sqlite3

class Database:
    def __init__(self, path: str) -> None:
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    CREATE TABLE IF NOT EXISTS survey_results(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(15) NOT NULL,
                        age INTEGER NOT NULL,
                        gender TEXT NOT NULL,
                        genre TEXT NOT NULL
                    )
                """
            )
            conn.execute(
                """
                    CREATE TABLE IF NOT EXISTS genres(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )
                """
            )
            conn.execute(
                """
                    CREATE TABLE IF NOT EXISTS books(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name text NOT NULL,
                        author text NOT NULL,
                        price INTEGER NOT NULL,
                        genre TEXT NOT NULL,
                        FOREIGN KEY(genre_id) REFERENCES genres(id)
                    )
                """
                )

            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)
            conn.commit()

    def fetch(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as conn:
            if not params:
                params = tuple()
            result = conn.execute(query, params)
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(r) for r in data]



# conn = sqlite3.connect("database.sqlite")
# cursor = conn.cursor()
#
# conn.execute("""
#     CREATE TABLE IF NOT EXISTS survey_results(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(15) NOT NULL,
#         age INTEGER NOT NULL,
#         gender TEXT NOT NULL,
#         genre TEXT NOT NULL
# )
# """)
#
# conn.commit()