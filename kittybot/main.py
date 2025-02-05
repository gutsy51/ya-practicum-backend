import requests
from telebot import TeleBot, types

bot = TeleBot(token='7632787987:AAFpqkjSWx0Gv2wA5uGC6-HwTZt1QMvHh2I')
URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_image():
    response = requests.get(URL).json()
    random_cat = response[0].get('url')
    return random_cat


@bot.message_handler(commands=['newcat'])
def new_cat(message):
    chat = message.chat
    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(commands=['start'])
def wake_up(message):
    chat = message.chat
    name = message.chat.first_name
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_newcat = types.KeyboardButton('/newcat')
    keyboard.add(button_newcat)

    bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}. Посмотри, какого котика я тебе нашёл',
        reply_markup=keyboard,
    )

    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(content_types=['text'])
def say_hi(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text='Привет, я KittyBot!')


if __name__ == '__main__':
    bot.polling()
