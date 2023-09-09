from telebot import types

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
