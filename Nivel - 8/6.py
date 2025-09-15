class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

animais = [Cachorro(), Gato()]
for a in animais:
    print(a.falar())
