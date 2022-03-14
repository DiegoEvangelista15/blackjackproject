import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start = input('Voce gostaria de jogar o Blackjack? Escreva "s" ou "n".\n')

my_hand = []
op_hand = []


def add_card(hand):
    x = hand.append(random.choice(cards))
    return x


def op_game():
    add_card(op_hand)
    my_sum = sum(my_hand)
    op_sum = sum(op_hand)
    while op_sum < 17:
        add_card(op_hand)
        op_sum = sum(op_hand)
    else:
        print(f'Sua mao tem: {my_hand}\nMao do computador: {op_hand}')
        if my_sum > 21:
            print(f'Voce ESTOUROU, sua mao de {my_sum} e maior que 21')
        elif op_sum > 21:
            print(f'O computador ESTOROU e voce VENCEU com a mao de {my_hand} que soma {my_sum}, '
                  f'pois o adversario tinha uma mao de {op_hand}'
                  f' e uma soma de {op_sum}')
        elif my_sum > op_sum:
            print(f'Voce VENCEU com a mao de {my_hand} que soma {my_sum}, pois o adversario tinha uma mao de {op_hand}'
                  f' e uma soma de {op_sum}')
        else:
            print(f'Voce PERDEU com a mao de {my_hand} que soma {my_sum}, pois o adversario tinha uma mao de {op_hand}'
                  f' e uma soma de {op_sum}')


stop_play = False

if start == 's':
    add_card(my_hand)
    add_card(my_hand)
    add_card(op_hand)
    print(f'Sua mao tem: {my_hand}\nPrimeira carta do computador: {op_hand[0]}')
    choice = input('Digite "s" para comprar outra carta, ou "n" para para parar.\n')
    if choice == "s":
        while stop_play == False:
            add_card(my_hand)
            print(f'Sua mao tem: {my_hand}\nPrimeira carta do computador: {op_hand[0]}')
            choice = input('Digite "s" para comprar outra carta, ou "n" para para parar.\n')
            if choice == "n":
                stop_play = True
        op_game()
    elif choice == "n":
        op_game()
else:
    print('Fim de jogo!!!!')
