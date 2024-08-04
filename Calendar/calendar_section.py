import tkinter
import customtkinter as ctk
from Calendar.Day import Day
from datetime import datetime, timedelta
import calendar
class CalendarSection(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        wid = self.winfo_screenwidth()-550 # 550 is width of other two sections combined
        hei = self.winfo_screenheight()

        self.time_frame_list = []
        # month/year -------------
        def get_current_week_months_and_year():
            # Get the current date
            today = datetime.today()
            # Calculate the start and end of the current week
            start_of_week = today - timedelta(days=today.weekday()) 
            end_of_week = start_of_week + timedelta(days=6) 
            # Get months from the start and end of the week
            months = [calendar.month_name[start_of_week.month], calendar.month_name[end_of_week.month]]
            # Get the current year
            current_year = today.year
            return months, current_year
        months, year = get_current_week_months_and_year()
        monthsstr = '-'.join(months)
        print(months)
        print(monthsstr)

        self.monthyr = ctk.CTkFrame(master=self, height=40)
        self.monthyr.pack(side="top", fill = "both", expand = True)
        myLbl = ctk.CTkLabel(self.monthyr, text=monthsstr + " " + str(year), width=wid, font=("Arial", 20))
        myLbl.pack(fill = "both", expand = True)



        # time of day ----------------------------
        self.time = ctk.CTkFrame(master=self, width=50, height=hei-40, corner_radius=0)
        self.time.pack(side = "left")
        self.time.pack_propagate(False)

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
        squareframe = ctk.CTkFrame(self.time, height=50, corner_radius=0, fg_color="gray85") # square top left
        squareframe.pack(side="top")

        for time in times_list:
            frame = ctk.CTkFrame(self.time, height=(hei-90)/28, width=50, corner_radius=0, border_width=0.5, fg_color="#f2f2f2")
            label = ctk.CTkLabel(frame, text=time, font=("Arial", 12))
            
            frame.pack(fill = "both", expand = True)
            frame.pack_propagate(False)
            label.pack()
            self.time_frame_list.append(label)



        
        # days of week ----------------

        today = datetime.now().date()
        start = today - timedelta(days=today.weekday()+1)
        week_dates = [start + timedelta(days=i) for i in range(7)]
        # print(week_dates)

        # for date in week_dates:
            # print(date.day)
            # print(date.strftime('%d'))
        # print(week_dates[0].day)


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

        #self.pack(fill = "both", expand = True)

