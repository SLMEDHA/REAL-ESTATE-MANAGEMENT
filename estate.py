from tkinter import *
from PIL import Image, ImageTk

class RealestateDbms:
    def __init__(self, root):
        self.root = root
        self.root.title("SMart Property Rover")
        self.root.geometry("1550x800+0+0")

        # top img
        img1 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\upp.png")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # logo
        img2 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\rlogo.png")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # title
        lbl_title = Label(self.root, text="SMart Property Rover", font=("times new roman", 29, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE, bg="black")
        main_frame.place(x=0, y=190, width=1550, height=620)

        # button frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE, bg="black")
        btn_frame.place(x=0, y=35, width=225, height=350)

        # menu label in the main frame
        lbl_menu = Label(main_frame, text="ESTATE INFO", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4,
                         relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=225)

        # Rest buttons in the button frame
        # customer_profile
        btn_1 = Button(btn_frame, text="Customer Profile", font=("times new roman", 15, "bold"), bg="black", fg="gold",
                       bd=0, command=self.user_details)
        btn_1.grid(row=0, column=0, padx=40, pady=10)
        
      
        # logout
        # customer_profile
        btn_2 = Button(btn_frame, text="Log Out", font=("times new roman", 15, "bold"),bg="black", fg="gold", bd=0,command=self.logout)
        btn_2.grid(row=1, column=0, pady=10)

        # bin frame yet to complete sub initiatives

        # right middle side img
        img3 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\mid.png")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)
        
    def logout(self):
        self.root.destroy()
        new_root = Tk()
        from login import Login_window
        login_obj = Login_window(new_root)  # Replace YourLoginClass with the actual class for your login page
        new_root.mainloop()


    def user_details(self):
        self.new_window = Toplevel(self.root)
        from user import user_prof
        self.app = user_prof(self.new_window)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        from customer import Cust_Win
        self.app = Cust_Win(self.new_window)

    def sell_details(self):
        self.new_window = Toplevel(self.root)
        from seller import Seller_Win
        self.app = Seller_Win(self.new_window)

    def property_details(self):
        self.new_window = Toplevel(self.root)
        from property import Property_Win
        self.app = Property_Win(self.new_window)

    def approve_property(self):
        self.new_window = Toplevel(self.root)
        from decide import Decide_Win
        self.app = Decide_Win(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = RealestateDbms(root)
    root.mainloop()
