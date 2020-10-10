import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

haberler = []
siteler = ["https://www.ensonhaber.com/rss/ensonhaber.xml"
           ,"https://www.aa.com.tr/tr/rss/default?cat=guncel"
           ,"http://www.star.com.tr/rss/rss.asp"
           ,"https://rss.dw.com/rdf/rss-tur-all"
           ,"https://www.haberturk.com/rss"] # BAZI ÖRNEK HABER WEB SİTELERİ

for i in siteler: # HER BİR SİTE İÇERİSİNDE ARAMA
    req = requests.get(i, headers=headers) # İLGİLİ SİTEYE BAĞLANTI İSTEĞİ GÖNDERME VE BAĞLANTI HATASI ÖNLEMEK İÇİN AGENT KULLANIMI
    soup = BeautifulSoup(req.content,"lxml") # VERİYİ ELDE EDİP HTML KISMINI PARÇALAMA
    metin = soup.select('item') # İSTENİLEN VERİ TÜRÜNÜN HTML ÖZELLİĞİNİ YAZIP SELECT FONKSİYONUYLA TAMAMINI SEÇME
    for j in metin: # ELDE EDİLEN TÜM SAYFANIN HER 'İTEM' KISMINI DÖNGÜYLE SAĞLAMA 
        haber = dict()
        haber['Başlık'] = j.title.text.strip() # SÖZLÜĞÜN BAŞLIK KISMINA METİNDEN ELDE ETTİĞİMİZ BAŞLIĞI YAZMA
        haber['Açıklama'] = j.description.text.strip() # SÖZLÜĞÜN AÇIKLAMA KISMINA METİNDEN ELDE ETTİĞİMİZ AÇIKLAMAYI YAZMA
        haber['Tarih'] = j.pubdate # SÖZLÜĞÜN TARİH KISMINA METİNDEN ELDE ETTİĞİMİZ TARİHİ YAZMA
        haberler.append(haber) # ELDE EDİLEN VERİ GRUBUNU HABERLER LİSTESİNE EKLEME

df = pd.DataFrame(haberler, columns=['Başlık','Açıklama','Tarih']) # BELİRTİLEN KOLONLARLA PANDAS DATAFRAME'Sİ OLUŞTURMA
df.to_csv('veto1s.csv', index = False, encoding = 'utf-8') # DATAFRAME'NİN İNDEX BELİRTİLMEYEN BİR CSV DOSYASINA DÖNÜŞTÜRÜLMESİ
