import tkinter
import customtkinter

mainwindow = customtkinter.CTk()
mainwindow._set_appearance_mode("System")
mainwindow.geometry("600x400")

ai_chat_section = customtkinter.CTkFrame(master = mainwindow, width = 500, fg_color="white")
ai_chat_section.pack(side = "right", fill = "y")

event_info_section = customtkinter.CTkFrame(master = mainwindow, width = 300, fg_color="blue")
event_info_section.pack(side="left", fill='y')

calendar_section = customtkinter.CTkFrame(master = mainwindow, fg_color= "green")
calendar_section.pack(fill = "both", expand=True)

#Chris
#########################################################################



#Ashley
#########################################################################





#Nick
#########################################################################







#########################################################################
mainwindow.mainloop()