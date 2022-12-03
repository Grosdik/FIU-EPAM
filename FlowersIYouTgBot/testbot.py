import requests
import json
import telebot
from telebot import types

bot = telebot.TeleBot('5178013358:AAGUS8ME38WydyyWVMqnJylZczwJBSimiFQ')

# link = 'http://localhost:53116/Orders/GetOrderInfo'
# response = requests.get(link).text
#
# data =  json.loads(response)
#
# count_msv = len(data['products'])
#
# address = data['address']
# result = 'Адрес: ' + address

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    takerole = types.KeyboardButton("Выбрать роль")
    markup.add(takerole)
    bot.send_message(message.chat.id, text="Здраствуйте, {0.first_name}! я бот, отправляющий заказы".format(message.from_user),
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Выбрать роль"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        сourier = types.KeyboardButton("Курьер")
        florist = types.KeyboardButton("Флорист")
        markup.add(сourier, florist)
        bot.send_message(message.chat.id, "Выберите нужную роль", reply_markup=markup)

    elif (message.text == "Курьер"):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        startwork = types.KeyboardButton(text="Начать работу", )
        keyboard.add(startwork)
        bot.send_message(message.chat.id, "Роль успешно выбрана", reply_markup=keyboard)

    elif (message.text == "Начать работу"):
        link = 'http://localhost:53116/Orders/GetOrderInfo'
        response = requests.get(link).text

        data = json.loads(response)

        count_msv = len(data['products'])

        address = data['address']
        result = 'Адрес: ' + address

        url = 'http://localhost:53116/Orders/AcceptOrder/' + str(data['id'])

        response = requests.put(url, json={'IsAccepted': True})

        for x in range(0, count_msv):
            prod = data['products'][x]['name']
            result += '\nПозиция для доставки №' + str(x + 1) + ': ' + prod

        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        ordercomplite = types.KeyboardButton(text="Заказ доставлен", )
        keyboard.add(ordercomplite)
        bot.send_message(message.chat.id, result, reply_markup=keyboard)

    elif(message.text == "Заказ доставлен"):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        endwork = types.KeyboardButton(text="Завершить работу")
        keyboard.add(endwork)
        bot.send_message(message.chat.id, "Ожидайте заказы", reply_markup=keyboard)

        link = 'http://localhost:53116/Orders/GetOrderInfo'
        response = requests.get(link).text
        data = json.loads(response)

        url = 'http://localhost:53116/Orders/AcceptOrder/8'
              # + str(data['id'])
        response = requests.put(url, json={
            'IsAccepted': True
        })

        while (True):
            link = 'http://localhost:53116/Orders/GetOrderInfo'
            responseL = requests.get(link).text
            if (responseL != 'null'):
                link = 'http://localhost:53116/Orders/GetUnacceptedOrders'
                responseC = requests.get(link).text

                countOrders = int(responseC);

                PauseTime = 30

                if (countOrders == 0):
                    PauseTime = 30
                elif (countOrders > 0 and countOrders < 5):
                    PauseTime = 15
                else:
                    PauseTime = 5

                data = json.loads(responseL)

                count_msv = len(data['products'])

                address = data['address']
                result = 'Адрес: ' + address

                for x in range(0, count_msv):
                    prod = data['products'][x]['name']
                    result += '\nПозиция для доставки №' + str(x + 1) + ': ' + prod

                print(result)

    elif(message.text == "Завершить работу"):
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        strtwrk = types.KeyboardButton("Начать работу")
        markup1.add(strtwrk)
        bot.send_message(message.chat.id, text="Вы закончили свою работу!", reply_markup=markup1)

    elif (message.text == "Флорист"):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        endwork = types.KeyboardButton(text="Начать работу", )
        keyboard.add(endwork)
        bot.send_message(message.chat.id, "Роль успешно выбрана", reply_markup=keyboard)


bot.polling(none_stop=True)