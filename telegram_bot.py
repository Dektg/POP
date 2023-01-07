import datetime

import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
from py_currency_converter import convert
import time
cg = CoinGeckoAPI()

bot = telebot.TeleBot('5986032038:AAHuxoPdJQSy09jRGUh7HMOkOhpZrk25hkM')#Подключение бота по ключу BotFather

@bot.message_handler(commands=['start'])#Бот отслеживает команду /start
def main(message):

    button = types.ReplyKeyboardMarkup(resize_keyboard=True)#Если это не написать кнопки будут очень большими
    button.add(types.KeyboardButton('🚀 Взлет'), types.KeyboardButton('📝 О проекте'), types.KeyboardButton('💻 Инвестиции'), types.KeyboardButton('🔧 Инструменты'), types.KeyboardButton('💳 Кошелёк'), types.KeyboardButton('⚙ Тех. Поддержка'))



    msg = bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=button)

    bot.register_next_step_handler(msg, choice)#Переход к следущему шагу

def choice(message):
    if message.text == '🚀 Взлет':
        vzlet(message)
    elif message.text == '📝 О проекте':
        qiwiethereum(message)
    elif message.text == '💻 Инвестиции':
        c_course(message)
    elif message.text == '🔧 Инструменты':
        c_course(message)
    elif message.text == '💳 Кошелёк':
        c_course(message)
    elif message.text == '⚙ Тех. Поддержка':
        c_course(message)
    else:
        main(message)

def c_course(message):
    price = cg.get_price(ids='bitcoin, ethereum', vs_currencies='rub')
    bot.send_message(message.chat.id, f'Курс криптовалют:\n\n'
       f'1 BTC == {price["bitcoin"]["rub"]} RUB\n'
       f'1 ETH == {price["ethereum"]["rub"]} RUB\n\n\n'
       f'Курс обмена:\n\n'
       f'1 BTC == {price["bitcoin"]["rub"] * 1.03} RUB\n'
       f'1 ETH == {price["ethereum"]["rub"] * 1.03} RUB')
    main(message)

def vzlet(message):

    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Пополнить', callback_data='question_1')
    item2 = types.InlineKeyboardButton('Вернуться', callback_data='goodbye')
    markup.add(item, item2)
    file = open('photo_1.jpeg', 'rb')

    bot.send_photo(message.chat.id, file, 'Для того чтобы взлететь, '
                                      'Вам нужно пополнить кошелек на 5000 RUB', reply_markup=markup)

def deposit(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Банковская карта', callback_data='balance_1')
    item2 = types.InlineKeyboardButton('Криптовалюта', callback_data='balance_2')
    markup.add(item, item2)

    bot.send_message(message.chat.id, '📤 Выберите платежную систему на которую хотите совершить перевод для '
                                                    'пополнение средств в бота\n▪ Моментальные зачисление, а также автоматическая конверсия.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'question_1':
            bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.id)
            deposit(call.message)
        elif call.data == 'goodbye':
            bot.send_message(call.message.chat.id,'Вернулся')
            main(call.message)

def proverka(message): #проверяет введенная сумма больше 5k
    try:
        global course
        course = {}
        proverka = {}
        proverka['qiwibitcoin'] = message.text
        course = float(proverka['qiwibitcoin'])

        price = cg.get_price(ids='bitcoin', vs_currencies='rub')  # курс

        if course >= 2000:
            msg = bot.send_message(message.chat.id, f'Вы получите {float("{0:.8f}".format(course / (price["bitcoin"]["rub"] * 1.03)))} BTC на ваш кошелек.\n'
                                              f'Пожалуйста укажите ваш BTC адрес.')
            bot.register_next_step_handler(msg, proverka2)#Переход к следущему шагу
        else:
            bot.send_message(message.chat.id, 'Минимальная сумма обмена составляет 2000 рублей')
            qiwibitcoin(message)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректные данные')
        qiwibitcoin(message)

def proverka2(message): #проверяет введенный кошелек
    global wallet
    wallet = {}
    wallet["proverka"] = message.text #Здесь мы указываем ваш кошелек
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)#Если это не написать кнопки будут очень большими
    button.add(types.KeyboardButton('Подтверждаю оплату'))

    price = cg.get_price(ids='bitcoin', vs_currencies='rub')  # курс
    msg = bot.send_message(message.chat.id, f'Вы обмениваете {course} на {float("{0:.8f}".format(course / (price["bitcoin"]["rub"] * 1.03)))} BTC.\n'
                                      f'Ваш кошелек: {wallet["proverka"]}\n\n'
                                      f'Мы ожидаем от вас оплаты на QIWI в размере {course} по реквизитам: +79510006255\n'
                                            f'После оплаты нажмите на кнопку подтверждения.', reply_markup=button)

    bot.register_next_step_handler(msg, finish)  # Переход к следущему шагу


def finish(message):
    price = cg.get_price(ids='bitcoin', vs_currencies='rub')  # курс

    if message.text == 'Подтверждаю оплату':
        bot.send_message(message.chat.id, f'Ваша заявка была создана {datetime.datetime.now()}.\nОбмен происходит обычно в течении 30 минут.\n'
                                          'Спасибо за использование нашего обменника BitsKhalifa.')
        bot.send_message(1328178979, f'Сумма обмена: {course}\n'
                                       f'Сумма к получению: {float("{0:.8f}".format(course / (price["bitcoin"]["rub"] * 1.03)))} BTC.\n'
                                       f'На кошелек: {wallet["proverka"]}\n\n'
                                       f'Время заявки: {datetime.datetime.now()}')

        main(message)

    else:
        pass


def qiwiethereum(message):
    button = types.ReplyKeyboardRemove()#Убираем кнопки н аэкране
    price = cg.get_price(ids='ethereum', vs_currencies='rub') #курс
    msg = bot.send_message(message.chat.id, f'1 Ethereum == {price["ethereum"]["rub"] * 1.03} RUB\n'
                                      f'Минимальная сумма обмена составляет 2000 рублей\n'
                                      f'Пожалуйста, введите сумму вашего обмена.', reply_markup=button)

    bot.register_next_step_handler(msg, eth_proverka)#Переход к следущему шагу

def eth_proverka(message): #проверяет введенная сумма больше 5k
    try:
        global course
        course = {}
        proverka = {}
        proverka['qiwiethereum'] = message.text
        course = float(proverka['qiwiethereum'])

        price = cg.get_price(ids='ethereum', vs_currencies='rub')  # курс

        if course >= 2000:
            msg = bot.send_message(message.chat.id, f'Вы получите {float("{0:.8f}".format(course / (price["ethereum"]["rub"] * 1.03)))} ETH на ваш кошелек.\n'
                                              f'Пожалуйста укажите ваш ETH адрес.')
            bot.register_next_step_handler(msg, eth_proverka2)#Переход к следущему шагу
        else:
            bot.send_message(message.chat.id, 'Минимальная сумма обмена составляет 2000 рублей')
            qiwiethereum(message)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректные данные')
        qiwiethereum(message)

def eth_proverka2(message): #проверяет введенный кошелек
    global wallet
    wallet = {}
    wallet["eth_proverka"] = message.text #Здесь мы указываем ваш кошелек
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)#Если это не написать кнопки будут очень большими
    button.add(types.KeyboardButton('Подтверждаю оплату'))

    price = cg.get_price(ids='ethereum', vs_currencies='rub')  # курс
    msg = bot.send_message(message.chat.id, f'Вы обмениваете {course} на {float("{0:.8f}".format(course / (price["ethereum"]["rub"] * 1.03)))} ETH.\n'
                                      f'Ваш кошелек: {wallet["eth_proverka"]}\n\n'
                                      f'Мы ожидаем от вас оплаты на QIWI в размере {course} по реквизитам: +79510006255\n\n'
                                            f'После оплаты нажмите на кнопку подтверждения.', reply_markup=button)

    bot.register_next_step_handler(msg, eth_finish)  # Переход к следущему шагу


def eth_finish(message):
    price = cg.get_price(ids='ethereum', vs_currencies='rub')  # курс

    if message.text == 'Подтверждаю оплату':
        bot.send_message(message.chat.id, f'Ваша заявка была создана {datetime.datetime.now()}.\nОбмен происходит обычно в течении 30 минут.\n'
                                          'Спасибо за использование нашего обменника BitsKhalifa.')
        bot.send_message(1328178979, f'Сумма обмена: {course}\n'
                                       f'Сумма к получению: {float("{0:.8f}".format(course / (price["ethereum"]["rub"] * 1.03)))} ETH.\n'
                                       f'На кошелек: {wallet["eth_proverka"]}\n\n'
                                       f'Время заявки: {datetime.datetime.now()}')

        main(message)

    else:
        pass



bot.polling()#Конец бота