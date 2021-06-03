from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Room



class HotelManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1350x700+0+0")

        #================wide image=====================#
        img1=Image.open("C:/Users/TIRTHARAJ/Desktop/python projects/project1/images/1.jpeg")
        img1=img1.resize((1350,140), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0, y=0, width=1350, height=140)

        #==logo image==#
        
        img2=Image.open("C:/Users/TIRTHARAJ/Desktop/python projects/project1/images/gh.jpeg")
        img2=img2.resize((230,140), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)
        
        #==title bar==#

        lbl_title=Label(self.root,text="Hotel Management System",font=("helvetica",35,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1350,height=50)

        #==main frame==#

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1350,height=620)
        
        #==Menu==#

        lbl_menu=Label(main_frame,text="Menu",font=("helvetica",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        ##==button frame==#

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=190)

        cust_btn1=Button(btn_frame,text="Customer",command=self.cust_details,width=18,font=("helvetica",14,"bold"),bg="black",fg="skyblue",bd=0,cursor="hand2")
        cust_btn1.grid(row=0,column=0,pady=1)

        cust_btn=Button(btn_frame,text="Room",command=self.room_details,width=18,font=("helvetica",14,"bold"),bg="black",fg="skyblue",bd=0,cursor="hand2")
        cust_btn.grid(row=1,column=0,pady=1)

        cust_btn=Button(btn_frame,text="Details",width=18,font=("helvetica",14,"bold"),bg="black",fg="skyblue",bd=0,cursor="hand2")
        cust_btn.grid(row=2,column=0,pady=1)

        cust_btn=Button(btn_frame,text="Report",width=18,font=("helvetica",14,"bold"),bg="black",fg="skyblue",bd=0,cursor="hand2")
        cust_btn.grid(row=3,column=0,pady=1)

        cust_btn=Button(btn_frame,text="Logout",command=self.logout,width=18,font=("helvetica",14,"bold"),bg="black",fg="skyblue",bd=0,cursor="hand2")
        cust_btn.grid(row=4,column=0,pady=1)

        #==right image==#

        img3=Image.open("C:/Users/TIRTHARAJ/Desktop/python projects/project1/images/2.jpeg")
        img3=img3.resize((1110,500), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=230, y=0, width=1110, height=500)


        img4=Image.open("C:/Users/TIRTHARAJ/Desktop/python projects/project1/images/6.jpeg")
        img4=img4.resize((230,140), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0, y=220, width=230, height=140)
        
        img5=Image.open("C:/Users/TIRTHARAJ/Desktop/python projects/project1/images/3.jpeg")
        img5=img5.resize((230,140), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0, y=360, width=230, height=140)




    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Room(self.new_window)
    def logout(self):
        root.destroy()






if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()