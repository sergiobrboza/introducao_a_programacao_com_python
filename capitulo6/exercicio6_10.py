
import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Radiobutton
from tkinter.ttk import Combobox
import random
import string

root = Tk()


class application():
    def __init__(self):
        self.root = root
        self.window()
        self.colors()
        self.widgets()
        self.password_generator()
        root.mainloop()

    def colors(self):
        self.color1 = '#a63737' # Red
        self.color2 = '#f0e6e6' # Beige
        self.color3 = '#fcfcfc' # White
        self.color4 = '#423e69' # Dark purple
        
    def window(self):
        self.root.title('PASSWORD GENERATOR')
        self.root.iconbitmap(r'password_generator\senha.ico')
        self.root.geometry('350x400')
        self.root.config(bg=colors.color2)
        self.root.resizable(False, False)

    def widgets(self):
        # Título
        self.lb_title1 = Label(self.root, text='PASSWORD', bg=self.color2, fg=self.color1,
         font=('Verdana 16 bold'))
        self.lb_title1.place(relx=0.31, rely=0.02, relwidth=0.4)

        self.lb_title2 = Label(self.root, text='GENERATOR', bg=self.color2, fg=self.color4,
         font=('Verdana 10 bold'))
        self.lb_title2.place(relx=0.36, rely=0.08, relwidth=0.3)

        # Senha
        self.ent_password = Entry(self.root, font='Arial 10 ')
        self.ent_password.place(relx=0.12, rely=0.18, relwidth=0.66)

        # Copiar a senha
        self.bt_copy = Button(self.root, text='COPY', bd=3, bg=self.color4, fg=self.color3,
         font='Verdana 7 bold')
        self.bt_copy.place(relx=0.82 , rely=0.175)

        # Label de quantidade de caracteres presentes na senha
        self.lb_amount = Label(self.root, text='Quantidade de caracteres:', bg=self.color2, fg=self.color4,
         font=('Verdana 11 bold'))
        self.lb_amount.place(relx=0.12, rely=0.3)

        # Criação da Combobox
        self.combo = Combobox(root, state="readonly")
        self.combo['values'] = (4, 6, 8, 10, 12, 14, 16)
        self.combo.current(0)
        self.combo.place(relx=0.82, rely=0.3, relwidth=0.11)

        # Configuração da senha
        var = tk.StringVar()

        self.lt_uppercase = Radiobutton(self.root, bg=self.color2, fg=self.color4,
         text='Maiúsculas', variable=var, value="1", font='Verdana 11 bold') # Adiciona Letras Maiúsculas
        self.lt_uppercase.place(relx=0.12, rely=0.45) 

        self.lt_tiny = Radiobutton(self.root, bg=self.color2, fg=self.color4,
         text='Minusculas', variable=var, value="2", font='Verdana 11 bold') # Adiciona Letras Mínusculas
        self.lt_tiny.place(relx=0.54, rely=0.45)

        self.lt_symbols = Radiobutton(self.root, bg=self.color2, fg=self.color4,
         text='Caracteres', variable=var, value="3", font='Verdana 11 bold') # Adiciona Símbolos
        self.lt_symbols.place(relx=0.12, rely=0.55)

        self.lt_number = Radiobutton(self.root, bg=self.color2, fg=self.color4,
        text='Números', variable=var, value="4", font='Verdana 11 bold') # Adiciona Números
        self.lt_number.place(relx=0.54, rely=0.55)

        # Botão para gerar a senha
        self.bt_pass_strong = Button(self.root, text='Gerar senha forte', bd=3, bg=self.color4, fg=self.color3,
         font='Verdana 10 bold') # Utilizada para gerar senhas com todas as opções
        self.bt_pass_strong.place(relx=0.29, rely=0.7, relwidth=0.42)

        self.bt_gene_password = Button(self.root, text='Gerar senha', bd=3, bg=self.color4, fg=self.color3,
         font='Verdana 10 bold') # Gera a senha selecionada pelo user
        self.bt_gene_password.place(relx=0.32, rely=0.82, relwidth=0.36)

    def password_generator(self):
        password_length = int(self.combo.get())

        use_uppercase = self.lt_uppercase.var.get() == '1'
        use_lowercase = self.lt_tiny.var.get() == '2'
        use_symbols = self.lt_symbols.var.get() == '3'
        use_numbers = self.lt_number.var.get() == '4'

app = application()