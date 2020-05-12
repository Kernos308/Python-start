import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
imie = pd.read_excel(xlsx,'Arkusz1')
plec=imie[(imie['Rok']>=2012)].groupby(['Plec']).count()
plec=plec['Liczba']
wykres = plec.plot.pie(subplots=True, autopct='%.2f%%', fontsize=15)
plt.title('Liczba urodzonych dziewczynek i chlopcow')
plt.show()