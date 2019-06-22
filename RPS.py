import random


mv = ['rock', 'paper', 'scissors']

s_moves = ['r', 'p', 's']


def beats(one, two):
    return ((one == 'scissors' and two == 'paper') or
            (one == 'rock' and two == 'scissors') or
            (one == 'paper' and two == 'rock'))


def c_hum_inp(s_moves):
    if s_moves == 'p':
        return 'paper'

    elif s_moves == 'r':
        return 'rock'

    else:
        return 'scissors'


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, thir_move):
        self.my_move = my_move
        self.other_move = thir_move


class RandomPlyer(Player):
    def move(self):
        return random.choice(mv)


class HumanPlyer(Player):

    def move(self):
        hum_inp = input(
            'chose (p) for paper'
            'or (r) for rock'
            'or (s) for scissors'
            'or (q) for quit')
        if hum_inp in s_moves:
            return c_hum_inp(hum_inp)
        elif hum_inp == 'q':
            return 'q'
        else:
            print ('un correct letter')
            return self.move()


class ReflectPlayer(Player):

    def __init__(self):
        super().__init__()
        self.other_move = random.choice(mv)

    def move(self):
        return self.other_move


class CyclePlayer(Player):

    def __init__(self):
        super().__init__()
        self.other_move = random.choice(mv)

    def move(self):
        if self.other_move == 'rock':
            return 'paper'

        elif self.other_move == 'paper':
            return 'scissors'

        else:
            return 'rock'


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        if (move1 == 'q') or (move2 == 'q'):
            return 'exit'
        print(f'Player1: {move1} Player2: {move2}')

        if beats(move1, move2):
            self.p1.score = self.p1.score+1
            print('player1 won')

        elif beats(move2, move1):
            self.p2.score = self.p2.score+1
            print ('player2 won')

        else:
            print('Equle')

        print (f'Score: (Player1: {self.p1.score},' +
                f'Player2: {self.p2.score})')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def player_game(self):
        print ('Game start')

        for round in range(3):
            print(f'Round {round+1}:')
            round_v = self.play_round()

            if round_v == 'exit':
                print('the end')
                break

        print ('Final Score')
        print(f'Player1 :{self.p1.score}, + Player 2: {self.p2.score}')

        if self.p1.score > self.p2.score:
            print('Player1 won')

        elif self.p1.score < self.p2.score:
            print('Player2 won')

        else:
            print('They are Equles')
        print('Game Over')


def select_comp_mode():
    comp_mode = input('chose: random, reflect, cycle as game mode')

    if comp_mode == 'random':
        return Game(HumanPlyer(), RandomPlyer())

    elif comp_mode == 'reflect':
        return Game(HumanPlyer(), ReflectPlayer())

    elif comp_mode == 'cycle':
        return Game(HumanPlyer(), CyclePlayer())

    else:
        print('indvalid')
        return select_comp_mode
if __name__ == '__main__':
    game = select_comp_mode()
    game.player_game()
