import telebot

bot = telebot.TeleBot('1377602523:AAHrDShJkWaccxSVu5iXji2Pc3xuEKSZuf0')


def callback_alarm(context: telegram.ext.CallbackContext):
    bot.send_message(chat_id=id, text='Hi, This is a daily reminder')


def reminder(update, context):
    bot.send_message(chat_id=update.effective_chat.id,
                     text='Daily reminder has been set! You\'ll get notified at 8 AM daily')
    context.job_queue.run_daily(callback_alarm, context=update.message.chat_id, days=(0, 1, 2, 3, 4, 5, 6),
                                time=time(hour=10, minute=10, second=10))
