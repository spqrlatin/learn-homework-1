"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from get_planet import *
import os
load_dotenv()

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


#PROXY = {
#    'proxy_url': 'socks5://t1.learn.python.ru:1080',
#    'urllib3_proxy_kwargs': {
#        'username': 'learn',
#        'password': 'python'
#    }
#}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)


def get_planet(update, context):
    user_text: str = update.message.text
    message_list = user_text.split(" ")
    print(message_list)
    if len(message_list) != 2:
        update.message.reply_text(r"Функция вызвана неправильно, формата вызова /planet PlanetName")
    else:
        planet_name = message_list[1]
        update.message.reply_text(f"Делаю поиск созвездия для планеты {planet_name}")
        update.message.reply_text(get_consilation(planet_name))

if __name__ == '__main__':
    print(get_consilation("Mars"))



def main():
    mybot = Updater(os.getenv("BOT_TOKEN"), use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", get_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
