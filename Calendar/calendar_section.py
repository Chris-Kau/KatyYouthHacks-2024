import tkinter
import customtkinter
from Calendar.Day import Day
class CalendarSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


        self.sunday = Day(self, "sunday", 0)
        self.sunday.pack(side = "left")

        self.monday = Day(self, "monday", 1)
        self.monday.pack(side = "left")

        self.tuesday = Day(self, "tuesday", 2)
        self.tuesday.pack(side = "left")

        self.wednesday = Day(self, "wednesday", 3)
        self.wednesday.pack(side = "left")

        self.thursday = Day(self, "thursday", 4)
        self.thursday.pack(side = "left")

        self.friday = Day(self, "friday", 5)
        self.friday.pack(side = "left")

        self.saturday = Day(self, "saturday", 6)
        self.saturday.pack(side = "left")


        # self.sunday = Day(self, "Homework", "00:00", "DO YOUR HOMEWORK", width = 50, height = 50)
        # self.sunday.pack(padx = 10, pady = 10)


        self.pack(fill = "both", expand = True)

