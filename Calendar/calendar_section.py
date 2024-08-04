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

        self.configure(width = 500)
        self.label_locations = []
        # month/year -------------
        def get_current_week_months_and_year():
            # Get the current date
            today = datetime.today()
            # Calculate the start and end of the current week
            if today.weekday() == 6:  # If today is Sunday
                start_of_week = today
            else:
                start_of_week = today - timedelta(days=today.weekday() + 1)
            end_of_week = start_of_week + timedelta(days=6)
            # Get months from the start and end of the week
            months = [calendar.month_name[start_of_week.month], calendar.month_name[end_of_week.month]]
            # Get the current year
            current_year = today.year
            return months, current_year
        months, year = get_current_week_months_and_year()
        if(months[0] == months[1]):
            monthsstr = months[0]
        else:
            monthsstr = '-'.join(months)
        print(months)
        print(monthsstr)

        self.monthyr = ctk.CTkFrame(master=self, height=40)
        self.monthyr.pack(side="top", fill = "both", expand = True)
        myLbl = ctk.CTkLabel(self.monthyr, text=monthsstr + " " + str(year), width=wid, font=("Arial", 20), fg_color="white")
        myLbl.pack(fill = "both", expand = True)
      

        # days of week ----------------
        today = datetime.today()
        if today.weekday() == 6:  # if today is Sunday
            start = today
        else:
            start = today - timedelta(days=today.weekday() + 1)
        week_dates = [start + timedelta(days=i) for i in range(7)]
        print(today)
        print(start)
        today = datetime.now().date()
        start = today - timedelta(days=today.weekday()+1)
        weekdays = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]


        # the top (day and date) --------------
        daydateframe = ctk.CTkFrame(master=self, width=wid, height = 50, corner_radius=0)
        daydateframe.pack(side="top")
        daydateframe.pack_propagate(False)
        squareframe = ctk.CTkFrame(daydateframe, width=50, corner_radius=0, fg_color="white") # square top left ------------------
        squareframe.pack(side="left")

        daywidth = wid = (self.winfo_screenwidth()-600)/7 # 550 is width of other two sections combined + 50 time
        for i in range(len(week_dates)):
            daydate = ctk.CTkLabel(daydateframe, width=daywidth, height = 50, corner_radius=0, font=("Arial", 18), fg_color="white")
            # daydate.grid(row=0, column=0, sticky="new")
            daydate.configure(text=str(weekdays[i]) + " " + str(week_dates[i].day))
            daydate.pack(side="left")

        
        # SCROLLLLL -----------------------
        self.events_holder = ctk.CTkScrollableFrame(self, width=wid, height=800, fg_color = "gray80")
        self.events_holder.pack(side="top", fill = "both", expand = True)

        # time of day ----------------------------
        self.time = ctk.CTkFrame(master=self.events_holder, width=50, height=800, corner_radius=0)
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
        for time in times_list:
            frame = ctk.CTkFrame(self.time, height=800/24, width=50, corner_radius=0, border_width=0.5, fg_color="#f2f2f2")
            label = ctk.CTkLabel(frame, text=time, font=("Arial", 12))
            
            frame.pack(fill = "both", expand = True)
            frame.pack_propagate(False)
            label.pack()
            self.label_locations.append(frame)
        

        # days of week columns cont. -----------------------
        self.sunday = Day(self.events_holder, "Sun", week_dates[0].day)
        self.sunday.pack(side = "left")

        self.monday = Day(self.events_holder, "Mon", week_dates[1].day)
        self.monday.pack(side = "left")

        self.tuesday = Day(self.events_holder, "Tue", week_dates[2].day)
        self.tuesday.pack(side = "left")

        self.wednesday = Day(self.events_holder, "Wed", week_dates[3].day)
        self.wednesday.pack(side = "left")
        
        self.thursday = Day(self.events_holder, "Thu", week_dates[4].day)
        self.thursday.pack(side = "left")

        self.friday = Day(self.events_holder, "Fri", week_dates[5].day)
        self.friday.pack(side = "left")

        self.saturday = Day(self.events_holder, "Sat", week_dates[6].day)
        self.saturday.pack(side = "left")






        self.grid(row=0, column=1, sticky="ew")
        self.pack_propagate(False)
        #self.pack(fill = "both", expand = True)

