import requests

class Game:
	def __init__(self, title, release_date, descprtion, price):
		self.__title = title
		self.__release_date = release_date
		self.__descprtion = descprtion
		self.__price = price
		
url = f'https://store.steampowered.com/franchise/freedomgames'
url2 = f'https://www.naver.com'
response = requests.get(url)
print(response)

game_lists.append(Game())