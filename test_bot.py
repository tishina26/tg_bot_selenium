#!/usr/bin/python

import telebot;
bot = telebot.TeleBot('5129230592:AAE0Jw1ikNmgTSBgQ4svS5bWCBrxFsy_o4k')

KEYS_FROM_BOT = [['ADMINsimka9803', 1491141823], ['0', 0]]
finish = 0
# get messages

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    t = message.text
    p = t.split()
    try:
        p[1] = int(p[1])
    except:
        pass
    global finish
    if p in KEYS_FROM_BOT:
        bot.send_message(message.from_user.id, "Hello, can I help you?")

        if p == KEYS_FROM_BOT[0]:
            bot.send_message(message.from_user.id, "prove you are admin")
            if message.from_user.id == KEYS_FROM_BOT[0][1]:
                bot.send_message(message.from_user.id, "all right, tell bot or добавить_юзера")
                bot.register_next_step_handler(message, admin)
            else:
                bot.send_message(message.from_user.id, "WARNING")
                bot.send_message(1491141823, "!!! SB TRIED YOUR AKK !!!")
        else:
            bot.send_message(message.from_user.id, "start creating bot, tell me your log and pas")
            bot.send_message(1491141823, "кто-то твоего бота юзает))")
            bot.register_next_step_handler(message, start_bot)
    elif t == 'стоп':
        bot.send_message(message.from_user.id, "will stop soon")

        finish = 1
    elif t == 'сломай':
        bot.send_message(message.from_user.id, "broken ahah")

        exit(0)
    else:
        bot.send_message(message.from_user.id, "Send code, please [пароль, id]")

def admin(message):
    t = message.text
    t = t.split()
    if t[0] == 'бот':
        bot.send_message(message.from_user.id, "логин пароль?")

        bot.register_next_step_handler(message, start_bot)
    elif t[0] == 'добавить_юзера':
        try:
            KEYS_FROM_BOT.append([t[1], int(t[2])])
            bot.send_message(message.from_user.id, KEYS_FROM_BOT)
        except:
            bot.send_message(message.from_user.id, "again, please")
    elif t[0] == 'назад':
        bot.register_next_step_handler(message, get_text_messages)
    else:
        bot.send_message(message.from_user.id, "again, please")
        bot.register_next_step_handler(message, admin)

login = 'q'
password = 'q'

def start_bot(message):
    global finish
    finish = 0
    t = message.text
    t = t.split()
    flag_l = 0
    flag_p = 0
    global login
    global password
    if t[0] == 'л':
        try:
            login = t[1]
            bot.send_message(message.from_user.id, login)

            flag_l = 1
        except:
            bot.send_message(message.from_user.id, "again, please")
            bot.register_next_step_handler(message, start_bot)
        try:
            if t[2] == 'п':
                try:
                    password = t[3]
                    bot.send_message(message.from_user.id, t[3])

                    flag_p = 1
                except:
                    bot.send_message(message.from_user.id, "again, please")
                    bot.register_next_step_handler(message, start_bot)
            else:
                bot.send_message(message.from_user.id, "again, please")
                bot.register_next_step_handler(message, start_bot)
        except:
            bot.send_message(message.from_user.id, "again, please")
            bot.register_next_step_handler(message, start_bot)
    else:
        bot.send_message(message.from_user.id, "login, password")
        bot.register_next_step_handler(message, start_bot)

    if flag_l == 0:
        bot.send_message(message.from_user.id, "login, please")
        bot.register_next_step_handler(message, start_bot)
    if flag_p == 0:
        bot.send_message(message.from_user.id, "password, please")
        bot.register_next_step_handler(message, start_bot)
    if flag_p == 1 and flag_l == 1:
        bot.send_message(message.from_user.id, "на сколько дней в кск писать?")
        bot.register_next_step_handler(message, kck_bot)

days_kck = 10

def kck_bot(message):
    t = message.text
    global days_kck
    try:
        days_kck = int(t)
        bot.send_message(message.from_user.id, "start?")
        bot.register_next_step_handler(message, YES_bot)
    except:
        bot.send_message(message.from_user.id, "только цифры")
        bot.register_next_step_handler(message, kck_bot)


# import start1.py
import time
from new_fun import main
#from version2 import main

from selenium import webdriver

cnt_all_horses = -1

def YES_bot(message):
    t = message.text
    if t == 'да':
        global login, password, days_kck, finish
        attempt = 0
        how_much_less_minute = 0
        begin_bot = time.time()
        end_bot = time.time()
        #driver = webdriver.Chrome('/home/uliana/Programm/lowadi/chromedriver')
        #main(driver, login, password, days_kck)
        #driver.quit()
        while (1):
            try:
                attempt = attempt + 1
                begin_part_bot = time.time()

                driver = webdriver.Chrome('/home/uliana/Programm/lowadi/chromedriver')
                main(driver, login, password, days_kck, message.from_user.id)
                driver.quit()

                end_bot = time.time()
                print("try attempt = ", attempt, "spent on it: ", int(end_bot) - int(begin_part_bot))
                #bot.send_message(1491141823, "try attempt = ", attempt, "spent on it: ", int(end_bot) - int(begin_part_bot))

                if int(end_bot) - int(begin_part_bot) < 120:
                    how_much_less_minute = how_much_less_minute + 1
                    if how_much_less_minute > 3:
                        print("TOO MUCH BAD ATTEMPTS, TRY AGAIN")
                        #bot.send_message(1491141823, "TOO MUCH BAD ATTEMPTS, TRY AGAIN")

                        return
            except:
                driver.quit()

                end_bot = time.time()
                print("except attempt = ", attempt, "spent on it: ", int(end_bot) - int(begin_part_bot))
                #bot.send_message(1491141823, "except attempt = ", attempt, "spent on it: ", int(end_bot) - int(begin_part_bot))

                if int(end_bot) - int(begin_part_bot) < 120:
                    how_much_less_minute = how_much_less_minute + 1
                    if how_much_less_minute >= 3:
                        print("TOO MUCH BAD ATTEMPTS, TRY AGAIN")
                        print(int(end_bot) - int(begin_bot), "seconds")
                        return
                pass

    else:
        bot.send_message(message.from_user.id, "только да/нет")
        bot.register_next_step_handler(message, YES_bot)

if finish == 0:
    bot.polling(none_stop=True, interval=0)
