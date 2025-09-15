class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vetor(1, 2)
v2 = Vetor(3, 4)
print(v1 + v2)
