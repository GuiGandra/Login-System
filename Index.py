#Importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase

#Criar nossa janela
jan = Tk()
jan.title('Aincrad Systems - Acess Panel')
jan.geometry('600x300')
jan.configure(background='white')
jan.resizable(width=False, height=False)
jan.iconbitmap(default='Imagens/Aincrad.ico')
# Caso queira dar transparencia -> jan.attributes('-alpha', 0.9)

#======= Carregando Imagens
logo = PhotoImage(file='Imagens/asuna.png')
kirito = PhotoImage(file='Imagens/Kirito 2.png')
congra = PhotoImage(file='Imagens/Congratulations.png')
klein = PhotoImage(file='Imagens/klein.png')

#=======Widgets============
LeftFrame = Frame(jan, width=200, height=300, bg='LIGHTSALMON', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=399, height=300, bg='CRIMSON', relief='raise')
RightFrame.pack(side=RIGHT)

KiritoLabel = Label(RightFrame, image=kirito, bg='CRIMSON')
KiritoLabel.place(x=50000, y=70)

kleinLabel = Label(RightFrame, image=klein, bg='CRIMSON')
kleinLabel.place(x=50000, y=120)

CongraLabel = Label(RightFrame, image=congra, bg='CRIMSON')
CongraLabel.place(x=50000, y=10)

LogoLabel = Label(LeftFrame, image=logo, bg='LIGHTSALMON')
LogoLabel.place(x=-50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=('Centur Gothic', 20), bg='CRIMSON', fg='White')
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=145, y=110)
#
PassLabel = Label(RightFrame, text="Password:", font=('Centur Gothic', 20), bg='CRIMSON', fg='White')
PassLabel.place(x=5, y=135)

PassEntry = ttk.Entry(RightFrame, width=30, show='*')
PassEntry.place(x=145, y=145)

def Register():
    #Removendo Widgets de login
    LoginButton.place(x=50000)
    RegisterButton.place(x=50000)
    #Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame, text='Name:', font=('Centur Gothic', 20), bg='CRIMSON', fg='White' )
    NomeLabel.place(x=5, y=38)
    NomeEntry= ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=90, y=49)

    EmailLabel = Label(RightFrame, text='Email:', font=('Centur Gothic', 20), bg='CRIMSON', fg='White')
    EmailLabel.place(x=5, y=68)
    EmailEntry= ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=90, y=79)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email == ""  and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="All Domains Need To Be Filled")
        else:
            DataBase.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBase.conn.commit()
            messagebox.showinfo(title='Register Info', message='Account Created Successfully')

    Register = ttk.Button(RightFrame, text='Register', width=30, command=RegisterToDataBase)
    Register.place(x=105, y=225)

    def BackToLogin():
        #Removendo Widgets de Cadastro
        NomeLabel.place(x=50000)
        NomeEntry.place(x=50000)
        EmailLabel.place(x=50000)
        EmailEntry.place(x=50000)
        Register.place(x=50000)
        #Trazendo de volta os Widgets de Login
        Back.place(x=50000)
        LoginButton.place(x=105)
        RegisterButton.place(x=105)
    Back = ttk.Button(RightFrame, text='Back', width=30, command=BackToLogin)
    Back.place(x=105, y=251)



RegisterButton = ttk.Button(RightFrame, text='Register', width=30, command=Register)
RegisterButton.place(x=105, y=251)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Selected")
    VerifyLogin = DataBase.cursor.fetchone()

    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            # messagebox.showinfo(title='Login Info', message='Access Successfully. Welcome!')
            UserLabel.place(x=50000)
            UserEntry.place(x=50000)
            PassLabel.place(x=50000)
            PassEntry.place(x=50000)
            KiritoLabel.place(x=250)
            RegisterButton.place(x=50000)
            LoginButton.place(x=50000)
            CongraLabel.place(x=50)
            kleinLabel.place(x=-50)

    except:
        messagebox.showerror(title='Login Info', message='Access Denied. Make sure you are registered in the system!')

    def BackToLogin():
        UserLabel.place(x=5)
        UserEntry.place(x=145)
        PassLabel.place(x=5)
        PassEntry.place(x=145)
        CongraLabel.place(x=50000)
        KiritoLabel.place(x=50000)
        Back.place(x=50000)
        LoginButton.place(x=105)
        RegisterButton.place(x=105)
        kleinLabel.place(x=50000)
    Back = ttk.Button(RightFrame, text='Back', width=30, command=BackToLogin)
    Back.place(x=105, y=251)

#Botoes
LoginButton = ttk.Button(RightFrame, text='Login', width=30, command=Login)
LoginButton.place(x=105, y=225)


jan.mainloop()
