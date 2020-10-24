import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

haberler = []
siteler = ["https://www.ensonhaber.com/rss/ensonhaber.xml"
           ,"https://www.aa.com.tr/tr/rss/default?cat=guncel"
           ,"http://www.star.com.tr/rss/rss.asp"
           ,"https://rss.dw.com/rdf/rss-tur-all"
           ,"https://www.haberturk.com/rss"]  # BAZI ÖRNEK HABER WEB SİTELERİ

for i in siteler:
    req = requests.get(i, headers=headers)
    soup = BeautifulSoup(req.content,"lxml")
    metin = soup.select('item')
    for j in metin:  # ELDE EDİLEN TÜM SAYFANIN HER 'İTEM' KISMINI DÖNGÜYLE SAĞLAMA 
        haber = dict()
        haber['Başlık'] = j.title.text.strip()
        haber['Açıklama'] = j.description.text.strip()
        haber['Tarih'] = j.pubdate
        haberler.append(haber)

df = pd.DataFrame(haberler, columns=['Başlık','Açıklama','Tarih'])
df.to_csv('veri.csv', index = False, encoding = 'utf-8')
