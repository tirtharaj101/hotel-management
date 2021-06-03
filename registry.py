from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="violet")

        #====insertintg image====#

        self.left=ImageTk.PhotoImage(file="images/reg.jpeg")
        left=Label(self.root, image=self.left).place(x=120, y=100 , width=400, height=500)

        #====register frame====#

        frame1=Frame(self.root, bg="white")
        frame1.place(x=520 , y=100 , width=700 , height=500)

        #=frame insider

        title=Label(frame1,text="REGISTER HERE",font=("arial", 25 , "bold"),bg="white",fg="green").place(x=50,y=30)

        #=row-1

        
        f_name=Label(frame1,text="FIRST NAME",font=("arial" ,15, "bold"),bg="white",fg="grey").place(x= 50,y=100)
        self.txt_fname=Entry(frame1,font=("arial" ,15),bg="lightgrey",fg="grey")
        self.txt_fname.place(x= 50,y=130,width=250)

        l_name=Label(frame1,text="LAST NAME",font=("arial" ,15, "bold"),bg="white",fg="grey").place(x= 370,y=100)
        txt_lname=Entry(frame1,font=("arial" ,15),bg="lightgrey",fg="grey").place(x=370,y=130,width=250)
        
        #=row 2

        m_no=Label(frame1,text="MOBILE NUMBER",font=("arial" ,15, "bold"),bg="white",fg="grey").place(x=50,y=170)
        txt_m_no=Entry(frame1,font=("arial" ,15),bg="lightgrey",fg="grey").place(x= 50,y=200,width=250)

        email=Label(frame1,text="EMAIL",font=("arial" ,15, "bold"),bg="white",fg="grey").place(x= 370,y=170)
        txt_email=Entry(frame1,font=("arial" ,15),bg="lightgrey",fg="grey").place(x=370,y=200,width=250)

        #row3

        ques=Label(frame1,text="SECURITY QUESTION",font=("arial" ,15, "bold"),bg="white",fg="grey").place(x= 50,y=240)
        cmb_quest=ttk.Combobox(frame1,font=("arial", 13 ),state='readonly')
        cmb_quest['values']=("Select","Your pet name","Your birth plaace","Your best friend name")
        cmb_quest.place(x=50,y=270,width=250)
        cmb_quest.current(0)

        
        ques_ans=Label(frame1,text="SECURITY ANSWER",font=("arial" ,15, "bold"),bg="white",fg="grey").place(x=370,y=240)
        txt_ques_ans=Entry(frame1,font=("arial",15,),bg="lightgrey",fg="grey").place(x=370,y=270,width=250)

        #====row4====#
        
        password=Label(frame1,text="PASSWORD",font=("arial",15,"bold"),bg="white",fg="grey").place(x=50,y=310)
        txt_password=Entry(frame1,font=("arial",15),bg="lightgrey",fg="grey").place(x=50,y=340,width=250)

        com_password=Label(frame1,text="CONFIEM PASSWORD",font=("arial",15,"bold"),bg="white",fg="grey").place(x=370,y=310)
        txt_com_password=Entry(frame1,font=("arial",15),bg="lightgrey",fg="grey").place(x=370,y=340,width=250)

        #====submit button====#
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",onvalue=1,offvalue=0,font=("arial",12),bg="white").place(x=50,y=380)

        #====picture button====#
        self.btn_img=ImageTk.PhotoImage(file="images/reg.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=250,y=420)

        #====log in====#
        btn_login=Button(self.root,text="Sign In",font=("arial",15,"bold"),bg="orange",fg="white",cursor="hand2").place(x=230,y=530,width=180)




    def register_data(self):
        print(self.txt_fname.get(),
        print(self.text_lname.get())


root=Tk()
obj=Register(root)
root.mainloop()