# print("Witaj świecie!")
# a = 'Ala'
# b = 'Marek'
# c = 'Kasia'
# print(a)
# print(b)
# print(c)
# # blok kodu
# # for element in kolekcja:
# #     for element2 in kolekcja2:

# dlugi_tekst = """Ala ma kota
# a kot jest głodny."""
# print(dlugi_tekst)

#           """ dokumentacja """

# print(type(a))
# print(a + b)
# print(2 - 3)
# print(2 * 3)
# print(2 / 3)
# print(2 // 3)
# print(2 % 3)
# print(2 ** 3)

# print(3,34 + 34.34)

# def pow(liczba, potega):
#     pass


# import math as m # OK
# from math import * # tak sobie, przesłania
# from math import pi, pow, # OK, ale przesłania

# m.pow()

# print("Ala ma " + str(4) + " lata")
# print("Ala ma {0}lata".format(4))
# print("Ala ma {} lata".format(4, 4, "Ala", 3.14))
# wiek = 4
# print(f"Ala ma {wiek} lata")

# str(1)
# int(1)
# float(1)


# imie = 'Ala'
# print(imie.upper())
# print(imie)
# imie = imie.upper()

# print(imie[0])

# listy

# lista = [1, 2, 3, 4, 'Ala', imie]
# lista2 = list() # ekwiwalent lista = []
# lista2 = lista.append(1)
# print(lista)
# lista[0] = 5 #dla list już można zmieniac dane
# lista3 = lista + lista2


# słownik
# pary wartości klucz: wartość
# slownik = {"imie": "Krzysztof", "wzrost": 183}
# print(slownik["imie"]) # odwołanie poprzez klucz
# print(slownik.keys())
# print(slownik.values())
# print(slownik.items())

#  wejscie = input()
#  print(wejscie)
#  print(type(wejscie))

#  import sys
#  wejscie2 = sys.stdin.readline()
#  print(wejscie2)
#  print(type(wejscie2))
# fsdasfsdsd
# fsdasfsdsd

# dsfssd
# dsfssd

# <class 'str'>

# liczba = 10
# if liczba < 10:
#     print ("mniejsza niz 10")
# elif liczba > 10:
#     print("wieksza niz 10")
# else:
#     print("nie da sie")
# # and or not
# # != rozny od 
#     if liczba > 0 and liczba < 11:
#         print("OK")
# # krocej
# if 0 < liczba < 11:
#     print("OK")
# # foreach
# imie = "Adrian"
# for litera in imie:
#         print(litera, end='')
# print()










# range(5) #start, stop, step
# # stop -> stop - step
# print(range(5))
# print(type(range(5)))
# print(list(range(2, 10, 2)))
# print(list(range(0, -10, -2)))
# # [od:do]
# print(imie[2])

# print(imie[::2])

# for liczba in range(5):
#     pass
# for ltera in imie[::2]:
#     pass #opuszczenie
# # !!!ZROBIC POPRZEDNIA LEKCJE!!!
# # LEKCJA 2
# #zad 1
# a = input("Podaj jakiekolwiek zdanie\n")

# print(a.count(" "))
# #zad 2
# b = input("Podaj liczbe 1\n")
# c = input("Podaj liczbe 2\n")
# wynik = int(b) * int(c)
# print(wynik)
# #zad 4
# d = input("Podaj dowolna liczbe calkowita\n")
# print(abs(int(d)))
# #zad 5
# a = input("Podaj liczbe a\n")
# b = input("Podaj liczbe b\n")
# c = input("Podaj liczbe c\n")
# a = int(a)
# b = int(b)
# c = int(c)
# if 0<a<10 and a>b or b>c:

#     print("Warunki sa spelnione")
# else:
#     print("Warunki nie sa spelnione")
#zad 6 

# print(list(range(0, 100, 5)))
#zad 7 (poprawic)
# a = input("Podaj kilka liczb calkowitych\n")
# for x in a:
#     print(pow(int(x), 2))
# else:
#     print("oto twoje potegi")
#zad 8
# a = input("Podaj kilka liczb calkowitych\n")
# while(a == int(a)):
#     list(a)
#zad 9 (poprawic)
# a = input("Podaj liczbe kilkucyfrowa\n")
# a= int(a)
# while(a>9):
#     wynik +=range(a::1)
#     print(a)
# else:
#     print("lipton")
# ĆW 3
# import this

# imie = 'Marianna'
# lista = []
# for litera in imie:
#     lista.append(litera.upper())
# print(lista)
# #rownowaznie
# print([litera.upper() for litera in imie])
# lista = [print(litera.upper()) for litera in imie]
# print(lista)


#suma cyfr
# liczba = 123456789
# print(sum([int(cyfra) for cyfra in str(liczba)]))
# #---------------
# print([2**n for n in range(5)])
# #-----------------------
# lista = [
#     [1, 2],
#     [3, 4]]
# print([element for wiersz in lista for element in wiersz if element %2 == 0])
# wynik = []
# for wiersz in lista:
#     for element in wiersz:
#         if element %2 == 0:
#             wynik.append(element)
# #------------------------------

# imie = 'Marianna'
# # klucz, wartosc = (0, 'M')
# # {0:'M', ...}
# {para[0]:para[1] for para in enumerate(imie)}
# slownik = {klucz:wartosc for klucz, wartosc in enumerate(imie)}
# slownik[0] # klucz
# print(slownik)
# slow_odwr = {wartosc:klucz for klucz, wartosc in slownik.items()}
# print(slow_odwr)


#set - zbiory  
# imie = 'Marianna'
# litery = set(imie)
# print(litery)

# # rozpakowanie krotki
# imie, nazwisko = ('Marian', 'Bąbel')
# # to tez rozpakowanie
# print({*range(9)})
# from timeit import timeit
# print(timeit("{*range(9)}", number=100000))
# print(timeit("set(range(9))", number=100000))
# print(timeit("[]", number=100000))
# print(timeit("list()", number=100000))
# kod = """
# lista = [
#     [1, 2],
#     [3, 4]]
# wynik = []
# for wiersz in lista:
#     for element in wiersz:
#         if element %2 == 0:
#              wynik.append(element)"""
# [element for wiersz in lista for element in wiersz if element %2 == 0]

# def dodaj(liczba1, liczba2):
#     return liczba1 + liczba2

# dodaj(2, 3)

# def witaj(imie='Jan'):
#     print(f'Witaj {imie}!')
# witaj()
# witaj("Arkadiusz")

# def witaj(imie, nazwisko='Kowalksi') OK
#def witaj(imie='Jan', nazwisko): błąd
#    print(f'Witaj {imie}!')

# MODULY I PAKIETY

# import start as s
# s.pow()


# ZAD 11 z diamenickiem?
# bedzie na repozytorium w kilku wersjach
