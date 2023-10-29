"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

# считываем данные в переменные из 3 файлов
with open('north_data/employees_data.csv') as csvfile:
    employees_data = list(csv.reader(csvfile))

with open('north_data/customers_data.csv') as csvfile:
    customers_data = list(csv.reader(csvfile))

with open('north_data/orders_data.csv') as csvfile:
    orders_data = list(csv.reader(csvfile))

# параметры для подключения к БД
conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
)

try:
    with conn:
        with conn.cursor() as cur:

            # заносим данные в таблицы пропуская первую строку[1:]
            cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', employees_data[1:])
            cur.execute("SELECT * FROM employees")

            cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', customers_data[1:])
            cur.execute("SELECT * FROM customers")

            cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', orders_data[1:])
            cur.execute("SELECT * FROM orders")

            # запускаем все считывания
            rows = cur.fetchall()

finally:   # влюбом случае закроем конект с БД
    conn.close()


# for customers in customers_data:
#     print(customers)