from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"

html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content, 'html.parser')

ul = soup.find('section','section chart-grid')

li_list = ul.find_all('li')

all_songs=[]

for li in li_list:
    a = li.h3.a 
    b = li.h4.a
    songs={}
    songs["Song's Names"] = a.string
    songs['Artists'] = b.string
    all_songs.append(songs)

    ## download songs
    
    options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
    }
    
    dl = YoutubeDL(options)
    dl.download([a.string])

pyexcel.save_as(records=all_songs, dest_file_name="top_songs.xlsx")