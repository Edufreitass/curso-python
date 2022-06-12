class Humano:
    # atributo de classe (estatico)
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        # atributo de instancia
        self.nome = nome

    def das_cavernas(self):
        # atributo de instancia
        self.especie = 'Homo Neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')  # Homo Sapiens
    print(f'jose.especie: {jose.especie}')  # Homo Sapiens
    print(f'grokn.especie: {grokn.especie}')  # Homo Neanderthalensis
