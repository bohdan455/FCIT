import telebot
import datetime
from config import token
from commands import *
from schedules import *

# створюємо екземпляр бота з токеном, який отримано від BotFather
bot = telebot.TeleBot(token['TOKEN'])


# Перевіряємо чи парний тиждень
@bot.message_handler(commands=['updates'])
def updates(updates):
    updates_info(updates, bot)


@bot.message_handler(commands=['lupdates'])
def lupdates(lupdates):
    lupdates_info(lupdates, bot)


@bot.message_handler(commands=['knai_11'])
def knAi_11(message):
    today = datetime.datetime.today()
    try:
        date = message.text.split(" ")
        #ЦЕ ЗАТИЧКА,ПОТІМ ТРЕБА БУДЕ ЦЕ ЗРОБИТИ НОРМАЛЬНО
        if date[1] == "групу":
            get_day_of_week(today.strftime("%d.%m"), message, bot, knai_11)
            return
        get_day_of_week(date[1], message, bot, knai_11)
    except:

        get_day_of_week(today.strftime("%d.%m"), message, bot, knai_11)


@bot.message_handler(commands=['kn_11'])
def Kn_11(message):
    today = datetime.datetime.today()
    try:
        date = message.text.split(" ")
        #ЦЕ ЗАТИЧКА,ПОТІМ ТРЕБА БУДЕ ЦЕ ЗРОБИТИ НОРМАЛЬНО
        if date[1] == "групу":
            get_day_of_week(today.strftime("%d.%m"), message, bot, kn_11)
            return
        date = message.text.split(" ")
        get_day_of_week(date[1], message, bot, kn_11)
    except:
        today = datetime.datetime.today()
        get_day_of_week(today.strftime("%d.%m"), message, bot, kn_11)


@bot.message_handler(commands=['kn_12'])
def Kn_12(message):
    today = datetime.datetime.today()
    try:
        date = message.text.split(" ")
        #ЦЕ ЗАТИЧКА,ПОТІМ ТРЕБА БУДЕ ЦЕ ЗРОБИТИ НОРМАЛЬНО
        if date[1] == "групу":
            get_day_of_week(today.strftime("%d.%m"), message, bot, kn_12)
            return
        date = message.text.split(" ")
        get_day_of_week(date[1], message, bot, kn_12)
    except:
        today = datetime.datetime.today()
        get_day_of_week(today.strftime("%d.%m"), message, bot, kn_12)


@bot.message_handler(commands=['get'])
def get(message):
    choose_group(message, bot)


@bot.message_handler(commands=['commands'])
def commands(commands):
    commands_info(commands, bot)


@bot.message_handler(commands=['start'])
def start(start):
    hello_start(start, bot)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "kn_11":
        Kn_11(call.message)
    elif call.data == "kn_12":
        Kn_12(call.message)
    elif call.data == "knai_11":
        knAi_11(call.message)


# запускаємо бота
print("Bot was started")
bot.polling()
