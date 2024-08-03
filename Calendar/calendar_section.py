import tkinter
import customtkinter as ctk
from Calendar.Day import Day
from datetime import datetime, timedelta

class CalendarSection(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        hei = self.winfo_screenheight()
        # square = ctk.CTkFrame(self, width=50, height=50)
        # square.pack(side="top")


        # time of day ----------------------------
        self.time = ctk.CTkFrame(master=self, width=50, height=hei)
        self.time.pack(side = "left")

        def get_times_list():
            times = []
            # Start from 12:00 AM
            current_time = datetime.strptime("12:00 AM", "%I:%M %p")
            
            # Collect times in a 24-hour period
            for _ in range(24):
                times.append(current_time.strftime("%I:%M %p"))
                # Move to the next hour
                current_time += timedelta(hours=1)
            
            return times
        
        times_list = get_times_list()
        # Create and place labels in the frame
        label = ctk.CTkLabel(self.time, height=50)
        label.pack(side="top")
        for time in times_list:
            label = ctk.CTkLabel(self.time, text=time, height=(hei-50)/26)
            label.pack(fill = "both", expand = True)



        
        # days of week ----------------

        today = datetime.now().date()
        start = today - timedelta(days=today.weekday()+1)
        week_dates = [start + timedelta(days=i) for i in range(7)]
        print(week_dates)

        for date in week_dates:
            print(date.day)
            # print(date.strftime('%d'))
        print(week_dates[0].day)


        self.sunday = Day(self, "Sun", week_dates[0].day)
        self.sunday.pack(side = "left")

        self.monday = Day(self, "Mon", week_dates[1].day)
        self.monday.pack(side = "left")

        self.tuesday = Day(self, "Tue", week_dates[2].day)
        self.tuesday.pack(side = "left")

        self.wednesday = Day(self, "Wed", week_dates[3].day)
        self.wednesday.pack(side = "left")

        self.thursday = Day(self, "Thu", week_dates[4].day)
        self.thursday.pack(side = "left")

        self.friday = Day(self, "Fri", week_dates[5].day)
        self.friday.pack(side = "left")

        self.saturday = Day(self, "Sat", week_dates[6].day)
        self.saturday.pack(side = "left")


        # self.sunday = Day(self, "Homework", "00:00", "DO YOUR HOMEWORK", width = 50, height = 50)
        # self.sunday.pack(padx = 10, pady = 10)


        self.pack(fill = "both", expand = True)

