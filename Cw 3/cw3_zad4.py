def monotonicznosc(a,b):
    if a>0:
        print("Rosnaca")
    elif a==0:
        print("Stala")
    else:
        print("Malejaca")
x=int(input('Podaj a: '))
y=int(input('Podaj b: '))
a = monotonicznosc
a(x, y)
