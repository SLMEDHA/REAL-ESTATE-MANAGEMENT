from tkinter import *
from PIL import Image,ImageTk
from user_profile import user_prof

class RealestateDbms:
    def __init__(self, root):
        self.root = root
        self.root.title("SMart Property Rover")
        self.root.geometry("1550x800+0+0")
        
        
        # top img
        img1 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\upp.png")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        #logo
        img2 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\rlogo.png")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
        
        #title
        lbl_title=Label(self.root,text="SMart Property Rover",font=("times new roman",34,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        
        #frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        #profile
        lbl_title=Label(main_frame,text="Estate_details",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=230,height=50)
        
       #btn frame
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
        
        usr_btn=Button(btn_frame,text="User_profile",command=self.user_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        usr_btn.pack()
        
        
        #right midd side img
        img3 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\mid.png")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)
        
        
    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=user_prof(self.new_window)
        
        
if __name__ == "__main__":
    root = Tk()
    obj = RealestateDbms(root)
    root.mainloop()
