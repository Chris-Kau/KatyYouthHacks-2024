import tkinter
import customtkinter
from Calendar.calendar_section import CalendarSection
from EventInfo.event_info_section import EventInfoSection
from AiChat.ai_chat_section import AiChatSection

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title = "Calendar App!!"
        self._set_appearance_mode("System")
        self.geometry("1200x800")

        self.ai_chat_section = AiChatSection(master = self, width = 300, height = 1000, fg_color = "white")
        self.ai_chat_section.pack(side = "right", fill = "both")

        self.event_info_section = EventInfoSection(master = self, width = 250, fg_color="blue")
        self.event_info_section.pack(side = "left", fill = "both")

        self.calendar_section = CalendarSection(master = self, fg_color= "green")
        self.calendar_section.pack(fill = "both", expand = True)

app = App()
app.mainloop()