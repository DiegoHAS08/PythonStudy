class Playlist:
    def __init__(self, nome, musicas):
        self.nome = nome
        self.musicas = musicas

    def __len__(self):
        return len(self.musicas)

p = Playlist("Rock", ["AC/DC", "Metallica", "Iron Maiden"])
print("Número de músicas:", len(p))
