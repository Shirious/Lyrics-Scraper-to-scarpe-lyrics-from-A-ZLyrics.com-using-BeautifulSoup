import requests
import bs4 as bs
import urllib.request
head = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring' }


data = []
artist,song = str(input("artist : ")) , str(input("song : "))

artist = artist.lower().replace(' ','')
song = song.lower().replace(' ','')
print(artist,song)

data = requests.get("https://www.azlyrics.com/lyrics/" +artist+"/"+song+".html" , headers = head)
soup = bs.BeautifulSoup(data.text,"lxml")

data = []
for link in soup.find_all('div') :
	data.append(link.text)
maxl = 0
for d in data :
	if len(d) > maxl :
		dt = d
		maxl = len(d)
for i in range(10) :
	dt = dt.replace('\n\n','\n')
dt  = dt.split('\n\r\n')

data = str(dt[0]) + str(dt[1])
print(data)
