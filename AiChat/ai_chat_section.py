import tkinter
import customtkinter
from AiChat.gpt2 import GPT
from AiChat.usermessage import UserMessage
class AiChatSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(side = "right", fill = "both")
        self.bottom_frame = UserMessage(self, width = 250, height = 50, fg_color = "grey")
        #bottom_frame.pack(side = "bottom")
