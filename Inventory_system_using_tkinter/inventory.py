from tkinter import *
from products import *
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        '''Navbar'''
        title = Label(self.root,text="Inventory Management System",font=("times new roman",25,"underline","italic"),bg="#010c48",fg="#fff",anchor="s",).place(x=0,y=0,relwidth=1,height=50)
        '''Left Menu'''
        left_menu= Frame(self.root,bd=2,relief=RIDGE)
        left_menu.place(x=0,y=50,width=200,height=665)
        menu = Label(left_menu,text="Menu Bar",font=("Helvetica",15,"bold"),bg="blue",fg="#ddd").pack(side=TOP,fill=X)
        btn_pro = Button(left_menu,text="Products",font=("Helvetica",15),command=self.prod,bg="#f0f0ff",fg="#000",cursor="hand2").pack(side=TOP,fill=X)
        '''Main Content'''
        total_sale = Label(self.root,text="Total Sales\n\n[No Data Available]",font=("Helvetica",15,"bold"),fg="#000").place(x=300,y=90,height=100,width=250)
        total_sale = Label(self.root,text="Total Sales\n\n[No Data Available]",font=("Helvetica",15,"bold"),fg="#000").place(x=800,y=90,height=100,width=250)
        total_sale = Label(self.root,text="Total Sales\n\n[No Data Available]",font=("Helvetica",15,"bold"),fg="#000").place(x=300,y=290,height=100,width=250)
        total_sale = Label(self.root,text="Total Sales\n\n[No Data Available]",font=("Helvetica",15,"bold"),fg="#000").place(x=800,y=290,height=100,width=250)

        """Footer"""
        footer = Label(self.root,text="Developed By Athar Naveed",font=("times new roman",15,"underline","italic"),bg="#010c48",fg="#fff",anchor="s",).pack(side=BOTTOM,fill=X)
        sec_footer = Label(self.root,text="For any issues, or feature addition contact him",font=("times new roman",15,"underline","italic"),bg="#010c48",fg="#fff",anchor="s",).pack(side=BOTTOM,fill=X)
    def prod(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Pro(self.new_win)
if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()