import tkinter
import customtkinter
from datetime import datetime
from Calendar.Event import Event

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
        if self.name_input.get() == "":
            self.name_input.configure(placeholder_text="Must include a name!!!", placeholder_text_color="red")

        if len(self.note_input.get()) > 50:
            self.note_input.configure(placeholder_text="There is a 50 character limit", placeholder_text_color="red")

        try:
            event_date = datetime.strptime(self.date_input.get(), "%m/%d/%y")
        except ValueError:
            self.date_input.delete(0, "end")
            self.date_input.configure(placeholder_text="Must be a valid date in format mm/dd/yy", placeholder_text_color="red")
        else:
            print("success")
            # print(self.name_input.get())
            # print(self.note_input.get())
            # print(event_date)
            # print(self.hour_input.get())
            # print(self.minute_input.get())
            day = str(event_date.strftime("%A")).lower()

            time_cords = []
            # for frame in self.calendar.time_frame_list:
            #     time_cords.append((frame.winfo_rootx(), frame.winfo_rooty()))
            for j in range(13):
                height=(self.hei-90)/26 * j
                time_cords.append(height)
            for j in range(11):
                height=(self.hei-145)/24 * j
                time_cords.append(height)
            print("LEN!U!*@&*!", len(time_cords))
            
            if self.am_or_pm.get() == "PM":
                self.hour_input.set(str(int(self.hour_input.get()) + 12))
            
            print("HOUR", self.hour_input.get())

            def place_new_event():
                new_event.place(y=time_cords[int(self.hour_input.get())-1])
                print("time cord change y value", time_cords[int(self.hour_input.get())][1])
                print("new root", new_event.winfo_rooty())


            if(day == "monday"):
                new_event = Event(self.calendar.monday, self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get())
                new_event.grid(row=0, column=0, padx=5, pady=5)
            elif(day == "tuesday"):
                new_event = Event(self.calendar.tuesday, self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get())
                new_event.grid(row=0, column=0, padx=5, pady=5)
            elif(day == "wednesday"):
                new_event = Event(self.calendar.wednesday, self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get(), width = 80, height = 20)
                new_event.grid(row=0, column=0, padx=5, pady=5)
                new_event.after(100, place_new_event)
            elif(day == "thursday"):
                new_event = Event(self.calendar.thursday, self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get())
                new_event.grid(row=0, column=0, padx=5, pady=5)
            elif(day == "friday"):
                new_event = Event(self.calendar.friday, self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get())
                new_event.grid(row=0, column=0, padx=5, pady=5)
            elif(day == "saturday"):
                new_event = Event(self.calendar.saturday, self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get())
                new_event.grid(row=0, column=0, padx=5, pady=5)
            elif(day == "sunday"):
                new_event = Event(self.calendar.sunday, self.name_input.get(), f"{self.hour_input.get()}:{self.minute_input.get()}", self.note_input.get())
                new_event.grid(row=0, column=0, padx=5, pady=5)
            
