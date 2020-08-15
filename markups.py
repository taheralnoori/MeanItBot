from telebot import types

language_markup = types.InlineKeyboardMarkup()
english_key = types.InlineKeyboardButton(text='English', callback_data='en')
french_key = types.InlineKeyboardButton(text='French', callback_data='fr')
german_key = types.InlineKeyboardButton(text='German', callback_data='de')
language_markup.add(english_key)
language_markup.add(french_key)
language_markup.add(german_key)
