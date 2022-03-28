from random import randint
import interacoes
import ambientes


def main():
    terreno_fazenda = ambientes.fazenda()
    terreno_caverna = ambientes.caverna()
    terreno_arena = ambientes.monster()
    print('Boas-vindas ao star dust_Game!')

    player_1 = interacoes.escolha_classe()

############################## CLASSE CULTIVADOR ##############################

    if player_1.classe == 'cultivador':
        print('Por ter escolhido ser cultivador, o teu ambiente de jogo é na fazenda.\n'
              'Você ganhou 6 grãos de café para começar a plantar!')
        player_1.semente_cafe += 6

        escolha_player_1 = input('MENU:'
                                 '\nProcurar: P/p'
                                 '\nPlantar: PL/pl'
                                 '\nRegar: R/r'
                                 '\nColher: C/c').upper()
        if escolha_player_1 == 'P':
            achados_sementes = randint(1,5)
            print(f'Você saiu para procurar sementes e encontrou: {achados_sementes}\n')
            player_1.bolsa += achados_sementes
        elif escolha_player_1 == 'PL':
            interacoes.print_fazenda(player_1,terreno_fazenda)
            escolha_semente = input(f'Bolsa:\n'
                         f'Sementes de cafe({player_1.semente_cafe}): C/c').upper()
            if escolha_semente == 'C':
                escolha_quantidade = int(input(f'Escolha quantas sementes você quer plantar.\n'
                                           'No nível 1 você tem 6 espaços livres para plantação.\n'
                                           '1 à 6 sementes'))
                terreno_fazenda.espaco_ocupado += escolha_quantidade
                print(f'Você plantou {escolha_quantidade} sementes.')
        elif escolha_player_1 == 'R':
            escolha_regador = input('Deseja regar?\n'
                                    'Sim S/s\n'
                                    'Não N/n').upper()
            if escolha_regador == 'S':
                print('Todas as plantas estão regadas')
            else:
                print('vsf')
        elif escolha_player_1 == 'C':
            print('Toda a colheita foi enviada para tua bolsa.')

############################## CLASSE MINERADOR ##############################

    elif player_1.classe == 'minerador':
        print('Por ter escolhido ser minerador, o teu ambiente de jogo é na caverna.\n'
              'Você ganhou 3 bombas ao escolher esta classe!')
        player_1.bomba += 3
        escolha_player_1 = input('MENU:'
                                 '\nMinerar: M/m').upper()

        if escolha_player_1 == 'M':
            print('Bem vindo a caverna!')
            interacoes.escolha_caverna(terreno_caverna)
            interacoes.chance_muro(player_1)
            escolha_player_1 = input('MENU:'
                                 '\nExplorar: E/e'
                                     '\nSair da caverna: S/s').upper()
            if escolha_player_1 == 'E':
                explorar = input('Você explorou ao redor e encontrou minérios...\n'
                                 'MENU:\n'
                                 'Coletar: C/c').upper()
                if explorar == 'C':
                    print('Todos minérios foram enviados para tua bolsa.')
                else:
                    print('Tente novamente.')
            elif escolha_player_1 == 'S':
                    print('Você saiu da caverna.')

############################## CLASSE LUTADOR ##############################
    elif player_1.classe == 'lutador':
        interacoes.combate(player_1, interacoes.monster_random())

# LANCAR NA SEHGUNDA FEIRA A 18H10 BLAAASSSSSSSS
#bls lança memo parça kero vê, filma tela aí tia

#WHILE 'SEM_CARINHOZINHO':
#    return OLOKO mAn



main()