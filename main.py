import tkinter
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title = "Calendar App"
        self._set_appearance_mode("System")
        self.geometry("600x400")

        self.ai_chat_section = customtkinter.CTkFrame(master = self, width = 500, fg_color="white")
        self.ai_chat_section.pack(side = "right", fill = "y")

        self.event_info_section = customtkinter.CTkFrame(master = self, width = 300, fg_color="blue")
        self.event_info_section.pack(side="left", fill='y')

        self.calendar_section = customtkinter.CTkFrame(master = self, fg_color= "green")
        self.calendar_section.pack(fill = "both", expand=True)

app = App()
app.mainloop()


#Chris
#########################################################################



#Ashley
#########################################################################





#Nick
#########################################################################







#########################################################################
mainwindow.mainloop()