import requests

DICT_URL = "https://api.dictionaryapi.dev/api/v1/entries/"

def find_word(language_code, word):
	response = requests.request("GET", DICT_URL + language_code.lower() + "/" + word)
	return response
