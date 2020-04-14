class Kwadrat():
    def __init__(self, x):
        self.x =x
    def __add__(self,kwadrat):
        return Kwadrat(self.x + kwadrat.x)
    def __str__(self):
        return f"Kwadrat x={self.x}"
kw1 = Kwadrat(10)
kw2 = Kwadrat(20)
kw3 = kw1 + kw2
print(kw3)