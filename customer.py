from tkinter import *
from pil import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Customer_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x580+230+220")

        # =================================Variables====================================================================
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_spouse = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # =============================Title============================================================================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==================================Logo========================================================================
        img2 = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\ayush_hotels.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg1 = Label(self.root, image=self.photoimage2, bd=4, relief=RIDGE)
        lblimg1.place(x=5, y=2, width=100, height=40)

        # ==================================Label Frame========================================================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ==================================Labels and Entries========================================================================
        # customer reference
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("arial", 13, "bold"), state="readpnly")
        entry_ref.grid(row=0, column=1)

        # customer name
        cname = Label(labelframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, width=29, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # spouse name
        lblsname = Label(labelframeleft, text="Spouse Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblsname.grid(row=2, column=0, sticky=W)

        txtsname = ttk.Entry(labelframeleft, textvariable=self.var_spouse, width=29, font=("arial", 13, "bold"))
        txtsname.grid(row=2, column=1)

        # gender combobox
        label_gender = Label(labelframeleft, text="Gender:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"]=["Male", "Female", "Other"]
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        #postcode
        lblPostCode = Label(labelframeleft, text="Post Code:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)

        txtPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post, width=29, font=("arial", 13, "bold"))
        txtPostCode.grid(row=4, column=1)

        # mobile number
        lblMobile = Label(labelframeleft, text="Mobile Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        txtMobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"))
        txtMobile.grid(row=5, column=1)

        # email
        lblEmail = Label(labelframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        txtEmail.grid(row=6, column=1)

        # nationality
        lblNationality = Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_nationality["value"] = ["Nepali", "Indian", "Chinese", "American", 'European', "Australian", "British", "Others"]
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # idproof type combobox
        lblIdProof = Label(labelframeleft, text="ID Proof Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_id["value"] = ["National Card", "Passport", "Driving Licence"]
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # id number
        lblIdNumber = Label(labelframeleft, text="ID Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number, width=29, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

        # address
        lbladdress = Label(labelframeleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbladdress.grid(row=10, column=0, sticky=W)

        txtaddress = ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font=("arial", 13, "bold"))
        txtaddress.grid(row=10, column=1)

        # =========================================Buttons==============================================================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # ==================================Table Frame Search Style========================================================================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
                                    font=("times new roman", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(table_frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var,  font=("arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ["Mobile", "Ref"]
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(table_frame, textvariable=self.txt_search,  width=24, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(table_frame, text="Search", command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(table_frame, text="Show All", command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

        # =========================================Show Data Table==============================================================
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("ref", "name", "spouse", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview())
        scroll_y.config(command=self.Cust_Details_Table.yview())

        self.Cust_Details_Table.heading("ref", text="Refer No.")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("spouse", text="Spouse Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="Post Code")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("spouse", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)

        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if self.var_mobile.get() == "" or self.var_spouse.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
                my_cursor = conn.cursor()
                my_cursor.execute('insert into customer values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_spouse.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added")
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong:{str(e)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from customer')
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_spouse.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])


    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
            my_cursor = conn.cursor()
            my_cursor.execute('update customer set name=%s, spouse=%s, gender=%s, postcode=%s, mobile=%s, email=%s, Nationality=%s, idproof=%s, idnumber=%s, address=%s where ref=%s', (


                self.var_cust_name.get(),
                self.var_spouse.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details have been updated successfully!", parent=self.root)


    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
            my_cursor = conn.cursor()
            query = "delete from customer where ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_spouse.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")

        x = random.randint(1000, 10000)
        self.var_ref.set(str(x))


    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

            conn.commit()
        conn.close()






if __name__ == '__main__':
    root = Tk()
    obj = Customer_Window(root)
    root.mainloop()