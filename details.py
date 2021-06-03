from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox


class Details:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x465+235+215")

        #==Title==#

        lbl_title=Label(self.root,text="Details",font=("helvetica",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1100,height=50)

        #==logo==#
        img2=Image.open("C:/Users/TIRTHARAJ/Desktop/python projects/project1/images/gh.jpeg")
        img2=img2.resize((100,47), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=4, y=2, width=100, height=47)

        #==left Frame==#

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,font=("helvetica",10,"bold"),padx=2)
        labelframeleft.place(x=4,y=50,width=380,height=410)

        #==left frame image==#

        img3=Image.open("C:/Users/TIRTHARAJ/Desktop/python projects/project1/images/5.jpeg")
        img3=img3.resize((370,400), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(labelframeleft,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=0, y=0, width=370, height=400)

        #==Right frame==#

        labelframeright=LabelFrame(self.root,bd=2,relief=RIDGE,font=("helvetica",10,"bold"),padx=2)
        labelframeright.place(x=390,y=50,width=705,height=410)

        lbl_about=Label(labelframeright,text="About Us",font=("helvetica",18,"bold"),bg="black",fg="gold")
        lbl_about.place(x=300,y=20)

       







if __name__=="__main__":
    root=Tk()
    obj=Details(root)
    root.mainloop()