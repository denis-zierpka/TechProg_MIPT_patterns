from app.users import player1, player2
from app.warrior import WarriorList


class Game:
    def __init__(self):
        self.winner = 0

    def choose_warriors(self, player):
        for i in range(3):
            print("Select 1, 2, 3, 4")
            a = int(input())
            while a < 1 or a > 4:
                print("Error!\nSelect 1, 2, 3, 4")
                a = int(input())
            player.add_warrior(WarriorList.list[a - 1]())

    def ask_for_attack(self):
        print("Select your player (1, 2 or 3):")
        a = int(input())
        a -= 1
        while a < 0 or a > 2:
            print("Error!\nSelect your player (1, 2 or 3):")
            a = int(input())
            a -= 1
        print("Select opponents player to attack (1, 2 or 3):")
        b = int(input())
        b -= 1
        while b < 0 or b > 2:
            print("Error!\nSelect opponents player to attack (1, 2 or 3):")
            b = int(input())
            b -= 1
        return [a, b]

    def start_battle(self):
        print('Player1:')
        self.choose_warriors(player1)
        print('Player2:')
        self.choose_warriors(player2)

        while player1.has_alive_warrior() and player2.has_alive_warrior():
            c = self.ask_for_attack()
            player1.perform_attack(player2, c[0], c[1])
            print('Player2 status:')
            print(player2.player_status())

            c = self.ask_for_attack()
            player2.perform_attack(player1, c[0], c[1])
            print('Player1 status:')
            print(player1.player_status())

    def play(self):
        # implement graphics
        self.start_battle()
