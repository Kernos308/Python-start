def generator(data):
    for index in range(len(data)):
        if index % 2 == 0:
            yield data[index]
        

napis = generator("Wizualizacja")
print(next(napis))
print(next(napis))
print("Danych")
print(next(napis))