import requests as req
from bs4 import BeautifulSoup as bs

def get_top_ten():
    h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

    res= req.get("https://www.melon.com/chart/index.htm",headers = h)

    soup = bs(res.text,'lxml')
    singer = [i.text for i in soup.select("span.checkEllipsis")]
    song = [i.text.strip() for i in soup.select("div.rank01>span")]

    top_ten_singer = singer[:10]
    top_ten_song = song[:10]

    return top_ten_singer, top_ten_song

def get_top_ten_string():
    top_ten_singer, top_ten_song = get_top_ten()

    top_ten_string = ''
    for i in range(10):
        top_ten_string += f'{i+1} {top_ten_singer[i]} - {top_ten_song[i]}\n'
    
    return top_ten_string

if __name__ == '__main__':
    top_ten_singer, top_ten_song = get_top_ten()

    for i in range(10):
        print(i+1, top_ten_singer[i], '-',top_ten_song[i])