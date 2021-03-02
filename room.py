import smtplib
from email.message import EmailMessage
from tkinter import *
from pil import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Room_Booking:
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

        # =============================Title============================================================================
        lbl_title = Label(self.root, text="Room Booking", font=("times new roman", 18, "bold"), bg="black",
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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ==================================Labels and Entries========================================================================
        # Customer Contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:",
                             font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, width=20, font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        # Fetch Data Button
        btnFetchData = Button(labelframeleft, command=self.Fetch_Contact, text="FetchData", font=("arial", 8, "bold"), bg="black", fg="gold",
                        width=9)
        btnFetchData.place(x=347, y=5)

        # Check_in Date
        check_in_date = Label(labelframeleft, text="Check_in Date:",
                      font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin, width=29, font=("arial", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1)

        # Check_out Date
        check_out_date = Label(labelframeleft, text="Check_out Date:",
                              font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)

        txtcheck_out_date = ttk.Entry(labelframeleft, textvariable=self.var_checkout, width=29, font=("arial", 13, "bold"))
        txtcheck_out_date.grid(row=2, column=1)

        # Room Type
        label_RoomType = Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
        my_cursor = conn.cursor()
        my_cursor.execute('select roomType from details')
        ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Avalilable Room
        lblRoomAvailable = Label(labelframeleft, font=("arial", 12, "bold"), text="Available Room:", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        # txtRoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=29)
        # txtRoomAvailable.grid(row=4, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
        my_cursor = conn.cursor()
        my_cursor.execute('select roomno from details')
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=("arial", 12, "bold"),
                                      width=27, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lblMeal = Label(labelframeleft, font=("arial", 12, "bold"), text="Meal:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # Number of Days
        lblNoOfDays = Label(labelframeleft, font=("arial", 12, "bold"), text="No Of Days:", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noofdays, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPaidTax = Label(labelframeleft, font=("arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)
        txtPaidTax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(labelframeleft, font=("arial", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)
        txtSubTotal = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, font=("arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(labelframeleft, font=("arial", 12, "bold"), text="Total Cost:", padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)
        txtTotalCost = ttk.Entry(labelframeleft, textvariable=self.var_total, font=("arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1)

        # =====================================Bill Button==============================================================
        btnBill = Button(labelframeleft, command=self.total, text="Bill", font=("arial", 12, "bold"), bg="black", fg="gold",
                        width=9)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # =========================================Buttons==============================================================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, command=self.add_data, text="Add", font=("arial", 12, "bold"), bg="black", fg="gold",
                        width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, command=self.update, text="Update", font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, command=self.mDelete, text="Delete", font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, command=self.reset, text="Reset", font=("arial", 12, "bold"), bg="black",
                          fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # ========================================Right Side Image======================================================
        img3 = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\bed.jpg")
        img3 = img3.resize((535, 235), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        lblimg2 = Label(self.root, image=self.photoimage3, bd=4, relief=RIDGE)
        lblimg2.place(x=760, y=55, width=535, height=235)

        # ==================================Table Frame Search Style========================================================================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
                                 font=("times new roman", 12, "bold"), padx=2)
        table_frame.place(x=435, y=290, width=860, height=250)

        lblSearchBy = Label(table_frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24,
                                    state="readonly")
        combo_search["value"] = ["Contact", "Room"]
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(table_frame, textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(table_frame, command=self.search, text="Search", font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(table_frame, command=self.fetch_data, text="Show All", font=("arial", 12, "bold"),
                            bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

        # =========================================Show Data Table==============================================================
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=(
        "contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview())
        scroll_y.config(command=self.room_table.yview())

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfDays")

        self.room_table["show"] = "headings"
        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("noOfdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()


    # =============Add Data=================
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
                my_cursor = conn.cursor()
                my_cursor.execute('insert into room values(%s, %s, %s, %s, %s, %s, %s)', (
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked.")
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong:{str(e)}", parent=self.root)

    # ================Fetch Data===========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from room')
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)

            conn.commit()
        conn.close()


    # ===============Get Cursor============
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])




    # ================Update Data==================
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
            my_cursor = conn.cursor()
            my_cursor.execute('update room set check_in=%s, check_out=%s, roomtype=%s, Room=%s, meal=%s, noOfdays=%s where Contact=%s', (


                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_contact.get(),
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details have been updated successfully!", parent=self.root)


    # =====================Delete Function================
    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
            my_cursor = conn.cursor()
            query = "delete from room where Contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()


    # ===========Reset Function================
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

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
                showDataFrame.place(x=450, y=55, width=300, height=180)

                lblName = Label(showDataFrame, text="Name:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                # ======================Gender========================
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
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
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
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
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
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
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAddress = Label(showDataFrame, text="Address:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl5 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)


    # ==============Search System==============
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)

            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
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

        conn = mysql.connector.connect(host="localhost", username="root", password="", database="ayush_hotels")
        my_cursor = conn.cursor()
        my_cursor.execute('insert into bill values(%s, %s, %s, %s)', (
            self.var_contact.get(),
            self.var_paidtax.get(),
            self.var_actualtotal.get(),
            self.var_total.get()
        ))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Bill Added.")





if __name__ == '__main__':
    root = Tk()
    obj = Room_Booking(root)
    root.mainloop()