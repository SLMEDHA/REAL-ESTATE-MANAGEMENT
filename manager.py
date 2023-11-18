from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_Win
from seller import Seller_Win
from property import Property_Win
from register import Register_Win
from decide import Decide_Win
from approve import Approve_Win

class RealestateDbmsManager:
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
        lbl_title=Label(self.root,text="SMart Property Rover",font=("times new roman",29,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        #frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        #button frame
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE, bg="black")
        btn_frame.place(x=0,y=35,width=225,height=350)

        #menu label in main fraem
        lbl_menu=Label(main_frame,text="Estate Info",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=225)
        #Rest buttons in button frame
        #admin profile
        btn_1=Button(btn_frame,text="Buyer Details",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,command=self.cust_details)
        btn_1.grid(row=0,column=0,padx=40,pady=10)

        #register property
        btn_2=Button(btn_frame,text="Seller details",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,command=self.sell_details)
        btn_2.grid(row=1,column=0,pady=10)

        #property details
        btn_3=Button(btn_frame,text="Property Details",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,command=self.property_details)
        btn_3.grid(row=2,column=0,pady=10)
        
        #user details
        btn_4=Button(btn_frame,text="Approve Property",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,command=self.approve_property)
        btn_4.grid(row=3,column=0,pady=10)

        #customer_profile
        btn_5=Button(btn_frame,text="Approve Registration",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,command=self.approve_registration)
        btn_5.grid(row=4,column=0,pady=10)

        #logout
        #customer_profile
        btn_5=Button(btn_frame,text="Log Out",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0)
        btn_5.grid(row=5,column=0,pady=10)
        
        # bin frame yet to complete sub intiatives
        
        #right midd side img
        img3 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\mid.png")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
        
    def sell_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Seller_Win(self.new_window)

    def property_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Property_Win(self.new_window)

    def approve_registration(self):
        self.new_window=Toplevel(self.root)
        self.app=Decide_Win(self.new_window)

    def approve_property(self):
        self.new_window=Toplevel(self.root)
        self.app=Approve_Win(self.new_window)

        
if __name__ == "__main__":
    root = Tk()
    obj = RealestateDbmsManager(root)
    root.mainloop()