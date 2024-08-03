import tkinter
import customtkinter
from Calendar.Event import Event
class Day(customtkinter.CTkFrame):
    def __init__(self, master, title, time, desc, **kwargs):
        super().__init__(master, **kwargs)

        # self.day = day
        self.day = Event(self, title, time, desc)

        # self.monday = Event(self, "Homework", "00:00", "PLEASE TELL ME TO DO MY HOMEWORK")
        self.day.pack()
        

