from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def choice_buttons():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    reg = types.KeyboardButton('register')
    start = types.KeyboardButton('/start')
    buttons.add(reg, start)

    return buttons

def num():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num_button = types.KeyboardButton('поделиться', request_contact=True)
    buttons.add(num_button)
    return buttons

def geo():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    geo_button = types.KeyboardButton('send location', request_location=True)
    buttons.add(geo_button)
    return buttons


def inline():
    buttons = types.InlineKeyboardMarkup()
    in_b = types.InlineKeyboardButton('Inline1', callback_data = 'in_button')
    in_b2 = types.InlineKeyboardButton('Inline2', callback_data = 'in_button2')
    buttons.row(in_b, in_b2)
    return buttons


def main(get_product_name_id):
    buttons = InlineKeyboardMarkup(row_width=2)
    order = InlineKeyboardButton(text='Оформить заказ', callback_data='order')
    cart = InlineKeyboardButton(text='Корзина', callback_data='cart')
    # return open
    all_pr = [InlineKeyboardButton(text=i[0], callback_data=i[1]) for i in get_product_name_id]
    buttons.row(order)
    buttons.add(*all_pr)
    buttons.row(cart)

    return buttons


def choose_count(plus_or_minus='', curretn_amount=1):
    buttons = InlineKeyboardMarkup(row_width=3)
    plus = InlineKeyboardButton(text='+', callback_data='plus')
    minus = InlineKeyboardButton(text='-', callback_data='minus')
    count = InlineKeyboardButton(text=str(curretn_amount), callback_data=str(curretn_amount))
    add_cart = InlineKeyboardButton(text='Добавить в корзину', callback_data='add_cart')
    back = InlineKeyboardButton(text='Назад', callback_data='back')
    #НОВОЕ!
    delete = InlineKeyboardButton(text='удалить продукт', callback_data='delete')

    if plus_or_minus == 'plus':
        new_amount = int(curretn_amount)
        count = InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))
    elif plus_or_minus == 'minus':
        if int(curretn_amount) > 1:
            new_amount = int(curretn_amount) - 1
            count = InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))

    buttons.add(minus, count, plus)
    buttons.row(add_cart)
    buttons.row(back)
    buttons.row(delete)

    return buttons





def get_cart():
    buttons = InlineKeyboardMarkup(row_width=1)
    clear = InlineKeyboardButton('Очистить корзину', callback_data='clear')
    order = InlineKeyboardButton('Оформить заказ', callback_data='order')
    back = InlineKeyboardButton('Назад', callback_data='back')
    buttons.add(clear, order, back)
    return buttons

