class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True → só existe uma instância
