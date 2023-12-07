from tkinter import *
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ""
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_click():
    window.after_cancel(timer)
    canvas.itemconfig(clock, text="00:00")
    timer_title.config(text="Timer", fg=GREEN)
    checks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_sec)
        timer_title.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        timer_title.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        timer_title.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    clock_formatted = time.strftime("%M:%S", time.gmtime(count))
    canvas.itemconfig(clock, text=clock_formatted)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            global mark
            mark += "✔"
            checks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
clock = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

timer_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
timer_title.grid(column=1, row=0)

start = Button(text="Start", bg="white", font=(FONT_NAME, 12, "bold"), command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg="white", font=(FONT_NAME, 12, "bold"), command=reset_click)
reset.grid(column=2, row=2)

checks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checks.grid(column=1, row=3)

window.mainloop()
