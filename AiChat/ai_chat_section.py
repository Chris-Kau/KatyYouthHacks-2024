import tkinter
import customtkinter
from AiChat.gpt2 import GPT
from AiChat.usertextbox import UserTextBox
class AiChatSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(side = "right", fill = "both", expand = True)
        self.bottom_frame = UserTextBox(self, width = 250, height = 100, corner_radius = 10, border_color = "black", fg_color = "transparent", border_width = 2)
        self.bottom_frame.pack(side = "bottom", pady = 10)
