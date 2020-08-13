from telebot import types

language_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
language_markup.add('English')
language_markup.add('French')
language_markup.add('German')
