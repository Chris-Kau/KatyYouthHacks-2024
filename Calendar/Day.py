import tkinter as tk
import customtkinter
from Calendar.Event import Event
class Day(customtkinter.CTkFrame):
    def __init__(self, master, day, date, **kwargs): # title, time, desc, 
        super().__init__(master, **kwargs)

        self.update()
        wid = (self.winfo_screenwidth()-600)/7 # 550 is width of other two sections combined + 50 time
        hei = self.winfo_screenheight()


        self.day_list = []
        # the (7) boxes of days ------------------
        self.frame = customtkinter.CTkFrame(self, border_width=1, border_color="gray50")
        # self.frame.configure(text = day)
        self.frame.configure(width=wid, height=800)
        self.frame.grid(row=0, column=0, padx=0, pady=0) 
        self.frame.pack_propagate(False)
        # self.frame.pack(side = "bottom")
        

        # the hours -----------------------------
        for i in range(2):
            for j in range(12):
                hours = customtkinter.CTkFrame(self.frame, height=800/24, border_width=0.5, border_color="gray80", corner_radius=0)
                hours.pack()

        # # -90 gives line almost exact between 12 and 1, -155 gives 11 and 12 (correct). 153 too
        # block1 = customtkinter.CTkFrame(self.frame, height=(hei-90)/2, corner_radius=0, fg_color="gray80", border_width=0)
        # block1.pack(side="top")
        # block1.pack_propagate(False)
        # block2 = customtkinter.CTkFrame(self.frame, height=(hei-90)/2, corner_radius=0, fg_color="gray80", border_width=0)
        # block2.pack(side="top")
        # block2.pack_propagate(False)

        # def append_hours(hours):
        #     self.day_list.append(hours)
        # for j in range(13):
        #     hours = customtkinter.CTkFrame(block1, height=(hei-90)/26, border_width=0.8, border_color="gray80", corner_radius=0)
        #     hours.pack()
        #     hours.after(100, append_hours, hours)
        # for j in range(11):
        #     hours = customtkinter.CTkFrame(block2, height=(hei-145)/24, border_width=0.7, border_color="gray80", corner_radius=0)
        #     hours.pack()


        self.pack()





        # self.day = Event(self, title, time, desc)
        # self.day.pack()
        
        # self.monday = Event(self, "Homework", "00:00", "PLEASE TELL ME TO DO MY HOMEWORK")
        
        

