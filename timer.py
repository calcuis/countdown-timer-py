from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title('Timer')
root.geometry('700x300')

sec = StringVar()
Entry(textvariable=sec, width=2, font='Calibri').place(x=330, y=120)
sec.set('00')

mins = StringVar()
Entry(textvariable=mins, width=2, font='Calibri').place(x=300, y=120)
mins.set('00')

def countdowntimer():
    times = int(mins.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)
        sec.set(second)
        mins.set(minute)

        root.update()
        time.sleep(1)
        
        if (times == 0):
            sec.set('00')
            mins.set('00')
            messagebox.showinfo("Countdown Timer", "Time's up!")
        times -= 1

Label(font=('Calibri', 22), text='Set the Timer').place(x=250, y=70)
Button(text='START', bd='2', font=('Calibri', 10), command=countdowntimer).place(x=305, y=160)

root.mainloop()
