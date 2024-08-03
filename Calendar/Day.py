import tkinter
import customtkinter
from Calendar.Event import Event
class Day(customtkinter.CTkFrame):
    def __init__(self, master, day, col, **kwargs): # title, time, desc, 
        super().__init__(master, **kwargs)

        self.update()
        wid = (self.winfo_screenwidth()-550)/7 # 550 is width of other two sections combined
        hei = self.winfo_screenheight()

        self.label = customtkinter.CTkLabel(self)
        self.label.configure(text = day)
        self.label.configure(width = wid-19, height = hei-600)

        self.label.grid(row=0, column=0, padx=10, pady = 300) 
        # self.grid_columnconfigure(col, weight=col)
        

        self.pack()


        # self.day = Event(self, title, time, desc)
        # self.day.pack()
        
        # self.monday = Event(self, "Homework", "00:00", "PLEASE TELL ME TO DO MY HOMEWORK")
        
        

