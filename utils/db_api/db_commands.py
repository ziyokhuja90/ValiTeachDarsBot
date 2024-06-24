# from typing import Union

# import asyncpg
# from asyncpg import Connection
# from asyncpg.pool import Pool

# from data import config


# class Database:
#     def __init__(self):
#         self.pool: Union[Pool, None] = None

#     async def create(self):
#         self.pool = await asyncpg.create_pool(
#             user=config.DB_USER,
#             password=config.DB_PASS,
#             host=config.DB_HOST,
#             database=config.DB_NAME,
#         )

#     async def execute(
#         self,
#         command,
#         *args,
#         fetch: bool = False,
#         fetchval: bool = False,
#         fetchrow: bool = False,
#         execute: bool = False,
#     ):
#         async with self.pool.acquire() as connection:
#             connection: Connection
#             async with connection.transaction():
#                 if fetch:
#                     result = await connection.fetch(command, *args)
#                 elif fetchval:
#                     result = await connection.fetchval(command, *args)
#                 elif fetchrow:
#                     result = await connection.fetchrow(command, *args)
#                 elif execute:
#                     result = await connection.execute(command, *args)
#             return result

#     # async def create_table_users(self):
#     #     sql = """
#     #     CREATE TABLE IF NOT EXISTS products_user (
#     #     id SERIAL PRIMARY KEY,
#     #     full_name VARCHAR(255) NOT NULL,
#     #     username varchar(255) NULL,
#     #     telegram_id BIGINT NOT NULL UNIQUE
#     #     );
#     #     """
#     #     await self.execute(sql, execute=True)

#     @staticmethod
#     def format_args(sql, parameters: dict):
#         sql += " AND ".join(
#             [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
#         )
#         return sql, tuple(parameters.values())

#     async def add_user(self, full_name, username, telegram_id):
#         sql = "INSERT INTO products_user (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
#         return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

#     async def select_all_users(self):
#         sql = "SELECT * FROM products_user"
#         return await self.execute(sql, fetch=True)
    
#     async def select_all_Categorys(self):
#         sql = """
#         SELECT * FROM Category
#         """
#         return await self.execute(sql, fetchall=True)
    
#     async def select_Subcategory(self , category):
#         sql = f"SELECT * FROM SubCategory Category='{category}'"
#         return await self.execute(sql)

#     async def select_user(self, **kwargs):
#         sql = "SELECT * FROM products_user WHERE "
#         sql, parameters = self.format_args(sql, parameters=kwargs)
#         return await self.execute(sql, *parameters, fetchrow=True)

#     async def count_users(self):
#         sql = "SELECT COUNT(*) FROM products_user"
#         return await self.execute(sql, fetchval=True)

#     async def update_user_username(self, username, telegram_id):
#         sql = "UPDATE products_user SET username=$1 WHERE telegram_id=$2"
#         return await self.execute(sql, username, telegram_id, execute=True)

#     async def delete_users(self):
#         await self.execute("DELETE FROM products_user WHERE TRUE", execute=True)

#     async def drop_users(self):
#         await self.execute("DROP TABLE products_user", execute=True)

#     ### Mahsulotlar uchun jadval (table) yaratamiz
#     # async def create_table_products(self):
#     #     sql = """
#     #     CREATE TABLE IF NOT EXISTS products_product (
#     #     id SERIAL PRIMARY KEY,
#     #
#     #     -- Mahsulot kategoriyasi
#     #     category_code VARCHAR(20) NOT NULL,
#     #     category_name VARCHAR(50) NOT NULL,
#     #
#     #     -- Mahsulot kategoriya ichida ketgoriyasi ("Go'sht"->"Mol go'shti")
#     #     subcategory_code VARCHAR(20) NOT NULL,
#     #     subcategory_name VARCHAR(50) NOT NULL,
#     #
#     #     -- Mahsulot haqida malumot
#     #     productname VARCHAR(50) NOT NULL,
#     #     photo varchar(255) NULL,
#     #     price INT NOT NULL,
#     #     description VARCHAR(3000) NULL
#     #     );
#     #     """
#     #     await self.execute(sql, execute=True)

#     async def add_product(
#         self,
#         # category_code,
#         category_name,
#         # subcategory_code,
#         subcategory_name,
#         lesson_name,
#         lesson_number,
#         videoId=None,
#         telegram=None,
#         youtube=None,
#         description="",
#     ):
#         sql = "INSERT INTO home_product (, category_name, , subcategory_name, lesson_name, lesson_number, videId, telegram, youtube, description) VALUES($1, $2, $3, $4, $5, $6, $7, $8) returning *"
#         return await self.execute(
#             sql,
#             # category_code,
#             category_name,
#             # subcategory_code,
#             subcategory_name,
#             lesson_name,
#             lesson_number,
#             videoId,
#             telegram,
#             youtube,
#             description,
#             fetchrow=True,
#         )

#     async def get_categories(self):
#         sql = "SELECT DISTINCT category_name FROM home_product"
#         return await self.execute(sql, fetch=True)

#     async def get_subcategories(self, category_name):
#         sql = f"SELECT DISTINCT subcategory_name FROM home_product WHERE category_name='{category_name}'"
#         return await self.execute(sql, fetch=True)

#     async def count_products(self, category_name, subcategory_name=None):
#         if subcategory_name:
#             sql = f"SELECT COUNT(*) FROM home_product WHERE category_name='{category_name}' AND subcategory_name='{subcategory_name}'"
#         else:
#             sql = f"SELECT COUNT(*) FROM home_product WHERE category_name='{category_name}'"
#         return await self.execute(sql, fetchval=True)

#     async def select_lesson(self, category, subcategory):
#         sql = f"SELECT * FROM home_product WHERE category_name='{category}' AND subcategory_name='{subcategory}'"
#         return await self.execute(sql, fetchval=True)

#     async def get_product(self, product_id):
#         sql = f"SELECT * FROM home_product WHERE id={product_id}"
#         return await self.execute(sql, fetchrow=True)

#     async def drop_products(self):
#         await self.execute("DROP TABLE home_product", execute=True)

from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config

class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        if self.pool is None:
            self.pool = await asyncpg.create_pool(
                user=config.DB_USER,
                password=config.DB_PASS,
                host=config.DB_HOST,
                database=config.DB_NAME,
            )

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        if self.pool is None:
            await self.create()  # Ensure the pool is initialized if not already
        
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
                else:
                    result = None
            return result

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO products_user (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM products_user"
        return await self.execute(sql, fetch=True)
    
    async def select_all_categories(self):
        sql = "SELECT * FROM Category"
        return await self.execute(sql, fetch=True)
    
    async def select_subcategory(self, category):
        sql = "SELECT * FROM SubCategory WHERE category=$1"
        return await self.execute(sql, category, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM products_user WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM products_user"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE products_user SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM products_user WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE products_user", execute=True)

    async def add_product(
        self,
        category_name,
        subcategory_name,
        lesson_name,
        lesson_number,
        videoId=None,
        telegram=None,
        youtube=None,
        description="",
    ):
        sql = """INSERT INTO home_product (category_name, subcategory_name, lesson_name, 
                 lesson_number, videoId, telegram, youtube, description) 
                 VALUES($1, $2, $3, $4, $5, $6, $7, $8) returning *"""
        return await self.execute(
            sql,
            category_name,
            subcategory_name,
            lesson_name,
            lesson_number,
            videoId,
            telegram,
            youtube,
            description,
            fetchrow=True,
        )

    async def get_categories(self):
        sql = "SELECT DISTINCT category_name FROM home_product"
        return await self.execute(sql, fetch=True)

    async def get_subcategories(self, category_name):
        sql = "SELECT DISTINCT subcategory_name FROM home_product WHERE category_name=$1"
        return await self.execute(sql, category_name, fetch=True)

    async def count_products(self, category_name, subcategory_name=None):
        if subcategory_name:
            sql = "SELECT COUNT(*) FROM home_product WHERE category_name=$1 AND subcategory_name=$2"
            return await self.execute(sql, category_name, subcategory_name, fetchval=True)
        else:
            sql = "SELECT COUNT(*) FROM home_product WHERE category_name=$1"
            return await self.execute(sql, category_name, fetchval=True)

    async def select_lesson(self, category, subcategory):
        sql = "SELECT * FROM home_product WHERE category_name=$1 AND subcategory_name=$2"
        return await self.execute(sql, category, subcategory, fetch=True)

    async def select_lessonLessonNumber(self, category, subcategory , lesson_number):
        sql = "SELECT * FROM home_product WHERE category_name=$1 AND subcategory_name=$2 AND lesson_number=$3"
        return await self.execute(sql, category, subcategory, lesson_number, fetch=True)

    async def get_product(self, product_id):
        sql = "SELECT * FROM home_product WHERE id=$1"
        return await self.execute(sql, product_id, fetchrow=True)

    async def drop_products(self):
        await self.execute("DROP TABLE home_product", execute=True)
