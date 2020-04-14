def lista(**klucz):
    print("Lista zakupow:\n")
    ilosc=0
    for i in klucz:
        print(i, klucz[i])
        ilosc+=klucz[i]
    print("\nSuma produktow:", ilosc)
lista(banany=5,mleko=2,cytryny=3,chleb=2)