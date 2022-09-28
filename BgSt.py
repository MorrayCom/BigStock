# page acceuil admin
from subprocess import call
from tkinter import *
from tkinter import ttk

import customtkinter as customtkinter
from PIL import Image, ImageTk


# import mysql.connector
# from tkinter import mess

def prodmag():
    fenetre2.destroy()
    call(["python", "prodmag.py"])


def acceuil():
    fenetre2.destroy()
    call(["python", "acceuilmag.py"])


def statiquemag():
    fenetre2.destroy()
    call(["python", "statiquemag.py"])


def fournmag():
    fenetre2.destroy()
    call(["python", "fourmag.py"])


def fenetre():
    fenetre2.destroy()
    call(["python", "acceilmag.py"])


def livrmag():
    fenetre2.destroy()
    call(["python", "livrmag.py"])


fenetre2 = Tk()
fenetre2.title("page d'acceil Admin")
fenetre2.geometry("1000x620")
fenetre2.resizable(False, False)
fenetre2.configure(bg="white")

# can = Canvas(fenetre2, width=1000, height=275, bg="#0ea598")
# img = PhotoImage(file="C:\\Users\\lenovo\\PycharmProjects\\pythonProject1\\BigStock\\stock.gif")
# can.create_image(1000,275, anchor=NW, image=img)
# can.place(x="",y="")
# corps
fram = Frame(fenetre2, bg='#FFFFFF', width='1000', height='250')
fram.place(x='', y='')

photo = ImageTk.PhotoImage(Image.open("C:\\Users\\lenovo\\Downloads\\fret.png"))
x = Label(fram, image=photo)
x.place(x='', y='')

bouton = customtkinter.CTkButton(master=fram, text="Accueil", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=prodmag)
bouton.place(x='10', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Produits", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=prodmag)
bouton.place(x='180', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Magasinier", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=prodmag)
bouton.place(x='360', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Fournisseur", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=prodmag)
bouton.place(x='570', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Deconnexion", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=prodmag)
bouton.place(x='800', y='170')
# recherche
logo = Label(fram, text="Bienvenue Administrateur!!!", font=('Italic', 20))
logo.place(x="640", y="60")
# logo
logo = Label(fram, text=" BIGSTOCK", font=('Italic', 35))
logo.place(x="40", y="40")

fram0 = Frame(fenetre2, width='1000', height='370')
fram0.place(x='', y='250')

# logo=PhotoImage(file=r"BIG STOCK1.png")
# img=Button( image=logo).place(x=10,y=20)
prod0 = Button(fram0, text="Total Produits\n      104", bg="#319BFE", command=prodmag, fg="white", font=('', 25,),
               width="15", height="3")
prod0.place(x="10", y="80")
prod1 = Button(fram0, text="Total Magasiniers\n     3", bg="#319BFE", command=livrmag, fg="white", font=('', 25,),
               width="15", height="3")
prod1.place(x="350", y="80")
prod2 = Button(fram0, text="Total Fournisseurs\n       15 ", bg="#319BFE", fg="white", command=fournmag, font=('', 25,),
               width="15", height="3")
prod2.place(x="700", y="80")

# copyrith
preven = Label(fenetre2, text="Copyright @ 0101 par Groupe 2/ODC", font=("Arial", 10))
preven.place(x="350", y="600")

fenetre2.mainloop()
