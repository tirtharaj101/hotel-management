from tkinter import*
from types import TracebackType
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
import random
class Cust_Win:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x465+235+215")

        #==variable==#

        self.var_ref=StringVar()
        s=random.randint(1000,9999)
        self.var_ref.set(str(s))

        self.var_cname=StringVar()
        self.var_fname=StringVar()
        self.var_gender=StringVar()
        self.var_pin=StringVar()
        self.var_mobno=StringVar()
        self.var_email=StringVar()
        self.var_nt=StringVar()
        self.var_idproof=StringVar()
        self.var_idno=StringVar()
        self.var_add=StringVar()




        #==Title==#

        lbl_title=Label(self.root,text="Add Customer Details",font=("helvetica",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1100,height=50)

        #==logo==#
        img2=Image.open("C:/Users/TIRTHARAJ/Desktop/python projects/project1/images/gh.jpeg")
        img2=img2.resize((100,47), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=4, y=2, width=100, height=47)

        #==Left frame==#

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Information",font=("helvetica",10,"bold"),padx=2)
        labelframeleft.place(x=4,y=50,width=380,height=410)

        #--labels and entry==#

        #==customer reference==#

        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("helvetica",10,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,state="readonly",font=("helvetica",10,"bold"))
        entry_ref.grid(row=0,column=1)
        
        #==customer name==#
        cname=Label(labelframeleft,text="Customer Name",font=("helvetica",10,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cname,width=29,font=("helvetica",10,"bold"))
        txtcname.grid(row=1,column=1)

        #==customer fathers name==#
        lblfname=Label(labelframeleft,text="Fathers Name",font=("helvetica",10,"bold"),padx=2,pady=6)
        lblfname.grid(row=2,column=0,sticky=W)
        txtfname=ttk.Entry(labelframeleft,textvariable=self.var_fname,width=29,font=("helvetica",10,"bold"))
        txtfname.grid(row=2,column=1)

        #==customer gender==#

        lblgender=Label(labelframeleft,text="Gender",font=("helvetica",10,"bold"),padx=2,pady=6)
        lblgender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("helvetica",10,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Select","Male","Female","Others")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        #==customer pincode==#
        lblpin=Label(labelframeleft,text="Pincode",font=("helvetica",10,"bold"),padx=2,pady=6)
        lblpin.grid(row=4,column=0,sticky=W)
        txtpin=ttk.Entry(labelframeleft,textvariable=self.var_pin,width=29,font=("helvetica",10,"bold"))
        txtpin.grid(row=4,column=1)

        #==customer mobile number==#
        lblmobno=Label(labelframeleft,text="Mobile no",font=("helvetica",10,"bold"),padx=2,pady=6)
        lblmobno.grid(row=5,column=0,sticky=W)
        txtmobno=ttk.Entry(labelframeleft,textvariable=self.var_mobno,width=29,font=("helvetica",10,"bold"))
        txtmobno.grid(row=5,column=1)

        #==customer email==#

        lblemail=Label(labelframeleft,text="Email",font=("helvetica",10,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("helvetica",10,"bold"))
        txtemail.grid(row=6,column=1)

        #==customer nationality==#

        lblnt=Label(labelframeleft,text="Nationality",font=("helvetica",10,"bold"),padx=2,pady=6)
        lblnt.grid(row=7,column=0,sticky=W)
        combo_nt=ttk.Combobox(labelframeleft,textvariable=self.var_nt,font=("helvetica",10,"bold"),width=27,state="readonly")
        combo_nt["value"]=("Select","Indian","Bangladeshi","Pakistani","Others")
        combo_nt.current(0)
        combo_nt.grid(row=7,column=1)

        #==customer id proof type==#

        lblidpro=Label(labelframeleft,text="Id Proof Type",font=("helvetica",10,"bold"),padx=2,pady=6)
        lblidpro.grid(row=8,column=0,sticky=W)
        combo_idpro=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("helvetica",10,"bold"),width=27,state="readonly")
        combo_idpro["value"]=("Select","Adhaar Card","Passport","Voter Card","Others")
        combo_idpro.current(0)
        combo_idpro.grid(row=8,column=1)


        #==customer id proof number==#
        lblidno=Label(labelframeleft,text="Id Proof No",font=("helvetica",10,"bold"),padx=2,pady=6)
        lblidno.grid(row=9,column=0,sticky=W)
        txtidno=ttk.Entry(labelframeleft,textvariable=self.var_idno,width=29,font=("helvetica",10,"bold"))
        txtidno.grid(row=9,column=1)

        #==Customer address==#

        lbladd=Label(labelframeleft,text="Address",font=("helvetica",10,"bold"),padx=2,pady=6)
        lbladd.grid(row=10,column=0,sticky=W)
        txtadd=ttk.Entry(labelframeleft,textvariable=self.var_add,width=29,font=("helvetica",10,"bold"))
        txtadd.grid(row=10,column=1)

        #==CRUD buttons==#

        btn_create=Button(labelframeleft,text="Add",command=self.insert_data,font=("helvetica",10,"bold"),bg="black",fg="gold",cursor="hand2")
        btn_create.place(x=10,y=355,width=60)

        btn_update=Button(labelframeleft,text="Update",command=self.update,font=("helvetica",10,"bold"),bg="black",fg="gold",cursor="hand2")
        btn_update.place(x=100,y=355,width=60)

        btn_delete=Button(labelframeleft,text="Delete",font=("helvetica",10,"bold"),bg="black",fg="gold",cursor="hand2")
        btn_delete.place(x=190,y=355,width=60)

        btn_reset=Button(labelframeleft,text="Reset",command=self.reset,font=("helvetica",10,"bold"),bg="black",fg="gold",cursor="hand2")
        btn_reset.place(x=280,y=355,width=60)

        
        #==Right frame==#

        labelframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("helvetica",10,"bold"),padx=2)
        labelframeright.place(x=390,y=50,width=705,height=410)
        
        #==inside label==#
        lbl_search=Label(labelframeright,text="Search",font=("helvetica",10,"bold"),bg="black",fg="gold")
        lbl_search.place(x=2,y=4,width=60,height=25)
        
        #==combo box 1==#

        combo_box1=ttk.Combobox(labelframeright,font=("helvetica",10,"bold"),width=27,state="readonly")
        combo_box1["value"]=("Select","Reference No","Mobile Number")
        combo_box1.current(0)
        combo_box1.place(x=70,y=4)


        #==input box 2==#

        input_box2=ttk.Entry(labelframeright,font=("helvetica",10,"bold"),width=27)
        txtbox2=ttk.Entry(labelframeright,width=29,font=("helvetica",10,"bold"))
        input_box2.place(x=290,y=4,width=210)

        #==inside label button 1==#
        lbl_btn1=Button(labelframeright,text="Search",font=("helvetica",9,"bold"),bg="black",fg="gold",cursor="hand2")
        lbl_btn1.place(x=515,y=3,width=70,height=25)

        #==inside label button 2==#
        lbl_btn1=Button(labelframeright,text="Reset",font=("helvetica",9,"bold"),bg="black",fg="gold",cursor="hand2")
        lbl_btn1.place(x=600,y=3,width=70,height=25)

        #==Table frame==#
        tblframe=Frame(labelframeright,bd=4,relief=RIDGE)
        tblframe.place(x=0,y=50,width=690,height=335)

        #==scrollbar==#
        scroll_x=Scrollbar(tblframe,orient=HORIZONTAL)
        scroll_y=Scrollbar(tblframe,orient=VERTICAL)

        self.table1=ttk.Treeview(tblframe,columns=("ref","name","father","gender","pincode","mobile","email","nationality","idproof","idnumber","address"),show="headings")

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.table1.xview)
        scroll_y.config(command=self.table1.yview)

        
        self.table1.heading("ref",text="Refer no")
        self.table1.heading("name",text="Name")
        self.table1.heading("father",text="Fathersname")
        self.table1.heading("gender",text="Gender")
        self.table1.heading("pincode",text="Pincode")
        self.table1.heading("mobile",text="Mobile No")
        self.table1.heading("email",text="Email Id")
        self.table1.heading("nationality",text="Nationality")
        self.table1.heading("idproof",text="Id Proof Type")
        self.table1.heading("idnumber",text="Id no")
        self.table1.heading("address",text="Address")

        self.table1["show"]="headings"
        self.table1.column("ref",width=100)
        self.table1.column("name",width=100)
        self.table1.column("father",width=100)
        self.table1.column("gender",width=100)
        self.table1.column("pincode",width=100)
        self.table1.column("mobile",width=80)
        self.table1.column("email",width=100)
        self.table1.column("nationality",width=100)
        self.table1.column("idproof",width=100)
        self.table1.column("idnumber",width=100)
        self.table1.column("address",width=100)

        self.table1.pack(fill=BOTH,expand=1)

        self.table1.bind("<ButtonRelease-1>",self.select_data)



 

        self.fetch_data()
        #self.table1.bind("<ButtonRelease-1>",self.get_cursor)
        #self.fetch_data()
    def insert_data(self):
        if self.var_mobno.get()=="" or self.var_fname.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="iiht1")
                cur=con.cursor()
                cur.execute("INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                self.var_ref.get(),
                                                                                self.var_cname.get(),
                                                                                self.var_fname.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_pin.get(),
                                                                                self.var_mobno.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nt.get(),
                                                                                self.var_idproof.get(),
                                                                                self.var_idno.get(),
                                                                                self.var_add.get()

                                                                            ))
                                                                            

                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success","Data inserted successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="iiht1")
        cur=con.cursor()
        cur.execute("SELECT * FROM customer")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.table1.delete(*self.table1.get_children())
            for i in rows:
                self.table1.insert('',END,values=i)
                
    #==selecting==#

    def select_data(self,event=""):
        cur_row=self.table1.focus()
        content=self.table1.item(cur_row)
        row=content["values"]
        self.var_ref.set(row[0])
        self.var_cname.set(row[1]) 
        self.var_fname.set(row[2]) 
        self.var_gender.set(row[3])
        self.var_pin.set(row[4])
        self.var_mobno.set(row[5])
        self.var_email.set(row[6])
        self.var_nt.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idno.set(row[9])
        self.var_add.set(row[10])

    def update(self):
        if self.var_cname.get()=="":
            messagebox.showerror("Error!","Please fill up the all fields")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="iiht1")
                cur=con.cursor()
                cur.execute("update customer set name=%s,father=%s,gender=%s,pincode=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(
                                                                               
                                                                                self.var_cname.get(),
                                                                                self.var_fname.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_pin.get(),
                                                                                self.var_mobno.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nt.get(),
                                                                                self.var_idproof.get(),
                                                                                self.var_idno.get(),
                                                                                self.var_add.get(),
                                                                                self.var_ref.get()           
                                                                                                               
                                                                                 )) 
                con.commit()
                self.fetch_data()
                con.close() 
                messagebox.showinfo("update","Customer details update sucessfully") 

            except:
                messagebox.showerror("Error","Sorry could not updated")

    def reset(self):
        self.var_cname.set("") 
        self.var_fname.set("") 
        self.var_gender.set("Select")
        self.var_pin.set("")
        self.var_mobno.set("")
        self.var_email.set("")
        self.var_nt.set("Select")
        self.var_idproof.set("Select")
        self.var_idno.set("")
        self.var_add.set("")
        s=random.randint(1000,9999)
        self.var_ref.set(str(s))










    

if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()