import tkinter
import customtkinter
from Calendar.calendar_section import CalendarSection
from EventInfo.event_info_section import EventInfoSection
from AiChat.ai_chat_section import AiChatSection

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title = "Calendar App"
        self._set_appearance_mode("System")
        self.geometry("600x400")

        self.ai_chat_section = CalendarSection(master = self, width = 500, fg_color = "white")

        self.event_info_section = EventInfoSection(master = self, width = 300, fg_color="blue")

        self.calendar_section = AiChatSection(master = self, fg_color= "green")

app = App()
app.mainloop()


#Chris
#########################################################################



#Ashley
#########################################################################





#Nick
#########################################################################







#########################################################################