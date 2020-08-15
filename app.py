import telebot
import markups
import config
import google_dict
import data_base

bot = telebot.TeleBot(config.bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	if user is None:
		db.insertUser(str(message.from_user.id), "en")
		msg = bot.send_message(message.chat.id, "I can explain to you any word.")
		msg = bot.send_message(message.chat.id, "Please select your preferred language:", reply_markup=markups.language_markup)

OFFSET = 127462 - ord('A')

def flag(code):
	code = code.upper()
	return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)

@bot.callback_query_handler(func = lambda m: True)
def setLanguage(call):
	if call.data == "en":
		setEnglishLanguage(call.message)
	elif call.data == "fr":
		setFrenchLanguage(call.message)
	elif call.data == "de":
		setGermanLanguage(call.message)

@bot.message_handler(commands=['English'])
def setEnglishLanguage(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	answer = "Now I know English" + flag('gb') + "."
	if user is None:
		db.insertUser(str(message.from_user.id), "en")
	elif user[1] != "en":
		db.updateLanguage(str(message.from_user.id), "en")
	else:
		answer = "I already know English" + flag('gb') + "."
	msg = bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['French'])
def setFrenchLanguage(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	answer = "Maintenant je connais le français" + flag('fr') + "."
	if user is None:
		db.insertUser(str(message.from_user.id), "fr")
	elif user[1] != "fr":
		db.updateLanguage(str(message.from_user.id), "fr")
	else:
		answer = "Je connais déjà le français" + flag('fr') + "."
	msg = bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['German'])
def setGermanLanguage(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	answer = "Jetzt kenne ich die Deutsche Sprache" + flag('de') + "."
	if user is None:
		db.insertUser(str(message.from_user.id), "de")
	elif user[1] != "de":
		db.updateLanguage(str(message.from_user.id), "de")
	else:
		answer = "Ich kenne schon Deutsch" + flag('de') + "."
	msg = bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['text'])
def getWord(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	data = google_dict.find_word(user[1], message.text)
	if (data.status_code == 200):
		bot.send_message(message.chat.id, createAnswer(user[1], data.json()))

def createAnswer(language, data):
	if language == 'en':
		answer = createEnglishAnswer(data)
	# elif language == 'fr':
	# 	answer = createFrenchAnswer(data)
	# elif language == "de":
	# 	answer = createGermanAnswer(data)
	return answer

def createEnglishAnswer(data_list):
	answer = ""
	for data in data_list:
		answer = "Word: " + data['word'] +".\n"
	return answer

if __name__ == '__main__':
	bot.polling(none_stop=True, interval=0)
