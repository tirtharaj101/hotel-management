from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registraion form")
        self.root.geometry("1350x700+10+0")

        self.photo=ImageTk.PhotoImage(file="images/registration.jpg")
        photo=Label(self.root,image=self.photo,anchor=NW).place(x=0,y=0)
        


        self.left=ImageTk.PhotoImage(file="images/reg.jpeg")
        left=Label(self.root, image=self.left).place(x=120,y=100, width=400, height=500)

        #===Register Frame===#
        frame1=Frame(self.root,bg="gold")
        frame1.place(x=520, y=100, width=700, height=500)

        
       

        #===Frame Insider=====#
        title=Label(frame1, text="REGISTER HERE", font=("arial", 25, "bold"),bg="gold", fg="green").place(x=50, y=30)

        #====row-1====#
        f_name=Label(frame1, text="First Name", font=("arial", 15, "bold"),bg="gold", fg="black").place(x=50, y=100)
        self.txt_fname=Entry(frame1, font=("arial",15), bg="white")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name=Label(frame1, text="Last Name", font=("arial", 15, "bold"),bg="gold", fg="black").place(x=370, y=100)
        self.txt_lname=Entry(frame1, font=("arial",15), bg="white")
        self.txt_lname.place(x=370, y=130, width=250)

        #====row-2====#
        Contact=Label(frame1, text="Contact No.", font=("arial", 15, "bold"),bg="gold", fg="black").place(x=50, y=170)
        self.txt_contact=Entry(frame1, font=("arial",15), bg="white")
        self.txt_contact.place(x=50, y=200, width=250)

        email=Label(frame1, text="Email", font=("arial", 15, "bold"),bg="gold", fg="black").place(x=370, y=170)
        self.txt_email=Entry(frame1, font=("arial",15), bg="white")
        self.txt_email.place(x=370, y=200, width=250)
  
        #====row-3====#       
        question=Label(frame1, text="Security Question", font=("arial", 15, "bold"),bg="gold", fg="black").place(x=50, y=240)
        self.cmb_quest=ttk.Combobox(frame1, font=("arial",13), state='readonly')
        self.cmb_quest['values']=("Select", "Your Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1, text="Answer", font=("arial", 15, "bold"),bg="gold", fg="black").place(x=370, y=240)
        self.txt_answer=Entry(frame1, font=("arial",15), bg="white")
        self.txt_answer.place(x=370, y=270, width=250)

        #====row-4====#
        password=Label(frame1, text="Password", font=("arial", 15, "bold"),bg="gold", fg="black").place(x=50, y=310)
        self.txt_password=Entry(frame1, font=("arial",15), bg="white",show="*")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword=Label(frame1, text="Confirm Password", font=("arial", 15, "bold"),bg="gold", fg="black").place(x=370, y=310)
        self.txt_cpassword=Entry(frame1, font=("arial",15), bg="white",show="*")
        self.txt_cpassword.place(x=370, y=340, width=250)

        #====Terms====#

        self.var_chk=IntVar()
        chk=Checkbutton(frame1, text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1, offvalue=0, bg="gold", font=("arial", 12)).place(x=50, y=380)

        #====Button====#
        self.btn_img=ImageTk.PhotoImage(file="images/reg.png")
        btn_register=Button(frame1, image=self.btn_img, bd=0, cursor="hand2",bg="gold", command=self.register_data).place(x=220, y=420)
        self.btn_img1=ImageTk.PhotoImage(file="images/ty.png")
        btn_login=Button(self.root,image=self.btn_img1,bd=0,bg="aqua",cursor="hand2",command=self.login).place(x=270,y=530)
    
    def login(self):
        root.destroy()
        import login

    




    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password Field Does Not Match",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree To Our Terms And Condition",parent=self.root)

        else:
            try:
                con=pymysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="iiht1"
                )
                cur=con.cursor()
                cur.execute("INSERT INTO students(f_name,l_name,contact,email,question,answer,password)VALUES(%s,%s,%s,%s,%s,%s,%s)",
                             (self.txt_fname.get(),
                              self.txt_lname.get(),
                              self.txt_contact.get(),
                              self.txt_email.get(),
                              self.cmb_quest.get(),
                              self.txt_answer.get(),
                              self.txt_password.get()
                              ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Register Successfull",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error","Registration failure",parent=self.root)



    


root=Tk()
obj=Register(root)
root.mainloop()