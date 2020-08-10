
import telebot
import markups as m

# import logging

# logger = telebot.logger
# logger.setLevel(logging.DEBUG)

TOKEN = "1348328650:AAHW2tlpYyhl_8C-J9QxPSc3mTaowen7ps0"

bot = telebot.TeleBot(TOKEN)#, parse_mode=None)
isRunning = False
curLanguage = "English"

@bot.message_handler(commands=['start'])
def send_welcome(message):
	global isRunning
	if not isRunning:
		msg = bot.send_message(message.chat.id, "Hello, my name is MeanIt! I can explain to you any word.")
		isRunning = True
		setLanguage(msg)

@bot.message_handler(commands=['setLanguage'])
def setLanguage(message):
	msg = bot.send_message(message.chat.id, "Please select your preferred language:", reply_markup=m.language_markup)
	if (message.text.lower == 'english'):
		curLanguage = "English"
	bot.register_next_step_handler(msg, findWord)

@bot.message_handler(commands=['findWord'])
def findWord(message):
	to_send = "Current language is " + curLanguage + ". Please enter an unknown word:"
	msg = bot.send_message(message.chat.id, to_send)
	bot.register_next_step_handler(msg, handle_word)

@bot.message_handler(content_types=['text'])
def handle_word(message):
	bot.send_message(message.chat.id,"Ok")

if __name__ == '__main__':
	bot.polling(none_stop=True)#, interval=0)
# handle /help
# handle /settings
