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


        # self.ai_chat_section = AiChatSection(master = self, width = 300, height = 1000, fg_color = "#adadad")
        # self.ai_chat_section.pack(side = "right", fill = "both")
        

        # self.event_info_section = EventInfoSection(master = self, width = 250, fg_color="blue")
        # self.event_info_section.pack(side = "left", fill = "both")
        
        # self.calendar_section = CalendarSection(master = self, fg_color= "green", corner_radius=0)
        # self.calendar_section.pack(fill = "both", expand = True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.calendar_section = CalendarSection(master=self, fg_color="green", corner_radius=0)
        self.calendar_section.grid(row=0, column=1, sticky="nsew")

        self.event_info_section = EventInfoSection(master=self, calendar=self.calendar_section, width=250, fg_color="#dedfe0")
        self.event_info_section.grid(row=0, column=0, sticky="ns")


        self.ai_chat_section = AiChatSection(master=self, width=300, height=1000, fg_color="#adadad")
        self.ai_chat_section.grid(row=0, column=2, sticky="ns")
app = App()
app.mainloop()