# Importa a biblioteca RANDOM inteira
import random

# "func_desenhaTabuleiro" = desenha o tabuleiro na tela para o jogador ver antes de escolher sua posição de jogada
def func_desenhaTabuleiro(ex_lista_1a9):
    # Imprime a placa que foi aprovada.
    # "ex_lista_1a9" é uma lista de preenchimento exemplificado que contém 10 strings que representam o tabuleiro (ignorando o índice 0)
    print(' --- --- ---')
    print('| ' + ex_lista_1a9[1] + ' | ' + ex_lista_1a9[2] + ' | ' + ex_lista_1a9[3] + ' |')
    print(' --- --- ---')
    print('| ' + ex_lista_1a9[4] + ' | ' + ex_lista_1a9[5] + ' | ' + ex_lista_1a9[6] + ' |')
    print(' --- --- ---')
    print('| ' + ex_lista_1a9[7] + ' | ' + ex_lista_1a9[8] + ' | ' + ex_lista_1a9[9] + ' |')
    print(' --- --- ---')

# "func_quemVaiPrimeiro" = escolhe aleatoriamente quem vai começar a jogar primeiro
def func_quemVaiPrimeiro():
    # Gera um numero aleatoriamente (ou 0 ou 1)
    if random.randint(0, 1) == 0:
        return 'COMPUTADOR'
    else:
        return 'JOGADOR'

# "func_jogarDeNovo" =  retorna "TRUE" se o jogador quiser jogar novamente, caso contrário, ela retorna "FALSE".
def func_jogarDeNovo():
    print('Você quer jogar de novo [SIM ou NÃO]? ')
    return input().lower().startswith('s')

# "func_fazMovimentoNoTabuleiro" = na posicao escolhida pelo jogador (PC ou JOGADOR), no índice escolhido da lista "ex_lista_1a9", o valor é substituido
# por X ou O (conforme quem estiver jogando)
def func_fazMovimentoNoTabuleiro(ex_lista_1a9, ex_letraJogador, ex_posicaoEscolhida):
    ex_lista_1a9[ex_posicaoEscolhida] = ex_letraJogador.upper()

def func_VerificaSeJaGanhou(ex_lista_1a9, ex_letraPCouJogador):
    # Dado a "ex_lista_1a9" e a "letraJogador", esta função retorna "True" se esse jogador (PC ou JOGADOR) ganhou.
    return ((ex_lista_1a9[7] == ex_letraPCouJogador and ex_lista_1a9[8] == ex_letraPCouJogador and ex_lista_1a9[9] == ex_letraPCouJogador) or  # Linha de cima (horizontal)
            (ex_lista_1a9[4] == ex_letraPCouJogador and ex_lista_1a9[5] == ex_letraPCouJogador and ex_lista_1a9[6] == ex_letraPCouJogador) or  # Linha do meio (horizontal)
            (ex_lista_1a9[1] == ex_letraPCouJogador and ex_lista_1a9[2] == ex_letraPCouJogador and ex_lista_1a9[3] == ex_letraPCouJogador) or  # Linha de baixo (horizontal)
            (ex_lista_1a9[7] == ex_letraPCouJogador and ex_lista_1a9[4] == ex_letraPCouJogador and ex_lista_1a9[1] == ex_letraPCouJogador) or  # Coluna da esquerda (vertical)
            (ex_lista_1a9[8] == ex_letraPCouJogador and ex_lista_1a9[5] == ex_letraPCouJogador and ex_lista_1a9[2] == ex_letraPCouJogador) or  # Coluna do meio (vertical)
            (ex_lista_1a9[9] == ex_letraPCouJogador and ex_lista_1a9[6] == ex_letraPCouJogador and ex_lista_1a9[3] == ex_letraPCouJogador) or  # Coluna da direita (vertical)
            (ex_lista_1a9[7] == ex_letraPCouJogador and ex_lista_1a9[5] == ex_letraPCouJogador and ex_lista_1a9[3] == ex_letraPCouJogador) or  # Diagonal
            (ex_lista_1a9[9] == ex_letraPCouJogador and ex_lista_1a9[5] == ex_letraPCouJogador and ex_lista_1a9[1] == ex_letraPCouJogador))    # Diagonal

# "func_duplicaTabuleiro" = faz uma cópia da lista "lista_1a9" (passada via parametro de chamada da funcão) e devolve a lista
def func_duplicaTabuleiro(ex_lista_1a9):
    lista_Duplicada1a9 = []

    # .append adiciona o valor atual da variavel "i" no final da lista "lista_Duplicada1a9" (que foi criada em branco, logo acima) e a variavel "i"
    # vai sendo incrementada de +1 a cada interação no FOR. Ao final de todas as intereção do FOR (delimitado por "for i in ex_lista_1a9", teremos
    # o seguinte:
    for i in ex_lista_1a9:
        lista_Duplicada1a9.append(i)
    return lista_Duplicada1a9

# "func_seNaoTemEspacoVazio" = retorna "TRUE" se NÃO houver espaço vazio na posicão informada.
def func_seNaoTemEspacoVazio(ex_lista_1a9, ex_posicaoEscolhida):
    return (ex_lista_1a9[ex_posicaoEscolhida] == 'X' or ex_lista_1a9[ex_posicaoEscolhida] == 'O')

# "func_posicaoEscolhidaJogador" = jogador escolhe o numero da sua jogada (seu movimento no tabuleiro)
def func_posicaoEscolhidaJogador(ex_lista_1a9):
    posicaoEscolhida = input('\n{} - Posição: '.format(nomeLido))
    # Valida se o que o jogador digitou no teclado um número no intervalo de 1 a 9
    while posicaoEscolhida not in '1 2 3 4 5 6 7 8 9'.split() or func_seNaoTemEspacoVazio(ex_lista_1a9, int(posicaoEscolhida)):
        if int(posicaoEscolhida)<1 or int(posicaoEscolhida)>9:
            print('Posição inválida.')
            posicaoEscolhida = input('\n{} - Posição: '.format(nomeLido))
        else:
            # Valida se a posicao escolhida já está em uso ou não (se já é X ou O)
            print('Posição já foi jogada.')
            posicaoEscolhida = input('\n{} - Posição: '.format(nomeLido))
    return int(posicaoEscolhida)


'''' "func_pcEscolheAleatoriamenteMovimentoNaLista" = retorna o movimento escolhido e validado [1-9] da lista "lista_1a9"
ou retorna "nulo(null)" se não houver um numero de movimento válido. '''


def func_pcEscolheAleatoriamenteMovimentoNaLista(ex_lista_1a9, ex_lista_cantos):
    # Cria a lista vazia "lista_movimentosPossiveis"
    lista_movimentosPossiveis = []

    for i in ex_lista_cantos:
        if not func_seNaoTemEspacoVazio(ex_lista_1a9, i):
            lista_movimentosPossiveis.append(i)

    if len(lista_movimentosPossiveis) != 0:
        return random.choice(lista_movimentosPossiveis)
    else:
        return None

# "func_obterMovimentoPC =  dado a lista (de 1 a 9) e a letra do computador, determine onde mover e retornar esse movimento.
def func_obterMovimentoPC(ex_lista_1a9, ex_letraPC):

    # A partir daqui começa a implementação do algoritmo de que implementa a inteligência artificial (AI) no jogo da velha

    # Primeiro, verificar se dá pra ganhar no próximo movimento
    for i in range(1, 10):
        # "func_duplicaTabuleiro" = faz uma cópia da lista "lista_1a9" e retorna pela função essa lista duplicada e adiciona a variavel
        # que agora é uma lista, chamada "lista_duplicada_1a9"
        lista_duplicada_1a9 = func_duplicaTabuleiro(lista_1a9)
        # "func_seNaoTemEspacoVazio" = retorna "TRUE" se NÃO houver espaço vazio na posicão informada.
        if not func_seNaoTemEspacoVazio(lista_duplicada_1a9, i):
            # "func_fazMovimentoNoTabuleiro" = faz o movimento no tabuleiro, substitui na posicao escolhida por X ou O
            func_fazMovimentoNoTabuleiro(lista_duplicada_1a9, letraPC, i)
            if func_VerificaSeJaGanhou(lista_duplicada_1a9, letraPC):
                return i

    # Verifique se o "jogador" pode ganhar no próximo movimento. Caso sim, bloqueie-o.
    for i in range(1, 10):
        lista_duplicada_1a9 = func_duplicaTabuleiro(lista_1a9)
        # "func_seNaoTemEspacoVazio" = retorna "TRUE" se NÃO houver espaço vazio na posicão informada.
        if not func_seNaoTemEspacoVazio(lista_duplicada_1a9, i):
            func_fazMovimentoNoTabuleiro(lista_duplicada_1a9, letraJogador, i)
            if func_VerificaSeJaGanhou(lista_duplicada_1a9, letraJogador):
                return i

    # Tentar tomar um dos cantos, se eles estiverem livres.
    posicaoEscolhida = func_pcEscolheAleatoriamenteMovimentoNaLista(lista_1a9, [1, 3, 7, 9])
    if posicaoEscolhida != None:
        return posicaoEscolhida

    # Tentar tomar o centro, se estiver livre.
    if not func_seNaoTemEspacoVazio(lista_1a9, 5):
        return 5

    # Mover-se para um dos lados.
    return func_pcEscolheAleatoriamenteMovimentoNaLista(ex_lista_1a9, [2, 4, 6, 8])

print('\n### Bem vindo ao Jogo da Velha ###\n')

while True:
    # Reinicia a lista ("ex_lista_1a9") de posições
    nomeLido = input('Nome do Jogador: ')
    lista_1a9 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letraJogador = 'X'
    letraPC = 'O'
    deuEmpate = 0
    vez = func_quemVaiPrimeiro()
    print('\nO {} vai começar primeiro.\n '.format(vez))
    continuarJogando = True

    while continuarJogando:
        if vez == 'JOGADOR':
            # func_desenhaTabuleiro = mostra o tabuleiro
            func_desenhaTabuleiro(lista_1a9)
            # posicaoEscolhida recebe a posição escolhida (e validada) pelo jogador no tabuleiro
            posicaoEscolhida = func_posicaoEscolhidaJogador(lista_1a9)
            ''' chama a função func_fazMovimentoNoTabuleiro e passa os parametros (lista de posicoes (de 1 a 9),
            a lera do jogador ( letra do Jogador = X) e a posicao escolhida (de 1 a 9) e isso faz com que a letra 
            X (do jogador) seja colocado na posicao escohida (de 1 a 9) da lista de posicoes do tabuleiro'''
            func_fazMovimentoNoTabuleiro(lista_1a9, letraJogador, posicaoEscolhida)
            ''' a "função func_VerificaSeJaGanhou" verifica todas as possibilidades onde o jogo possa ser ganho pelo jogador
            (horizontal, vertical e diagonal) '''
            if func_VerificaSeJaGanhou(lista_1a9, letraJogador):
                # se o jogador ganhou, faça:
                func_desenhaTabuleiro(lista_1a9)
                print('\nVocê venceu.\n')
                continuarJogando = False
            # se o jogador NÃO ganhou (ou seja o retorno da função "func_VerificaSeJaGanhou == False", faça:
            else:
                deuEmpate+=1
                if deuEmpate>=9:
                    # mostra o tabuleiro cheio na tela
                    func_desenhaTabuleiro(lista_1a9)
                    print('\nEmpate.\n')
                    # sai das condicionais e pergunta se o jogador quer continuar jogando o jogo
                    break
                # se não deu empate, é a vez do PC jogar
                else:
                    vez = 'COMPUTADOR'

        # vez do PC jogar porque a condicional "if vez == 'jogador':" deu FALSO
        else:
            ''' Invoca a funçao "func_obterMovimentoPC" que é uma complexa função que chama outras funções dentro de sí
            para dar o resultado final = retorna X ou O para armazenar na variavel "posicaoEscolhida" '''
            posicaoEscolhida = func_obterMovimentoPC(lista_1a9, letraPC)
            print('Computador - Posição: {}\n'.format(posicaoEscolhida))
            func_fazMovimentoNoTabuleiro(lista_1a9, letraPC, posicaoEscolhida)

            if func_VerificaSeJaGanhou(lista_1a9, letraPC):
                func_desenhaTabuleiro(lista_1a9)
                print('\nComputador venceu.\n')
                continuarJogando = False
            else:
                deuEmpate=deuEmpate+1
                if deuEmpate>=9:
                    func_desenhaTabuleiro(lista_1a9)
                    print('\nEmpate.\n')
                    break
                else:
                    vez = 'JOGADOR'

    if not func_jogarDeNovo():
        break