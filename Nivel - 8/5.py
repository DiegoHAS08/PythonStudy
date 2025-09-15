class Nadador:
    def nadar(self):
        print("Está nadando.")

class Corredor:
    def correr(self):
        print("Está correndo.")

class TriAtleta(Nadador, Corredor):
    pass

t = TriAtleta()
t.nadar()
t.correr()
