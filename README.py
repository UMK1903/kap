#CSS ile de filtreleyebiliriz, ben bunu tercih ediyorum.
sozler=icerigiAl.select("div#PageContent")
for i in range(0,len(sozler)): #döngüyü, aldığımız dönütün uzunluğu ile sınırlandırıyoruz.
print(sozler[i].contents[0].text +": "+sozler[i].contents[2]+"\n") #Etiket içeriklerini çekip yazdırıyoruz.

import requests
from bs4 import BeautifulSoup
url="http://guzelsozlerblog.com/gunun-sozu"
response=requests.get(url)
<span style="color:#ff0000;">response.encoding= "iso-8859-9"</span> #Bu kod ile çektiğimiz verideki "ş,ç,i" gibi karakterlerde çıkabilecek problemleri önlüyoruz.
AnalizEdilecekIcerik=response.text
icerigiAl=BeautifulSoup(AnalizEdilecekIcerik,"lxml")


print(filtre) #tüm filtreyi yazdırdık
print(filtre[0]) #filtreden gelen verinin sadece 0.indexine ait içe

filtre=icerigiAl.find_all(id="PageContent") #id değeriyle filtreleme yaptık

icerigiAl=BeautifulSoup(AnalizEdilecekIcerik,"lxml") #BS4 HTML kodunu analiz ediyor
#"lxml" parametresini kütüphanenin bize verdiği uyarı gereği kullandık. Parametresiz veya diğer parametreler ile kullanabilirsiniz. Bu parametre hakkında daha fazla bilgi için--&gt; https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser


import requests
from bs4 import BeautifulSoup
url="http://guzelsozlerblog.com/gunun-sozu"
response=requests.get(url)
print(response.text)
AnalizEdilecekIcerik=response.text #Sayfadan gelen HTML kodunu atadık


import requests #requests kütühanemizi dahil ettik
url="http://guzelsozlerblog.com/gunun-sozu" #web sayfası URL sini atadık
response=requests.get(url) #kütüphane yardımıyla web sayfasına gittik
print(response.text) #web sayfasının çıktısını yazdırdık


import requests
from bs4 import BeautifulSoup

url="http://guzelsozlerblog.com/gunun-sozu" #Our url which will we read

response=requests.get(url) #Go to URL
response.encoding= "iso-8859-9" #Web site's charset --> <meta http-equiv="content-type" content="text/html; charset=iso-8859-9">
#Encoding is important for your text's characters which get from website

AnalizEdilecekIcerik=response.text #get HTML code of URL

icerigiAl=BeautifulSoup(AnalizEdilecekIcerik,"lxml") #read and analyze HTML code of url
#we use "lxml" because, when it wasn't there, there was an error. Code was running but we don't want to see warning :)
#warning text said this parameter to me. You can read this URL for parameters: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser

#Filter HTML code which analyzed with CSS selector for just div tags
sozler=icerigiAl.select("div#PageContent") #get div containers

gonderilecekYazi="" #we will sent this to telegram chat

for i in range(0,len(sozler)): #iterate from 0 to length of our list
    gonderilecekYazi+=sozler[i].contents[0].text +": "+sozler[i].contents[2]+"\n\n"

token = "1252889534:AAHvfHepWgNprrTLzmZp7h-D7_8kPeT6s64" #telegram token
chat_id = "486819640" #telegram id

requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 486819640, 'text': gonderilecekYazi}).json()
#telegram sendMessage url, more commands --> https://core.telegram.org/bots
