from tkinter import *

fenetre = Tk()
fenetre.geometry('1000x620')
fenetre.configure(background="white")
fenetre.resizable(height=FALSE, width =FALSE)
fenetre.title('BigStock')
#admin et reccherch

frame0 = Frame(fenetre,width=1000, height=185, bg="#D9D9D9")
txtId = Entry(fenetre,  font=("",20))
txtId.place(x='390', y='135')
label0 = Label(fenetre, text="Admin",font=("Arial_bold", 20), bg='#D9D9D9')
label0.place(x='880',y='120')
frame0.place(x='0', y='0')

#frame menu
frame = Frame(fenetre, width=250, height=425, bg="#395FB8")
label = Label(fenetre, text="Menu", font=("Arial_bold", 30), bg='#395FB8', fg='white')
label.place(x='815', y='215')
# label.pack(side='right')
bouton=Button(fenetre, text="Produits",  font=("",20), width=12)
bouton.place(x='750', y='280')
bouton=Button(fenetre, text="Magasiniers",  font=("",20), width=12)
bouton.place(x='750', y='340')
bouton=Button(fenetre, text="Fournisseurs", font=("",20), width=12)
bouton.place(x='750', y='400')
bouton=Button(fenetre, text="Deconnexion", font=("",20), bg='#060638', fg='white')
bouton.place(x='770', y='510')
frame.place(x='745', y='190')
#corps
frame0 = Frame(fenetre,width=740, height=425, bg="#D9D9D9")
bouton=Button(fenetre, text="Produits",  font=("",30), width=12, bg='#395FB8',  fg='white')
bouton.place(x='20', y='280')
bouton=Button(fenetre, text="Magasiniers",  font=("",30), width=12, bg='#395FB8',  fg='white')
bouton.place(x='380', y='280')
bouton=Button(fenetre, text="Fournisseurs", font=("",30), width=12, bg='#395FB8',  fg='white')
bouton.place(x='20', y='400')
bouton=Button(fenetre, text="Statistique", font=("",30), width=12, bg='#395FB8', fg='white')
bouton.place(x='380', y='400')
frame0.place(x='0', y='190')


fenetre.mainloop()