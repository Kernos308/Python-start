#zad 1
# a = input("Podaj dowolne zdanie\n")
# print(a.count(" "))


#zad 2
import sys

# print("Podaj dwie liczby calkowite")
# a = int(sys.stdin.readline())
# b = int(sys.stdin.readline())
# c = a*b
# c = str(c)
# sys.stdout.write(c)


#zad 4

# a = input("Podaj liczbę:")
# a = int(a)
# print(abs(a))


#zad 5


# a = input("Podaj pierwsza liczbe: ")
# b = input("Podaj druga liczbe: ")
# c = input("Podaj trzecia liczbe: ")

# a = int(a)
# b = int(b)
# c = int(c)

# if a>0 and a<=0 and a>b:
#     print(str(a) + "jest w przedziale (0, 10> i jest wieksze od" + str(b))
# elif b>c:
#     print("Komunikat 2")
# else:
#     print("Komunikat 3")



# zad 6



for x in range(5, 105, 5):
    print(str(x) + " ")

#zad 7

a = input("Podaj kilka liczb: ")
a = list(a)
for x in a:
    if x == " ":
        a.remove(" ")

for x in a:
    x= int(x)
    b = x*x
    print(str(b) + " ")
