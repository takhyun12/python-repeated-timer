import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from repeated_timer import Repeated_Timer


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Repeated timer with Tkinter")
        self.geometry("530x200")
        self.resizable(0, 0)

        self.repeated_timer = None  # Declares a repeated_timer variable inside a Tk object.

        self.label = tk.Label(self, text=f"타이머 테스트")
        self.label.grid(column=0, row=0, sticky="", padx=(80, 0), pady=(30, 0))

        self.start_button = tk.Button(self, text="Start", width=30, overrelief="solid",
                                      font=('Roboto', 16, 'bold'),
                                      command=lambda: self.start_button_clicked())
        self.start_button.grid(column=0, row=2, sticky="", padx=(80, 0), pady=(30, 0))

    def start_button_clicked(self):
        if self.start_button['text'] == 'Start':
            '''Start Event'''
            self.repeated_timer = Repeated_Timer(interval=1, duration=30, function=timer_tick,
                                                 label=self.label)  # Assign object to variable repeated_timer
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


def timer_tick(*args: tuple, **kwargs: dict):
    # timer tick event!!
    # You can put your code in here
    # print('timer tick!', args, kwargs)
    kwargs['label'].configure(text=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.closing_event)
    app.mainloop()
