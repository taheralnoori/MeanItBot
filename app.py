import telebot
import markups
import google_dict
import data_base
import os
import time

bot_token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	if user is None:
		db.insertUser(str(message.from_user.id), "en")
	else:
		db.updateLanguage(str(message.from_user.id), "en")
	msg = bot.send_message(message.chat.id, "يمكنني أن أشرح لك أي كلمة فقط كلمات اسرلي ما اريد اي شي ورمان حيرم عليك 🌝🌚.\nيرجى تحديد لغتك المفضلة:", reply_markup=markups.language_markup)

@bot.message_handler(commands=['help'])
def get_info(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	if user[1] == 'en':
		get_info_en(message)
	elif user[1] == 'fr':
		get_info_fr(message)
	elif user[1] == 'de':
		get_info_de(message)

def get_info_en(message):
	msg = "مرحبا، اسمي *MeanIt*! أنا هنا من أجلك للمساعدة في الكلمات الجديدة! فقط أضف الكلمة هنا وسأريك المعاني!"
	msg += "\n\nيمكنك التحكم بي عن طريق إرسال هذه الأوامر:\n\n"
	msg += "*تغيير اللغة:\n*"
	msg += "/english - حدد اللغة الإنجليزية الحالية.\n"
	msg += "/french - حدد اللغة الحالية الفرنسية.\n"
	msg += "/german - حدد اللغة الإنجليزية الألمانية.\n\n"
	msg += "/help - احصل على مساعدة بشأن استخدام الروبوت.\n"
	bot.send_message(message.chat.id, msg, parse_mode='Markdown')

def get_info_fr(message):
	msg = "Bonjour, je m'appelle *MeanIt*! Je suis là pour vous aider avec de nouveaux mots! Ajoutez simplement le mot ici et je vous montrerai les significations!"
	msg += "\n\nVous pouvez me contrôler en envoyant ces commandes:\n\n"
	msg += "*Changer de langue:\n*"
	msg += "/english - définir la langue actuelle anglais.\n"
	msg += "/french - définir la langue actuelle Français.\n"
	msg += "/german - définir la langue actuelle Allemand.\n\n"
	msg += "/help - obtenir de l'aide sur l'utilisation du bot.\n"
	bot.send_message(message.chat.id, msg, parse_mode='Markdown')

def get_info_de(message):
	msg = "Hallo, mein name ist *MeanIt*! Ich bin hier für Sie mit neuen Worten zu helfen! Fügen Sie einfach das Wort hier unten hinzu und ich zeige Ihnen die Bedeutungen!"
	msg += "\n\nSie können mich kontrollieren, indem Sie diese Befehle senden:\n\n"
	msg += "*Sprache ändern:\n*"
	msg += "/english - aktuelle Sprache Englisch einstellen.\n"
	msg += "/french - aktuelle Sprache Französisch einstellen.\n"
	msg += "/german - aktuelle Sprache Deutsch einstellen.\n\n"
	msg += "/help - holen Sie sich Hilfe bei der Verwendung des bot.\n"
	bot.send_message(message.chat.id, msg, parse_mode='Markdown')

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

@bot.message_handler(commands=['english'])
def setEnglishLanguage(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	answer = "الآن أعرف اللغة الإنجليزية" + flag('gb') + "\nPlease enter an unknown word."
	if user is None:
		db.insertUser(str(message.from_user.id), "en")
	elif user[1] != "en":
		db.updateLanguage(str(message.from_user.id), "en")
	else:
		answer = "أعرف اللغة الإنجليزية بالفعل" + flag('gb') + "\nPlease enter an unknown word."
	msg = bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['french'])
def setFrenchLanguage(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	answer = "Maintenant je connais le français" + flag('fr') + "\nVeuillez saisir un mot inconnu."
	if user is None:
		db.insertUser(str(message.from_user.id), "fr")
	elif user[1] != "fr":
		db.updateLanguage(str(message.from_user.id), "fr")
	else:
		answer = "Je connais déjà le français" + flag('fr') + "\nVeuillez saisir un mot inconnu."
	msg = bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['german'])
def setGermanLanguage(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	answer = "Jetzt kenne ich die Deutsche Sprache" + flag('de') + "\nBitte geben Sie ein unbekanntes Wort ein."
	if user is None:
		db.insertUser(str(message.from_user.id), "de")
	elif user[1] != "de":
		db.updateLanguage(str(message.from_user.id), "de")
	else:
		answer = "Ich kenne schon Deutsch" + flag('de') + "\nBitte geben Sie ein unbekanntes Wort ein."
	msg = bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['text'])
def getWord(message):
	db = data_base.DataBase()
	user = db.findUser(str(message.from_user.id))
	data = google_dict.find_word(user[1], message.text)
	if (data.status_code == 200):
		createAnswer(data.json(), message)
	else:
		if user[1] == 'en':
			bot.send_message(message.chat.id, "Unknown word.")
		elif user[1] == 'fr':
			bot.send_message(message.chat.id, "Mot inconnu.")
		elif user[1] == 'de':
			bot.send_message(message.chat.id, "Unbekanntes Wort.")

def createAnswer(data_list, message):
	for data in data_list:
		audio = None
		word = data['word'].capitalize()
		answer = f"*{word}*\n\n"
		answer += "*Pronunciation*:"
		for phonetics in data["phonetics"]:
			for (key, value) in phonetics.items():
				if key == 'audio':
					audio = value
				else:
					key = key.capitalize()
					answer += f"\n{key}: {value}"
		answer += "\n\n"
		answer += "*Meaning*:\n"
		for i, (key, value) in enumerate(data['meaning'].items()):
			key = key.capitalize()
			answer += f"_{key}_:\n"
			for j, word in enumerate(value):
				answer += f"{i + 1}.{j + 1}"
				for k, v in word.items():
					k = k.capitalize()
					answer += f" *{k}*: {v}"
				answer += "\n"
			answer += "\n"
		answer += "\n"
		bot.send_message(message.chat.id, answer, parse_mode='Markdown')
		if audio is not None:
			msg = bot.send_audio(message.chat.id, audio)


if __name__ == '__main__':
	bot.polling(none_stop=True, interval=0)
