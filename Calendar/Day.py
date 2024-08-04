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
        self.frame.configure(width=wid, height=hei-40)
        self.frame.grid(row=0, column=0, padx=0, pady=0) 
        self.frame.pack_propagate(False)
        # self.frame.pack(side = "bottom")
        

        # the top (day and date) --------------
        # self.textbox = customtkinter.CTkTextbox(master=self, width=1, height = 50, corner_radius=0, font=("Arial", 16))
        self.label = customtkinter.CTkLabel(master=self, width=1, height = 50, corner_radius=0, font=("Arial", 18))

        self.label.grid(row=0, column=0, sticky="new") # sticky = nsew
        self.label.configure(text=str(day) + " " + str(date))

        # the hours -----------------------------
        block = customtkinter.CTkFrame(self.frame, height=50, fg_color="red", bg_color="red") # CORRECTLY covering the part thats the day titling
        block.pack(side="top") 
        block = customtkinter.CTkFrame(self.frame, height=55, fg_color="red", bg_color="red") # covering the bottom???
        block.pack(side="bottom") 

        # -90 gives line almost exact between 12 and 1, -155 gives 11 and 12 (correct). 153 too
        block1 = customtkinter.CTkFrame(self.frame, height=(hei-90)/2, corner_radius=0, fg_color="gray80", border_width=0)
        block1.pack(side="top")
        block1.pack_propagate(False)
        block2 = customtkinter.CTkFrame(self.frame, height=(hei-90)/2, corner_radius=0, fg_color="gray80", border_width=0)
        block2.pack(side="top")
        block2.pack_propagate(False)
        for j in range(13):
            hours = customtkinter.CTkFrame(block1, height=(hei-90)/26, border_width=0.8, border_color="gray80", corner_radius=0, fg_color="white")
            hours.pack()
        for j in range(11):
            hours = customtkinter.CTkFrame(block2, height=(hei-145)/24, border_width=0.7, border_color="gray80", corner_radius=0, fg_color="white")
            hours.pack()


        self.pack()

        # self.day = Event(self, title, time, desc)
        # self.day.pack()
        
        # self.monday = Event(self, "Homework", "00:00", "PLEASE TELL ME TO DO MY HOMEWORK")
        
        

