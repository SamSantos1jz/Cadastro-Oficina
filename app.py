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
        self.geometry("930x500")

    def appaerence(self):
        self.lb_apm = ctk.CTkLabel(self, text="Tema",  bg_color="transparent", 
                                   text_color=['#000','#fff']).place(x=50, y=430)
        self.opt_apm = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                        command=self.change_apm).place(x=50, y=460)
        

    def all_system(self):
        
        frame = ctk.CTkFrame(self, width=1000, height=70, corner_radius=0, bg_color="teal", 
                             fg_color="teal").place(x=0, y=0)
        title_main= ctk.CTkLabel(frame, text="SISTEMA CAR HENRIQUE", font=("arial", 24),
                                  text_color="#fff", bg_color="teal").place(x=360, y=20)
        
        span = ctk.CTkLabel(self, text="Por favor preencha todos os campos.", font=("Century Gothic bold",
                                         10), text_color=["#000", "#fff"]).place(x=50, y=70)

        # Entrys
        name_entry = ctk.CTkEntry(self, width=350, font=("Century Ghotic bold", 16), fg_color="transparent")
        tel_entry = ctk.CTkEntry(self, width=200, font=("Century Ghotic bold", 16), fg_color="transparent")
        adress_entry = ctk.CTkEntry(self, width=350, font=("Century Ghotic bold", 16), fg_color="transparent")
        cel_entry = ctk.CTkEntry(self, width=200, font=("Century Ghotic bold", 16), fg_color="transparent")
        adress_num_entry = ctk.CTkEntry(self, width=100, font=("Century Ghotic bold", 16), fg_color="transparent")
        date_entry = ctk.CTkEntry(self, width=100, font=("Century Gothic bold", 16), fg_color="transparent")
        payment_entry = ctk.CTkEntry(self, width=150, font=("Century Gothic bold", 16), fg_color="transparent")
        car_entry = ctk.CTkEntry(self, width=250, font=("Century Gothic bold", 16), fg_color="transparent")


        # ComboBox 
        payment_combo_box = ctk.CTkComboBox(self, values=["---","PAGO", "PENDENTE"], font=("Century Ghotic bold", 14))
        payment_combo_box.set("---")

        # OBSERVAÇÕES
        obs_entry = ctk.CTkTextbox(self, width=830, height=150, font=("arial", 18), border_color="#aaa", border_width=2, fg_color="transparent")


        # labels
        lb_date = ctk.CTkLabel(self, text="Data", font=("Century Gothic bold",
                                    13), text_color=["#000", "#fff"])

        lb_name = ctk.CTkLabel(self, text="Cliente", font=("Century Gothic bold",
                                         13), text_color=["#000", "#fff"])
        
        lb_name_car = ctk.CTkLabel(self, text="Carro", font=("Century Gothic bold", 
                                        13), text_color=["#000", "#fff"])
        
        lb_celular = ctk.CTkLabel(self, text="Celular", font=("Century Gothic bold",
                                         13), text_color=["#000", "#fff"])
        
        lb_telefone = ctk.CTkLabel(self, text="Telefone", font=("Century Gothic bold",
                                         13), text_color=["#000", "#fff"])
        
        lb_endereco = ctk.CTkLabel(self, text="Endereço", font=("Century Gothic bold",
                                         13), text_color=["#000", "#fff"])
        
        lb_payment = ctk.CTkLabel(self, text="Visto de pagamento", font=("Century Gothic bold",
                                         13), text_color=["#000", "#fff"])
       
        lb_obs = ctk.CTkLabel(self, text="Observação", font=("Century Gothic bold",
                                         13), text_color=["#000", "#fff"])

        # POSIÇÃO DOS ELEMENTOS DA TELA
        lb_date.place(x=50, y=120)
        date_entry.place(x=50, y=150)
        
        lb_name.place(x=160, y=120)
        name_entry.place(x=160, y=150)

        lb_endereco.place(x=520, y=120)
        adress_entry.place(x=520, y=150)

        lb_telefone.place(x=50, y=200)
        tel_entry.place(x=50, y=230)

        lb_celular.place(x=260, y=200)
        cel_entry.place(x=260, y=230)

        lb_name_car.place(x=470, y=200)
        car_entry.place(x=470, y=230)

        lb_payment.place(x=730, y=200)
        payment_combo_box.place(x=730, y=230)

        lb_obs.place(x=50, y=270)
        obs_entry.place(x=50, y=300)


    def change_apm(self, new_appaerence_mode):
        ctk.set_appearance_mode(new_appaerence_mode)

if __name__=="__main__":
    app = App()
    app.mainloop()