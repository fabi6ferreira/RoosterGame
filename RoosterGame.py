def menu():
    continuar = 1
    while continuar:
        continuar = int(input("## JOGO DO GALO [6x6] ##\n" +
                              "1. Começar o jogo\n" +
                              "0. Sair \n" +
                              "Escolhe uma opção: "))
        if continuar:
            game()
        else:
            print("Foi bom...\n" +
                  "Espero ver-te em breve...\n")
def game():
    jogada = 0
    
    while ganhou() == 0:
        print("\nJogador ", jogada % 2 + 1)
        exibe()
        linha  = int(input("\nQual a linha: "))
        coluna = int(input("Qual a coluna: "))
        if board[linha-1][coluna-1] == 0:
            if(jogada%2+1)==1:
                board[linha-1][coluna-1]=1
            else:
                board[linha-1][coluna-1]=-1
        else:
            print("Infelizmente essa posição já foi utilizada.\nTens que escolher outra!")
            jogada -= 1
        if ganhou():
            print("Jogador ", jogada % 2 + 1, " ganhou após ", jogada + 1, " rodadas")
        jogada += 1
        if jogada >= 64:
            print("Empate\n")
            break
def ganhou():
    # verificar linhas
    for i in range(6):
        soma = board[i][0] + board[i][1] + board[i][2] + board[i][3] + board[i][4] + board[i][5]
        if soma == 6 or soma == -6:
            return 1
    # verificar colunas
    for i in range(6):
        soma = board[0][i] + board[1][i] + board[2][i] + board[3][i] +  board[4][i] + board[5][i]
        if soma == 6 or soma == -6:
            return 1
    # verificar diagonais
    diagonal1 = board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4] + board[5][5]
    diagonal2 = board[0][5] + board[1][4] + board[2][3] + board[3][2] + board[4][1] + board[5][0]
    if diagonal1 == 6 or diagonal1 == -6 or diagonal2 == 6 or diagonal2 == -6:
        return 1
    return 0
def exibe():
    for i in range(6):
        for j in range(6):
            if board[i][j] == 0:
                print(" - ", end=' ')
            elif board[i][j] == 1:
                print("|X|", end=' ')
            elif board[i][j] == -1:
                print("|O|", end=' ')
        print()
# inicializa a matriz 6x6 a zeros
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

menu()
