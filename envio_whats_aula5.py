import webbrowser
import pyautogui
import pyautogui as pg
import sqlite3
import datetime
import calendar
from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import messagebox

class Whats_envio():
    def __init__(self):
        self.whats_tela()
    def whats_tela(self):
        self.janela = Tk()
        self.janela.title("Mensagens Whatsapp")
        self.janela.geometry("1000x750+70+30")
        self.janela.resizable(False, False)

        Label_principal = Label(self.janela, text="Mensagens Whatsapp")
        Label_principal.place(relx=0.3, rely=0, relwidth=0.4, relheight=0.05)

        data_frame = Label(self.janela, text="Selecione a data:")
        data_frame.place(relx=0.05, rely=0, relwidth=0.2, relheight=0.05)

        self.data_envio = Calendar(self.janela, text="Código", locale="pt")
        self.data_envio.place(relx=0.05, rely=0.05, relwidth=0.3, relheight=0.22)

        self.barracliente = ttk.Scrollbar(self.janela, orient='vertical')
        self.nome_entry = ttk.Treeview(self.janela, height=6,
                yscrollcommand=self.barracliente.set, column=("col1", "col2", "col3", "col4"))
        self.nome_entry.heading("#0", text="")
        self.nome_entry.column("#0", width=-10)
        self.nome_entry.heading("#1", text="Hora")
        self.nome_entry.column("#1", width=30)
        self.nome_entry.heading("#2", text="Nome")
        self.nome_entry.column("#2", width=70)
        self.nome_entry.heading("#3", text="DDD")
        self.nome_entry.column("#3", width=15)
        self.nome_entry.heading("#4", text="Fone")
        self.nome_entry.column("#4", width=70)

        self.nome_entry.place(relx=0.03, rely=0.3, relwidth=0.34, relheight=0.65)


        self.janela.mainloop()


Whats_envio()