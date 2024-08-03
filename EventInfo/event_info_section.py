import tkinter
import customtkinter
class EventInfoSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(side = "left", fill = "both")