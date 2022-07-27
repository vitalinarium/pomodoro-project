from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
    canvas.itemconfig(timer_text, text='00:00')
    check_label.config(text='')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global check_count
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text='Work', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))


        count_down(work_sec)
    elif reps == 8:
        timer_label.config(text='Long Break', fg=RED, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
        count_down(long_break_sec)
        check_count += 1
        check_label.config(text=check_count * '✔', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'),
                           highlightthickness=0)
    elif reps == 2 or reps == 4 or reps == 6:
        check_count +=1
        timer_label.config(text='Break', fg=PINK, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
        check_label.config(text=check_count * '✔', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'), highlightthickness = 0)
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)
#count_down(5)
timer_label = Label(text='Timer', highlightthickness=0)
timer_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=timer_reset)
reset_button.grid(column=2, row=2)

check_label = Label(text=' ', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'), highlightthickness=0)
check_label.grid(column=1, row=2)

window.mainloop()