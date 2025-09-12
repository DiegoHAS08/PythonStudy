class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som indefinido")

class Cachorro(Animal):
    def falar(self):
        print("Au Au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

dog = Cachorro("Rex")
cat = Gato("Mimi")

dog.falar()
cat.falar()
