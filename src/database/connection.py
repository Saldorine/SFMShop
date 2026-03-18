import psycopg2
from psycopg2 import Error



def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="sfmshop",
            user="postgres",
            password="12345678"
            )
        return conn
    except Error as e:
        print("Ошибка при подключении к базе данных:", e)
        return None


def add_product(conn, name, price, quantity):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", (name, price, quantity))
            conn.commit()
    except Error  as e:
        print("Ошибка при добавлении товара:", e)


def get_all_products(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            result = cursor.fetchall()
        return result
    except Error as e:
        print("Ошибка при получении товаров:", e)
        return None

def update_product_price(conn, product_id, new_price):
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE products SET price=%s WHERE id=%s", (new_price, product_id))
            conn.commit()
    except Error as e:
        print("Ошибка при попытке обновить данные товара:", e)


def create_user(conn, name, email):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("Пользователь создан:", name, email)
    except Error as e:
        print("Ошибка при создании нового пользователя:", e)


def get_user_by_id(conn, user_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id=%s", (user_id, ))
            id, name, email, *_ = cursor.fetchone()
            result = {'id': id, 'name': name, 'email': email}
        return result
    except Error as e:
        print("Ошибка при получении пользователя:", e)
        return None


def create_order(conn, user_id, total):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO orders (user_id, total) VALUES (%s, %s)", (user_id, total))
            conn.commit()
            print(f"Заказ создан: user_id={user_id}, total={total:.2f}")
    except Error as e:
        print("Ошибка при создании заказа:", e)


def get_user_orders(conn, user_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM orders WHERE user_id=%s", (user_id, ))
            result = cursor.fetchall()
        return result
    except Error as e:
        print("Ошибка при получении заказа пользователя:", e)
        return []


def delete_order(conn, order_id):
    try:
        with conn.cursor() as cursor:
            deleted_rows = 0
            cursor.execute("DELETE FROM order_items WHERE order_id=%s", (order_id, ))
            deleted_rows += cursor.rowcount
            cursor.execute("DELETE FROM orders WHERE id=%s", (order_id, ))
            deleted_rows += cursor.rowcount

            conn.commit()
        return deleted_rows
    except Error as e:
        print("Ошибка при попытке удалить заказ:", e)
        return None
