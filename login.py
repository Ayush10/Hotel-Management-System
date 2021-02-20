from tkinter import *
from tkinter import ttk

import mysql.connector
from pil import Image, ImageTk
from tkinter import messagebox
from hotel import HotelManagementSystem
from register import Register


# def main():
#     win =Tk()
#     app = Login_Window(win)
#     win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(
            file=r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\login.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=690, y=170, width=340, height=450)  # x=610

        user_login_image = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\laptop_user.png")
        user_login_image = user_login_image.resize((100, 100))
        self.photoimage = ImageTk.PhotoImage(user_login_image)
        user_label_image = Label(image=self.photoimage, bg="white", borderwidth=0)
        user_label_image.place(x=810, y=175, width=100, height=100)  # x=750

        get_started = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="black", bg="white")
        get_started.place(x=95, y=100)

        # ==============================================================================================================
        username_label = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="white")
        username_label.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password_label = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password_label.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # ==============================================================================================================
        image1 = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\loginn.png")
        image1 = image1.resize((20, 20))
        self.photoimage1 = ImageTk.PhotoImage(image1)
        label_image = Label(image=self.photoimage1, bg="white", borderwidth=0)
        label_image.place(x=740, y=323, width=20, height=20)  # x=750

        image2 = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\password.png")
        image2 = image2.resize((20, 20))
        self.photoimage2 = ImageTk.PhotoImage(image2)
        label_image = Label(image=self.photoimage2, bg="white", borderwidth=0)
        label_image.place(x=740, y=397, width=20, height=20)  # x=750

        # ==================================Login Button================================================================
        login_button = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3,
                              relief=RIDGE, fg="black", bg="light blue", activeforeground="black",
                              activebackground="light blue")
        login_button.place(x=110, y=300, width=120, height=35)

        # ==================================Register Button=============================================================
        register_button = Button(frame, command=self.register_window, text="New User Register",
                                 font=("times new roman", 10, "bold"), borderwidth=0, fg="black",
                                 bg="white", activeforeground="black", activebackground="white")
        register_button.place(x=15, y=350, width=160)

        # ==================================Forgot Password Button======================================================
        forgot_password_button = Button(frame, command=self.forgot_password_window, text="Forgot Password",
                                        font=("times new roman", 10, "bold"), borderwidth=0, fg="black",
                                        bg="white", activeforeground="black", activebackground="white")
        forgot_password_button.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields Required!!")
        elif self.txtuser.get() == "Ayush" and self.txtpass.get() == "Ayush":
            messagebox.showinfo("Success", "Welcome to Ayush Hotels")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="ayush_hotels")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            # Email = self.txtuser.get()
            # Password = self.txtpass.get()
            row = my_cursor.fetchone()

            # if row == None:
            #  messagebox.showerror("Error", "Invalid Username & Password")
            # else:
            #     for (email, passs) in my_cursor:
            #         if Email == email and Password == passs:
            #             self.new_window = Toplevel(self.root)
            #             self.app = HotelManagementSystem(self.new_window)
            #         else:
            #             return

                # if login:
                #     self.new_window = Toplevel(self.new_window)
                #     self.app = HotelManagementSystem(self.new_window)
                # else:
                #     self.new_window = Toplevel(self.root)
                #     self.app = HotelManagementSystem(self.new_window)

            if row == None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("Yes/No", "Accessible to Admin only")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                    # TODO: Add Hotel Management System Here 2:17
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()

    # ======================================Reset Password Window=======================================================
    def reset_password(self):
        if self.combo_security_question.get() == "Select":
            messagebox.showerror("Error", "Select the security question", parent=self.root2)
        elif self.txt_securityA.get() == "":
            messagebox.showerror("Error", " Please enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="ayush_hotels")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_security_question.get(), self.txt_securityA.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the correct answers.", parent=self.root2)
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info/Success",
                                    "Your password has been successfully reset. Please login to continue.",
                                    parent=self.root2)
                self.root2.destroy()

    # ======================================Forget Password Window======================================================
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="ayush_hotels")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("Error", "Please enter the valid user name")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("540x450+610+170")

                l = Label(self.root, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_questions = Label(self.root2, text="Select Security Questions",
                                           font=("times new roman", 15, "bold"),
                                           bg="white")
                security_questions.place(x=50, y=80)

                self.combo_security_question = ttk.Combobox(self.root2,
                                                            font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_question["values"] = ["Select", "Your Birth Place", "Your Parents Name",
                                                          "Your Girlfriend's Name"]
                self.combo_security_question.place(x=50, y=110, width=250)
                self.combo_security_question.current(0)

                security_answers = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"),
                                         bg="white",
                                         fg="black")
                security_answers.place(x=50, y=150)

                self.txt_securityA = ttk.Entry(self.root2,
                                               font=("times new roman", 15, "bold"))
                self.txt_securityA.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),
                                     bg="white",
                                     fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2,
                                             font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", font=("times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=150, y=290)


# class Register:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Register")
#         self.root.geometry("1550x800+0+0")
#
#         # =================================Variables====================================================================
#         self.var_fname = StringVar()
#         self.var_lname = StringVar()
#         self.var_contact = StringVar()
#         self.var_email = StringVar()
#         self.var_securityQ = StringVar()
#         self.var_securityA = StringVar()
#         self.var_password = StringVar()
#         self.var_confirm_password = StringVar()
#         self.var_check = IntVar()
#
#         # ============================Background Image===================================================================
#         self.bg = ImageTk.PhotoImage(
#             file=r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\login.jpg")
#
#         background_label = Label(self.root, image=self.bg)
#         background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
#         # ============================Left Image========================================================================
#         self.bg1 = ImageTk.PhotoImage(
#             file=r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\register.jpg")
#
#         left_background_label = Label(self.root, image=self.bg1)
#         left_background_label.place(x=50, y=100, width=470, height=550)
#
#         # ============================Main Frame========================================================================
#         frame = Frame(self.root, bg="white")
#         frame.place(x=520, y=100, width=800, height=550)
#
#         register_label = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green",
#                                bg="white")
#         register_label.place(x=20, y=20)
#
#         # =============================Label And Entry==================================================================
#
#         # ===================Row 1=======================
#         fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
#         fname.place(x=50, y=100)
#
#         fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
#         fname_entry.place(x=50, y=130, width=250)
#
#         last_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         last_name.place(x=370, y=100)
#
#         self.lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
#         self.lname_entry.place(x=370, y=130, width=250)
#
#         # ===================Row 2=======================
#         contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
#         contact.place(x=50, y=170)
#
#         self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
#         self.txt_contact.place(x=50, y=200, width=250)
#
#         email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         email.place(x=370, y=170)
#
#         self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
#         self.txt_email.place(x=370, y=200, width=250)
#
#         # ===================Row 3=======================
#         security_questions = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"),
#                                    bg="white")
#         security_questions.place(x=50, y=240)
#
#         self.combo_security_question = ttk.Combobox(frame, textvariable=self.var_securityQ,
#                                                     font=("times new roman", 15, "bold"), state="readonly")
#         self.combo_security_question["values"] = ["Select", "Your Birth Place", "Your Parents Name",
#                                                   "Your Girlfriend's Name"]
#         self.combo_security_question.place(x=50, y=270, width=250)
#         self.combo_security_question.current(0)
#
#         security_answers = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",
#                                  fg="black")
#         security_answers.place(x=370, y=240)
#
#         self.txt_securityA = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
#         self.txt_securityA.place(x=370, y=270, width=250)
#
#         # ===================Row 4=======================
#         password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
#         password.place(x=50, y=310)
#
#         self.txt_contact = ttk.Entry(frame, textvariable=self.var_password, font=("times new roman", 15, "bold"))
#         self.txt_contact.place(x=50, y=340, width=250)
#
#         email = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         email.place(x=370, y=310)
#
#         self.txt_email = ttk.Entry(frame, textvariable=self.var_confirm_password, font=("times new roman", 15, "bold"))
#         self.txt_email.place(x=370, y=340, width=250)
#
#         # ====================================Check Button==============================================================
#         check_button = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions",
#                                    font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
#         check_button.place(x=50, y=380)
#
#         # ====================================Buttons===================================================================
#         img = Image.open(
#             r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\register.png")
#         img = img.resize((200, 50), Image.ANTIALIAS)
#         self.photoimage = ImageTk.PhotoImage(img)
#         b1 = Button(frame, command=self.register_data, image=self.photoimage, borderwidth=0, cursor="hand2",
#                     font=("times new roman", 15, "bold"))
#         b1.place(x=50, y=420, width=200)
#
#         img1 = Image.open(
#             r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\login.png")
#         img1 = img1.resize((200, 50), Image.ANTIALIAS)
#         self.photoimage1 = ImageTk.PhotoImage(img1)
#         b1 = Button(frame, image=self.photoimage1, command=self.return_login(), borderwidth=0, cursor="hand2",
#                     font=("times new roman", 15, "bold"))
#         b1.place(x=370, y=420, width=200)
#
#     # =============================Function Declaration=================================================================
#     def register_data(self):
#         if self.var_fname.get() == "" or self.var_email.get() or self.var_securityQ.get() == "Select":
#             messagebox.showerror("Error", "All Fields Are Required!!")
#         elif self.var_password.get() != self.var_confirm_password.get():
#             messagebox.showerror("Error", "Password & Confirm Password must be same.")
#         elif self.var_check.get() == 0:
#             messagebox.showerror("Error", "Please Agree to our terms and conditions.")
#         else:
#             conn = mysql.connector.connect(host="localhost", user="root", password="", database="ayush_hotels")
#             my_cursor = conn.cursor()
#             query = ("select * from register where meail=%s")
#             value = (self.var_email.get(),)
#             my_cursor.execute(query, value)
#             row = my_cursor.fetchone()
#
#             if row != None:
#                 messagebox.showerror("Error", "User already exists, please use another email.")
#             else:
#                 my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)", (self.var_fname.get(),
#                                                                                               self.var_lname.get(),
#                                                                                               self.var_contact.get(),
#                                                                                               self.var_email.get(),
#                                                                                               self.var_securityQ.get(),
#                                                                                               self.var_securityA.get(),
#                                                                                               self.var_password.get(),
#                                                                                               ))
#
#             conn.commit()
#             conn.close()
#             messagebox.showinfo("Success", "Register Successfully")
#
#     def return_login(self):
#         self.root.destroy()


if __name__ == '__main__':
    win = Tk()
    app = Login_Window(win)
    win.mainloop()
