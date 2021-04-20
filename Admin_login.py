import tkinter
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Login System")
        self.root.geometry("1350x700+0+0")
    
    #=======All Images=======
        self.bg_icon=ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon=PhotoImage(file="images/user.png")
        self.password_icon=PhotoImage(file="images/password.png")
        self.admin_icon=PhotoImage(file="images/admin.png")
        self.login_icon=PhotoImage(file="images/login.png")

        #=====Variables=======
        self.uname=StringVar()
        self.pass_=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon).pack()

        title=Label(self.root,text="Admin Login",font=("Segoe UI",30,"bold"),bg="navy blue",fg="white")
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        adminlbl=Label(Login_Frame,image=self.admin_icon,bg="white",bd=0).grid(row=0,columnspan=2,pady=10)

        lbluser=Label(Login_Frame,text="Username/Email",image=self.user_icon,compound=LEFT,font=("Segoe UI",15,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=2,textvariable=self.uname,relief=SOLID,font=("Segoe UI",15)).grid(row=1,column=1,padx=20)

        lblpassword=Label(Login_Frame,text="Password",image=self.password_icon,compound=LEFT,font=("Segoe UI",15,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpassword=Entry(Login_Frame,bd=2,textvariable=self.pass_,relief=SOLID,font=("Segoe UI",15)).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame,image=self.login_icon,bg="white",bd=0,command=self.login_).grid(row=3,column=1,pady=5)

    def login_(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.uname.get()=="admin" or "admin@gmail.com" and self.pass_.get()=="162002":
            messagebox.showinfo("Sucessfull","Welcome Admin")
        else:
            messagebox.showerror("Error","Invalid Username/email or Password")


    




root=Tk()
obj=Login_System(root)
root.mainloop()
