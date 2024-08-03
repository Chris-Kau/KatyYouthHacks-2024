import tkinter
import customtkinter
class Conversation(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(side="top", padx = 10, pady = 10, fill = "both", expand = True)
        self.conversationbox = customtkinter.CTkTextbox(self, padx = 10, pady = 5)
        self.conversationbox.pack(fill = "both", expand = True)

        self.update_text("blehhh", "Chris")
        self.update_text("bloooo", "ai")
        self.update_text("blahhhhh", "Chris")
        self.update_text("bliiiiih", "ai")
    
    def get_text(self):
        return self.conversationbox.get("0.0", "end")
    
    def update_text(self, newtext, user):
        last_line = self.conversationbox.index("end-1c linestart")
        self.conversationbox.insert(f"{last_line}", f"{user}: {newtext} \n\n")
        return self.conversationbox.index("end-1c linestart")