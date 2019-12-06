import telebot
import parcer
import schedule
import time

bot = telebot.TeleBot('1035544822:AAEsqmCrzyQzXyh6yKGb7KTsTQXX_ICh7z4')


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Бот начал работу...")
        print(message.user.id)


def mane():
    print('Функция mane() нчачала работу...')
    for game in parcer.NewGames():
        if parcer.check_the_entry(game):
            bot.send_message(509585214, 'Доступно новое предложение: \n %s \n'
                                        '\n От: %s \n\n Цена: %s руб' % (game.link_, game.seller, game.price))


schedule.every(3).minutes.do(mane)
while True:
    schedule.run_pending()
    time.sleep(1)



