import tkinter as tk
import customtkinter
from Calendar.Event import Event
class Day(customtkinter.CTkFrame):
    def __init__(self, master, day, date, **kwargs): # title, time, desc, 
        super().__init__(master, **kwargs)

        self.update()
        wid = (self.winfo_screenwidth()-600)/7 # 550 is width of other two sections combined + 50 time
        hei = self.winfo_screenheight()

        # the (7) boxes of days ------------------
        self.frame = customtkinter.CTkFrame(self, border_width=1, border_color="gray50")
        # self.frame.configure(text = day)
        self.frame.configure(width=wid, height=hei)
        self.frame.grid(row=0, column=0, padx=0, pady=0) 
        self.frame.pack_propagate(False)

        # the top (day and date) --------------
        # self.textbox = customtkinter.CTkTextbox(master=self, width=1, height = 50, corner_radius=0, font=("Arial", 16))
        self.label = customtkinter.CTkLabel(master=self, width=1, height = 50, corner_radius=0, font=("Arial", 18))

        self.label.grid(row=0, column=0, sticky="new") # sticky = nsew
        self.label.configure(text=str(day) + " " + str(date))

        # the hours -----------------------------
        block = customtkinter.CTkFrame(self.frame, height=50) # covering the part thats the day titling
        block.pack(side="top") 
        for i in range(2):
            for j in range(12):
                hours = customtkinter.CTkFrame(self.frame, height=(hei-50)/27, border_width=0.5, border_color="gray80", corner_radius=0)
                hours.pack()

        self.pack()

        # self.day = Event(self, title, time, desc)
        # self.day.pack()
        
        # self.monday = Event(self, "Homework", "00:00", "PLEASE TELL ME TO DO MY HOMEWORK")
        
        

