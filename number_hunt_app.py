import tkinter as tk
import random

BG = "#121212"
CARD = "#1e1e1e"
ACCENT = "#4CAF50"
TEXT = "#ffffff"

secret = None
attempts = 0
max_num = 0

def start(level):
    global secret, attempts, max_num
    settings = {
        "Easy": (20, 6),
        "Medium": (50, 7),
        "Hard": (100, 8)
    }
    max_num, attempts = settings[level]
    secret = random.randint(1, max_num)
    status.config(text=f"Guess 1–{max_num}\nAttempts: {attempts}")
    entry.delete(0, tk.END)

def guess():
    global attempts
    if secret is None:
        return

    value = entry.get()
    if not value.isdigit():
        status.config(text="❌ Enter a number")
        return

    value = int(value)
    attempts -= 1

    if value < secret:
        status.config(text=f"⬇ Too low | Attempts: {attempts}")
    elif value > secret:
        status.config(text=f"⬆ Too high | Attempts: {attempts}")
    else:
        status.config(text="🎉 YOU WIN!")
        return

    if attempts == 0:
        status.config(text=f"💀 Game over! Number was {secret}")

# Window
root = tk.Tk()
root.title("Number Hunt")
root.geometry("380x360")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(root, text="🎮 Number Hunt", font=("Segoe UI", 20, "bold"),
         bg=BG, fg=ACCENT).pack(pady=15)

card = tk.Frame(root, bg=CARD)
card.pack(padx=20, pady=10, fill="both", expand=True)

btn_frame = tk.Frame(card, bg=CARD)
btn_frame.pack(pady=10)

for i, level in enumerate(["Easy", "Medium", "Hard"]):
    tk.Button(
        btn_frame, text=level, width=8,
        bg=ACCENT, fg="black",
        activebackground="#66ff99",
        command=lambda l=level: start(l)
    ).grid(row=0, column=i, padx=6)

entry = tk.Entry(card, justify="center", font=("Segoe UI", 14))
entry.pack(pady=15)

tk.Button(card, text="Guess", bg=ACCENT, fg="black",
          font=("Segoe UI", 12),
          command=guess).pack()

status = tk.Label(card, text="Choose a difficulty",
                  bg=CARD, fg=TEXT, wraplength=300)
status.pack(pady=20)

root.mainloop()
