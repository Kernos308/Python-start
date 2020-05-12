import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel(xlsx,'Arkusz1')
lata=imiona.groupby(['Rok']).count()
lata=lata['Imie']
wykres=lata.plot.bar()
wykres.set_ylabel('Liczba urodzin')
wykres.set_xlabel('Rok')
plt.title('Liczba urodzonych dzieci dla kazdego roku')
plt.show()