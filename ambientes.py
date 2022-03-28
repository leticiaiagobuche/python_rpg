from random import randint

class fazenda:
    def __init__(self):
        self.espaco_livre_maximo = 6
        self.espaco_livre_minimo = 0
        self.espaco_ocupado = 0

class caverna:
    ####configurar self.tipo para modificar para 1 quando acessar tal caverna

    def __init__(self):
        self.cobre = 0
        self.ferro = 0
        self.ouro = 0
        self.carvao = 0
        self.tipo = 0

    def cav_ruim(self):
        self.cobre += randint(0, 3)
        self.ferro += randint(0, 1)
        self.carvao += randint(1,4)
        self.tipo = 0

    def cav_menos_ruim(self):
        self.cobre += randint(1,3)
        self.ferro += randint(0,3)
        self.carvao += randint(1,5)
        self.tipo = 0

    def cav_mediana(self):
        self.cobre += randint(2,5)
        self.ferro += randint(1,3)
        self.carvao += randint(2,7)
        self.tipo = 0

    def cav_boa(self):
        self.cobre += randint(0,3)
        self.ferro += randint(2,5)
        self.ouro += randint(0,2)
        self.carvao += randint(3,5)
        self.tipo = 0

    def cav_super_boa(self):
        self.cobre += randint(0,1)
        self.ferro += randint(3,5)
        self.ouro += randint(2,3)
        self.tipo = 0

    def print_atributo(self, cav):
        print(f'cobre {cav.cobre}')

class monster:
    def __init__(self):
        self.vida = 0
        self.vida_max = 0
        self.dano = 0
        self.xp = 0

    def noob(self):
        self.vida += 10
        self.vida_max += 10
        self.dano += 3
        self.xp += 2

    def medium(self):
        self.vida += 15
        self.vida_max += 15
        self.dano += 6
        self.xp += 6

    def hard(self):
        self.vida += 21
        self.vida_max += 21
        self.dano += 10
        self.xp += 12