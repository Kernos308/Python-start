# zad 1
a = 7
b = 3
c = "Ala"
d = "Kot"
e = 3.14
f = 123.123
print(a, b, c, d, e, f)
# zad 2
a0 = 1
a1 = 2
a2 = 3
dodawanie = a0 + a1
odejmowanie = a1 - a0
mnozenie = a0 * a1
dzielenie = a1 / a0
reszta = a2 % a1
potega = a1 ** a2
# zad 3
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)
a %= 3
print(a)
# zad 4
from math import *
x = 10
y = exp(x)
print(y)
z = pow(log(5 + sin(8)**2), 1/6)
print(z)
x1 = abs(3.55)
x2 = abs(4.80)
print(x1, x2)
# zad 5
a = 'JACEK'
b = 'GROSS'
print(str.capitalize(a), str.capitalize(b))
#zad 6
c = 'Fajna piosenka la la la, fajna piosenka la la la, fajna piosenka la la la'
d = c.count('la')
print(d)
#zad 7
a = 'Zielony'
print(a[1], a[6])
#zad 8
print(c.split())
#zad 9

h = 5.13
b = 'jeden'
c = 0x1b3
print('%(a)f ,%(b)s, %(c)he' % {'a':h, 'b':b, 'c':c} )
#zad 10
lista = ["Gwiezdne wojny", "Wladca Pierscieni", "Avengers", "Fajny film"]
lista.sort()
print(lista)
#zad 11

#zad 12
zdanie = "Ala ma fajnego duzego kocura"
lista2 = [zdanie.split()]
print(lista2)
#zad 13
znajomi = {
    "Piotr" : "Nierzwik",
    "Pawel" : "Winiak",
    "Rafal" : "Ryzu"
}

for imie in znajomi:
    print('%s ma przezwisko: %s' % (imie, znajomi[imie]))
#zad 14
skroty = {
    "bd" : "bede",
    "np" : "na przyklad",
    "tb" : "tobie",
    "cb" : "ciebie"
}
znajomi = skroty.copy()
#zad 16
x = znajomi.values()
print(x.count())