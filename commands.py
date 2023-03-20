from telebot import TeleBot, types
import datetime
from schedules import *


def hello_start(start, bot):
    bot.reply_to(start,
                 "Привіт! Я - ФКІТ помічник Адольф :)\nЯ вмію показувати розклад групам які є в моїй базі.\nПропоную тобі написати /commands щоб дізнатися мій функціонал)")


def commands_info(commands, bot):
    bot.reply_to(commands,
                 "/kn_11, /kn_12, /knai_11 - Розклад для певної групи.\nНаприклад: /knai_11 - видає розклад на поточний день. А якщо написати /knai_11 17.03, то видасть розклад на задану дату.\n/lupdates - видає останнє обновлення бота")


def lupdates_info(lupdates, bot):
    bot.reply_to(lupdates,
                 "Обновлення 17.03\n- Доданий розклад для КНШІ-11, КН-11, КН-12\n- Додані команди /knai_11 | /kn_11 | /kn_12\n- Додана команда /commands де описують дію функції")


def updates_info(updates, bot):
    bot.reply_to(updates,
                 "Обновлення 16.03\n- Доданий розклад для КНШІ-11 та частково КН-11\n- Додані команди /kndai_11 та /kn_11")


def is_week_even(date_string):
    date = datetime.datetime.strptime(date_string, '%d.%m.%Y')
    week_number = date.isocalendar()[1]
    if week_number % 2 == 0:
        return 2
    else:
        return


def choose_group(message, bot):
    markup = types.InlineKeyboardMarkup()
    kn_11 = types.InlineKeyboardButton('kn_11', callback_data="kn_11")
    kn_12 = types.InlineKeyboardButton('kn_12', callback_data="kn_12")
    knai_11 = types.InlineKeyboardButton('knai_11', callback_data="knai_11")
    markup.row(kn_11, kn_12,knai_11)
    msg = bot.reply_to(message, "Вибери групу", reply_markup=markup)


def get_day_of_week(date, message, bot, group):
    try:
        # конвертуємо текст повідомлення в об'єкт дати
        date_obj = datetime.datetime.strptime(f"{date}.2023", '%d.%m.%Y')
        # отримуємо день тижня з об'єкту дати та відправляємо його користувачу
        day_of_week = date_obj.strftime('%A')
        if day_of_week == 'Saturday' or day_of_week == 'Sunday':
            bot.send_video(
                message.chat.id,
                'https://media2.giphy.com/media/yzvVXSvrg7JxC/giphy.gif?cid=ecf05e478hwvp20k93i9oir96xgsjxqti3dzqqwlryhv40by&rid=giphy.gif&ct=g',
                None, "Сьогодні вихідний, можеш балдіти :)")
            return
        if is_week_even(f"{date}.2023") == 2:
            # bot.reply_to(message, group[day_of_week]["pair"])
            bot.send_video(
                message.chat.id,
                'https://i0.wp.com/www.printmag.com/wp-content/uploads/2021/02/4cbe8d_f1ed2800a49649848102c68fc5a66e53mv2.gif?fit=476%2C280&ssl=1',
                None, group[day_of_week]["pair"])
        else:
            bot.send_video(
                message.chat.id,
                'https://i0.wp.com/www.printmag.com/wp-content/uploads/2021/02/4cbe8d_f1ed2800a49649848102c68fc5a66e53mv2.gif?fit=476%2C280&ssl=1',
                None, group[day_of_week]["not_even"])
            # bot.reply_to(message, group[day_of_week]["not_even"])
    except ValueError:
        bot.send_video(
            message.chat.id,
            'https://media0.giphy.com/media/j9XoexYMmd7LdntEK4/giphy.gif?cid=ecf05e47oarpmxga8qsihrkw1v3qqbuzzmva0qq23x8esoku&rid=giphy.gif&ct=g',
            None, "Неправильний формат дати! Введіть дату у форматі 'дд.мм'")
        # bot.reply_to(message, "Неправильний формат дати! Введіть дату у форматі 'дд.мм'")
