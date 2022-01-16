from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#57CC99"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 37, "normal"), fg=RED, bg=YELLOW)
        count_down(long_break_secs)
    elif reps % 2 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 37, "normal"), fg=PINK, bg=YELLOW)
        count_down(short_break_secs)
    else:
        timer_label.config(text="Work", font=(FONT_NAME, 37, "normal"), fg=GREEN, bg=YELLOW)
        count_down(work_secs)
    # Add the check label
    if reps == 3 or reps == 5 or reps == 7:
        check_label.config(text="✔")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.iconphoto(False, PhotoImage(file='tomato.png'))
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 37, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=202, height=226, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(101, 113, image=image)
timer_text = canvas.create_text(113, 135, text="00:00", font=(FONT_NAME, 31, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", width=10, font=("Arial", 13, "bold"), bg="#F0D9FF", command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", width=10, font=("Arial", 13, "bold"), bg="#F0D9FF", command=reset)
reset_button.grid(column=2, row=3)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=4)

window.mainloop()
