class cultivo:
    def __init__(self):
        self.classe = 'cultivador'
        self.enxada = 0
        self.regador = 0
        self.espantalho = 0
        self.nivel_cultivador = 0
        self.bolsa = 0
        self.bolsa_max = 15
        self.semente_cafe = 0
        self.moeda = 0
        self.bau = 0


class mineracao:
    def __init__(self):
        self.classe = 'minerador'
        self.picareta = 1
        self.bomba = 0
        self.nivel_minerador = 0
        self.carrinho = 0
        self.lanterna = 1
        self.bolsa = self.bomba + self.picareta + self.lanterna
        self.bolsa_max = 15
        self.moeda = 0
        self.bau = 0

class lutador:
    def __init__(self):
        self.classe = 'lutador'
        self.saude = 3
        self.forca = 3
        self.ataque = self.forca * 1
        self.defesa = self.saude * 2
        self.vida = self.saude * 5
        self.vida_max = self.saude * 5
        self.nivel_lutador = 1
        self.bolsa = 0
        self.bolsa_max = 15
        self.moeda = 0
        self.bau = 0
        self.bau_max = 50
        self.xp = self.nivel_lutador * 20

    def golpe_fulminante(self):
        dano = self.ataque * 2
        self.vida -= 2
        print(f'Você usou o golpe fulminante!'
              f'\nHit: {dano}')
        return dano


class armazem:
    def __init__(self):
        self.bau = 0
        self.bau_max = 50
