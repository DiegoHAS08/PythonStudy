class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar(self, nome, telefone):
        self.contatos[nome] = telefone

    def listar(self):
        for nome, tel in self.contatos.items():
            print(f"{nome}: {tel}")

agenda = Agenda()
agenda.adicionar("Ana", "1111-2222")
agenda.adicionar("Bruno", "3333-4444")
agenda.listar()
