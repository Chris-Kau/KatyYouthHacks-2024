import tkinter
import customtkinter
from Calendar.Day import Day
class CalendarSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.sunday = Day(self, "Homework", "00:00", "DO YOUR HOMEWORK", width = 50, height = 50)
        self.sunday.pack(padx = 10, pady = 10)


        # self.monday = Day(self, "Monday", width = 50, height = 50)
        self.pack(fill = "both", expand = True)
        # self.monday.pack(padx = 10, pady = 10)
