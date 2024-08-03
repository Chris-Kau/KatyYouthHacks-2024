import tkinter
import customtkinter
from Calendar.Event import Event
class Day(customtkinter.CTkFrame):
    def __init__(self, master, day, date, **kwargs): # title, time, desc, 
        super().__init__(master, **kwargs)

        self.update()
        wid = (self.winfo_screenwidth()-600)/7 # 550 is width of other two sections combined + 50 time
        hei = self.winfo_screenheight()

        self.label = customtkinter.CTkLabel(self)
        self.label.configure(text = day)
        self.label.configure(width=wid-19, height=hei-600)

        self.label.grid(row=0, column=0, padx=10, pady = 300) 

        self.textbox = customtkinter.CTkTextbox(master=self, width=1, height = 50, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="new") # sticky = nsew
        
        self.textbox.tag_config("center", justify="center")
        self.textbox.insert("0.0", str(day) + " " + str(date))
        
        


        self.pack()

        # self.day = Event(self, title, time, desc)
        # self.day.pack()
        
        # self.monday = Event(self, "Homework", "00:00", "PLEASE TELL ME TO DO MY HOMEWORK")
        
        

