from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import pymysql
from hotel import HotelManagementSystem
#from registration import Register
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Form")
        self.root.geometry("1350x700+0+0")

        self.photo=ImageTk.PhotoImage(file="images/registration.jpg")
        photo=Label(self.root,image=self.photo,anchor=NW).place(x=0,y=0)
        


        self.left=ImageTk.PhotoImage(file="images/reg.jpeg")
        left=Label(self.root, image=self.left).place(x=120,y=100, width=400, height=500)

        #===Login Frame===#
        frame1=Frame(self.root,bg="gold")
        frame1.place(x=520, y=100, width=700, height=500)

        
       

        #===Frame Insider=====#
        title=Label(frame1, text="LOGIN HERE", font=("arial", 25, "bold"),bg="gold", fg="green").place(x=50, y=30)

        #====row-1====#
        email=Label(frame1, text="Email/Username", font=("arial", 15, "bold"),bg="gold", fg="black").place(x=50, y=100)
        self.txt_email=Entry(frame1, font=("arial",15), bg="white")
        self.txt_email.place(x=50, y=130, width=600)

        
        #====row-2====#
        password=Label(frame1, text="Password", font=("arial", 15, "bold"),bg="gold", fg="black").place(x=50, y=170)
        self.txt_password=Entry(frame1, font=("arial",15), bg="white",show="*")
        self.txt_password.place(x=50, y=200, width=600)
        #button
        self.btn_img1=ImageTk.PhotoImage(file="images/ty.png")
        btn_reg=Button(self.root,image=self.btn_img1,bd=0,bg="gold",cursor="hand2",command=self.login_data).place(x=570,y=360)

        self.btn_img2=ImageTk.PhotoImage(file="images/signup.png")
        btn_login=Button(self.root,command=self.register,image=self.btn_img2,bd=0,bg="aqua",cursor="hand2").place(x=270,y=530)
    

    

    def login_data(self):
        if self.txt_email.get()==""  or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        
        else:
            try:
                con=pymysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="iiht1"
                )
                cur=con.cursor()
                cur.execute("SELECT * from  students where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("faliure","Login Faliure",parent=self.root)
                else:
                    #self.hotel
                    #messagebox.showinfo("Success","Login successful",parent=self.root) 
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                    
            except Exception as es:
                messagebox.showerror("Error","Registrations failure",parent=self.root)    
    
    def register(self):
        root.destroy()
        import registration
        

root=Tk()
obj=Login(root)
root.mainloop()