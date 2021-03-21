from app.users import player1, player2
from app.warrior import WarriorList


def enter_number_mes():
    print('Enter number from 1 to 4, standing for next warriors')
    num = 1
    for i in WarriorList.list:
        print(str(num) + ' ' + i.type.value)
        num += 1
    print('-----------------')


def print_start_info():
    print('-----------------')
    print('Player1 status:')
    print(player1.player_status())
    print('-----------------')
    print('Player2 status:')
    print(player2.player_status())


class Game:
    def __init__(self):
        self.winner = 0

    def choose_warriors(self, player):
        enter_number_mes()
        for i in range(3):
            while True:
                try:
                    a = int(input())
                    if a < 1 or a > 4:
                        print("Error!")
                        continue
                    player.add_warrior(WarriorList.list[a - 1]())
                    break
                except Exception:
                    print("Error!")
                    continue

    def ask_for_attack(self, player, player_opp):
        print("Select your player (1, 2 or 3):")
        a = 0
        while True:
            try:
                a = int(input())
                a -= 1
                if a < 0 or a > 2:
                    print("Error!")
                    continue
                if not player.warriors[a].alive:
                    print('Warrior is not alive')
                    continue
                break
            except Exception:
                print("Error!")
                continue

        print("Select opponents player to attack (1, 2 or 3):")
        b = 0
        while True:
            try:
                b = int(input())
                b -= 1
                if b < 0 or b > 2:
                    print("Error!")
                    continue
                if not player_opp.warriors[b].alive:
                    print('Warrior is not alive')
                    continue
                break
            except Exception:
                print("Error!")
                continue

        return [a, b]

    def start_battle(self):
        print('Player1:\nChoose 3 warriors you would like to see in your team')
        self.choose_warriors(player1)
        print('Player2:\nChoose 3 warriors you would like to see in your team')
        self.choose_warriors(player2)

        print_start_info()

        while player1.has_alive_warrior() and player2.has_alive_warrior():
            print('-----------------')
            print('Player1, your turn')
            c = self.ask_for_attack(player1, player2)
            player1.perform_attack(player2, c[0], c[1])
            print('Player2 status:')
            print(player2.player_status())

            if not player1.has_alive_warrior() or not player2.has_alive_warrior():
                break
            print('-----------------')
            print('Player2, your turn')
            c = self.ask_for_attack(player2, player1)
            player2.perform_attack(player1, c[0], c[1])
            print('Player1 status:')
            print(player1.player_status())

        if player1.has_alive_warrior():
            print('Player1 won!')
        else:
            print('Player2 won!')

    def play(self):
        # implement graphics
        self.start_battle()
