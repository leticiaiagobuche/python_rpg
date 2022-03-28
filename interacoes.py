import personagens
import ambientes
from random import randint


def monster_random():
    dado = randint(0,100)
    if dado < 100:
        monster_noob = ambientes.monster()
        monster_noob.noob()
        return monster_noob
    elif 51 < dado < 81:
        monster_medium = ambientes.monster()
        monster_medium.medium()
        return monster_medium
    else:
        monster_hard = ambientes.monster()
        monster_hard.hard()
        return monster_hard

def combate(player, monster):
    cat_jump = True
    print('Hora do combate!')
    while monster.vida > 0 and player.vida > 0 and cat_jump == True:
        print()
        print('***** Vez do Player *****')
        print()
        escolha_combate = input('MENU:'
                                '\nAtacar: a/A'
                                '\nHabilidades: h/H'
                                '\nMochila: m/M'
                                '\nFugir: f/F').upper()
        while escolha_combate not in ['A', 'H', 'M', 'F']:
            print('Escolha uma opção válida!')
            escolha_combate = input('MENU:'
                                '\nAtacar: a/A'
                                '\nHabilidades: h/H'
                                '\nMochila: m/M'
                                '\nFugir: f/F').upper()
        if escolha_combate == 'A':
            print('O jogador atacou o monstro!')
            monster.vida -= player.ataque
            print(f'Hit: {player.ataque}'
                  f'\nMonster: {monster.vida} / {monster.vida_max}')
        elif escolha_combate == 'H':
            skill = input('MENU:'
                  '\nGolpe fulminante: G/g').upper()
            if skill == 'G':
                monster.vida -= player.golpe_fulminante()
                print(f'Hit: {player.golpe_fulminante}'
                      f'\nMonster: {monster.vida} / {monster.vida_max}')
        elif escolha_combate == 'M':
            skill = input('MENU: ')
        elif escolha_combate == 'F':
            cat_jump = False
        print()
        print('***** Vez do Monstro *****')
        print()
        player.vida -= monster.dano
        print(f'Hit: {monster.dano}'
              f'\nPlayer: {player.vida} / {player.vida_max}')



def chance_muro(player):
    dado = randint(1,100)
    if dado < 21:
        escolha = input('Você se deparou com um muro...\n'
                         'MENU:\n'
                         'Bomba: B/b\n'
                         'Sair: S/s').upper()
        if escolha == 'B':
            if player.bomba != 0:
                print('KABUMMM!!!\n'
                      'Passagem liberada')
            else:
                print('Você não tem bombas.')
                escolha = input('Você se deparou com um muro...\n'
                                'MENU:\n'
                                'Bomba: B/b\n'
                                'Sair: S/s').upper()
                if escolha == 'S':
                    print('Você saiu da caverna.')
        elif escolha == 'S':
            print('Você saiu da caverna.')


def escolha_caverna(caverna):
    dado = randint(1,100)
    if dado < 21:
        return caverna.cav_ruim()
    elif 20 < dado < 41:
        print('cav_menos_ruim')
        return caverna.cav_menos_ruim()
    elif 40 < dado < 61:
        print('cav_mediana')
        return caverna.cav_mediana()
    elif 60 < dado > 81:
        print('cav_boa')
        return caverna.cav_boa()
    elif 80 < dado < 101:
        print('cav_super_boa')
        return caverna.cav_super_boa()


def print_fazenda(player, ambiente):
    print(f'Você possui {player.bolsa} sementes dentro da tua bolsa.'
          f'\nA fazenda possui {ambiente.espaco_livre_maximo} espaços livres.'
          f'\nA fazenda tem {ambiente.espaco_ocupado} espaços ocupados.')

def escolha_classe():
    usuario = input('Escolha qual classe quer começar:\n'
                    '\nCultivador C/c'
                    '\nMinerador M/m'
                    '\nLutador L/l').upper()

    if usuario == 'C':
        print('Você escolheu a classe cultivador!')
        jogador = personagens.cultivo()
        return jogador
    elif usuario == 'M':
        print('Você escolheu a classe minerador!')
        jogador = personagens.mineracao()
        return jogador
    elif usuario == 'L':
        print('Você escolheu a classe lutador!')
        jogador = personagens.lutador()
        return jogador
    else:
        print('Inválido, tente novamente.')












