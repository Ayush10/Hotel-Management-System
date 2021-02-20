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
        x = random.randint(1000, 10000)
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
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref:",
                             font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"), state="readpnly")
        entry_ref.grid(row=0, column=1)

        # customer name
        cname = Label(labelframeleft, textvariable=self.var_cust_name, text="Customer Name:",
                      font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # spouse name
        lblsname = Label(labelframeleft, textvariable=self.var_spouse, text="Spouse Name:", font=("arial", 12, "bold"),
                         padx=2, pady=6)
        lblsname.grid(row=2, column=0, sticky=W)

        txtsname = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtsname.grid(row=2, column=1)

        # gender combobox
        label_gender = Label(labelframeleft, textvariable=self.var_gender, text="Gende:r",
                             font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ["Male", "Female", "Other"]
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # postcode
        lblPostCode = Label(labelframeleft, textvariable=self.var_post, text="Post Code:", font=("arial", 12, "bold"),
                            padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)

        txtPostCode = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtPostCode.grid(row=4, column=1)

        # mobile number
        lblMobile = Label(labelframeleft, textvariable=self.var_mobile, text="Mobile Number:",
                          font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        txtMobile = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtMobile.grid(row=5, column=1)

        # email
        lblEmail = Label(labelframeleft, textvariable=self.var_email, text="Email:", font=("arial", 12, "bold"), padx=2,
                         pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtEmail.grid(row=6, column=1)

        # nationality
        lblNationality = Label(labelframeleft, textvariable=self.var_nationality, text="Nationality:",
                               font=("arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_nationality["value"] = ["Nepali", "Indian", "Chinese", "American", 'European', "Australian", "British",
                                      "Others"]
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # idproof type combobox
        lblIdProof = Label(labelframeleft, textvariable=self.var_id_proof, text="ID Proof Type:",
                           font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_id["value"] = ["National Card", "Passport", "Driving Licence"]
        combo_id.current(0)
        combo_id.grid(row=3, column=1)

        # id number
        lblIdNumber = Label(labelframeleft, textvariable=self.var_id_number, text="ID Number:",
                            font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

        # address
        lbladdress = Label(labelframeleft, textvariable=self.var_address, text="Address:", font=("arial", 12, "bold"),
                           padx=2, pady=6)
        lbladdress.grid(row=10, column=0, sticky=W)

        txtaddress = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtaddress.grid(row=10, column=1)

        # =========================================Buttons==============================================================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 12, "bold"), bg="black", fg="gold",
                        width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 12, "bold"), bg="black",
                          fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)









if __name__ == '__main__':
    root = Tk()
    obj = Customer_Window(root)
    root.mainloop()