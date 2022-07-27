import requests


def get_word_from_api():
	url = "https://random-words-with-pronunciation.p.rapidapi.com/word"

	headers = {
		"X-RapidAPI-Key": "727c2558d7mshc6004fe691efe0ep10381djsnf9399ab0785f",
		"X-RapidAPI-Host": "random-words-with-pronunciation.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers)
	my_dict = response.json()[0]
	return my_dict
