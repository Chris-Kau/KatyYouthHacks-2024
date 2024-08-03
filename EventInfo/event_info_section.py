import tkinter
import customtkinter

class EventInfoSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(side = "left", fill = "both")
        self.pack_propagate(0)
        self.input_frame = customtkinter.CTkFrame(self, height=400, bg_color="transparent", fg_color="green")
        self.input_frame.pack(fill="x")

        self.name_frame = customtkinter.CTkFrame(self.input_frame, fg_color="orange", height=100)
        self.name_frame.pack(fill="x")
        self.name_label = customtkinter.CTkLabel(self.name_frame, text="Event/Task:")
        self.name_label.pack()
        self.name_input = customtkinter.CTkEntry(self.name_frame, placeholder_text="Event/Tasks Name", justify="left")
        self.name_input.pack()

        self.date_frame = customtkinter.CTkFrame(self.input_frame, fg_color="brown", height=100)
        self.date_frame.pack(fill="x")
        self.date_label = customtkinter.CTkLabel(self.date_frame, text="Date:")
        self.date_label.pack()
        self.date_input = customtkinter.CTkEntry(self.date_frame, placeholder_text="mm/dd/yy")
        self.date_input.pack()

        self.date_time = customtkinter.CTkFrame(self.input_frame, fg_color="orange", height=100)
        self.date_time.pack(fill="x")        


    def create_event(self):
        print("pressed")
        # input_box = tkinter.Toplevel()
        # input_box.title("Add an event")
        # input_box.geometry("400x300")
        # test_text = customtkinter.CTkLabel(input_box, text="testing 123")
        # close_button = customtkinter.CTkButton(input_box, text="close", command=input_box.destroy)  
        # test_text.pack()
        # close_button.pack()
        # input_box.mainloop()
        self.master.popup()