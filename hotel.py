from tkinter import *
from pil import Image, ImageTk
from customer import Customer_Window
from report import Report_Generating
from room import Room_Booking
from details import DetailsRoom


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ==================================First Image=================================================================
        img1 = Image.open(r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\hotel.jpg")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimage1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ==================================Logo========================================================================
        img2 = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\ayush_hotels.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg1 = Label(self.root, image=self.photoimage2, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=230, height=140)

        # ==================================Title========================================================================
        lbl_title = Label(self.root, text="Hotel Management System", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ==================================Title========================================================================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ==================================Menu========================================================================
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ==================================Button Frame========================================================================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, command=self.customer_details,  text="CUSTOMER", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.roombooking, width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, command=self.detailsroom, text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, command=self.reportroom, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, command=self.logout, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        # ==================================Right Side Image========================================================================
        img3 = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\hotel1.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimage3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1310, height=590)

        # ==================================Down Images========================================================================
        img4 = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\room.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image=self.photoimage4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(
            r"E:\College\4th Semester All\Advanced Programming\Individual Project\python Project\pythonProject1\images\food.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimage5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(main_frame, image=self.photoimage5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=420, width=230, height=190)


    def customer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_Window(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_Booking(self.new_window)

    def detailsroom(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    def reportroom(self):
        self.new_window = Toplevel(self.root)
        self.app = Report_Generating(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()