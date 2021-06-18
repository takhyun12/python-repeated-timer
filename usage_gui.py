import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from repeated_timer import Repeated_Timer


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Repeated timer with Tkinter")
        self.geometry("600x250")
        self.resizable(0, 0)

        self.repeated_timer = None  # Declares a repeated_timer variable inside a Tk object.

        self.start_button = tk.Button(self, text="Start", width=30, overrelief="solid",
                                      font=('Roboto', 16, 'bold'),
                                      command=lambda: self.start_button_clicked())
        self.start_button.pack()

    def start_button_clicked(self):
        if self.start_button['text'] == 'Start':
            '''Start Event'''
            self.repeated_timer = Repeated_Timer(interval=1, duration=30, function=timer_tick,
                                                 args1='args1', args2='args2')  # Assign object to variable repeated_timer
            self.repeated_timer.start()   # Timer Start

            self.start_button['text'] = 'Stop'
            self.start_button.configure(fg='red')

        else:
            '''Stop Event'''
            self.repeated_timer.stop()  # Timer Stop

            self.start_button['text'] = 'Start'
            self.start_button.configure(fg='black')

    def closing_event(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            try:
                self.repeated_timer.stop()
            except AttributeError:
                pass
            finally:
                self.destroy()


def timer_tick(*args: tuple, **kwargs: tuple):
    # timer tick event!!
    # You can put your code in here
    print('timer tick!')


if __name__ == '__main__':
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.closing_event)
    app.mainloop()
