import tkinter
import customtkinter
class UserMessage(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(side = "bottom")
        textbox = customtkinter.CTkTextbox(self, width = 250, height = 50, fg_color="grey")
        textbox.pack(fill = "both", expand = True)
