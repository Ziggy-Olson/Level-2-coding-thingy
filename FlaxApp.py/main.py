import tkinter as tk
from style import *

# Main window
window = tk.Tk()

window.title("Harakeke Guide")
window.geometry("900x600")
window.minsize(900, 600)
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
    text="Welcome to the Harakeke Guide, Learn about harakeke and how it can be prepared and used for weaving. Select a category below to get started.",
    font=BODY_FONT,
    bg=BOX_BACKGROUND,
    fg=TEXT,
    wraplength=750,
    justify="left",
    padx=20,
    pady=20
)

information.pack(fill="both", expand=True, pady=10)

#Home button
def show_home():
    information.config(
        text="Welcome to the Harakeke Guide\n\n"
             "Learn about harakeke and how it can be prepared "
             "and used for weaving.\n\n"
             "Select a category below to get started."
    )
home_button = tk.Button(
    content,
    text="Home",
    font=BODY_FONT,
    bg=BUTTON_BACKGROUND,
    fg=TEXT,
    width=12,
    height=2,
    command=show_home
)

home_button.pack(pady=5)

# Category areas
categories = [
    "Harvesting Harakeke",
    "Preparing Harakeke",
    "Basics to weaving",
    "Advanced weaving"
]
# Category buttons
for category in categories:

    box = tk.Button(
        content,
        text=category,
        font=BODY_FONT,
        bg=BUTTON_BACKGROUND,
        activebackground=BUTTON_ACTIVE,
        fg=TEXT,
        width=20,
        height=3,
        wraplength=120,
        command=lambda c=category: show_information(c)
    )

    box.pack(side="left", padx=5, pady=10)


# Start program
window.mainloop()