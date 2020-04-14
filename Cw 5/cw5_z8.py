class Samogloski:
    def __init__(self, x):
        self.x = x
        self.ix = -1
        self.wynik = isinstance(self.x, str)
        self.slowo =[]

    def __iter__(self):
        return self

    def __next__(self):
        if self.wynik:
            self.ix = self.ix + 1

            if self.x[self.ix] == "a" or self.x[self.ix] == "e" or self.x[self.ix] == "i"\
                or self.x[self.ix] == "o" or self.x[self.ix] == "u" or self.x[self.ix] == "y":

                self.slowo.append(self.x[self.ix])

        else:
            print("Podaj string")
            raise StopIteration
        return self.slowo       
slowo = Samogloski("daikwdaoiid")
print(next(slowo))
print(next(slowo))
print(next(slowo))
print(next(slowo))
print(next(slowo))
print(next(slowo))
print(next(slowo))
print(next(slowo))
print(next(slowo))
print(next(slowo))
print(next(slowo))