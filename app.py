import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import openpyxl, xlrd
import pathlib
from openpyxl import workbook


# colocando aparencia padrao do sistema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.appaerence()
        self.all_system()

    def layout_config(self):
        self.title("Sistema de cadastro de Oficina")
        self.geometry("700x500")

    def appaerence(self):
        self.lb_apm = ctk.CTkLabel(self, text="Tema",  bg_color="transparent", 
                                   text_color=['#000','#fff']).place(x=50, y=430)
        self.opt_apm = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                        command=self.change_apm).place(x=50, y=460)
        

    def all_system(self):
        frame = ctk.CTkFrame(self, width=700, height=70, corner_radius=0, bg_color="teal", 
                             fg_color="teal").place(x=0, y=0)
        title_main= ctk.CTkLabel(frame, text="Sistema Car Henrique", font=("Century Gothic bold", 24),
                                  text_color="#fff", bg_color="teal").place(x=230, y=20)
        
        span = ctk.CTkLabel(self, text="Por favor preencha todos os campos.", font=("Century Gothic bold",
                                         12), text_color=["#000", "#fff"]).place(x=50, y=70)

        # labels






    def change_apm(self, new_appaerence_mode):
        ctk.set_appearance_mode(new_appaerence_mode)

if __name__=="__main__":
    app = App()
    app.mainloop()