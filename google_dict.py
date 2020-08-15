import requests
import config

def find_word(language_code, word):
	response = requests.request("GET", config.dict_url + language_code + "/" + word)
	return response
