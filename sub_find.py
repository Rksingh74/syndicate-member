from email._header_value_parser import Domain
from tkinter import *
from tkinter import messagebox, Toplevel,ttk
from tkinter.ttk import Treeview

import requests
class syndicate:
    def __init__(self, ):
        self.window = Tk()  # to create an independent window
        
        # --------- settings --------------------
        self.window.title("Syndicate Security")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()

        w1 = w-100 
        h1 = h-200
        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1,h1,50, 80)) # w,h,x,y
        # ----------- widgets -------------------------------------
        color1 = "#FFF6FA"
        color2 = "#C13168"
        font1 = ("Clarendon Blk BT", 20,"bold")
        self.window.config(background="#06170e")

        self.hdlbl = Label(self.window, text="Syndicate Security", background=color2,
                           font=("times new roman",40,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)

        self.L1 = Label(self.window, text="Secure your organisation", background="#06170e", font=("times new roman",20,"bold"),fg="white")

        self.Domain = Entry(self.window, font=font1)

        self.b2 = Button(self.window, text="Exit", font=font1, background="white", command=self.deleteData)
        self.b1 = Button(self.window, text="Search", font=font1, background="white", command=self.subfinder)
        self.b3 = Button(self.window, text="yes", font=font1, background="white", command=self.subdirectory)
        
        self.L2 = Label(self.window, text="Are you want to find subdirectory", background="#06170e", font=("times new roman",20,"bold"),fg="white")


        self.ButtonFrame=Frame(self.window,bd=8,relief=RIDGE,padx=20)
        self.ButtonFrame.place(x=1095,y=115,width=310,height=505)

        self.lblsearch=Label(self.ButtonFrame,text="Results",width=18,font=("times new roman",18,"bold"),bg='#06170e',fg="gold",padx=0)
        self.lblsearch.grid(row=0,column=5,sticky=W)

        self.mytabel1 = Treeview(self.window, columns=['c1'], height=22)
        self.mytabel1.heading('c1', text="")
        self.mytabel1['show'] = 'headings'
        self.mytabel1.column('c1', width=300, anchor='center',)
       
        # -------------placements -----------------------------------

        self.hdlbl.place(x=0, y=0, width=w1, height=70)
        x1 = 100
        y1 = 100
        x_diff = 150
        y_diff = 100

        self.L1.place(x=450, y=250)
        self.L2.place(x=350, y=440)
        self.Domain.place(x=350 , y=300,width=500)
        self.mytabel1.place(x=1100, y=150)

        y1 += y_diff
        self.b1.place(x=520, y=350, width=150, height=40)
        self.b2.place(x=531 ,y=400, width=130, height=35)
        self.b3.place(x=800 ,y=440, width=100, height=35)

        self.window.mainloop()

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Exit?", parent=self.window)
        if ans == 'yes':
            self.window.destroy()  # Close the main window

    # def clearPage(self):
    #     self.Domain.delete(0, END)

    def subfinder(self):
        domain = self.Domain.get()  # Get the domain from the Entry widget
        sub_domain = "word.txt"

        with open(sub_domain, "r") as file:
            file1 = file.read().splitlines()

        for sub in file1:
            url = f"https://{sub}.{domain}"
            try:
                response = requests.get(url)
                response.raise_for_status()
                if response.status_code == 200:
                    # Add the found URL to tihe Treeview widget
                    self.mytabel1.insert("", "end", values=(url,))
            except requests.RequestException as e:
                print(f"Error with {url}: {e}")

    def subdirectory(self):
        domain = self.Domain.get()  # Get the domain from the Entry widget
        sub_domain = "word.txt"

        with open(sub_domain, "r") as file:
            file1 = file.read().splitlines()  # Split the lines in the file into a list

        for sub in file1:
            url = f"https://{domain}/{sub}"
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)
                if response.status_code == 200:
                    self.mytabel1.insert("", "end", values=(url,))
            except requests.RequestException as e:
                print(f"Error with {url}: {e}")

    # subdirectory()            

    def validation_check(self):
        if len(self.Domain.get()) < 2:
            messagebox.showwarning("Validation Check", "Enter Domain", parent=self.window)
            return False
        return True

if __name__ == '__main__':

   syndicate()


