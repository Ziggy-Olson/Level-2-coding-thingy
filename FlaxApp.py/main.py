import tkinter as tk
from style import *

# Main window
window = tk.Tk()

window.title("Flax / Harakeke Guide")
window.geometry("900x600")
window.configure(bg=BACKGROUND)


# Title
title = tk.Label(
    window,
    text="Flax / Harakeke Guide",
    font=TITLE_FONT,
    bg=BACKGROUND,
    fg=TEXT
)

title.pack(pady=20)


# Main content area
content = tk.Frame(
    window,
    bg=BACKGROUND
)

content.pack(fill="both", expand=True, padx=30, pady=10)


# Main information area
information = tk.Label(
    content,
    text="Empty text to be added",
    font=BODY_FONT,
    bg=BOX_BACKGROUND,
    fg=TEXT,
    width=50,
    height=10
)

information.pack(pady=10)


# Category areas
categories = [
    "Empty text to be added",
    "Empty text to be added",
    "Empty text to be added",
    "Empty text to be added"
]

for category in categories:

    box = tk.Label(
        content,
        text=category,
        font=BODY_FONT,
        bg=BOX_BACKGROUND,
        fg=TEXT,
        width=25,
        height=3
    )

    box.pack(side="left", padx=5, pady=10)


# Start program
window.mainloop()