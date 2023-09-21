import telebot
import data
import buttons
#from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot('6087928480:AAFM7NYRgrZhMAOPcxi9UU2U-Js9G01FTeI')
user = {}
data.add_product('apple', 10000, 10, 'Apple just an apple', '')


@bot.message_handler(commands=['start'])
def start(message):
    # global user_id
    user_id = message.from_user.id
    print(message)
    print(user_id)
    check = data.check(user_id)
    if check:
        products = data.get_product_name_id()
        # bot.send_message(user_id, 'привет!', reply_markup=buttons.choice_buttons())
        bot.send_message(user_id, 'Привет!', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, 'Выберите опции', reply_markup=buttons.main(products))
    elif not check:
        bot.send_message(user_id, 'Привет отправьте ваше имя')

def get_name(message):
    user_id = message.from_user.id
    user = message.text
    bot.send_message(user_id, 'Отправьте свой номер!', reply_markup=buttons.num())
    bot.register_next_step_handler(message, get_num, user)
    # user_name = message.text
    # bot.send_message(user_id, 'fine, so send me a num', reply_markup=buttons.num())


def get_num(message, name):
    user_id = message.from_user.id

    if message.contact:
        phone_number = message.contact.number
        data.reg_user(user_id, name, phone_number, 'Not yet')
        bot.send_message(user_id, 'Вы успешно зарегистрировались!', reply_markup=telebot.types.ReplyKeyboardRemove())
        products = data.get_product_name_id()
        bot.send_message(user_id, 'Выберите пункт из меню', reply_markup=buttons.main(products))
    elif not message.contact:
        bot.send_message(user_id, 'Отправьте ваш контакт через кнопку', reply_markup=buttons.num())
        bot.register_next_step_handler(message, get_num, name)


@bot.callback_query_handler(lambda call: call.data in ['plus', 'minus', 'add_cart', 'back'])
def get_product_count(call):
    user_id = call.message.chat.id
    if call.data == 'plus':
        actual = user[user_id]['product_quantity']

        user[user_id]['product_quantity'] += 1
        bot.edit_message_reply_markup(chat_id=user_id, message_id=call.message.message_id,
                                      reply_markup=buttons.choose_count('plus', actual))

    elif call.data == 'minus':
        actual = user[user_id]['product_quantity']

        user[user_id]['product_quantity'] -= 1
        bot.edit_message_reply_markup(chat_id=user_id, message_id=call.message.message_id,
                                      reply_markup=buttons.choose_count('minus', actual))

    elif call.data == 'back':
        products = data.get_product_name_id()
        bot.edit_message_text('Выберите пункт меню', user_id, call.message.message_id,
                              reply_markup=buttons.main(products))

    elif call.data == 'add_cart':
        product_count = user[user_id]['product_quantity']
        user_product = user[user_id]['pr_name']

        data.append_product(user_id, user_product, product_count)
        products = data.get_product_name_id()
        bot.edit_message_text('Продукт был добавлен в вашу корзину\n Что-то ещё?',
                              user_id, call.message.message_id,
                              reply_markup=buttons.main(products))


@bot.callback_query_handler(lambda call: call.data in ['order', 'cart', 'clear_cart'])
def main_menu(call):
    user_id = call.message.chat.id
    message_id = call.message.chat.id
    if call.data == 'order':
        bot.delete_message(user_id, message_id)
        bot.send_message(user_id, 'Отправьте вашу геолокацию для заказа!', reply_markup=buttons.geo())
        bot.register_next_step_handler(call.message, start)
    elif call.data == 'cart':
        user_cart = data.get_cart(user_id)

        full = 'Ваша корзина:\n\n'
        total = 0

        for i in user_cart:
            full += f'{i[0]} * {i[1]} = {i[2]}\n'
            total += i[2]

        full = f'\n Всего ко оплате: {total}'

        bot.edit_message_text(full, user_id, message_id, reply_markup=buttons.get_cart())


@bot.message_handler(content_types=['text'])
def start_bot(message):
    user_id = message.text
    if message.text == 'register':
        bot.send_message(user_id, 'send me your name', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)


def get_loc(message, user_name, user_num):
    user_id = message.text
    if message.location:
        user_location = message.location
        bot.send_message(user_id, 'send what you want', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_serv, user_name, user_num, user_location)
    else:
        bot.send_message(user_id, 'send by button')
        bot.register_next_step_handler(message, get_loc, user_name, user_num)

def get_serv(message, user_name, user_num, user_loc):
    user_id = message.text
    user_serv = message.text
    bot.send_message(user_id, 'how many days')
    bot.register_next_step_handler(message, get_deadl, user_num, user_name, user_serv, user_loc)

def get_deadl(message, user_num, user_name, user_serv, user_loc):
    user_id = message.text
    user_deadl = message.text
    bot.send_message(-1001500295547, f'New order!\n\n Client name {user_name}\n'
                                          f'Number: {user_num}\n'
                                          f'Location: {user_loc}\n'
                                          f'Servicing: {user_serv}\n'
                                          f'Deadline: {user_deadl}\n')
    bot.send_message(user_id, 'Successfull')
    bot.register_next_step_handler(message, start_bot)

# @bot.message_handler(commands=['inlines'])
# def inline_t():
#     bot.send_message(user_id, 'Выберите кнопку', reply_markup=buttons.inline())







#-1001500295547
bot.infinity_polling()



