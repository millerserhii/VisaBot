import json
import telebot


bot = telebot.TeleBot('api')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, напиши страну: ')

@bot.message_handler(content_types=['text'])
def send_text(message):
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
        bot.send_message(message.chat.id, data.get(message.text))


bot.polling()
