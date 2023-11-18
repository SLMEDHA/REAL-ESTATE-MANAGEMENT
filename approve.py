#approving properties
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector


class Approve_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("SMart Property Rover")
        self.root.geometry("1150x550+230+220")

        #varialbles
        self.var_propid=StringVar()
        self.var_type=StringVar()
        self.var_desc=StringVar()
        self.var_address=StringVar()
        self.var_price=StringVar()
        self.var_seller=StringVar()
        self.var_pstatus=StringVar()

        #title
        lbl_title=Label(self.root,text="APPROVE OR REJECT PROPERTY",font=("times new roman",29,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1150,height=50)

         #logo
        img2 = Image.open(r"C:\Users\S.L.MEDHA\Downloads\rlogo.png")
        img2=img2.resize((100,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

        #label frame----
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Property info",font=("times new roman",10,"bold"), padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #labels and entry
        #property id
        lbl_propid=Label(labelframeleft,text="Property ID",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_propid.grid(row=0,column=0,sticky=W)
        entry_propid=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_propid,state="readonly")
        entry_propid.grid(row=0,column=1)

        #seller id
        sellerid=Label(labelframeleft,text="Seller ID:",font=("arial",10,"bold"),padx=2,pady=6)
        sellerid.grid(row=1,column=0,sticky=W)
        txt_sellerid=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_seller)
        txt_sellerid.grid(row=1,column=1)

        #property type combobox
        label_propertytype=Label(labelframeleft,text="Property type:",font=("arial",10,"bold"),padx=2,pady=6)
        label_propertytype.grid(row=2,column=0,sticky=W)
        combo_propertytype=ttk.Combobox(labelframeleft,font=("arial",10,"bold"),width=27,state="readonly",textvariable=self.var_type)
        combo_propertytype["value"]=("Land","Flat","Villa")
        #combo_propertytype.current(0)
        combo_propertytype.grid(row=2,column=1)

        #property descriptionss
        desc=Label(labelframeleft,text="Property Description:",font=("arial",10,"bold"),padx=2,pady=6)
        desc.grid(row=3,column=0,sticky=W)
        txt_desc=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_desc)
        txt_desc.grid(row=3,column=1)

        #property address
        address=Label(labelframeleft,text="Property address:",font=("arial",10,"bold"),padx=2,pady=6)
        address.grid(row=4,column=0,sticky=W)
        txt_address=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_address)
        txt_address.grid(row=4,column=1)

        #property price
        price=Label(labelframeleft,text="Property price:",font=("arial",10,"bold"),padx=2,pady=6)
        price.grid(row=5,column=0,sticky=W)
        txt_price=ttk.Entry(labelframeleft,width=22,font=("arial",10,"bold"),textvariable=self.var_price)
        txt_price.grid(row=5,column=1)
        
       
        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE,bg="black")
        btn_frame.place(x=0,y=360,width=412,height=40)
        
        btnaccept=Button(btn_frame,text="Accept",command=self.accept,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnaccept.grid(row=0,column=0,padx=3)

        btnreject=Button(btn_frame,text="Reject",command=self.reject,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnreject.grid(row=0,column=1,padx=3)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=2,padx=3)
        
        #table frame search
        
        #label frame ----
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and search",font=("times new roman",10,"bold"), padx=2)
        table_frame.place(x=435,y=50, width=860,height=490)

        label_searchby=Label(table_frame,text="Search By",font=("arial",10,"bold"),bg="red",fg="white")  
        label_searchby.grid(row=0,column=0,sticky=W,padx=2)        


        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",10,"bold"),width=27,state="readonly")
        combo_search["value"]=("propid","ptype")
        combo_search.current(0)
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
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("propid","pseller","ptype","pdesc","paddr","price","pstatus"),xscrollcommand=scroll_x.set,
                                                                    yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("propid",text="Property ID")
        self.Cust_Details_Table.heading("pseller",text="Seller ID")
        self.Cust_Details_Table.heading("ptype",text="Property Type")
        self.Cust_Details_Table.heading("pdesc",text="Property Description")
        self.Cust_Details_Table.heading("paddr",text="Property Address")
        self.Cust_Details_Table.heading("price",text="Price")
        self.Cust_Details_Table.heading("pstatus",text="Property Status")

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("propid",width=100)
        self.Cust_Details_Table.column("pseller",width=100)
        self.Cust_Details_Table.column("ptype",width=100)
        self.Cust_Details_Table.column("pdesc",width=100)
        self.Cust_Details_Table.column("paddr",width=100)
        self.Cust_Details_Table.column("price",width=100)
        self.Cust_Details_Table.column("pstatus",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def accept(self):
        if self.var_type.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="SLMedha21!",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("UPDATE property SET pstatus=%s WHERE propid=%s",
                  ("ready", self.var_propid.get()))
                messagebox.showinfo("Congratulations","The property has been approved",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showwarning("Warning",f"Something went wrong:{str(e)}",parent=self.root)

    def reject(self):
        if self.var_type.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="SLMedha21!",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("UPDATE property SET pstatus=%s WHERE propid=%s",
                  ("rejected", self.var_propid.get()))
                messagebox.showinfo("Note","The property has been rejected",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showwarning("Warning",f"Something went wrong:{str(e)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="SLMedha21!",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from property")
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
        print(row)
        self.var_propid.set(row[0])   
        self.var_seller.set(row[1])
        self.var_type.set(row[2]) 
        self.var_desc.set(row[3])
        self.var_address.set(row[4]) 
        self.var_price.set(row[5]) 
        self.var_pstatus.set(row[6]) 


    def reset(self):
        self.var_propid.set("")   
        self.var_seller.set("")
        self.var_type.set("") 
        self.var_desc.set("")
        self.var_address.set("") 
        self.var_price.set("") 
        self.var_pstatus.set("") 


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="SLMedha21!",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM property WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows=my_cursor.fetchall()
        if len( rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__=="__main__":
    root=Tk()
    obj=Approve_Win(root)
    root.mainloop()