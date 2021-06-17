import datetime
import tkinter as tk  # GUI
from tkinter import ttk  # GUI
from tkinter import messagebox # GUI

from repeated_timer import Repeated_Timer

class AppGui(tk.Tk):
    def __init__(self):
        """ GUI Setting Starts Here """
        super().__init__()  # Inheritance from tkinter class
        self.title("Timer Sample")
        self.geometry("600x100")
        self.resizable(0, 0)

        self.start_button = tk.Button(self, overrelief="solid", width=15, text="Start", repeatdelay=1000, repeatinterval=100,
                                 command=lambda: self.start_button_clicked())
        self.start_button.grid(column=0, row=3)
        """ GUI Setting Ends Here """

    def start_button_clicked(self):
        # If Tick Starts, start a new thread
        if self.start_button['text'] == 'Start':
            # Set Timer
            self.repeated_timer = Repeated_Timer(interval=1, duration=30, function=self.timer_tick_event, args1='args1', args2='args2')
            self.repeated_timer.start()

            self.start_button['text'] = 'Stop'
            self.start_button.configure(fg='red')

        # If Tick Stopped, initialize everything
        # + Once variables are initialized, pre-exist thread will be stopped automatically
        else:
            self.repeated_timer.stop()

            self.start_button['text'] = 'Start'
            self.start_button.configure(fg='black')

    def timer_tick_event(self, *args: tuple, **kwargs: tuple):
        print('timer tick!\t', datetime.datetime.now())

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.repeated_timer.stop()
            self.destroy()

if __name__ == '__main__':
    app = AppGui()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()  # execute GUI
