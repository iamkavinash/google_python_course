class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b

p1 = Calc(10,15)

print(p1.add())
print(p1.sub())