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