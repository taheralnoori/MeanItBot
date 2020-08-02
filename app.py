from telebot import types
import telebot
import logging

logger = telebot.logger
logger.setLevel(logging.DEBUG)

TOKEN = "1348328650:AAHW2tlpYyhl_8C-J9QxPSc3mTaowen7ps0"

CUR_LANGUAGE="English"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('English')
	msg = bot.send_message(message.chat.id, "Hello, my name is MeanIt! I can explain to you any word. Please select your preferred language:",\
	reply_markup=markup)
	bot.register_next_step_handler(msg, set_language)

def set_language(message):
	if (message.text.lower == 'english'):
		CUR_LANGUAGE = "English"
	msg = bot.send_message(message.chat.id, "Please enter an unknown word:")
	bot.register_next_step_handler(msg, find_word)

@bot.message_handler(content_types=['text'])
def find_word(message):
	bot.send_message(message.chat.id,"Ok")

if __name__ == '__main__':
	bot.polling(none_stop=True, interval=0)
