
import telebot
import markups as m

import logging

logger = telebot.logger
logger.setLevel(logging.DEBUG)

TOKEN = "1348328650:AAHW2tlpYyhl_8C-J9QxPSc3mTaowen7ps0"

bot = telebot.TeleBot(TOKEN)
curLanguage = ""

@bot.message_handler(commands=['start'])
def send_welcome(message):
	msg = bot.send_message(message.chat.id, "I can explain to you any word.")
	msg = bot.send_message(message.chat.id, "Please select your preferred language:", reply_markup=m.language_markup)

@bot.message_handler(commands=['English'])
def setEnglishLanguage(message):
	if curLanguage != "English":
		curLanguage = "English"
		msg = bot.send_message(message.chat.id, "Now I know English.")

@bot.message_handler(commands=['French'])
def setFrenchLanguage(message):
	if curLanguage != "French":
		curLanguage = "French"
		msg = bot.send_message(message.chat.id, "Maintenant je connais le français.")

@bot.message_handler(commands=['German'])
def setGermanLanguage(message):
	if curLanguage != "German":
		curLanguage = "German"
		msg = bot.send_message(message.chat.id, "Jetzt kenne ich die Deutsche Sprache.")

@bot.message_handler(content_types=['text'])
def handle_word(message):
	if (message.text.lower == 'english'):
		setEnglishLanguage(message)
	elif (message.text.lower == 'french'):
		setFrenchLanguage(message)
	elif (message.text.lower == 'german'):
		setGermanLanguage(message)
	# bot.send_message(message.chat.id,"Ok")

if __name__ == '__main__':
	bot.polling(none_stop=True)#, interval=0)
