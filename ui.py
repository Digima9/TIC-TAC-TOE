import tkinter as tk
import random


class InterFace:
    def __init__(self):
        self.characters = ["X", "O"]
        self.buttons = [["", "", ""],
                        ["", "", ""],
                        ["", "", ""]]

        self.player = random.choice(self.characters)
        self.stop_game = False
        self.window = tk.Tk()
        self.window.geometry("680x720")
        self.window.title("TIC_TAC_TOE")
        self.window.configure(background="white")

        self.label = tk.Label(width=50, height=5, background="white", text="Welcome to TIC-TAK-TOE Game", fg="black", font=("Helvetica", "20"))
        self.label.grid(column=0, row=0, columnspan=3)

        self.new_game_button = tk.Button(text="Start Game", padx=10, pady=10, command=self.start_restart)
        self.new_game_button.grid(column=0, row=1, columnspan=3, pady=5)
        self.window.mainloop()

    def start_restart(self):
        #   creating the buttons
        for i_row in range(3):
            for j_col in range(3):
                self.buttons[i_row][j_col] = tk.Button(
                    height=3, width=3, padx=60, pady=30,
                    font=("Helvetica", "30"),
                    command=lambda row=i_row, column=j_col: self.clicked_button(row, column))
                self.buttons[i_row][j_col].grid(row=i_row+2, column=j_col, padx=10, pady=2)

                self.stop_game = False
                self.label.configure(text=f"Player {self.player}'s Turn")
                self.new_game_button.configure(text="New Game")

    def clicked_button(self, row, column):
        if self.player == "X" and self.stop_game == False:
            self.buttons[row][column].configure(text="X")
            self.buttons[row][column] = 'X'
            self.player = 'O'
            self.label.configure(text=f"Player {self.player}'s Turn")
            print(self.is_empty_spaces())

        elif self.player == 'O' and self.stop_game == False:
            self.buttons[row][column].configure(text="O")
            self.buttons[row][column] = "O"
            self.player = "X"
            self.label.configure(text=f"Player {self.player}'s Turn")
            print(self.is_empty_spaces())

        self.check_if_win()

    def check_if_win(self):

        for i in range(3):
            # vertical check
            if self.buttons[i][0] == self.buttons[i][1] == self.buttons[i][2]:
                self.stop_game = True
                self.label.configure(text=f"Player {self.buttons[i][0]}'s Won", font=("Helvetica", "20"))
            # horizontal check
            elif self.buttons[0][i] == self.buttons[1][i] == self.buttons[2][i]:
                self.stop_game = True
                self.label.configure(text=f"Player {self.buttons[0][i]}'s Won", font=("Helvetica", "20"))
            # crosscheck 1
            elif self.buttons[0][0] == self.buttons[1][1] == self.buttons[2][2]:
                self.stop_game = True
                self.label.configure(text=f"Player {self.buttons[0][0]}'s Won", font=("Helvetica",  "20"))
            # crosscheck 2
            elif self.buttons[0][2] == self.buttons[1][1] == self.buttons[2][0]:
                self.stop_game = True
                self.label.configure(text=f"Player {self.buttons[0][2]}'s Won", font=("Helvetica",  "20"))

            # elif (self.buttons[0][0] and self.buttons[0][1] and self.buttons[0][2]
            #       and self.buttons[1][0] and self.buttons[1][1] and self.buttons[1][2]
            #       and self.buttons[2][0] and self.buttons[2][1] and self.buttons[2][2] != ""):
            #     self.stop_game = True
            #     self.label.configure(text=f"DRAW", font=("Helvetica", "20"))

            # Draw check
            elif not self.is_empty_spaces():
                self.stop_game = True
                self.label.configure(text=f"DRAW", font=("Helvetica", "20"))

    def is_empty_spaces(self):
        spaces = 9
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column] == "O" or self.buttons[row][column] == "X":
                    spaces -= 1
        if spaces == 0:
            return spaces
        else:
            return spaces














