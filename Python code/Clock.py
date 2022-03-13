import tkinter as tk
import time
import random


class Clock:
    colors = [ 'blue', 'green', 'black', 'orange','red', 'purple', 'brown', 'yellow', 'pink']

    def __init__(self):
        self.master = tk.Tk()
        self.color = random.choice(Clock.colors)

    def settings(self):
        self.master.title('My Clock')

    def widgets(self):
        def count_time(time1=''):
            time2 = time.strftime('%H:%M:%S')
            if time2 != time1:
                time1 = time2
                clock.config(text=time2)
                clock.after(200, count_time)

        clock = tk.Label(self.master, font=('Poppins', 40, 'bold'), background=self.color, foreground='black')
        clock.pack(anchor='center')

        count_time()
        tk.mainloop()


if __name__ == '__main__':
    my_clock = Clock()
    my_clock.settings()
    my_clock.widgets()
