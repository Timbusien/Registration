import telebot

import buttons

bot = telebot.TeleBot('6087928480:AAFM7NYRgrZhMAOPcxi9UU2U-Js9G01FTeI')

@bot.message_handler(commands=['start'])
def start(message):
    global user_id
    user_id = message.from_user.id
    print(message)
    bot.send_message(user_id, 'привет!', reply_markup=buttons.choice_buttons())


@bot.message_handler(content_types=['text'])
def start_bot(message):
    if message.text == 'register':
        bot.send_message(user_id, 'send me your name', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_name = message.text
    bot.send_message(user_id, 'fine, so send me a num', reply_markup=buttons.num())
    bot.register_next_step_handler(message, get_num, user_name)

def get_num(message, user_name):
    if message.contact and message.contact.phone_number:
        user_num = message.contact.phone_number
        bot.send_message(user_id, 'send location')
        bot.register_next_step_handler(message, get_loc, user_name, user_num)
    else:
        bot.send_message(user_id, 'use button for location', reply_markup=buttons.geo())
        bot.next_step_backend(message, get_num)

def get_loc(message, user_name, user_num):
    if message.location:
        user_location = message.location
        bot.send_message(user_id, 'send what you want', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_serv, user_name, user_num, user_location)
    else:
        bot.send_message(user_id, 'send by button')
        bot.register_next_step_handler(message, get_loc, user_name, user_num)

def get_serv(message, user_name, user_num, user_loc):
    user_serv = message.text
    bot.send_message(user_id, 'how many days')
    bot.register_next_step_handler(message, get_deadl, user_num, user_name, user_serv, user_loc)

def get_deadl(message, user_num, user_name, user_serv, user_loc):
    user_deadl = message.text
    bot.send_message(-1001500295547, f'New order!\n\n Clietn name {user_name}\n'
                                          f'Number: {user_num}\n'
                                          f'Location: {user_loc}\n'
                                          f'Servicing: {user_serv}\n'
                                          f'Deadline: {user_deadl}\n')
    bot.send_message(user_id, 'Successfull')
    bot.register_next_step_handler(message,start_bot)




#-1001500295547
bot.infinity_polling()


