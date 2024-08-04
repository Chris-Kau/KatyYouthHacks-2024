import tkinter
import customtkinter
from datetime import datetime
from Calendar.Event import Event
from Calendar.Day import Day
from mongodbclass import DBEvent, DBDay, find_days


class EventInfoSection(customtkinter.CTkFrame):
    def __init__(self, master, calendar, **kwargs):
        super().__init__(master, **kwargs)
        #self.pack(side = "left", fill = "both")
        self.hei = self.winfo_screenheight()

        self.calendar = calendar
        self.pack_propagate(0)
        self.input_frame = customtkinter.CTkFrame(self, height=400, bg_color="transparent", fg_color="#c7ccd1")
        self.input_frame.pack(fill="x")

        self.name_frame = customtkinter.CTkFrame(self.input_frame, fg_color="transparent", height=100)
        self.name_frame.pack(fill="x")
        self.name_label = customtkinter.CTkLabel(self.name_frame, text="Event/Task:")
        self.name_label.pack()
        self.name_input = customtkinter.CTkEntry(self.name_frame, placeholder_text="Event/Tasks Name")
        self.name_input.pack(fill="x")

        self.note_frame = customtkinter.CTkFrame(self.input_frame, fg_color="transparent", height=100)
        self.note_frame.pack(fill="x")
        self.note_label = customtkinter.CTkLabel(self.note_frame, text="Notes:")
        self.note_label.pack()
        self.note_input = customtkinter.CTkEntry(self.note_frame, placeholder_text="Event/Tasks description")
        self.note_input.pack(fill="x")

        self.date_frame = customtkinter.CTkFrame(self.input_frame, fg_color="transparent", height=100)
        self.date_frame.pack(fill="x")
        self.date_label = customtkinter.CTkLabel(self.date_frame, text="Date:")
        self.date_label.pack()
        self.date_input = customtkinter.CTkEntry(self.date_frame, placeholder_text="mm/dd/yy")
        self.date_input.pack(fill="x")

        self.time_frame = customtkinter.CTkFrame(self.input_frame, fg_color="transparent", height=100)
        self.time_frame.pack(fill="x")
        self.time_label = customtkinter.CTkLabel(self.time_frame, text="Time:")
        self.time_label.pack()
        self.hour_minute_frame = customtkinter.CTkFrame(self.time_frame, fg_color="transparent")
        self.hour_minute_frame.pack(fill="x")
        self.hour_label = customtkinter.CTkLabel(self.hour_minute_frame, text="Hour:")
        self.hour_label.pack(side="left")
        self.hour_input = customtkinter.CTkComboBox(self.hour_minute_frame, values=[f"{x}" for x in range(1, 13)], width=60)
        self.hour_input.pack(side="left")
        self.am_or_pm = customtkinter.CTkComboBox(self.hour_minute_frame, values=["AM", "PM"], width=60)
        self.am_or_pm.pack(side="left")
        self.minute_label = customtkinter.CTkLabel(self.hour_minute_frame, text="Minute:")
        self.minute_label.pack(side="left")
        self.minute_input = customtkinter.CTkComboBox(self.hour_minute_frame, values=[f"{x}" for x in range(5, 60, 5)], width=60)
        self.minute_input.pack(side="left")

        self.create_button = customtkinter.CTkButton(self.input_frame, text="Create Event", command=self.create_event)
        self.create_button.pack(pady=5)


    def create_event(self):
        print("pressed")
        valid_name = True
        valid_note = True
        valid_date = True
        if self.name_input.get() == "":
            self.name_input.configure(placeholder_text="Must include a name!!!", placeholder_text_color="red")
            valid_name = False

        if len(self.note_input.get()) > 50:
            self.note_input.configure(placeholder_text="There is a 50 character limit", placeholder_text_color="red")
            valid_note = False

        try:
            event_date = datetime.strptime(self.date_input.get(), "%m/%d/%y")
        except ValueError:
            self.date_input.delete(0, "end")
            self.date_input.configure(placeholder_text="Must be a valid date in format mm/dd/yy", placeholder_text_color="red")
            valid_date = False
        
        if not valid_name or not valid_note or not valid_date:
            return


        #self.calendar.wednesday.hours_locations

        print("success")
        pm_or_am = 0
        if self.am_or_pm.get() == "PM":
            pm_or_am = 1

        
        print("HOUR INDEX", int(self.hour_input.get()))
        def place_event(event, newy):
            event.place(y=newy)
        day_name = event_date.strftime("%A").lower()
        if day_name == "sunday":
            pmlist = self.calendar.sunday.hours_locations[12:]
            pmlist.append(pmlist[0])
            amlist = self.calendar.sunday.hours_locations[:12]
            amlist.append(amlist[0])
            sunday_list = [amlist,pmlist]
            sunday_list = sunday_list[pm_or_am]
            self.new_event = Event(sunday_list[int(self.hour_input.get())], self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get(), width = 100, height = 800/24)
            self.new_event.grid(row=0, column=0)      
        elif day_name == "monday":
            pmlist = self.calendar.monday.hours_locations[12:]
            pmlist.append(pmlist[0])
            amlist = self.calendar.monday.hours_locations[:12]
            amlist.append(amlist[0])
            monday_list = [amlist,pmlist]
            monday_list = monday_list[pm_or_am]
            self.new_event = Event(monday_list[int(self.hour_input.get())], self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get(), width = 100, height = 800/24)
            self.new_event.grid(row=0, column=0)      
        elif day_name == "tuesday":
            pmlist = self.calendar.tuesday.hours_locations[12:]
            pmlist.append(pmlist[0])
            amlist = self.calendar.tuesday.hours_locations[:12]
            amlist.append(amlist[0])
            tuesday_list = [amlist,pmlist]
            tuesday_list = tuesday_list[pm_or_am]
            self.new_event = Event(tuesday_list[int(self.hour_input.get())], self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get(), width = 100, height = 800/24)
            self.new_event.grid(row=0, column=0)      
        elif day_name == "wednesday":
            pmlist = self.calendar.wednesday.hours_locations[12:]
            pmlist.append(pmlist[0])
            amlist = self.calendar.wednesday.hours_locations[:12]
            amlist.append(amlist[0])
            wednesday_list = [amlist,pmlist]
            wednesday_list = wednesday_list[pm_or_am]
            self.new_event = Event(wednesday_list[int(self.hour_input.get())], self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get(), width = 100, height = 800/24)
            self.new_event.grid(row=0, column=0)
            #self.new_event.after(100, place_event, self.new_event,temp_loc[int(self.hour_input.get())][1])
        elif day_name == "thursday":
            pmlist = self.calendar.thursday.hours_locations[12:]
            pmlist.append(pmlist[0])
            amlist = self.calendar.thursday.hours_locations[:12]
            amlist.append(amlist[0])
            thursday_list = [amlist,pmlist]
            thursday_list = thursday_list[pm_or_am]
            self.new_event = Event(thursday_list[int(self.hour_input.get())], self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get(), width = 100, height = 800/24)
            self.new_event.grid(row=0, column=0)
        elif day_name == "friday":
            pmlist = self.calendar.friday.hours_locations[12:]
            pmlist.append(pmlist[0])
            amlist = self.calendar.friday.hours_locations[:12]
            amlist.append(amlist[0])
            friday_list = [amlist,pmlist]
            friday_list = friday_list[pm_or_am]
            self.new_event = Event(friday_list[int(self.hour_input.get())], self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get(), width = 100, height = 800/24)
            self.new_event.grid(row=0, column=0)
        elif day_name == "saturday":
            pmlist = self.calendar.saturday.hours_locations[12:]
            pmlist.append(pmlist[0])
            amlist = self.calendar.saturday.hours_locations[:12]
            amlist.append(amlist[0])
            saturday_list = [amlist,pmlist]
            saturday_list = saturday_list[pm_or_am]
            self.new_event = Event(saturday_list[int(self.hour_input.get())], self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get(), width = 100, height = 800/24)
            self.new_event.grid(row=0, column=0)        
        found_day = find_days(event_date)
        if found_day:
            print("bleh")
            new_event = DBEvent(self.name_input.get(), self.note_input.get(), int(self.hour_input.get()), int(self.minute_input.get()))
            found_day.add_event(new_event)
            found_day.save()
            return
        
        new_day = DBDay(event_date)
        new_day.save()    
        new_event = DBEvent(self.name_input.get(), self.note_input.get(), int(self.hour_input.get()), int(self.minute_input.get()))
        new_day.add_event(new_event)
        new_day.save()




