import requests
import config

def find_word(language_code, word):
	response = requests.request("GET", config.dict_url + language_code.lower() + "/" + word)
	return response
