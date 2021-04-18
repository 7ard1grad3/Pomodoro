import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#6DD627"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
after_id = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global marks, reps
    marks = ""
    reps = 0
    window.after_cancel(after_id)
    canvas.itemconfig(timer_canvas, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_countdown():
    global reps, marks
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        logo.config(text='LONG BREAK')
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        logo.config(text='SHORT BREAK')
    else:
        if reps > 1:
            marks += "✔"
            checkmarks.config(text=marks)
        count_down(WORK_MIN * 60)
        logo.config(text='WORK')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(secs):
    global after_id
    sec = secs % 60
    if sec in range(0, 10):
        sec = f"0{sec}"
    canvas.itemconfig(timer_canvas, text=f"{math.floor(secs / 60)}:{sec}")
    if secs > 0:
        after_id = window.after(1000, count_down, secs - 1)
    else:
        start_countdown()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)

# Text
# miles
logo = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
logo.grid(column=2, row=0)

# BG
bg = PhotoImage(file='bg.png')
canvas.create_image(150, 130, image=bg)
timer_canvas = canvas.create_text(150, 150, text='00:00', fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Start

start_btn = Button(text='Start', command=start_countdown, bg=YELLOW, fg=RED, font=(FONT_NAME, 10, "bold")
                   )
start_btn.grid(column=1, row=3)

# Reset

reset_btn = Button(text='Reset', command=reset, bg=YELLOW, fg=RED, font=(FONT_NAME, 10, "bold"))
reset_btn.grid(column=3, row=3)

#
# miles
checkmarks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
checkmarks.grid(column=2, row=5)

# canvas.pack()

window.mainloop()
