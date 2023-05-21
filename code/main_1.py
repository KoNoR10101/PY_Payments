import telebot
from telebot import types
from img import Deagle, Awp, Nova, Music_kit
import sqlite3
import random

bot = telebot.TeleBot('6173123594:AAEdnBacKch67wWdhPa1nAkQeJxMgJmwKhM')

not_correct_answer = ['Извини, я не понял', 'Try again', 'Повторите попытку']  # некорректные сообщения


@bot.message_handler(commands=['start'])
def start_mess(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('Товары🛍')
    button_2 = types.KeyboardButton('Профиль📝')
    button_3 = types.KeyboardButton('Инструкция📋')
    button_4 = types.KeyboardButton('Техподдержка🛠️')
    markup.row(button_1, button_2)
    markup.row(button_3, button_4)
    bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)
    registration(message)

#меню
@bot.message_handler()
def information_obr(message):
    reg = False

    if message.text == 'Товары🛍':
        buyMenu(message)

    elif message.text == 'Инструкция📋':
        infoMenu(message)

    elif message.text == 'Техподдержка🛠️':
        FAQ(message)

    elif message.text == 'Профиль📝':
        profile(message)

    elif message.text == 'Товар1🛍':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('оплатить товар 1💳')
        button2 = types.KeyboardButton('Назад🔙')
        button3 = types.KeyboardButton('Оставить отзыв')
        markup.row(button1, button2)
        markup.row(button3)
        bot.send_photo(message.chat.id, Awp)
        bot.send_message(message.chat.id, 'оплатить товар 1💳?', reply_markup=markup)
        product = message.text

    elif message.text == 'Товар2🛍':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('оплатить товар 2💳')
        button2 = types.KeyboardButton('Назад🔙')
        button3 = types.KeyboardButton('Оставить отзыв')
        markup.row(button1, button2)
        markup.row(button3)
        bot.send_photo(message.chat.id, Nova)
        bot.send_message(message.chat.id, 'оплатить товар 2💳?', reply_markup=markup)
        product = message.text


    elif message.text == 'Товар3🛍':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('оплатить товар 3💳')
        button2 = types.KeyboardButton('Назад🔙')
        button3 = types.KeyboardButton('Оставить отзыв')
        markup.row(button1, button2)
        markup.row(button3)
        bot.send_photo(message.chat.id, Deagle)
        bot.send_message(message.chat.id, 'оплатить товар 3💳?', reply_markup=markup)
        product = message.text


    elif message.text == 'Товар4🛍':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('оплатить товар 4💳')
        button2 = types.KeyboardButton('Назад🔙')
        button3 = types.KeyboardButton('Оставить отзыв')
        markup.row(button1, button2)
        markup.row(button3)
        bot.send_photo(message.chat.id, Music_kit)
        bot.send_message(message.chat.id, 'оплатить товар 4💳?', reply_markup=markup)
        product = message.text


    elif message.text == 'гайд📋':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


    elif message.text == 'Назад🔙':
        buyMenu(message)


    elif message.text == '✏Написать разработчику':
        text = 'вот ссылка: https://t.me/NOreVerseSHELL'
        bot.send_message(message.chat.id, text)

    elif message.text == 'оплатить товар 1💳':
        buy1 = 'вот ссылка: https://oplata.qiwi.com/form?invoiceUid=5388b2bb-2303-45a1-a869-d106f313dc05'
        bot.send_message(message.chat.id, buy1)

    elif message.text == 'оплатить товар 2💳':
        buy2 = 'вот ссылка: https://my.qiwi.com/Liudmyla-BlDUQU8D1i'
        bot.send_message(message.chat.id, buy2)

    elif message.text == 'оплатить товар 3💳':
        buy3 = 'вот ссылка: https://my.qiwi.com/Liudmyla-BlDUQU8D1i'
        bot.send_message(message.chat.id, buy3)

    elif message.text == 'оплатить товар 4💳':
        buy4 = 'вот ссылка: https://my.qiwi.com/Liudmyla-BlDUQU8D1i'
        bot.send_message(message.chat.id, buy4)

    elif message.text == 'Назад в меню🔙':
        start_mess(message)


    elif message.text == 'Зарегистрироваться':
        registration(message)

    elif message.text == 'История покупок':
        bot.send_message(message.chat.id, "Просим прощения, данная функция пока что не работает")

    elif message.text == 'Оставить отзыв' or message.text == 'Отзывы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Вот ссылка на чат с отзывами.\n'
                                          'Будем рады узнать ваше мнение.\nhttps://t.me/+AuWyQp3V121kNjJi'
                                          , reply_markup=markup)

    else:
        bot.send_message(message.chat.id, not_correct_answer[random.randint(0, 2)])


def buyMenu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('Товар1🛍')
    button_2 = types.KeyboardButton('Товар2🛍')
    button_3 = types.KeyboardButton('Товар3🛍')
    button_4 = types.KeyboardButton('Товар4🛍')
    button_5 = types.KeyboardButton('Назад в меню🔙')

    markup.row(button_1, button_2)
    markup.row(button_3, button_4)
    markup.row(button_5)
    bot.send_message(message.chat.id, 'На данный момент это все товары:', reply_markup=markup)



def profile(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('Отзывы')
    button_2 = types.KeyboardButton('История покупок')
    button_3 = types.KeyboardButton('Назад в меню🔙')

    markup.row(button_1, button_2)
    markup.row(button_3)
    bot.send_message(message.chat.id, 'Переходим в раздел: Профиль', reply_markup=markup)


def infoMenu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('гайд📋')  # здесь будет файл с инструкцией
    file = open('гайдик.txt', "rb")

    f = file.read()
    bot.send_document(message.chat.id, f)
    file.close()
    button_2 = types.KeyboardButton('Назад в меню🔙')
    markup.row(button_1, button_2)


def FAQ(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('✏Написать разработчикам')
    button2 = types.KeyboardButton('Назад в меню🔙')
    markup.row(button1, button2)

    bot.send_message(message.chat.id, 'Раздел ТП.\nПо вопросам псать сюда.',
                     reply_markup=markup)


def registration(message):
    con = sqlite3.connect('PY_Payments_db.db')
    cur = con.cursor()
    query1 = f'''SELECT * FROM users_id WHERE id={message.from_user.id}'''
    res = cur.execute(query1).fetchall()
    if bool(res) == False:
        query = f'''insert into users_id (id, user_nickname, user_name, user_surname) values ({message.from_user.id},
         '{message.from_user.username}', '{message.from_user.first_name}',
         '{message.from_user.last_name}')'''# вывод данных
        cur.execute(query)

    con.commit()
    con.close()


bot.polling(none_stop=True)