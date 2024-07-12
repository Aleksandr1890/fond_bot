import aiosqlite


# Определение модели пользователя
class MyUser:
    def __init__(
            self, user_id, username,
            name=None, surname=None, surname_2=None,
            phone=None, inn=None, status=None, register=False
    ):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.surname = surname
        self.surname_2 = surname_2
        self.phone = phone
        self.inn = inn
        self.status = status
        self.register = register


async def create_database():
    # Укажите имя файла базы данных, например, "my_database.db"
    db_file = "db_id"

    # Открываем базу данных
    async with aiosqlite.connect(db_file) as db:
        # Создаем курсор для выполнения SQL-запросов
        cursor = await db.cursor()

        # Создаем таблицы и выполняем другие операции с базой данных
        await cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                username TEXT,
                name TEXT,
                surname TEXT,
                surname_2 TEXT,
                phone TEXT,
                inn TEXT,
                status TEXT,
                register BOOLEAN
            )
        ''')

        await cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                username TEXT,
                conference BOOLEAN,
                seminar BOOLEAN
            )
        ''')

        # Закрываем курсор и сохраняем изменения
        await db.commit()


# Функция для добавления пользователя в базу данных
async def add_user(user):
    async with aiosqlite.connect('db_id') as db:
        await db.execute(
            "INSERT OR REPLACE INTO users (user_id, username) VALUES (?, ?)",
            (user.user_id, user.username)
        )
        await db.execute(
            "INSERT OR REPLACE INTO events (user_id, username, conference, seminar) VALUES (?, ?, False, False)",
            (user.user_id, user.username)
        )
        await db.commit()


# Функция для получения пользователя из базы данных
async def get_user(user_id, username):
    async with aiosqlite.connect('db_id') as db:
        cursor = await db.execute(
            "SELECT user_id, username FROM users WHERE user_id=?",
            (user_id,)
        )
        row = await cursor.fetchone()
        if row:
            return MyUser(user_id, username)
        return None


# Функция для добавления регистраций в базу данных
async def register_user(user, user_id):
    async with aiosqlite.connect('db_id') as db:
        await db.execute(
            "UPDATE users SET name=?, phone=?, inn=?, status=?, register=? WHERE user_id=?",
            (user.name, user.phone, user.inn, user.status, user.register, user_id)
        )
        await db.commit()


async def get_register_user(user_id):
    async with aiosqlite.connect('db_id') as db:
        cursor = await db.execute(
            "SELECT register FROM users WHERE user_id=? AND register=1",
            (user_id,)
        )
        row = await cursor.fetchone()
        if row:
            return True
        else:
            return False


async def get_events_data(user_id):
    async with aiosqlite.connect('db_id') as db:
        cursor = await db.execute(
            "SELECT conference, seminar FROM events WHERE user_id=?",
            (user_id,)
        )
        row = await cursor.fetchone()
        return row
