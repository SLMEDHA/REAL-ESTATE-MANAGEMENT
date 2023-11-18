from tkinter import *
from tkinter import ttk
from tkinter import messagebox  
from PIL import Image, ImageTk
import mysql.connector
from estate import RealestateDbms
from manager import RealestateDbmsManager
class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1050x550+0+0")

        original_image = Image.open(r"C:\Users\S.L.MEDHA\Downloads\mid.png")
        resized_image = original_image.resize((1050, 550), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(resized_image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=310, y=100, width=340, height=450)

        img1 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\login.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=430, y=105, width=100, height=100)

        get_str = Label(frame, text="SM ENTRY", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Label for Username
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username_lbl.place(x=70, y=155)

        self.txtuser = Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Label for Password
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password_lbl.place(x=70, y=215)

        self.txtpass = Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=240, width=270)
        
        # loginbtn
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)
        
        # registerbtn
        registerbtn = Button(frame, text="New User Register", command=self.register_win, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=85, y=350, width=160)
        
        # forgetbtn
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window, font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=85, y=370, width=160)
        
    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
            
    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()
        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
        elif username == "manager" and password == "mngpass":
            messagebox.showinfo("Success", "Welcome Manager")
            self.open_dashboard("manager")
        else:
            messagebox.showinfo("Success", "Welcome User")
            self.open_dashboard("user")

    def open_dashboard(self, role):
        self.new_window = Toplevel(self.root)
        if role == "manager":
            self.app =RealestateDbmsManager(self.new_window)
        else:
            # User Dashboard
            self.app =RealestateDbms(self.new_window)

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter your username and password to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="SLMedha21!", database="mydata")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("My Error", "Please enter a valid user name")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+178")
                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select the Question", font=("times new roman", 15), bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your friend name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)
                
                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15), bg="white", fg="black")
                security_A.place(x=50, y=150)
                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)
                
                new_pswd = Label(self.root2, text="New Password", font=("times new roman", 15), bg="white", fg="black")
                new_pswd.place(x=50, y=210)
                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=240, width=250)
                
                btn = Button(self.root2, text="Reset", font=("times new roman", 15, "bold"), fg="white", bg="green", command=self.reset_pass)
                btn.place(x=100, y=290)

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select security Question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="SLMedha21!", database="mydata")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s and securityQ=%s and securityA=%s"
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Answer", parent=self.root2)
            else:
                query = "update register set pass=%s where email=%s"
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login with the new password", parent=self.root2)
                self.root2.destroy()


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #============variable============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        #===========bg image ============
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\S.L.MEDHA\Downloads\bg2.png")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #===========left image ============
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\S.L.MEDHA\Downloads\smartcity.png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        #===========main frame ============
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        reg_lbl = Label(frame, text="Register here", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        reg_lbl.place(x=20, y=20)

        #===========label and entry==========
        #======row1=
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        #===========row2
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        #============row3
        security_Q = Label(frame, text="Select the Question", font=("times new roman",15), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your friend name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)
        
        security_A = Label(frame, text="Security Answer", font=("times new roman",15), bg="white", fg="black")
        security_A.place(x=370, y=240)
        self.txt_security=ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        #=============row 4
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)
        
        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        #===============buttons
        b1 = Button(frame, text="Register", command=self.register_date, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red")
        b1.place(x=50, y=380, width=150)

        b2 = Button(frame, text="Login", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="gold", activeforeground="white", activebackground="red", command=self.return_login)
        b2.place(x=370, y=380, width=150)
    def register_date(self):
        if (
            self.var_fname.get() == ""
            or self.var_email.get() == ""
            or self.var_securityQ.get() == "Select"
        ):
            messagebox.showerror("Error", "All fields are required")
        elif not self.var_pass.get() or self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "Password and confirm password must be the same and not empty"
            )
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="SLMedha21!",database="mydata")
            my_cursor=conn.cursor()
            query="select * from register where email=%s"
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error","User already exist,please another one")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                  ( self.var_fname.get(),
                                    self.var_lname.get(),
                                    self.var_contact.get(),
                                    self.var_email.get(),
                                    self.var_securityQ.get(),
                                    self.var_securityA.get(),
                                    self.var_pass.get(),
                                    self.var_confpass.get()
                                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Succesfully")
            
    def return_login(self):
        self.root.destroy()
            
def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()
        
if __name__ == "__main__":
    main()