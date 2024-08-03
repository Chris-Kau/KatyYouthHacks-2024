import tkinter
import customtkinter
from Calendar.Event import Event
class Day(customtkinter.CTkFrame):
    def __init__(self, master, day, **kwargs):
        super().__init__(master, **kwargs)
        self.day = day
        self.monday = Event(self, "00:00", "Homework", "PLEASE TELL ME TO DO MY HOMEWORK")
        self.monday.pack()
        

