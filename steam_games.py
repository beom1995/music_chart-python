import requests
from bs4 import BeautifulSoup

class Song:
	def __init__(self, title, artist, albumtitle, rank):
		self.__title = title
		self.__artist = artist
		self.__albumtitle = albumtitle
		self.__rank = rank

	def get_title(self):
		return self.__title
	
	def get_artist(self):
		return self.__artist
	
	def get_albumtitle(self):
		return self.__albumtitle
	
	def get_rank(self):
		return self.__rank

	@staticmethod
	def print_songs(song_list, criteria):
		list = []
		match criteria:
			case '0':
				list = song_list
			case '1':
				list = sorted(song_list, key=lambda x: x.get_title())
			case '2':
				list = sorted(song_list, key=lambda x: x.get_artist())
			case '3':
				list = sorted(song_list, key=lambda x: x.get_albumtitle())

		for song in list:
			print('곡명: ', song.get_title())
			print('순위: ', song.get_rank())
			print('가수: ', song.get_artist())
			print('앨범명: ', song.get_albumtitle())
			print('---------------------------------------')
	

def crawling():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
	song_list = []
	for i in range(1,5):
		data = requests.get(f'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20240401&hh=16&rtm=Y&pg={i}', headers=headers)

		soup = BeautifulSoup(data.content, 'html.parser')
		tr_tags = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

		for song in tr_tags:
			title = song.select_one('td.check > input')['title']
			artist = song.select_one('td.info > a.artist').get_text()
			albumtitle = song.select_one('td.info > a.albumtitle').get_text()
			rank = song.select_one('td.number').get_text(separator=', ', strip=True).split(',')[0]
			song_list.append(Song(title, artist, albumtitle, rank))

	return song_list

if __name__ == '__main__':
	criteria = input('정렬 기준을 선택하세요(0: 기본, 1: 곡명, 2: 가수명, 3: 앨범명): ')
	song_list = crawling()
	Song.print_songs(song_list, criteria)