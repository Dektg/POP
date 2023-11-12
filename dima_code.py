import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

bot = telebot.TeleBot('5986032038:AAHuxoPdJQSy09jRGUh7HMOkOhpZrk25hkM')
by_tokens_tinkoff = False
by_tokens_sber = False
by_tokens_btc = False
by_tokens_ltc = False
by_calc = False
by_tokens_eth = False
by_tokens_usdt = False

@bot.message_handler(commands=['start'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)#Если это не написать кнопки будут очень большими
    item1 = types.KeyboardButton('🚀 Взлет')
    item2 = types.KeyboardButton('📝 О проекте')
    item3 = types.KeyboardButton('💻 Инвестиции')
    item4 = types.KeyboardButton('🔧 Инструменты')
    item5 = types.KeyboardButton('💳 Кошелёк')
    item6 = types.KeyboardButton('⚙ Тех. Поддержка')
    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'Вы вернулись', reply_markup=markup)

@bot.message_handler(content_types='text')
def callback(message):
    global by_tokens_tinkoff, by_tokens_sber, by_calc, by_tokens_btc, by_tokens_ltc, by_tokens_eth, by_tokens_usdt
    if message.text == "🚀 Взлет":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Пополнить", callback_data='btn1')
        markup.add(button1)
        #bot.send_message(message.chat.id, "1", reply_markup=markup)
        bot.send_photo(message.chat.id, open('img/in_5000.jpeg', 'rb'), caption="Для того чтобы взлететь, Вам нужно пополнить кошелек на 5000 RUB", reply_markup=markup)
    elif message.text == "📝 О проекте":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                           row_width=2)  # Если это не написать кнопки будут очень большими
        item1 = types.KeyboardButton('🚀 Инвестиции в NiHoo Man')
        item2 = types.KeyboardButton('💫 Инвестиции в NiHoo Temple')
        item3 = types.KeyboardButton('🎁 Система дарения')
        item4 = types.KeyboardButton('🤖 Система клонов')
        item5 = types.KeyboardButton('🤑 Вознаграждение за приглашение')
        item6 = types.KeyboardButton('🤑 Вознаграждение за пополнение реферала')
        item7 = types.KeyboardButton('💰 Что такое арбитраж')
        item8 = types.KeyboardButton('👥 Условия для сетевиков')
        item9 = types.KeyboardButton('⬅️ Вернуться')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)

        bot.send_message(message.chat.id, 'Выберите пункт', reply_markup=markup)
    elif message.text == "💻 Инвестиции":
        markup = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton("➕ Инвестировать", callback_data='invest_btn1')
        button2 = types.InlineKeyboardButton("🪙Реинвестировать", callback_data='invest_btn2')
        button3 = types.InlineKeyboardButton("➖ Вывести дивиденты", callback_data='invest_btn3')
        button4 = types.InlineKeyboardButton("🌟 Вывести инвестиции", callback_data='invest_btn4')
        button5 = types.InlineKeyboardButton("💫 Инвестиции NiHoo Temple", callback_data='invest_btn5')
        markup.add(button1, button2, button3, button4, button5)
        # bot.send_message(message.chat.id, "1", reply_markup=markup)
        bot.send_message(message.chat.id, "▪ Инвестируя в NiHoo Man вы будете получать 0,8% в сутки а так же система умножит ваши вложения, что бы продвинуть живую очередь на получение подарков! ( Благодаря системе клонов )\n"
                                          "\n📠 Процент от инвестиций: 0.8% в сутки\n⏱ Время доходности: 24 часа\n📆 Срок вклада: Бессрочный c возможностью вывода через 100 дней\n\n💳 Ваш вклад: 0.0 RUB\n💵 Пассив: 0.0 руб/день\n"
                                          "💵 На вывод: 0.0₽\nКомиссия на вывод - 5%", reply_markup=markup)
    elif message.text == "🔧 Инструменты":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                           row_width=3)  # Если это не написать кнопки будут очень большими
        item1 = types.KeyboardButton('💰 Калькулятор')
        item2 = types.KeyboardButton('👥 Реферальная ссылка')
        item3 = types.KeyboardButton('📄 Презентация')
        item4 = types.KeyboardButton('⬅️ Вернуться')

        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id, 'Выберите пункт', reply_markup=markup)
    elif message.text == "💳 Кошелёк":
        markup = types.InlineKeyboardMarkup(row_width=1)

        button1 = types.InlineKeyboardButton("🪙Реинвестировать", callback_data='balance_btn1')
        button2 = types.InlineKeyboardButton("➖ Вывести дивиденты", callback_data='balance_btn2')

        markup.add(button1, button2)
        # bot.send_message(message.chat.id, "1", reply_markup=markup)
        bot.send_photo(message.chat.id, open('img/balance.jpeg', 'rb'),
                       caption="🤖 Ваш ID: 1328178979"
                        "\n📆 Профиль создан: 2023-01-05"
                        "\n🚀 Статус: В ожидании  ❌"
                        "\n✨ Оплатил заранее: Нет (0₽) ❌"
                        "\n👥 Лично приглашенные за всё время: 2"
                        "\n🙋‍♂️ Лично приглашенные в этом месяце: 0 (0)"
                        "\n♻️ Повторно зашедшие рефералы: 0"
                        "\nВаш депозит: 💰👇"
                        "\n——————————————————"
                        "\n🏦 Общие накопления в системе дарения - 0₽"
                        "\n🎁 Системы дарения - 0₽"
                        "\n🤑 За приглашения - 0₽"
                        "\n😱 За инвестиции реферала - 0₽"
                        "\n🪙 Вы реинвестировали - 0₽"
                        "\n——————————————————"
                        "\n💵 Общий депозит: 0₽"
                        "\n💵 Пассив: 0 руб/день"
                        "\nЧтобы получать дивиденды, пополните баланс!"
                        "\n💵 На вывод: 0.0₽ "
                        "\n( минимальная сумма вывода 1000₽ )", reply_markup=markup)
    elif message.text == "⚙ Тех. Поддержка":
        bot.send_message(message.chat.id, 'По любым вопросам пишите @smfadmin \nОтветит в течении часа!')

    elif by_tokens_tinkoff == True:
        try:
            summ = int(message.text)
            if summ >= 5000:
                if summ % 5000 == 0:
                    bot.send_message(message.chat.id,
                                     f'☑️Заявка на пополнение №1653 успешно создана\n\n💵 Сумма к оплате: 👉 {summ} RUB 🔥\n\n❗️Внимание🔥 перевод нужно совершить точно с комиссией, иначе деньги не зачисляются❗️\n\n💳 Реквизиты для оплаты:')
                    bot.send_message(message.chat.id, f'2200700745061704')

                    markup = types.InlineKeyboardMarkup()
                    button = types.InlineKeyboardButton("❌ Отменить заявку", callback_data='remove_btn')
                    markup.add(button)
                    bot.send_message(message.chat.id,
                                     f'⏳ Заявка действительна: 60 минут.\n\nОплата производится через любые платежные системы: QIWI, перевод с карты на карту, наличные (терминал), Яндекс.Деньги, и другие платежные системы.\n'
                                     f'\nℹ️ После успешного перевода денег по указанным реквизитам бот автоматически начислит {summ} RUB на ваш баланс. Или же Вы можете отменить данную заявку нажав на кнопку «❌ Отменить заявку»\n'
                                     f'\n⚠️ Необходимо перевести точную сумму с учетом комиссии банка, иначе заявка будет считаться неоплаченной.\n\nЕсли Вы перевели неправильную сумму, сразу сообщите об этом оператору @smfadmin.\n'
                                     f'\n💸 Деньги зачислятся в систему в течении 5 минут, ожидайте 😌',
                                     reply_markup=markup)
                    by_tokens_tinkoff = False
                else:
                    bot.send_message(message.chat.id, "сумма должна быть кратна 5000")
            else:
                bot.send_message(message.chat.id, "сумма должна быть больше 5000")
        except:
            bot.send_message(message.chat.id, "🚫 Это не число, введите корректную сумму!")

    elif by_tokens_sber == True:
        try:
            summ = int(message.text)
            if summ >= 5000:
                if summ % 5000 == 0:
                    bot.send_message(message.chat.id,
                                     f'☑️Заявка на пополнение №1653 успешно создана\n\n💵 Сумма к оплате: 👉 {summ} RUB 🔥\n\n❗️Внимание🔥 перевод нужно совершить точно с комиссией, иначе деньги не зачисляются❗️\n\n💳 Реквизиты для оплаты:')
                    bot.send_message(message.chat.id, f'2202205076831087')

                    markup = types.InlineKeyboardMarkup()
                    button = types.InlineKeyboardButton("❌ Отменить заявку", callback_data='remove_btn')
                    markup.add(button)
                    bot.send_message(message.chat.id,
                                     f'⏳ Заявка действительна: 60 минут.\n\nОплата производится через любые платежные системы: QIWI, перевод с карты на карту, наличные (терминал), Яндекс.Деньги, и другие платежные системы.\n'
                                     f'\nℹ️ После успешного перевода денег по указанным реквизитам бот автоматически начислит {summ} RUB на ваш баланс. Или же Вы можете отменить данную заявку нажав на кнопку «❌ Отменить заявку»\n'
                                     f'\n⚠️ Необходимо перевести точную сумму с учетом комиссии банка, иначе заявка будет считаться неоплаченной.\n\nЕсли Вы перевели неправильную сумму, сразу сообщите об этом оператору @smfadmin.\n'
                                     f'\n💸 Деньги зачислятся в систему в течении 5 минут, ожидайте 😌',
                                     reply_markup=markup)
                    by_tokens_sber = False
                else:
                    bot.send_message(message.chat.id, "сумма должна быть кратна 5000")
            else:
                bot.send_message(message.chat.id, "сумма должна быть больше 5000")
        except:
            bot.send_message(message.chat.id, "🚫 Это не число, введите корректную сумму!")

    elif by_tokens_btc == True:
        try:
            summ = int(message.text)
            if summ >= 5000:
                if summ % 5000 == 0:
                    bot.send_message(message.chat.id, summ)
                    by_tokens_btc = False

                    price = cg.get_price(ids='bitcoin, ethereum', vs_currencies='rub')

                    bot.send_message(message.chat.id,
                                     f'☑️Заявка на пополнение №530 успешно создана\n\nСумма к оплате: {int(summ) / price["bitcoin"]["rub"]} BTC')
                    bot.send_message(message.chat.id, f'3HHfaXYF3CruaRk3oftbpwt4h2wTuTJbxX')

                    markup = types.InlineKeyboardMarkup()
                    button = types.InlineKeyboardButton("❌ Отменить заявку", callback_data='remove_btn')
                    markup.add(button)
                    bot.send_message(message.chat.id,
                                     f'⏳ Заявка №530 и BTC-адрес действительны: 60 минут.\n\nПосле успешной отправки {int(summ) / price["bitcoin"]["rub"]} BTC на указанный BTC-адрес выше, отправьте скриншот об оплате @smfadmin и администратор подтвердит зачисление.\n\nИли же Вы можете отменить данную заявку нажав на кнопку «❌ Отменить заявку»\n\n💸 Криптовалюта зачислится в систему в течении 20 минут, ожидайте 😌',
                                     reply_markup=markup)
                    by_tokens_btc = False

                else:
                    bot.send_message(message.chat.id, "сумма должна быть кратна 5000")


            else:
                bot.send_message(message.chat.id, "сумма должна быть больше 5000")
        except:
            bot.send_message(message.chat.id, "🚫 Это не число, введите корректную сумму!")

    elif by_tokens_ltc == True:
        try:
            summ = int(message.text)
            if summ >= 5000:
                if summ % 5000 == 0:
                    bot.send_message(message.chat.id, summ)
                    by_tokens_ltc = False

                    price = cg.get_price(ids='bitcoin, litecoin', vs_currencies='rub')

                    bot.send_message(message.chat.id,
                                     f'☑️Заявка на пополнение №530 успешно создана\n\nСумма к оплате: {int(summ) / price["litecoin"]["rub"]} LTC')
                    bot.send_message(message.chat.id, f'3HHfaXYF3CruaRk3oftbpwt4h2wTuTJbxX')

                    markup = types.InlineKeyboardMarkup()
                    button = types.InlineKeyboardButton("❌ Отменить заявку", callback_data='remove_btn')
                    markup.add(button)
                    bot.send_message(message.chat.id,
                                     f'⏳ Заявка №530 и LTC-адрес действительны: 60 минут.\n\nПосле успешной отправки {int(summ) / price["litecoin"]["rub"]} LTC на указанный LTC-адрес выше, отправьте скриншот об оплате @smfadmin и администратор подтвердит зачисление.\n\nИли же Вы можете отменить данную заявку нажав на кнопку «❌ Отменить заявку»\n\n💸 Криптовалюта зачислится в систему в течении 20 минут, ожидайте 😌',
                                     reply_markup=markup)
                    by_tokens_ltc = False

                else:
                    bot.send_message(message.chat.id, "сумма должна быть кратна 5000")


            else:
                bot.send_message(message.chat.id, "сумма должна быть больше 5000")
        except:
            bot.send_message(message.chat.id, "🚫 Это не число, введите корректную сумму!")

    elif by_tokens_eth == True:
        try:
            summ = int(message.text)
            if summ >= 5000:
                if summ % 5000 == 0:
                    bot.send_message(message.chat.id, summ)
                    by_tokens_eth = False

                    price = cg.get_price(ids='bitcoin, ethereum', vs_currencies='rub')

                    bot.send_message(message.chat.id,
                                     f'☑️Заявка на пополнение №530 успешно создана\n\nСумма к оплате: {int(summ) / price["ethereum"]["rub"]} ETH')
                    bot.send_message(message.chat.id, f'3HHfaXYF3CruaRk3oftbpwt4h2wTuTJbxX')

                    markup = types.InlineKeyboardMarkup()
                    button = types.InlineKeyboardButton("❌ Отменить заявку", callback_data='remove_btn')
                    markup.add(button)
                    bot.send_message(message.chat.id,
                                     f'⏳ Заявка №530 и ETH-адрес действительны: 60 минут.\n\nПосле успешной отправки {int(summ) / price["ethereum"]["rub"]} ETH на указанный ETH-адрес выше, отправьте скриншот об оплате @smfadmin и администратор подтвердит зачисление.\n\nИли же Вы можете отменить данную заявку нажав на кнопку «❌ Отменить заявку»\n\n💸 Криптовалюта зачислится в систему в течении 20 минут, ожидайте 😌',
                                     reply_markup=markup)
                    by_tokens_eth = False

                else:
                    bot.send_message(message.chat.id, "сумма должна быть кратна 5000")



            else:
                bot.send_message(message.chat.id, "сумма должна быть больше 5000")
        except:
            bot.send_message(message.chat.id, "🚫 Это не число, введите корректную сумму!")

    elif by_tokens_usdt == True:
        try:
            summ = int(message.text)
            if summ >= 5000:
                if summ % 5000 == 0:
                    bot.send_message(message.chat.id, summ)
                    by_tokens_usdt = False

                    price = cg.get_price(ids='bitcoin, tether', vs_currencies='rub')

                    bot.send_message(message.chat.id,
                                     f'☑️Заявка на пополнение №530 успешно создана\n\nСумма к оплате: {int(summ) / price["tether"]["rub"]} USDT')
                    bot.send_message(message.chat.id, f'3HHfaXYF3CruaRk3oftbpwt4h2wTuTJbxX')

                    markup = types.InlineKeyboardMarkup()
                    button = types.InlineKeyboardButton("❌ Отменить заявку", callback_data='remove_btn')
                    markup.add(button)
                    bot.send_message(message.chat.id,
                                     f'⏳ Заявка №530 и USDT-адрес действительны: 60 минут.\n\nПосле успешной отправки {int(summ) / price["tether"]["rub"]} USDT на указанный USDT-адрес выше, отправьте скриншот об оплате @smfadmin и администратор подтвердит зачисление.\n\nИли же Вы можете отменить данную заявку нажав на кнопку «❌ Отменить заявку»\n\n💸 Криптовалюта зачислится в систему в течении 20 минут, ожидайте 😌',
                                     reply_markup=markup)
                    by_tokens_usdt = False

                else:
                    bot.send_message(message.chat.id, "сумма должна быть кратна 5000")



            else:
                bot.send_message(message.chat.id, "сумма должна быть больше 5000")
        except:
            bot.send_message(message.chat.id, "🚫 Это не число, введите корректную сумму!")



    elif by_calc == True:
        try:
            summ = int(message.text)

            markup = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton("Рассчитать снова",
                                                callback_data='calc_btn1')
            markup.add(button)
            bot.send_photo(message.chat.id, open('img/calc.jpeg', 'rb'), caption="💱 В данном разделе Вы сумеете рассчитать Вашу прибыль, от суммы вашей инвестиции в наш проект:\n" +
                             f'\n💵 Ваша инвестиция: {int(summ)} RUB\n' +
                             f'\nПрибыль в сутки: {int(summ) * 0.008} RUB\nПрибыль в месяц: {int(summ) * 0.24} RUB\nПрибыль в год: {int(summ) * 2.88} RUB',
                             reply_markup=markup)
            by_calc = False

        except:
            bot.send_message(message.chat.id, "🚫 Это не число, введите корректную сумму!")



    elif message.text == "💰 Калькулятор":

        #button = types.ReplyKeyboardRemove()  # Убираем кнопки н аэкране
        bot.send_message(message.chat.id, 'Введите сумму, которую хотите рассчитать:')
        by_calc = True

    elif message.text == "👥 Реферальная ссылка":
        bot.send_photo(message.chat.id, open('img/refs.jpeg', 'rb'),
                       caption="🤖 Ваш ID: 1328178979 "

"\n👥 Всего приглашенных рефералов: 0"
"\n🧑‍💼 Всего активированных рефералов: 0"
"\n\nВаша команда:"
"\n🫂 Всего людей в структуре: 2"
"\n👩🏻‍🚀 Всего активных людей в структуре: 0 "
"\n\n✨ Всего людей инвестировали в проект: 613"
"\n\n🎁 Сумма пополнений в проекте: 7.640.000"
"\n🪐 Лучшая достигнутая планета: Юпитер"
"\n\nВаша реферальная ссылка:"
"\nhttps://t.me/space_gift_bot?start=1328178979")
    elif message.text == "📄 Презентация":
        bot.send_document(message.chat.id, open('img/Презентация NiHoo Man.pdf', 'rb'))
    elif message.text == "⬅️ Вернуться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                           row_width=2)  # Если это не написать кнопки будут очень большими
        item1 = types.KeyboardButton('🚀 Взлет')
        item2 = types.KeyboardButton('📝 О проекте')
        item3 = types.KeyboardButton('💻 Инвестиции')
        item4 = types.KeyboardButton('🔧 Инструменты')
        item5 = types.KeyboardButton('💳 Кошелёк')
        item6 = types.KeyboardButton('⚙ Тех. Поддержка')
        markup.add(item1, item2, item3, item4, item5, item6)

        bot.send_message(message.chat.id, 'Вы вернулись', reply_markup=markup)

    elif message.text == '🚀 Инвестиции в NiHoo Man':
        bot.send_message(message.chat.id,
                         "🚀 Инвестиции в NiHoo Man\n\nНаша команда создала новую инвестиционную платформу,\nкоторая позволяет получать 18% прибыли в месяц, благодаря алгоритмам системы дарения и новому перспективному направлению крипто-арбитраж\n"
                         "\n💰Что такое арбитраж\n\nКриптовалютный арбитраж - это покупка криптовалюты на одной бирже и продажа\nна другой, с целью получения прибыли на разнице курсов.\n\nПростыми словами:"
                         "\nмы купили на одной бирже актив за 1000$, продали на другой бирже за 1050$\n= заработали чистыми 50$. Наша команда забирает на себя всю рутину,\nВам остается только получать дивиденды с нашей платформы!\n"
                         "\nДанное направление очень перспективное благодаря возможности гонять большие обьемы в крипте и зарабатывать на разнице курсов. Также на данный момент представлена минимальная конкуренция на рынке крипто арбитража из за не знания как на этом рынке зарабатывать с минимальными рисками.💱\n"
                         "\nИнвистиции бесрочные с заморозкой на 100 дней\nВы можете пополнять депозит 2-мя способами\n1. Переводом на карту\n2. Пополнение через криптовалюту\n\nNiHoo Man это уникальный инструмент, ведь сумму Вашего депозита, можно увеличить 4-мя способами!\n"
                         "\n1.  Инвестиции в NiHoo Man 18% в мес.\n2.  Вознаграждение за приглашение + 5000 ₽\n3.  Вознаграждение за пополнение реферала 10%\n4.  Благодаря Новой системе дарения\n\nДивиденды вы можете выводить в любое удобное для вас время ( минимальная сумма вывода 1000 р)\n"
                         "\nВремя нахождения в проекте позволяет не только отбить свои вложения, но и приумножить свой пассивный доход.<a href='https://telegra.ph/file/ae07cb02bfa72b30aabd6.jpg'>&#8203;</a>", parse_mode='html')
    elif message.text == '💫 Инвестиции в NiHoo Temple':
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("💫 Перейти на сайт Nihoo.ru", url="https://nihoo.ru", callback_data='site')
        markup.add(button)
        bot.send_message(message.chat.id,
                         "💫 Инвестиции в Nihoo Temple\n\nЭто проект исключительно для крупных инвесторов, которые понимают что такое-крипто-арбитраж и преспетивы этого направления. \n"
                         "\nДепозит будет передаваться в управление специалистам, которые работают с большими депозитами за счет этого можно будет получать повышенный процент доходности \n"
                         "\nв Space money инвесторы получают 2% в сутки, так же с бесрочными инвистициями 100 дней \n\nИнвестировать можете через наш сайт Nihoo.ru пополнение депозита только в криптовалюте  (USDT). \n"
                         "\nУ вас есть выбор, инвестировать в Nihoo Man и увеличить свой депозит с помощью других участников, или инвестировать крупную сумму \n( от 2 млн. руб ) на сайте NiHoo Temple и получать 2 % также с крипто арбитража.\n"
                         "\nВсе в ваших руках, действуйте!.<a href='https://telegra.ph/file/50778f3f001acbae49654.jpg'>&#8203;</a>",
                         reply_markup=markup, parse_mode='html')
    elif message.text == '🎁 Система дарения':
        bot.send_message(message.chat.id,
                         "🎁 Система дарения\n\nПредставьте общую очередь, где каждый участник получает дивиденды и для активации в системе новый пользователь должен сделать подарок ранее присоединившемуся участнику. \n"
                         "\nЭто первый инвестиционный проект, где участники увеличивают депозиты друг друга за счет взаимопомощи! Чем раньше вы присоединитесь к системе дарения, тем больше увеличится ваш депозит! \n"
                         "\nБонус! За ваши подарки другим участникам, NiHoo Man  поощряет и начисляет на ваш депозит, сумму кратную подаркам на всех планетах!\n"
                         "\nДля активации в системе дарения и возможность получать подарки, необходимо пополнить кошелек \nна 5000₽ и подарить их участнику ранее зашедшему в систему ( участнику на планете Меркурий ) \nПосле активации вы получаете бонус от NiHoo Man. Система начислит на ваш депозит 5000₽. \n"
                         "\nПока вы находитесь в очереди, вам будут начисляться дивиденды в размере 0,6% в сутки. После того как очередь дойдет до вас, новые участники начнут дарить подарки вам! Таким образом, время нахождения в проекте позволяет не только отбить свои вложения, но и приумножить свой пассивный доход.\n"
                         "\nЧасть денег подаренные от участников системы дарения на ваш депозит,  можно выводить \nна каждой планете любым удобным способом, но с вычетом 20% комиссии!\n\n🚀 Планета Меркурий \n- Всего подарков - 25.000₽\n- На вывод - 10.000₽\n- Подарок от NiHoo Man - 15.000₽\n"
                         "\n🚀 Планета Венера \n- Всего подарков - 75.000₽\n- На вывод - 25.000₽\n- Подарок от NiHoo Man - 50.000₽\n\n🚀 Планета Земля \n- Всего подарков - 250.000₽\n- На вывод - 50.000₽\n- Подарок от Space gift - 200.000₽\n\n🚀 Планета Марс \n- Всего подарков - 1.000.000₽\n- На вывод - 200.000₽\n- Подарок от NiHoo Man - 800.000₽\n"
                         "\n🚀 Планета Юпитер \n- Общий депозит - 4.000.000₽\n- На вывод - 1.000.000₽\n- Подарок от NiHoo Man - 3.000.000₽\n\n🚀 Планета Сатурн \n- Общий депозит - 15.000.000₽\n- На вывод - 3.000.000₽\n- Остаток депозита \nNiHoo Man - 12.000.000₽\n"
                         "\n💸 Всего будет выведено в карман - \n4.285.000₽ - 20% = 3.428.000₽\n\nОстаток депозита 12.000.000₽ под 18% это - 72.000₽ в день!\n"
                         "\nСистема дарения NiHoo Man сделана таким образом, что в конце месяца система обнуляется и игра стартует заново. Это сделано для того чтобы юбка не расширялась и участники могли перезайти в очередь одни из первых, где их продвинут новые  и старые участники. "
                         "Но стоит понимать что система дарения в данном проекте вторична и вы можете увеличивать депозит также другими ранее перечисленными способами, чтобы получать дивиденды с крипто-арбитража.\n\nЕсли после обнуления системы дарения участник не активировался повторно, то ему приостанавливают выплаты дивидендов до момента повторной активации!<a href='https://i.ibb.co/HxQPmC9/gift.png'>&#8203;</a>",
                         parse_mode='html')
    elif message.text == '🤖 Система клонов':
        bot.send_message(message.chat.id,
                         "Система клонов\n\nКто такой клон и его роль в системе?\nB NiHoo Man пополнение депозита всегда кратно 5000 (10 000 руб., 120 000 руб., 325 000 руб.,)\n"
                         "Берем участника, который решил пополнить депозит на 305 000 руб. и уже сегодня начнет получать по 0.6% девидендов в день. Сумма депозита дублируется и создаются клоны\n"
                         "\nКак это проиходит?\n305 000 руб. мы делим на 5 000 руб. (кратной сумме входа) и получаем 61 клон в общую очередь для быстрого продвижения живых участников.\n"
                         "\nЦель клона?\nЦелью клона является продвинуть живых участников для получения подарков, но самиклоны на эти уровни не попадают.\nТаким образом очередь двигается в разы быстрее!<a href='https://telegra.ph/file/f09ff0b1d66548ebd96f2.jpg'>&#8203;</a>",
                         parse_mode='html')
    elif message.text == '🤑 Вознаграждение за приглашение':
        bot.send_message(message.chat.id,
                         "🤑 Вознаграждения за приглашения\n\nЗа каждого приглашенного участника, который перешел по вашей\nреферальной ссылке и активировался в системе,  NiHoo Man начисляет\n+ 5000 р на Ваш депозит. \n"
                         "\nПредставим, что вы за 2 месяца пригласили по своей реф. ссылке 80 новых участников, активированных в системе. NiHoo Man начислит к вашему депозиту +400 тыс. руб. под 18% дивидендов прибыли в месяц ( это 72000 руб./мес. )  \n"
                         "\nТаким образом вы можете не рисковать деньгами\nи увеличить депозит исключительно за счет приглашений!\n\nДепозит от вознаграждения нельзя вывести, он распространяется\nисключительно на дивиденды от проекта!"
                         "<a href='https://telegra.ph/file/e63d7c9b46914214f9b60.jpg'>&#8203;</a>",
                         parse_mode='html')
    elif message.text == '🤑 Вознаграждение за пополнение реферала':
        bot.send_message(message.chat.id,
                         "🤑 Вознаграждение за пополнение рефералом\n\nПроект NiHoo Man дарит 10% на ваш депозит от суммы пополнения \nвашим рефералом своего кошелька. \n"
                         "\nПредставим, что вы пригласили 5 участников в проект NiHoo Man. 2 участника\nпринимают решение пополнить депозит на 100 тыс. руб. и на 1 млн. руб. "
                         "\nNiHoo Man фиксирует пополнение кошельков вашими рефералами  \nи пополняет ваш депозит на + 110 тыс. руб. \n\nПриглашая больше людей, вы увеличиваете количество\nинструментов пополнения вашего депозита!\n"
                         "\nДепозит от вознаграждения нельзя вывести, он распространяется\nисключительно на дивиденды от проекта!<a href='https://telegra.ph/file/0508bad3b7be0bf20643c.jpg'>&#8203;</a>",
                         parse_mode='html')
    elif message.text == '💰 Что такое арбитраж':
        bot.send_message(message.chat.id,
                         "Что такое арбитраж\nКриптовалютный арбитраж - это покупка криптовалюты на одной бирже и продажа на другой, с целью получения прибыли на разнице курсов.\n"
                         "\nПростыми словами:\nмы купили на одной бирже актив за 1000$, продали на другой бирже за 1050$ == заработали чистыми 50$. Наша команда забирает на себя всю рутину,\nВам остается только получать дивиденды с нашей платформы!\n"
                         "\nДанное направление очень перспективное благодаря возможности гонять большие обьемы в крипте и зарабатывать на разнице курсов. Также на данный момент представлена минимальная конкуренция на рынке крипто арбитража "
                         "из за не знания как на этом рынке зарабатывать с минимальными рисками.<a href='https://telegra.ph/file/beaf77332138c0135f012.jpg'>&#8203;</a>",
                         parse_mode='html')
    elif message.text == '👥 Условия для сетевиков':
        bot.send_message(message.chat.id,
                         "👥 Условия для сетивиков\n\nДля того чтобы не стоять на старте в общей очереди, участник может включать сверх-звуковую скорость\n"
                         "и перелетать от планеты к планете. \n\nЕсли участник в очереди на планете Меркурий пригласил 5 человек, которые\n"
                         "пригласили еще по 5 человек - этот участник автоматически перемещается в очередь на планету Венера,\nтем самым обгоняя сотни, а то и тысячи людей!  \n"
                         "\nАвтоматический перелет в очередь на планету Венера \n- 2 лично приглашенных, приглашают 5 новых участников\n"
                         "\nАвтоматический перелет в очередь на планету Земля \n- 4 лично приглашенных, приглашают 5 новых участников\n"
                         "\nАвтоматический перелет в очередь на планету Марс \n- 8 лично приглашенных, приглашают 5 новых участников\n"
                         "\nАвтоматический перелет в очередь на планету Юпитер \n- 16 лично приглашенных, приглашают 5 новых участников.<a href='https://telegra.ph/file/634731a5a105b63710caa.jpg'>&#8203;</a>",
                         parse_mode='html')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global by_tokens_tinkoff, by_tokens_sber, by_calc, by_tokens_btc, by_tokens_ltc, by_tokens_eth, by_tokens_usdt
    if (call.data == "btn1" or call.data == "invest_btn1"):
        mk_inp = types.InlineKeyboardMarkup(row_width=1)
        mk_but1 = types.InlineKeyboardButton("▪ Банковская карта RUB", callback_data='mkbtn1')
        mk_but2 = types.InlineKeyboardButton("▪ Криптовалюта", callback_data='mkbtn2')
        mk_inp.add(mk_but1, mk_but2)
        bot.delete_message(call.from_user.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "📤 Выберите платежную систему на которую хотите совершить перевод для пополнение средств в бота \n▪ Моментальные зачисление, а также автоматическая конверсия.", reply_markup=mk_inp)
        #bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=foto2, caption="noitpac"),chat_id=call.message.chat.id, message_id=call.message.message_id)
    if (call.data == "mkbtn1"):
        mk_mkbtn1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Tinkoff", callback_data='tinkoff')
        btn2 = types.InlineKeyboardButton("Sberbank", callback_data='sberbank')
        mk_mkbtn1.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="🏦 Выберите банк через который будет удобно произвести оплат. Если вашего банка нет в списке, вы можете совершать межбанковский перевод, а комиссию мы возьмём на себя!", reply_markup=mk_mkbtn1)
    if (call.data == "mkbtn2"):
        mk_mkbtn1 = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("BTC", callback_data='btc_btn1')
        btn2 = types.InlineKeyboardButton("LTC", callback_data='ltc_btn2')
        btn3 = types.InlineKeyboardButton("ETH", callback_data='eth_btn3')
        btn4 = types.InlineKeyboardButton("USDT", callback_data='usdt_btn4')
        mk_mkbtn1.add(btn, btn2, btn3, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="🏦 Выберите криптовалюту которой будет удобно сделать пополнение",
                              reply_markup=mk_mkbtn1)
    if call.data == "tinkoff":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите сумму на которую хотите пополнить баланс. Минимальная сумма: 5000.0 RUB")
        by_tokens_tinkoff = True


    if call.data == "sberbank":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите сумму на которую хотите пополнить баланс. Минимальная сумма: 5000.0 RUB")
        by_tokens_sber = True

    if call.data == "btc_btn1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите сумму на которую хотите пополнить баланс. Минимальная сумма: 5000.0 RUB")
        by_tokens_btc = True


    if call.data == "ltc_btn2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите сумму на которую хотите пополнить баланс. Минимальная сумма: 5000.0 RUB")
        by_tokens_ltc = True

    if call.data == "eth_btn3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите сумму на которую хотите пополнить баланс. Минимальная сумма: 5000.0 RUB")
        by_tokens_eth = True

    if call.data == "usdt_btn4":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите сумму на которую хотите пополнить баланс. Минимальная сумма: 5000.0 RUB")
        by_tokens_usdt = True

    if (call.data == "invest_btn2" or call.data == "balance_btn1"):
        bot.answer_callback_query(callback_query_id=call.id, text="🚫Реинвестирование временно недоступно.", show_alert=True)

    if (call.data == "invest_btn3" or call.data == "balance_btn2"):
        bot.answer_callback_query(callback_query_id=call.id, text="🚫У вас на балансе не достаточно средств для вывода, минимальная сумма: 1000 RUB", show_alert=True)

    if (call.data == "invest_btn4"):
        bot.answer_callback_query(callback_query_id=call.id, text="🚫Вывод через бота временно ограничен.", show_alert=True)

    if (call.data == "invest_btn5"):
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("💫 Перейти на сайт Nihoo.ru", url="https://nihoo.ru",callback_data='site')
        markup.add(button)
        bot.delete_message(call.from_user.id, call.message.message_id)
        bot.send_message(call.message.chat.id,
                         "💫 Инвестиции в Nihoo Temple\n\nЭто проект исключительно для крупных инвесторов, которые понимают что такое-крипто-арбитраж и преспетивы этого направления. \n"
                         "\nДепозит будет передаваться в управление специалистам, которые работают с большими депозитами за счет этого можно будет получать повышенный процент доходности \n"
                         "\nв Space money инвесторы получают 2% в сутки, так же с бесрочными инвистициями 100 дней \n\nИнвестировать можете через наш сайт Nihoo.ru пополнение депозита только в криптовалюте  (USDT). \n"
                         "\nУ вас есть выбор, инвестировать в Nihoo Man и увеличить свой депозит с помощью других участников, или инвестировать крупную сумму \n( от 2 млн. руб ) на сайте NiHoo Temple и получать 2 % также с крипто арбитража.\n"
                         "\nВсе в ваших руках, действуйте!.<a href='https://telegra.ph/file/50778f3f001acbae49654.jpg'>&#8203;</a>",reply_markup=markup, parse_mode='html')

    if (call.data == "calc_btn1"):
        bot.send_message(call.message.chat.id, 'Введите сумму, которую хотите рассчитать:')
        by_calc = True

    if (call.data == "remove_btn"):
        bot.delete_message(call.from_user.id, call.message.message_id)
        bot.send_message(call.message.chat.id,'Заявка на пополнение была успешно отменена.')
        by_tokens_btc = False



bot.infinity_polling()