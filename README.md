# MeanItBot
MeanIt is a Telegram Bot that helps you learn new words!
Type in a word and it shows you its meanings!
Bot supports 3 languages:
* English
* French
* German

The bot is written using [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI "pyTelegramBotAPI").
The user's current language is saved in the Sqlite database.
After six months of non-use of the bot, the record in the database is cleared.
Updates are obtained using webhooks.
Word searches are done using the [(unofficial) Google Dictionary API](https://dictionaryapi.dev/ "Google Dictionary API").


# Commands

You can control bot by sending these commands:
* Change language:
  * /english - set current language English.
  * /french - set current language French.
  * /german - set current language German.

* /help - get help on using the bot.
