import smtplib
from tkinter import *
from pil import Image, ImageTk
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from email.message import EmailMessage

class Report_Generating:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x580+230+220")

        # =================================Variables====================================================================
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()
        self.var_finaltotal = StringVar()

        # =============================Title============================================================================
        lbl_title = Label(self.root, text="Report", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==================================Logo========================================================================
        img2 = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\ayush_hotels.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg1 = Label(self.root, image=self.photoimage2, bd=4, relief=RIDGE)
        lblimg1.place(x=5, y=2, width=100, height=40)

        # ==================================Label Frame========================================================================
        labelframecenter = LabelFrame(self.root, bd=2, relief=RIDGE, text="Report",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframecenter.place(x=200, y=50, width=895, height=510)

        # ==================================Labels and Entries========================================================================
        # Customer Contact
        lbl_cust_contact = Label(labelframecenter, text="Customer Contact:",
                                 font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=1, sticky=W)

        entry_contact = ttk.Entry(labelframecenter, textvariable=self.var_contact, width=20, font=("arial", 13, "bold"))
        entry_contact.place(x=336, y=5)

        # Fetch Data Button
        btnFetchData = Button(labelframecenter, command=self.Fetch_Contact, text="FetchData", font=("arial", 8, "bold"),
                              bg="black", fg="gold",
                              width=9)
        btnFetchData.place(x=530, y=5)

        # Paid Tax
        lblPaidTax = Label(labelframecenter, font=("arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblPaidTax.grid(row=1, column=1, sticky=W)
        txtPaidTax = ttk.Entry(labelframecenter, textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtPaidTax.place(x=336, y=40)

        # Sub Total
        lblSubTotal = Label(labelframecenter, font=("arial", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lblSubTotal.grid(row=2, column=1, sticky=W)
        txtSubTotal = ttk.Entry(labelframecenter, textvariable=self.var_actualtotal, font=("arial", 13, "bold"), width=29)
        txtSubTotal.place(x=336, y=75)

        # Total Cost
        lblTotalCost = Label(labelframecenter, font=("arial", 12, "bold"), text="Total Cost:", padx=2, pady=6)
        lblTotalCost.grid(row=3, column=1, sticky=W)
        txtTotalCost = ttk.Entry(labelframecenter, textvariable=self.var_total, font=("arial", 13, "bold"), width=29)
        txtTotalCost.place(x=336, y=110)

        # Final Cost after discount
        lblFinalCost = Label(labelframecenter, font=("arial", 12, "bold"), text="Final Cost:", padx=2, pady=6)
        lblFinalCost.grid(row=4, column=1, sticky=W)
        txtFinalCost = ttk.Entry(labelframecenter, textvariable=self.var_finaltotal, font=("arial", 13, "bold"), width=29)
        txtFinalCost.place(x=336, y=145)

        # =====================================Bill Button==============================================================
        btnBill = Button(labelframecenter, command=self.total, text="Bill", font=("arial", 12, "bold"), bg="black",
                         fg="gold",
                         width=30)
        btnBill.place(x=290, y=200)

        # =====================================Email Button==============================================================
        btnSendEmail = Button(labelframecenter, command=self.Send_Email, text="Send Email", font=("arial", 12, "bold"), bg="black",
                         fg="gold",
                         width=30)
        btnSendEmail.place(x=290, y=450)

        # showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
        # showDataFrame.place(x=150, y=240, width=595, height=205)

    # ==================================================All Data Fetch==================================================
    def Fetch_Contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please Enter Contact Number.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This number is Not Found.", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=350, y=309, width=595, height=205)

                lblName = Label(showDataFrame, text="Name:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                # ======================Gender========================
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="ayush_hotels")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataFrame, text="Gender:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                # ======================Email========================
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="ayush_hotels")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataFrame, text="Email:", font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl3 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=60)

                # ======================Nationality========================
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="ayush_hotels")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNationality = Label(showDataFrame, text="Nationality:", font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=90)

                lbl4 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=90)

                # ======================Address========================
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="ayush_hotels")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAddress = Label(showDataFrame, text="Address:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl5 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)

                # ======================Customer Category========================
                # conn = mysql.connector.connect(host="localhost", username="root", password="",
                #                                database="ayush_hotels")
                # my_cursor = conn.cursor()
                # query = ("select total from bill where contact=%s")
                # value = (self.var_contact.get(),)
                # my_cursor.execute(query, value)
                # row = my_cursor.fetchone()
                # row_value = float(''.join(map(str, row)))
                # customer_category = "Normal"
                # discount = 0
                # print(row)
                # print(str(row_value))

                row = random.randrange(10000, 150000)

                if row > 50000:
                    customer_category = "Gold Customer"
                    discount = 0.4 * int(row)
                elif row >= 30000 and int(row) < 50000:
                    customer_category = "Silver Customer"
                    discount = 0.25 * int(row)
                elif row >= 15000 and int(row) < 30000:
                    customer_category = "Bronze Customer"
                    discount = 0.15 * int(row)
                elif row < 15000:
                    customer_category = "Normal Customer"
                    discount = 0.02 * int(row)

                lblCustomerCategory = Label(showDataFrame, text="Customer Category:", font=("arial", 12, "bold"))
                lblCustomerCategory.place(x=0, y=150)

                lbl6 = Label(showDataFrame, text=customer_category, font=("arial", 12, "bold"))
                lbl6.place(x=90, y=150)

                # ======================Total========================
                finalPrice = row - discount

                lblFinalPrice = Label(showDataFrame, text="Price after Discount:", font=("arial", 12, "bold"))
                lblFinalPrice.place(x=0, y=180)

                lbl7 = Label(showDataFrame, text=finalPrice, font=("arial", 12, "bold"))
                lbl7.place(x=90, y=180)

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%y")
        outDate = datetime.strptime(outDate, "%d/%m/%y")
        self.var_noofdays.set(abs(outDate - inDate).days)

        if (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Luxury"):
            q1 = float(1500)
            q2 = float(5000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % (q5 * 0.15))
            ST = "Rs." + str("%.2f" % q5)
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.15)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Launch" and self.var_roomtype.get() == "Luxury"):
            q1 = float(1500)
            q2 = float(5000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % (q5 * 0.15))
            ST = "Rs." + str("%.2f" % q5)
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.15)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury"):
            q1 = float(1500)
            q2 = float(5000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % (q5 * 0.15))
            ST = "Rs." + str("%.2f" % q5)
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.15)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Double"):
            q1 = float(1000)
            q2 = float(3500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % (q5 * 0.15))
            ST = "Rs." + str("%.2f" % q5)
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.15)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif (self.var_meal.get() == "Launch" and self.var_roomtype.get() == "Double"):
            q1 = float(1000)
            q2 = float(3500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % (q5 * 0.15))
            ST = "Rs." + str("%.2f" % q5)
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.15)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            q1 = float(1000)
            q2 = float(3500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % (q5 * 0.15))
            ST = "Rs." + str("%.2f" % q5)
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.15)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single"):
            q1 = float(500)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % (q5 * 0.15))
            ST = "Rs." + str("%.2f" % q5)
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.15)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Launch" and self.var_roomtype.get() == "Single"):
            q1 = float(500)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % (q5 * 0.15))
            ST = "Rs." + str("%.2f" % q5)
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.15)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            q1 = float(500)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % (q5 * 0.15))
            ST = "Rs." + str("%.2f" % q5)
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.15)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

    # ============Send Mail====================
    def send_mail(self):
        total = re.findall(r'\b\d+\b', self.var_total.get())
        if total > 50000:
            customerCategory = "Gold"
        elif total > 30000 and total <= 50000:
            customerCategory = "Silver"
        elif total > 15000 and total <= 30000:
            customerCategory = "Bronze"
        elif total <= 15000:
            customerCategory = "Normal"

        lblCustomerCategory = Label(self.root, text="Customer Category:", font=("arial", 12, "bold"))
        lblCustomerCategory.place(x=4500, y=460)

        lblCustomerCategory = Label(self.root, text=customerCategory, font=("arial", 12, "bold"))
        lblCustomerCategory.place(x=90, y=60)


    def Send_Email(self):
        # msg = EmailMessage()
        # msg.set_content("The total bill is 150000. You are our Gold customer.")
        # msg['Subject'] = "Your Total bill"
        # msg['From'] = "ayushojha010@gmail.com"
        # msg['To'] = "ayushojha010@gmail.com"
        #
        # # Send the message via our own SMTP server.
        # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.login("ayushojha010@gmail.com", "Iamnotgoingtodie")
        # server.send_message(msg)
        # server.quit()

        sender = "brcewayn01@gmail.com"
        receiver = "brcewayn01@gmail.com"
        message = EmailMessage()

        # message = """From: Ayush Ojha <brcewayn01@gmail.com
        # To: To brcewayn01@gmail.com
        # Subject: Customer checkout.
        #
        # Customer has checked out from the hotel."""

        message = EmailMessage()
        message.set_content("The total bill is 150000. You are our Gold customer.")
        message['Subject'] = "Your Total bill"
        message['From'] = "brcewayn01@gmail.com"
        message['To'] = "brcewayn01@gmail.com"


        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("brcewayn01@gmail.com", "Iamjusttrying@10")
        server.send_message(message)
        server.quit()



if __name__ == '__main__':
    root = Tk()
    obj = Report_Generating(root)
    root.mainloop()