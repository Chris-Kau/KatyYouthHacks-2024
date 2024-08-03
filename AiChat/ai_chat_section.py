import tkinter
import customtkinter
from AiChat.gpt2 import GPT
from AiChat.usertextbox import UserTextBox
from AiChat.conversation import Conversation
class AiChatSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack_propagate(False)
        self.pack(side = "right", fill = "both", expand = True)
        self.usertextbox = UserTextBox(self, width = 250, height = 100, corner_radius = 10, border_color = "black", fg_color = "transparent", border_width = 2)
        self.usertextbox.pack(side = "bottom", pady = 10)

        self.conversation = Conversation(self, fg_color = "#bfbfbf")
        self.conversation.pack(side = "top", padx = 10, pady = 10, fill = "both", expand = True)
