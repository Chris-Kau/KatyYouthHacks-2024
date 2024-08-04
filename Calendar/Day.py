import tkinter as tk
import customtkinter
from Calendar.Event import Event
class Day(customtkinter.CTkFrame):
    def __init__(self, master, day, date, **kwargs): # title, time, desc, 
        super().__init__(master, **kwargs)

        self.update()
        wid = (self.winfo_screenwidth()-600)/7 # 550 is width of other two sections combined + 50 time
        hei = self.winfo_screenheight()

        self.hours_locations = []


        self.day_list = []
        # the (7) boxes of days ------------------
        self.frame = customtkinter.CTkFrame(self, border_width=1, border_color="gray50")
        # self.frame.configure(text = day)
        self.frame.configure(width=wid, height=800)
        self.frame.grid(row=0, column=0, padx=0, pady=0) 
        self.frame.pack_propagate(False)
        self.frame.grid_propagate(False)
        # self.frame.pack(side = "bottom")
        

        # the hours -----------------------------
        for i in range(2):
            for j in range(12):
                hours = customtkinter.CTkFrame(self.frame, height=800/24, border_width=0.7, fg_color="white", border_color="gray90", corner_radius=0)
                hours.pack()
                #hours.pack_propagate(0)
                self.hours_locations.append(hours)
        self.pack()





        # self.day = Event(self, title, time, desc)
        # self.day.pack()
        
        # self.monday = Event(self, "Homework", "00:00", "PLEASE TELL ME TO DO MY HOMEWORK")
        
        

