from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql


class Room:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x465+235+215")


         #==variable==#

        self.var_rno=StringVar()
        self.var_bno=StringVar()
        self.var_btype=StringVar()
        self.var_rtype=StringVar()
        self.var_broom=StringVar()
        self.var_roomsrv=StringVar()

         #==Title==#

        lbl_title=Label(self.root,text="Add Room Details",font=("helvetica",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1100,height=50)

        #==logo==#
        img2=Image.open("C:/Users/TIRTHARAJ/Desktop/python projects/project1/images/gh.jpeg")
        img2=img2.resize((100,47), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=4, y=2, width=100, height=47)

        #==Left frame==#

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Information",font=("helvetica",10,"bold"),padx=2)
        labelframeleft.place(x=4,y=50,width=380,height=410)

        #==Room no==#
        roomno=Label(labelframeleft,text="Room no",font=("helvetica",10,"bold"),padx=2,pady=6)
        roomno.grid(row=1,column=0,sticky=W)
        txtroomno=ttk.Entry(labelframeleft,textvariable=self.var_rno,width=29,font=("helvetica",10,"bold"))
        txtroomno.grid(row=1,column=1)
        
        #==Bed no==#
        roomno=Label(labelframeleft,text="Bed no",font=("helvetica",10,"bold"),padx=2,pady=6)
        roomno.grid(row=2,column=0,sticky=W)
        txtroomno=ttk.Entry(labelframeleft,textvariable=self.var_bno,width=29,font=("helvetica",10,"bold"))
        txtroomno.grid(row=2,column=1)

        #==Bed Type==#
        bedtype=Label(labelframeleft,text="Bed Type",font=("helvetica",10,"bold"),padx=2,pady=6)
        bedtype.grid(row=3,column=0,sticky=W)
        combo_btype=ttk.Combobox(labelframeleft,textvariable=self.var_btype,font=("helvetica",10,"bold"),width=27,state="readonly")
        combo_btype["value"]=("Select","Double","Single","Others")
        combo_btype.current(0)
        combo_btype.grid(row=3,column=1)

        #==Room Type==#
        roomtype=Label(labelframeleft,text="Room Type",font=("helvetica",10,"bold"),padx=2,pady=6)
        roomtype.grid(row=4,column=0,sticky=W)
        combo_rtype=ttk.Combobox(labelframeleft,textvariable=self.var_rtype,font=("helvetica",10,"bold"),width=27,state="readonly")
        combo_rtype["value"]=("Select","Air Conditioned","Non Air Conditioned")
        combo_rtype.current(0)
        combo_rtype.grid(row=4,column=1)

        #==Bathroom Type==#
        bthroomtype=Label(labelframeleft,text="Bathroom Type",font=("helvetica",10,"bold"),padx=2,pady=6)
        bthroomtype.grid(row=5,column=0,sticky=W)
        combo_rtype=ttk.Combobox(labelframeleft,textvariable=self.var_broom,font=("helvetica",10,"bold"),width=27,state="readonly")
        combo_rtype["value"]=("Select","Attached","Common")
        combo_rtype.current(0)
        combo_rtype.grid(row=5,column=1)

        #==Room Service==#
        roomsrv=Label(labelframeleft,text="Room Service",font=("helvetica",10,"bold"),padx=2,pady=6)
        roomsrv.grid(row=6,column=0,sticky=W)
        combo_rtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomsrv,font=("helvetica",10,"bold"),width=27,state="readonly")
        combo_rtype["value"]=("Select","Yes","No")
        combo_rtype.current(0)
        combo_rtype.grid(row=6,column=1)

        #==CRUD buttons==#

        btn_create=Button(labelframeleft,text="Add",command=self.insert_data,font=("helvetica",10,"bold"),bg="black",fg="gold",cursor="hand2")
        btn_create.place(x=10,y=355,width=60)

        btn_update=Button(labelframeleft,text="Update",font=("helvetica",10,"bold"),bg="black",fg="gold",cursor="hand2")
        btn_update.place(x=100,y=355,width=60)

        btn_delete=Button(labelframeleft,text="Delete",font=("helvetica",10,"bold"),bg="black",fg="gold",cursor="hand2")
        btn_delete.place(x=190,y=355,width=60)

        btn_reset=Button(labelframeleft,text="Reset",font=("helvetica",10,"bold"),bg="black",fg="gold",cursor="hand2")
        btn_reset.place(x=280,y=355,width=60)

        #==Right frame==#

        labelframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("helvetica",10,"bold"),padx=2)
        labelframeright.place(x=390,y=50,width=705,height=410)

         #==inside label==#
        lbl_search=Label(labelframeright,text="Search",font=("helvetica",10,"bold"),bg="black",fg="gold")
        lbl_search.place(x=2,y=4,width=60,height=25)
        
        #==combo box 1==#

        combo_box1=ttk.Combobox(labelframeright,font=("helvetica",10,"bold"),width=27,state="readonly")
        combo_box1["value"]=("Select","Room No","Room Type")
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

        self.table1=ttk.Treeview(tblframe,columns=("RoomNo","BedNo","Bedtype","RoomType","Bathroom","RoomService"),show="headings")

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.table1.xview)
        scroll_y.config(command=self.table1.yview)

        
        self.table1.heading("RoomNo",text="RoomNo")
        self.table1.heading("BedNo",text="BedNo")
        self.table1.heading("Bedtype",text="BedType")
        self.table1.heading("RoomType",text="RoomType")
        self.table1.heading("Bathroom",text="Bathroom")
        self.table1.heading("RoomService",text="RoomService")

        self.table1["show"]="headings"
        self.table1.column("RoomNo",width=100)
        self.table1.column("BedNo",width=100)
        self.table1.column("Bedtype",width=100)
        self.table1.column("RoomType",width=100)
        self.table1.column("Bathroom",width=100)
        self.table1.column("RoomService",width=80)

        self.table1.pack(fill=BOTH,expand=1)

        self.fetch_data()

    def insert_data(self):
        if self.var_rno.get()=="" or self.var_bno.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="iiht1")
                cur=con.cursor()
                cur.execute("INSERT INTO room VALUES(%s,%s,%s,%s,%s,%s)",(

                                                                        self.var_rno.get(),
                                                                        self.var_bno.get(),
                                                                        self.var_btype.get(),
                                                                        self.var_rtype.get(),
                                                                        self.var_broom.get(),
                                                                        self.var_roomsrv.get(),
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
        cur.execute("SELECT * FROM room")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.table1.delete(*self.table1.get_children())
            for i in rows:
                self.table1.insert('',END,values=i)




        



if __name__=="__main__":
    root=Tk()
    obj=Room(root)
    root.mainloop()