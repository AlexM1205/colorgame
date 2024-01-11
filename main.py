import tkinter as tk
import random

class ColorGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Color Game")

        self.colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"]
        self.score = 0
        self.attempts = 0
        self.max_attempts = 3

        self.create_widgets()

    def create_widgets(self):
        self.instructions_label = tk.Label(self.master, text="Click on the color of the TEXT, not the word.", font=("Helvetica", 12), pady=10)
        self.instructions_label.pack()

        self.color_label = tk.Label(self.master, text="", font=("Helvetica", 24))
        self.color_label.pack(pady=20)

        self.btn_frame = tk.Frame(self.master)
        self.btn_frame.pack()

        self.buttons = []
        for color in self.colors:
            button = tk.Button(self.btn_frame, text=color, width=10, height=2, command=lambda c=color: self.check_color(c))
            button.pack(side=tk.LEFT, padx=5, pady=5)
            self.buttons.append(button)

        self.score_label = tk.Label(self.master, text="Score: 0", font=("Helvetica", 16))
        self.score_label.pack(pady=10)

        self.next_round()

    def next_round(self):
        random_color = random.choice(self.colors)
        self.color_label.config(text=random.choice(self.colors), fg=random_color.lower())
        random.shuffle(self.colors)
        self.attempts = 0

    def check_color(self, selected_color):
        correct_color = self.color_label.cget("fg")
        if selected_color.lower() == correct_color:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.next_round()
        else:
            self.attempts += 1
            if self.attempts >= self.max_attempts:
                self.game_over()
            else:
                self.instructions_label.config(text=f"Incorrect! Attempts left: {self.max_attempts - self.attempts}")

    def game_over(self):
        self.instructions_label.config(text="Game Over! Click on 'Restart' to play again.")
        for button in self.buttons:
            button.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = ColorGame(root)
    restart_button = tk.Button(root, text="Restart", command=lambda: app.__init__(root))
    restart_button.pack(pady=10)
    root.mainloop()


if __name__ == "__main__":
    main()
