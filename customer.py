from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
import random

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("SMart Property Rover")
        self.root.geometry("1150x550+230+220")

        #varialbles
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        print(x)

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()


        #title
        lbl_title=Label(self.root,text="ADD BUYER DETAILS",font=("times new roman",29,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1150,height=50)

         #logo
        img2 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\rlogo.png")
        img2=img2.resize((100,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

        #label frame----
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Buyer Details",font=("times new roman",10,"bold"), padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #labels and entry
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_ref,state="readonly")
        entry_ref.grid(row=0,column=1)

        #cust name
        cname=Label(labelframeleft,text="Customer name:",font=("arial",10,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txt_cname=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_cust_name)
        txt_cname.grid(row=1,column=1)

        #mother name
        mname=Label(labelframeleft,text="mother name:",font=("arial",10,"bold"),padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)
        txt_mname=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_mother)
        txt_mname.grid(row=2,column=1)

        

        #gender combobox
        label_gender=Label(labelframeleft,text="Gender:",font=("arial",10,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,font=("arial",10,"bold"),width=27,state="readonly",textvariable=self.var_gender)
        combo_gender["value"]=("Male","Female","Others")
        # combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #post code
        pcode=Label(labelframeleft,text="Post code:",font=("arial",10,"bold"),padx=2,pady=6)
        pcode.grid(row=4,column=0,sticky=W)
        txt_pcode=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_post)
        txt_pcode.grid(row=4,column=1)

        #mobile
        mobile=Label(labelframeleft,text="mobile:",font=("arial",10,"bold"),padx=2,pady=6)
        mobile.grid(row=5,column=0,sticky=W)
        txt_mobile=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_mobile)
        txt_mobile.grid(row=5,column=1)

        #email
        email=Label(labelframeleft,text="E-mail:",font=("arial",10,"bold"),padx=2,pady=6)
        email.grid(row=6,column=0,sticky=W)
        txt_email=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_email)
        txt_email.grid(row=6,column=1)

        #nationality
        nationality=Label(labelframeleft,text="Nationality:",font=("arial",10,"bold"),padx=2,pady=6)
        nationality.grid(row=7,column=0,sticky=W)
        combo_nationality=ttk.Combobox(labelframeleft,font=("arial",10,"bold"),width=27,state="readonly",textvariable=self.var_nationality)
        combo_nationality["value"]=("Indian","British","American","Korean")
        # combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
        
        #id proof
        idproof=Label(labelframeleft,text="ID proof:",font=("arial",10,"bold"),padx=2,pady=6)
        idproof.grid(row=8,column=0,sticky=W)
        combo_idproof=ttk.Combobox(labelframeleft,font=("arial",10,"bold"),width=27,state="readonly",textvariable=self.var_idproof)
        combo_idproof["value"]=("Aadhar Card","Driving License","Passport","PAN card")
        # combo_idproof.current(0)
        combo_idproof.grid(row=8,column=1)
        

        #ID number
        idno=Label(labelframeleft,text="ID number:",font=("arial",10,"bold"),padx=2,pady=6)
        idno.grid(row=9,column=0,sticky=W)
        txt_idno=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_idnumber)
        txt_idno.grid(row=9,column=1)

        #Address
        address=Label(labelframeleft,text="Address:",font=("arial",10,"bold"),padx=2,pady=6)
        address.grid(row=10,column=0,sticky=W)
        txt_address=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_address)
        txt_address.grid(row=10,column=1)

        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE,bg="black")
        btn_frame.place(x=0,y=360,width=412,height=40)
        
        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnadd.grid(row=0,column=0,padx=3)

        btnupdate=Button(btn_frame,text="update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=3)

        btndelete=Button(btn_frame,text="delete",command=self.mDelete,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=2,padx=3)

        btnreset=Button(btn_frame,text="reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=3,padx=3)
        
        #table frame search
        
        #label frame ----
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and search",font=("times new roman",10,"bold"), padx=2)
        table_frame.place(x=435,y=50, width=860,height=490)

        label_searchby=Label(table_frame,text="Search By",font=("arial",10,"bold"),bg="red",fg="white")  
        label_searchby.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",10,"bold"),width=27,state="readonly")
        combo_search["value"]=("Mobile","ref")
        #combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,width=22,font=("arial",10,"bold"))
        txt_search.grid(row=0,column=2,padx=2)

        btnsearch=Button(table_frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnsearch.grid(row=0,column=3,padx=3)

        btnshowall=Button(table_frame,text="Show all",command=self.fetch_data,  font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnshowall.grid(row=0,column=4,padx=3)
        #show data table
        details_table=Frame(table_frame,bd=2,relief=RIDGE,bg="black")
        details_table.place(x=0,y=50,width=700,height=300)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile","email","nationality",   
                                                                    "idproof","idnumber","address"),xscrollcommand=scroll_x.set,
                                                                    yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer no")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Post Code")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="E-mail")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id proof")
        self.Cust_Details_Table.heading("idnumber",text="ID number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Errror","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="SLMedha21!",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (self.var_ref.get(), self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(),
                 self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
                 self.var_idproof.get(), self.var_idnumber.get(), self.var_address.get())
                )

                messagebox.showinfo("Success","Customer has been added",parent=self.root)
                conn.commit()
                self.fetch_data()

                conn.close()
            except Exception as e:
                messagebox.showwarning("Warning",f"Something went wrong:{str(e)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="SLMedha21!",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]
        self.var_ref.set(row[0])     
        self.var_cust_name.set(row[1]) 
        self.var_mother.set(row[2]) 
        self.var_gender.set(row[3]) 
        self.var_post.set(row[4]) 
        self.var_mobile.set(row[5]) 
        self.var_email.set(row[6]) 
        self.var_nationality.set(row[7]) 
        self.var_idproof.set(row[8]) 
        self.var_idnumber.set(row[9]) 
        self.var_address.set(row[10]) 
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="SLMedha21!",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("Update customer set  Name=%s,mother=%s,gender=%s,postcode=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",
                ( self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(),
                 self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
                 self.var_idproof.get(), self.var_idnumber.get(), self.var_address.get(),self.var_ref.get())
            )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated sucessfully",parent=self.root)
    def mDelete(self):
        mDelete=messagebox.askyesno("Real Estate", "Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="SLMedha21!",database="mydata")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
            messagebox.showinfo("Delete","Buyers's details has been deleted sucessfully",parent=self.root)
        else:
            if not mDelete:
              return
        conn.commit()
        self.fetch_data()

        conn.close()
    def reset(self):
        #self.var_ref.set("")     
        self.var_cust_name.set("") 
        self.var_mother.set("") 
        #self.var_gender.set("") 
        self.var_post.set("") 
        self.var_mobile.set("") 
        self.var_email.set("") 
        #self.var_nationality.set("") 
        #self.var_idproof.set("") 
        self.var_idnumber.set("") 
        self.var_address.set("") 
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="SLMedha21!",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM customer WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows=my_cursor.fetchall()
        if len( rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

        
if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()