from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#EF4040"
RED = "#B80000"
DARK_GREEN = "dark green"
FONT_NAME = "Courier"
GREEN = "#9bdeac"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    my_label.config(text="Timer", fg=RED)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
"""Creating the command to be triggered once the 'Start' button gets clicked"""


def start_timer():
    global reps
    reps += 1

    long_work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        my_label.config(text="Break", fg="white")

    elif reps % 2 == 0:
        countdown(short_break)
        my_label.config(text="Break", fg=PINK)

    else:
        countdown(long_work)
        my_label.config(text="Work", fg=DARK_GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
"""Creating the countdown method"""


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = (math.floor(reps / 2))
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

"""Creating screen"""
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

"""Creating canvas to put tomato image on"""
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


"""Creating 'Timer' Label"""
my_label = Label(text="Timer", fg=DARK_GREEN, bg=GREEN, font=(FONT_NAME, 50))
my_label.grid(column=1, row=0)

"""Creating 'Start' Button"""
start_button = Button(text="Start", highlightbackground=GREEN, highlightcolor=GREEN, highlightthickness=2,
                      command=start_timer, font=FONT_NAME)
start_button.grid(column=0, row=2)

"""Creating 'Reset' Button"""
reset_button = Button(text="Reset", highlightbackground=GREEN, highlightcolor=GREEN, highlightthickness=2,
                      command=reset_timer, font=FONT_NAME)
reset_button.grid(column=2, row=2)

"""Creating checkmark symbol"""
checkmark_label = Label(bg=GREEN, fg="green", font=(FONT_NAME, 30))
checkmark_label.grid(column=1, row=3)


window.mainloop()
