import tkinter
import customtkinter
from Calendar.Day import Day
from datetime import datetime, timedelta

class CalendarSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # today = datetime.datetime.now()
        # week = today.strftime("%V")
        # print(week)

        # d = "2024-W31"
        # r = datetime.datetime.strptime(d + '-1', "%Y-U%U-%w") # monday date
        # print(r)

        today = datetime.now().date()
        start = today - timedelta(days=today.weekday()+1)
        week_dates = [start + timedelta(days=i) for i in range(7)]
        print(week_dates)

        for date in week_dates:
            print(date.day)
            # print(date.strftime('%d'))
        print(week_dates[0].day)


        self.sunday = Day(self, "Sunday", week_dates[0].day)
        self.sunday.pack(side = "left")

        self.monday = Day(self, "Monday", week_dates[1].day)
        self.monday.pack(side = "left")

        self.tuesday = Day(self, "Tuesday", week_dates[2].day)
        self.tuesday.pack(side = "left")

        self.wednesday = Day(self, "Wednesday", week_dates[3].day)
        self.wednesday.pack(side = "left")

        self.thursday = Day(self, "Thursday", week_dates[4].day)
        self.thursday.pack(side = "left")

        self.friday = Day(self, "Friday", week_dates[5].day)
        self.friday.pack(side = "left")

        self.saturday = Day(self, "Saturday", week_dates[6].day)
        self.saturday.pack(side = "left")


        # self.sunday = Day(self, "Homework", "00:00", "DO YOUR HOMEWORK", width = 50, height = 50)
        # self.sunday.pack(padx = 10, pady = 10)


        self.pack(fill = "both", expand = True)

