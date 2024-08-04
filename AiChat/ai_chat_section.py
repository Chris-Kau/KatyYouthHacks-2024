import tkinter
import customtkinter
from AiChat.gpt2 import GPT
class AiChatSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack_propagate(False)
        self.pack(side = "right", fill = "both", expand = True)
        self.gpt = GPT()
        self.usertextbox = customtkinter.CTkTextbox(self, width = 250, height = 100, corner_radius = 10, border_color = "black", fg_color = "transparent", border_width = 2)
        self.usertextbox.bind("<Return>", self.on_enter_pressed)
        self.usertextbox.pack(side = "bottom", pady = 10)

        self.conversationframe = customtkinter.CTkFrame(self, fg_color = "#bfbfbf")
        self.conversationframe.pack(side = "top", padx = 10, pady = 10, fill = "both", expand = True)

        self.conversationbox = customtkinter.CTkTextbox(self.conversationframe, padx = 10, pady = 5)
        self.conversationbox.pack(fill = "both", expand = True)
        self.conversationbox.configure(state="disabled")


    def on_enter_pressed(self, event):
        text = self.usertextbox.get("0.0", "end")
        self.update_text(text, "\nChris")
        #response = self.gpt.chat_with_bot(text)
        #response = "test_response"
        response = self.gpt.MakeSchedule(text)
        self.update_text(response, "System")
        self.usertextbox.delete("0.0", "end")
        return "break"

    def get_text(self):
        return self.conversationbox.get("0.0", "end")
    
    def update_text(self, newtext, user):
        self.conversationbox.configure(state="normal")
        last_line = self.conversationbox.index("end-1c linestart")
        self.conversationbox.insert(f"{last_line}", f"{user}: {newtext} \n")
        self.conversationbox.configure(state="disabled")