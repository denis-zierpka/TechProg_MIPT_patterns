from tkinter import *
from app.users import player1, player2
from app import warrior

root = Tk()
root.geometry("800x500")


def start(root):
    units_list = [
        warrior.Archer,
        warrior.Horseman,
        warrior.Infantryman,
        warrior.Swordsman,
    ]
    for i in range(3):
        print("Select 1, 2, 3, 4")
        a = int(input())
        player1.add_warrior(units_list[a - 1]())
    for i in range(3):
        print("Select 1, 2, 3, 4")
        a = int(input())
        player2.add_warrior(units_list[a - 1]())

    print(player1.status())
    print(player2.status())
    root.destroy()


def play():
    mybutton = Button(root, text="Start game", padx=100, pady=100, command=lambda: start(root))
    mybutton.pack()
    root.mainloop()
