
import telebot
import markups as m

TOKEN = "1348328650:AAHW2tlpYyhl_8C-J9QxPSc3mTaowen7ps0"

bot = telebot.TeleBot(TOKEN)
curLanguage = ""
isStart = False
OFFSET = 127462 - ord('A')

@bot.message_handler(commands=['start'], func = lambda m: isStart == False)
def send_welcome(message):
	global isStart
	msg = bot.send_message(message.chat.id, "I can explain to you any word.")
	msg = bot.send_message(message.chat.id, "Please select your preferred language:", reply_markup=m.language_markup)
	isStart = True

def flag(code):
	code = code.upper()
	return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	if call.data == "English":
		setEnglishLanguage(call.message)
	elif call.data == "French":
		setFrenchLanguage(call.message)
	elif call.data == "German":
		setGermanLanguage(call.message)

@bot.message_handler(commands=['English'], func = lambda m: curLanguage != "English")
def setEnglishLanguage(message):
	global curLanguage
	if curLanguage != "English":
		curLanguage = "English"
		answer = "Now I know English" + flag('gb') + "."
		msg = bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['French'], func = lambda m: curLanguage != "French")
def setFrenchLanguage(message):
	global curLanguage
	if curLanguage != "French":
		curLanguage = "French"
		answer = "Maintenant je connais le français" + flag('fr') + "."
		msg = bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['German'], func = lambda m: curLanguage != "German")
def setGermanLanguage(message):
	global curLanguage
	if curLanguage != "German":
		curLanguage = "German"
		answer = "Jetzt kenne ich die Deutsche Sprache" + flag('de') + "."
		msg = bot.send_message(message.chat.id, answer)

if __name__ == '__main__':
	bot.polling(none_stop=True, interval=0)
