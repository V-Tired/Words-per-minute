from tkinter import *
import random
from text import excerpts

"""A GUI application that counts words per minute based on accuracy compared to the displayed text."""


# Colors and Fonts
LIGHT = "#CDC2A5"
LGR = "#B5CB99"
DGR = "#5F6F52"
WHT = "#F3EEEA"
FONT = ("futura", 18, "normal")
FONT2 = ("futura", 18, "bold")
FONT_T = ("futura", 24, "bold")

timer = None
text = random.choice(excerpts)


def start():
    """On button press, creates the textbox and the test words then displays them on screen. Starts timer."""
    textbox.grid(column=1, row=3, padx=20, pady=20)
    textbox.focus()
    test_words.grid(column=1, row=2, padx=20, pady=20)

    test_words.config(text=text)
    count_down(60)


def reset():
    """Resets the timer and the text boxes."""
    window.after_cancel(timer)
    global text
    text = random.choice(excerpts)
    canvas.itemconfig(timer_text, text=f"00:00")
    wpm.grid_forget()
    textbox.delete("1.0", "end-1c")
    textbox.grid_forget()
    test_words.grid_forget()


def stop():
    """At timer's end, compares typed words to those in the excerpt for accuracy."""
    correct_words = 0
    words = textbox.get("1.0", "end-1c").strip().split(" ")
    for word in words:
        if word in text:
            correct_words += 1
    words = len(words)
    wpm.grid(column=1, row=4, padx=20, pady=20)
    wpm.config(text=f"Word Accuracy: {correct_words}\nWords per minute: {words}")


def count_down(count):
    """Counts down a minute and displays it on screen"""
    minutes = count//60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        stop()


# Window & Canvas Config
window = Tk()
window.minsize(950, 600)
window.config(bg=LIGHT)
canvas = Canvas(bg=LIGHT, highlightthickness=0, height=80, width=80)
timer_text = canvas.create_text(40, 40, text="00:00", fill=DGR, font=FONT_T)
canvas.grid(column=1, row=1)
window.columnconfigure(1, weight=1)


# Labels and Textbox
welcome = Label(text="Test Your Words Per Minute", bg=DGR, fg=LGR, font=FONT2, padx=20, pady=10)
welcome.grid(column=1, row=0, padx=20, pady=20)

wpm = Label(text="", bg=DGR, fg=LIGHT, font=FONT2, padx=20, pady=10)
test_words = Label(text="", bg=LIGHT, fg="black", font=("futura", 12, "normal"),)

textbox = Text(width=60, height=10, bg=WHT, fg="black", font=("futura", 12, "normal"), relief="sunken", wrap=WORD,)

# Buttons
start_button = Button(text="Start", bg=DGR, fg=LGR, font=FONT2, command=start)
start_button.grid(column=0, row=1, padx=20, pady=20)

stop_button = Button(text="Reset", bg=DGR, fg=LGR, font=FONT2, command=reset)
stop_button.grid(column=2, row=1, padx=20, pady=20)

window.mainloop()
