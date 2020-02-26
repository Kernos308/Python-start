print("Witaj świecie!")
a = 'Ala'
b = 'Marek'
c = 'Kasia'
print(a)
print(b)
print(c)
# blok kodu
# for element in kolekcja:
#     for element2 in kolekcja2:

dlugi_tekst = """Ala ma kota
a kot jest głodny."""
print(dlugi_tekst)

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

print("Ala ma " + str(4) + " lata")
print("Ala ma {0}lata".format(4))
print("Ala ma {} lata".format(4, 4, "Ala", 3.14))
wiek = 4
print(f"Ala ma {wiek} lata")

# str(1)
# int(1)
# float(1)


# imie = 'Ala'
# print(imie.upper())
# print(imie)
# imie = imie.upper()

# print(imie[0])

# listy

lista = [1, 2, 3, 4, 'Ala', imie]
lista2 = list() # ekwiwalent lista = []
lista2 = lista.append(1)
print(lista)
lista[0] = 5 #dla list już można zmieniac dane
lista3 = lista + lista2


# słownik
# pary wartości klucz: wartość
slownik = {"imie": "Krzysztof", "wzrost": 183}
print(slownik["imie"]) # odwołanie poprzez klucz
print(slownik.keys())
print(slownik.values())
print(slownik.items())