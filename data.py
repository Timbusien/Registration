import sqlite3
from datetime import datetime

db = sqlite3.connect('my_database.db')

KFC = db.cursor()
# store = db.cursor()
# cart = db.cursor()

KFC.execute('CREATE TABLE IF NOT EXISTS user'
             ' (name TEXT, number TEXT, tg_id INT, address TEXT, date DATETIME);')

KFC.execute('CREATE TABLE IF NOT EXISTS store'
            '(pr_name TEXT, pr_des TEXT, price REAL, product_id PRIMARY KEY AUTOINCREMENT, product_quantity INT, pr_data DATETIME, TEXT, photo TEXT);')

KFC.execute('CREATE TABLE IF NOT EXISTS cart'
            '(user_id INT, user_product TEXT, quantity INT, total REAL);')


def reg_user(tg_id, name, number, address):
    db = sqlite3.connect('my_database.db')
    KFC = db.cursor()

    KFC.execute('INSERT INTO user '
                '(tg_id, name, address, number, date) VALUES'
                '(?, ?, ?, ?, ?);', (tg_id, name, number, address, datetime.now()))

    db.commit()

def check(user_id):
    db = sqlite3.connect('my_database.db')

    KFC = db.cursor()

    checking = KFC.execute('SELECT tg_id user WHERE tg_id=?, (user_id,)')

    if checking.fetchone():
        return True
    else:
        return False


def add_product(pr_name, price, pr_quantity, photo, pr_des):
    db = sqlite3.connect('my_database.db')
    KFC = db.cursor()

    KFC.execute('INSERT INTO store '
                '(pr_name, price, pr_quantity, pr_des, pr_photo) VALUES'
                '(?, ?, ?, ?, ?);', (pr_name, price, pr_quantity, pr_des, photo, datetime.now()))

    db.commit()


def get_product_name_id():
    db = sqlite3.connect('my_database.db')
    KFC = db.cursor()

    product = KFC.execute('SELECT pr_name, product_id, pr_quantity, FROM store;').fetchall()
    #print(product)
    sorted_pr = [(i[0], i[1]) for i in product if i[2] > 0]

    return sorted_pr

def get_product_id(pr_id):
    db = sqlite3.connect('my_database.db')
    KFC = db.cursor()

    product_id = KFC.execute('SELECT pr_name, pr_des, photo, price'
                             'FROM store WHERE pr_id=?', (pr_id,)).fetchone()

    return product_id


def append_product(user_id, user_product, quantity):
    db = sqlite3.connect('my_database.db')
    KFC = db.cursor()

    price_product = get_product_id(user_product)[2]

    db.execute('INSERT INTO cart '
               '(user_id, user_product, quantity)'
               'VALUES (?, ?, ?, ?);', (user_id, user_product, quantity, quantity * price_product))


