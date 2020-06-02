
from bs4 import BeautifulSoup
import urllib3
import pandas as pd

url='https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed&page='
http=urllib3.PoolManager()
li={'Tytul':[], 'Platforma':[], 'Data_wydania':[], 'Ocena':[]}
for nr in range(1,11):
    soup=BeautifulSoup(http.request('GET',url+'nr').data,'lxml')
    for element in soup.find_all('table'):
        for i in element.find_all('td',{'class':'clamp-summary-wrap'}):
            li['Tytul'].append(i.find('h3').string.strip())
            for j in i.find_all('div'):
                if j['class'] == ['clamp-score-wrap']:
                    li['Ocena'].append(float(j.find('div').string.strip()))
                elif j['class'] == ['clamp-details']:
                    li['Platforma'].append(j.find('span',{'class':'data'}).string.strip())
                    li['Data_wydania'].append(j.find('span',{'class':None}).string)
df=pd.DataFrame(li)
df=df.drop_duplicates()
p=df[df['Platforma']=='PC'].sort_values('Ocena',ascending=False)
print(p[:10])