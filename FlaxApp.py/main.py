import tkinter as tk
from style import *

# Main window
window = tk.Tk()

window.title("Harakeke Guide")
window.geometry("900x600")
window.configure(bg=BACKGROUND)


# Title
title = tk.Label(
    window,
    text="Harakeke Guide",
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

# Information for each category
category_information = {
    "Harvesting Harakeke": "Harakeke should only be harvested on public propertie. you should always cut away from yourself, and not in wet weather",
    "Preparing Harakeke": "Mattering on what youre weaving you need to prepare the Harakeke in different ways from removing the fibre or just cuting off the edge",
    "Basics to weaving": "Patterns :P will show image later",
    "Advanced weaving": "Step by step basket or flower"
}

def show_information(category):
    information.config(text=category_information[category])
    
# Main information area
information = tk.Label(
    content,
    text="Empty text to be added",
    font=BODY_FONT,
    bg=BOX_BACKGROUND,
    fg=TEXT,
    wraplength=750,
    justify="left",
    padx=20,
    pady=20
)

information.pack(fill="both", expand=True, pady=10)



# Category areas
categories = [
    "Harvesting Harakeke",
    "Preparing Harakeke",
    "Basics to weaving",
    "Advanced weaving"
]

for category in categories:

    box = tk.Button(
        content,
        text=category,
        font=BODY_FONT,
        bg=BOX_BACKGROUND,
        fg=TEXT,
        width=20,
        height=3,
        wraplength=120,
        command=lambda c=category: show_information(c)
    )

    box.pack(side="left", padx=5, pady=10)


# Start program
window.mainloop()