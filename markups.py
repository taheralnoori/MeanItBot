from telebot import types

language_markup = types.InlineKeyboardMarkup()
english_key = types.InlineKeyboardButton(text='English', callback_data='English')
french_key = types.InlineKeyboardButton(text='French', callback_data='French')
german_key = types.InlineKeyboardButton(text='German', callback_data='German')
language_markup.add(english_key)
language_markup.add(french_key)
language_markup.add(german_key)
