from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
class Pro:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x650+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="grey")
        self.root.focus_force()
        #Variables
        self.searchBy = StringVar()
        self.searchTxt = StringVar()
        self.prod_id = IntVar()
        self.prod_name = StringVar()
        self.prod_price = IntVar()
        self.prod_quantity = IntVar()
        SearchFrame = LabelFrame(self.root,text="Search Product")
        SearchFrame.place(x=0,y=2,width=1100,height=70)
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.searchBy,values=("Search via","pro_name","pro_id"),state="readonly",justify=CENTER)
        cmb_search.place(x=10,y=10,width=180,height=30)
        cmb_search.current(0)
        txt_search = Entry(SearchFrame,textvariable=self.searchTxt,font=(20)).place(x=200,y=10,width=150,height=30)
        btn_search = Button(SearchFrame,text="Search",command=self.search,bg="#010c48",fg="white",cursor="hand2").place(x=370,y=9,width=150,height=30)

        # Title
        title = Label(self.root,text="Product Details",font=("Helvetica",12,"bold"),bg="#010c48",fg="white").place(x=0,y=65,width=1100,height=25)
        #row 1
        lbl_proId = Label(self.root,text="Product Id:",font=("Helvetica",12,"bold"),bg="grey").place(x=350,y=120)
        txt_proId = Entry(self.root,textvariable=self.prod_id,font=(15),bd=3).place(x=350,y=155,width=140,height=25)
        lbl_proName = Label(self.root,text="Product Name:",font=("Helvetica",12,"bold"),bg="grey").place(x=600,y=120)
        txt_proName = Entry(self.root,textvariable=self.prod_name,font=(15),bd=3).place(x=600,y=155,width=140,height=25)
        #row 2
        lbl_proPrice = Label(self.root,text="Product Price:",font=("Helvetica",12,"bold"),bg="grey").place(x=350,y=200)
        txt_proPrice = Entry(self.root,textvariable=self.prod_price,font=(15),bd=3).place(x=350,y=245,width=140,height=25)
        lbl_proQuantity = Label(self.root,text="Product Quantity:",font=("Helvetica",12,"bold"),bg="grey").place(x=600,y=200)
        txt_proQuantity = Entry(self.root,textvariable=self.prod_quantity,font=(15),bd=3).place(x=600,y=245,width=140,height=25)
        #buttons
        btn_add = Button(self.root,text="Add",command=self.add,bg="#010c48",fg="white",cursor="hand2").place(x=500,y=320,width=150,height=30)
        btn_del = Button(self.root,text="Delete",command=self.delete,bg="#010c48",fg="white",cursor="hand2").place(x=650,y=320,width=150,height=30)
        btn_upd = Button(self.root,text="Update",command=self.update,bg="#010c48",fg="white",cursor="hand2").place(x=800,y=320,width=150,height=30)
        btn_clear = Button(self.root,text="Clear",command=self.clear,bg="#010c48",fg="white",cursor="hand2").place(x=950,y=320,width=150,height=30)

        #Display window
        pro_frame = Frame(self.root,bd=3,relief=RIDGE)
        pro_frame.place(x=0,y=370,relwidth=1,height=280)

        scrollx = Scrollbar(pro_frame,orient=HORIZONTAL)
        scrolly = Scrollbar(pro_frame,orient=VERTICAL)
        self.ProductTable = ttk.Treeview(pro_frame,columns=("pro_id","pro_name","pro_price","pro_quantity"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        scrolly.pack(side=RIGHT,fill=Y)
        self.ProductTable.heading("pro_id",text="Product Id")
        self.ProductTable.heading("pro_name",text="Product Name")
        self.ProductTable.heading("pro_price",text="Product Price")
        self.ProductTable.heading("pro_quantity",text="Product Quantity")
        
        self.ProductTable["show"] = "headings"
      
        self.ProductTable.column("pro_id",width=90)
        self.ProductTable.column("pro_name",width=90)
        self.ProductTable.column("pro_price",width=90)
        self.ProductTable.column("pro_quantity",width=90)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    #-----------------Making functions--------------------------------------------
    def add(self):
        con =sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        try:
            if self.prod_id.get() == 0:
                messagebox.showerror("Error","Product id is required!",parent=self.root)
            else:
                cur.execute('select * from product where pro_id=?',(self.prod_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Product id already exist!",parent=self.root)
                else:
                    cur.execute('insert into product (pro_id,pro_name,pro_price,pro_quantity) values (?,?,?,?)',(
                        self.prod_id.get(),
                        self.prod_name.get(),
                        self.prod_price.get(),
                        self.prod_quantity.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute('select * from product')
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    def get_data(self,ev):
        f = self.ProductTable.focus()
        content = (self.ProductTable.item(f))
        row = content["values"]
        print(row)
        self.prod_id.set(row[0]),
        self.prod_name.set(row[1]),
        self.prod_price.set(row[2]),
        self.prod_quantity.set(row[3])
    
    def update(self):
        con =sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        try:
            if self.prod_id.get() == 0:
                messagebox.showerror("Error","Product id is required!",parent=self.root)
            else:
                cur.execute('select * from product where pro_id=?',(self.prod_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product id!",parent=self.root)
                else:
                    cur.execute('update product set pro_name=?,pro_price=?,pro_quantity=? where pro_id=?',(
                        self.prod_id.get(),
                        self.prod_name.get(),
                        self.prod_price.get(),
                        self.prod_quantity.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.prod_id.get() == 0:
                messagebox.showerror("Error","Product id is required!",parent=self.root)
            else:
                cur.execute('select * from product where pro_id=?',(self.prod_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product id!",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete this item?",parent=self.root)
                    if op == True:
                     cur.execute('delete from product where pro_id=?',(self.prod_id.get(),))
                     con.commit()
                     messagebox.showinfo("Deleted","Product deletion success",parent=self.root)
                     self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    def clear(self):
        self.prod_id.set(""),
        self.prod_name.set(""),
        self.prod_price.set(""),
        self.prod_quantity.set("")
        self.searchTxt.set("")
        self.searchBy.set("Select")
        self.show()
    def search(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.searchBy.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.searchTxt.get()=="":
                messagebox.showerror("Error","Search input is required",parent=self.root)
            else:
                cur.execute('select * from product where '+self.searchBy.get()+" LIKE '%"+self.searchTxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!= 0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else: 
                    messagebox.showerror("Error","No, record found!!")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
if __name__ == "__main__":
    root = Tk()
    obj = Pro(root)
    root.mainloop()