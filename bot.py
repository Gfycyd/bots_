import telebot
from config import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добрый день, студенты")

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, "Напиши свои идеи:")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMJX_ILPgra2YRRwIebMS6d6fhTdOoAAqQAAwN8kwwvBKk8X4ANxx4E')
    else:
        bot.send_message(message.chat.id, "Напиши мне Привет)")


@bot.message_handler(content_types=['sticker'])
def start_message(message):
    print(message)

bot.polling(none_stop=True)