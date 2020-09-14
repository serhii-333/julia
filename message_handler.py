import time
from random import randrange

import schedule
import telebot

bot = telebot.TeleBot('1377602523:AAHrDShJkWaccxSVu5iXji2Pc3xuEKSZuf0')


class Love:
    def __init__(self):
        self.__loveWords = ['Kitty <3',
                            'I love you <3<3<3<3',
                            '<3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3',
                            ':kissing_heart :kissing_heart :kissing_heart :kissing_heart',
                            ':heart_eyes_cat :heart_eyes_cat :heart_eyes_cat :heart_eyes_cat',
                            'I love you :kiss :kiss :kiss :kiss :kiss',
                            ':heart :heart :heart :heart :heart']

    def getRandomLoveWord(self):
        words_count = len(self.__loveWords)
        random_number = randrange(words_count - 1)
        word = self.__loveWords[random_number]
        return word


def sendMessage(user_id):
    love = Love()
    love_word = love.getRandomLoveWord()
    bot.send_message(user_id, love_word)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message == 'Hi':
        bot.send_message(message.from_user.id, "<3")
    if message == 'start':
        schedule.every(4).hours.do(sendMessage, message.from_user.id)
        while True:
            schedule.run_pending()
            time.sleep(1)
