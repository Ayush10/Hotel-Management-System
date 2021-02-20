from tkinter import *
from tkinter import ttk
from pil import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # =================================Variables====================================================================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_check = IntVar()

        # ============================Background Image===================================================================
        self.bg = ImageTk.PhotoImage(
            file=r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\login.jpg")

        background_label = Label(self.root, image=self.bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # ============================Left Image========================================================================
        self.bg1 = ImageTk.PhotoImage(
            file=r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\hotel-register.jpg")

        left_background_label = Label(self.root, image=self.bg1)
        left_background_label.place(x=100, y=120, width=470, height=550)

        # ============================Main Frame========================================================================
        frame = Frame(self.root, bg="white")
        frame.place(x=570, y=120, width=800, height=550)

        register_label = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green",
                               bg="white")
        register_label.place(x=20, y=20)

        # =============================Label And Entry==================================================================

        # ===================Row 1=======================
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        last_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        last_name.place(x=370, y=100)

        self.lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.lname_entry.place(x=370, y=130, width=250)

        # ===================Row 2=======================
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # ===================Row 3=======================
        security_questions = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"),
                                   bg="white")
        security_questions.place(x=50, y=240)

        self.combo_security_question = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                                    font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_question["values"] = ["Select", "Your Birth Place", "Your Parents Name",
                                                  "Your Girlfriend's Name"]
        self.combo_security_question.place(x=50, y=270, width=250)
        self.combo_security_question.current(0)

        security_answers = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",
                                 fg="black")
        security_answers.place(x=370, y=240)

        self.txt_securityA = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_securityA.place(x=370, y=270, width=250)

        # ===================Row 4=======================
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password.place(x=50, y=310)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_password, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=340, width=250)

        email = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=310)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_confirm_password, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=340, width=250)

        # ====================================Check Button==============================================================
        check_button = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions",
                                   font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
        check_button.place(x=50, y=380)

        # ====================================Buttons===================================================================
        img = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\register.png")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data, image=self.photoimage, borderwidth=0, cursor="hand2",
                    font=("times new roman", 15, "bold"))
        b1.place(x=50, y=420, width=200)

        img1 = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\login.png")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, command=self.return_login, image=self.photoimage1, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=370, y=420, width=200)

    # =============================Function Declaration=================================================================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All Fields Are Required!!")
        elif self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same.")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree to our terms and conditions.")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="ayush_hotels")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row != None:
                messagebox.showerror("Error", "User already exists, please use another email.")
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)", (self.var_fname.get(),
                                                                                              self.var_lname.get(),
                                                                                              self.var_contact.get(),
                                                                                              self.var_email.get(),
                                                                                              self.var_securityQ.get(),
                                                                                              self.var_securityA.get(),
                                                                                              self.var_password.get(),
                                                                                              ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully")

    def return_login(self):
        self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    app = Register(root)
    root.mainloop()
