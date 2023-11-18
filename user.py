from tkinter import *
from tkinter.ttk import Combobox, Treeview  # Import Combobox from ttk
from PIL import Image, ImageTk
from customer import Cust_Win  # Import the CustomerPage class from customer.py
from seller import Seller_Win  # Import the SellerPage class from seller.py

class user_prof:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Property Rover")
        self.root.geometry("1050x550+230+220")

        # add user details
        lbl_title = Label(self.root, text="ADD USER DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo
        img2 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\rlogo.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="User Details",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Buttons for customer and seller
        btn_customer = Button(labelframeleft, text="Customer", command=self.open_customer_page)
        btn_customer.grid(row=0, column=0, pady=10, padx=20)

        btn_seller = Button(labelframeleft, text="Seller", command=self.open_seller_page)
        btn_seller.grid(row=1, column=0, pady=10, padx=20)

    def open_customer_page(self):
         self.new_window = Toplevel(self.root)
         self.app = Cust_Win(self.new_window)
        

    def open_seller_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Seller_Win(self.new_window)
        


if __name__ == "__main__":
    root = Tk()
    obj = user_prof(root)
    root.mainloop()
