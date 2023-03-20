import telebot
import datetime
from config import token
from commands import *
from schedules import *
# створюємо екземпляр бота з токеном, який отримано від BotFather
bot = telebot.TeleBot(token['TOKEN'])
#Перевіряємо чи парний тиждень
@bot.message_handler(commands=['updates'])
def updates(updates):
    updates_info(updates, bot)
@bot.message_handler(commands=['lupdates'])
def lupdates(lupdates):
    lupdates_info(lupdates, bot)
@bot.message_handler(commands=['knai_11'])
def knAi_11(message):
    try:
        date = message.text.split(" ")
        get_day_of_week(date[1], message, bot, knai_11)
    except:
        today = datetime.datetime.today()
        get_day_of_week(today.strftime("%d.%m"), message, bot, knai_11)
@bot.message_handler(commands=['kn_11'])
def Kn_11(message):
    try:
        date = message.text.split(" ")
        get_day_of_week(date[1], message, bot, kn_11)
    except:
        today = datetime.datetime.today()
        get_day_of_week(today.strftime("%d.%m"), message, bot, kn_11)
@bot.message_handler(commands=['kn_12'])
def Kn_12(message):
    try:
        date = message.text.split(" ")
        get_day_of_week(date[1], message, bot, kn_12)
    except:
        today = datetime.datetime.today()
        get_day_of_week(today.strftime("%d.%m"), message, bot, kn_12)
@bot.message_handler(commands=['commands'])
def commands(commands):
    commands_info(commands, bot)
@bot.message_handler(commands=['start'])
def start(start):
    hello_start(start, bot)

# запускаємо бота
print("Bot was started")
bot.polling()