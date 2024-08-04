import tkinter
import customtkinter
class Event(customtkinter.CTkTextbox):
    def __init__(self, master, title, time, description, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(text_color = "black", fg_color = "white", wrap = "word") #read-only
        #self.tag_config("center", justify = "center")
        self.insert("1.0", title + " ") #insert at line 0, character 0
        self.insert("1.end", time + "\n") 
        if description != " ":
            self.insert("2.0", description + "\n")
        #self.pack()
        self.configure(state = "disabled")
        self.grid(row=0, column=0)

