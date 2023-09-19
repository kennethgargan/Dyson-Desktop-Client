import customtkinter as ctk

class View(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Dyson Desktop Client")
        self.root.geometry("1000x600")

        self.main_frame = ctk.CTkFrame(root, fg_color="transparent")
        self.main_frame.pack(fill=ctk.BOTH, expand=True)


        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0,weight=1)
        
        self.main_frame_top = ctk.CTkFrame(self.main_frame,fg_color="blue")
        self.main_frame_top.grid(row=0,column=0,sticky="nsew",rowspan=2)

        self.main_frame_middle = ctk.CTkFrame(self.main_frame,fg_color="yellow")
        self.main_frame_middle.grid(row=1,column=0,sticky="nsew",rowspan=1)

        self.main_frame_top.grid_columnconfigure(0,weight=1)
        self.main_frame_middle.grid_columnconfigure(1,weight=1)

    def set_controller(self, controller):
        self.controller = controller