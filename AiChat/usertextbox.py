import tkinter
import customtkinter
from AiChat.gpt2 import GPT
class UserTextBox(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.gpt = GPT()
        self.pack(side = "bottom")
        self.pack_propagate(False)
        
        self.usertextbox = customtkinter.CTkTextbox(self, width = 250, height = 50, corner_radius=10)
        self.usertextbox.bind("<Return>", self.on_enter_pressed)
        self.usertextbox.pack(side = "bottom", expand = True, padx = 10, pady = 10)

    def on_enter_pressed(self, event):
        text = self.usertextbox.get("0.0", "end")
        print(text)
        print("THIS WAS PRESSED: ", event)
        self.usertextbox.delete("0.0", "end")
        return "break"
