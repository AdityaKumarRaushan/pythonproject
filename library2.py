from tkinter import *
from tkinter import ttk 
import mysql.connector
from datetime import date, timedelta
from tkinter import messagebox




class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("IIIT Kottayam Central Library")
        self.root.iconbitmap('D:\classProject\library\projectsrc\libicon2.ico')
        self.root.geometry("1550x800+0+0")

        #####################  variables for getting  the data ####################################
        self.membervar=StringVar()
        self.prnvar=StringVar()
        self.batchvar=StringVar()
        self.firstvar=StringVar()
        self.lastvar=StringVar()
        self.rollvar=StringVar()
        self.addressvar=StringVar()
        self.postvar=StringVar()
        self.mobilevar=StringVar()
        self.bookidvar=StringVar()
        self.booktitlevar=StringVar()
        self.authorvar=StringVar()
        self.dateborrowedvar=StringVar()
        self.duedatevar=StringVar()
        self.daysbookvar=StringVar()
        self.latefinevar=StringVar()
        self.dateoverduevar=StringVar()
        self.actualpricevar=StringVar()
        

        ########################################## HEADER ###########################################
        lbltitle = Label(self.root, text="IIITK Central Library Admin", bg='#1F4477', fg="white", bd=20, font=("Helvetica", 50, "bold"),padx=2, pady=5)
        lbltitle.pack(side = TOP, fill= X)





        #########################  FRAME FOR STUDENT DETAILS  AND BOOK DETAILS  ####################
        frame = Frame(self.root,  bd = 12, bg='#47728A', padx= 20)
        frame.place(x=0, y=120, width=1530, height= 400)

        dataframeleft = LabelFrame(frame, text="Borrower Details" , bd =12, bg='#FFDDAF', font=('arial', 12, "bold"))
        dataframeleft.place(x=0, y=5, width=990, height=360)





        #################   FIELDS INSIDE OUR DATAFRAME LEFT    ###########################
        lbl = Label(dataframeleft , text="Member Type : " ,bg='#FFDDAF', font=("times new roman ", 11, "bold"), padx=2, pady=6)
        lbl.grid(row=0, column=0,sticky=W)

        combMem = ttk.Combobox(dataframeleft,textvariable=self.membervar,font=("times new roman", 15, "bold"), width=27, state="readonly")
        combMem["values"] = ["Admin Staff", "B.tech Student", "M.tech Student" , "Proffessor","Ph.D"]
        combMem.grid(row=0, column=1)

        lbl1 = Label(dataframeleft, text="PRN No : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl1.grid(row=1, column=0)
        txtfield1 = Entry(dataframeleft, textvariable=self.prnvar ,font=("rimes new roman", 12, "bold"), width=32)
        txtfield1.grid(row=1, column=1, sticky=W)

        lbl2 = Label(dataframeleft, text="Batch(Year) : " ,bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl2.grid(row=2, column=0)
        txtfield2 = Entry(dataframeleft, textvariable=self.batchvar, font=("rimes new roman", 12, "bold"), width=32)
        txtfield2.grid(row=2, column=1, sticky=W)

        lbl3 = Label(dataframeleft, text="First Name : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl3.grid(row=3, column=0)
        txtfield3 = Entry(dataframeleft, textvariable=self.firstvar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield3.grid(row=3, column=1, sticky=W)

        lbl4 = Label(dataframeleft, text="Last Name : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl4.grid(row=4, column=0)
        txtfield4 = Entry(dataframeleft, textvariable=self.lastvar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield4.grid(row=4, column=1, sticky=W)

        lbl5 = Label(dataframeleft, text="Reg No : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl5.grid(row=5, column=0)
        txtfield5 = Entry(dataframeleft, textvariable=self.rollvar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield5.grid(row=5, column=1, sticky=W)

        lbl6 = Label(dataframeleft, text="Address : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl6.grid(row=6, column=0)
        txtfield6 = Entry(dataframeleft, textvariable=self.addressvar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield6.grid(row=6, column=1, sticky=W)

        lbl7 = Label(dataframeleft, text="Post Code : ",bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl7.grid(row=7, column=0)
        txtfield7 = Entry(dataframeleft,textvariable=self.postvar, font=("rimes new roman", 12, "bold"), width=32)
        txtfield7.grid(row=7, column=1, sticky=W)

        lbl8 = Label(dataframeleft, text="Mobile No : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl8.grid(row=8, column=0)
        txtfield8 = Entry(dataframeleft, textvariable=self.mobilevar, font=("rimes new roman", 12, "bold"), width=32)
        txtfield8.grid(row=8, column=1, sticky=W)

        lbl9 = Label(dataframeleft, text="Book Id : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl9.grid(row=0, column=3)
        txtfield9 = Entry(dataframeleft, textvariable=self.bookidvar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield9.grid(row=0, column=4, sticky=W)

        lbl10 = Label(dataframeleft, text="Book Title : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl10.grid(row=1, column=3)
        txtfield10 = Entry(dataframeleft, textvariable=self.booktitlevar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield10.grid(row=1, column=4, sticky=W)

        lbl11 = Label(dataframeleft, text="Author Name : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl11.grid(row=2, column=3)
        txtfield11 = Entry(dataframeleft, textvariable=self.authorvar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield11.grid(row=2, column=4, sticky=W)

        lbl12 = Label(dataframeleft, text="Date Borrowed : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl12.grid(row=3, column=3)
        txtfield12 = Entry(dataframeleft, textvariable=self.dateborrowedvar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield12.grid(row=3, column=4, sticky=W)

        lbl13 = Label(dataframeleft, text="Date Due : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl13.grid(row=4, column=3)
        txtfield13 = Entry(dataframeleft, textvariable=self.duedatevar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield13.grid(row=4, column=4, sticky=W)

        lbl14 = Label(dataframeleft, text="Days on Book : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl14.grid(row=5, column=3)
        txtfield14 = Entry(dataframeleft, textvariable=self.daysbookvar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield14.grid(row=5, column=4, sticky=W)

        lbl15 = Label(dataframeleft, text="Late Return Fine : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl15.grid(row=6, column=3)
        txtfield15 = Entry(dataframeleft, textvariable=self.latefinevar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield15.grid(row=6, column=4, sticky=W)

        lbl16 = Label(dataframeleft, text="Date Over Due : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl16.grid(row=7, column=3)
        txtfield16 = Entry(dataframeleft, textvariable=self.dateoverduevar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield16.grid(row=7, column=4, sticky=W)

        lbl17 = Label(dataframeleft, text="Actual Price : ", bg='#FFDDAF', font=("times new roman" ,12, "bold"), padx=0, pady=6)
        lbl17.grid(row=8, column=3)
        txtfield17 = Entry(dataframeleft, textvariable=self.actualpricevar,font=("rimes new roman", 12, "bold"), width=32)
        txtfield17.grid(row=8, column=4, sticky=W)





        ######################## RIGHT DATAFRAME OF FRAME   ##################################
        dataframeright = LabelFrame(frame, text="Book Details" , bd =12, bg='#FFDDAF', font=('arial', 12, "bold"))
        dataframeright.place(x=895, y=5, width=580, height=360)

        self.txtBox=Text(dataframeright, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        
        booklist=["Introduction to Computer Science Using Python", "Code: The Hidden Language of Computer Hardware and Software",
                        "The Elements of Computing Systems: Building a Modern Computer from First Principles","The Pragmatic Programmer"
                        "Structure and Interpretation of Computer Programs", "Modern Operating Systems", "Introduction to Algorithms",
                        "The New Turing Omnibus: Sixty-Six Excursions in Computer Science", "Free Software, Free Society",
                        "The C++ Programming Language", "Computer Organization and Design", "Programming Pearls",
                        "Design Patterns", "Hackers: Heroes of the Computer Revolution", "Computer Graphics: Principles and Practice",
                        "Data Structures and Algorithms", "The Art of UNIX Programming", "Land of Lisp: Learn to Program in Lisp, One Game at a Time!",
                        "The Soul of A New Machine", "Programming Ruby", "Operating Systems: Principles and Practice",
                        "Understanding Cryptography", "Win32 Programming", "Architecture of Computer Hardware and System Software",
                        "Introduction to the Theory of Computation", "Computer Systems: A Programmer's Perspective", "The Inmates Are Running the Asylum",
                        "Distributed Systems: Principles and Paradigms", "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                        "Rebel Code: Linux And The Open Source Revolution", "Natural Language Processing with Python","Programming Massively Parallel Processors",
                        "Database System Concepts", "Probability and Computing: Randomized Algorithms and Probabilistic Analysis",
                        "Advanced Programming in the UNIX Environment"]

        def select_data(event=""):
            value = str(listBox.get(listBox.curselection()))
            date1 = date.today()
            date2 = timedelta(days=15)
            date3 = date1 + date2
            self.dateborrowedvar.set(date1)
            self.duedatevar.set(date3)
            x = value
            if x=="Introduction to Computer Science Using Python":
                self.bookidvar.set("123")
                self.booktitlevar.set("Introduction to Computer Science Using Python")
                self.authorvar.set("Charles Dierbach")
                 
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 568")                    

            elif x == "Code: The Hidden Language of Computer Hardware and Software":
                self.bookidvar.set("124")
                self.booktitlevar.set("Code: The Hidden Language of Computer Hardware and Software")
                self.authorvar.set("Charles Petzold")

                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 678")

            elif x == "The Elements of Computing Systems: Building a Modern Computer from First Principles":
                self.bookidvar.set("126")
                self.booktitlevar.set("The Elements of Computing Systems: Building a Modern Computer from First Principles")
                self.authorvar.set("Noam Nisan")
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 890")


            elif x == "The Pragmatic Programmer":
                self.bookidvar.set("127")
                self.booktitlevar.set("The Pragmatic Programmer")
                self.authorvar.set("Andy Hunt")

                self.daysbookvar.set(20)
                self.latefinevar.set("Rs 80")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 476")

            elif x == "Structure and Interpretation of Computer Programs":
                self.bookidvar.set("128")
                self.booktitlevar.set("Structure and Interpretation of Computer Programs")
                self.authorvar.set("Gerald Jay Sussman")

                self.daysbookvar.set(30)
                self.latefinevar.set("Rs 100")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 800")

            elif x == "Modern Operating Systems":
                self.bookidvar.set("129")
                self.booktitlevar.set("Modern Operating Systems")
                self.authorvar.set("Andrew S. Tanenbaum")

                self.daysbookvar.set(25)
                self.latefinevar.set("Rs 90")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 654")


            elif x == "Introduction to Algorithms":
                self.bookidvar.set("130")
                self.booktitlevar.set("Introduction to Algorithms")
                self.authorvar.set("Thomas H. Cormen")

                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 648")

            elif x == "The New Turing Omnibus: Sixty-Six Excursions in Computer Science":
                self.bookidvar.set("131")
                self.booktitlevar.set("The New Turing Omnibus: Sixty-Six Excursions in Computer Science")
                self.authorvar.set("A.K. Dewdney")
    
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 550")

            elif x == "Free Software, Free Society":
                self.bookidvar.set("132")
                self.booktitlevar.set("Free Software, Free Society")
                self.authorvar.set("Richard Stallman")
            
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 520")

            elif x == "The C++ Programming Language":
                self.bookidvar.set("133")
                self.booktitlevar.set("The C++ Programming Language")
                self.authorvar.set("Bjarne Stroustrup")
            
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")
        # copying

            elif x == "Computer Organization and Design":
                self.bookidvar.set("134")
                self.booktitlevar.set("Computer Organization and Design")
                self.authorvar.set("David A Patterson")
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")


            elif x == "Programming Pearls":
                self.bookidvar.set("135")
                self.booktitlevar.set("Programming Pearls")
                self.authorvar.set("Programming Pearls")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")


            elif x == "Design Patterns":
                self.bookidvar.set("136")
                self.booktitlevar.set("Design Patterns")
                self.authorvar.set("Erich Gamma; Richard Helm")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")


            elif x ==  "Hackers: Heroes of the Computer Revolution":
                self.bookidvar.set("137")
                self.booktitlevar.set( "Hackers: Heroes of the Computer Revolution")
                self.authorvar.set("Steven Levy")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")



            elif x == "Computer Graphics: Principles and Practice":
                self.bookidvar.set("138")
                self.booktitlevar.set("Computer Graphics: Principles and Practice")
                self.authorvar.set("dhf")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")


            elif x == "Data Structures and Algorithms":
                self.bookidvar.set("139")
                self.booktitlevar.set("Data Structures and Algorithms")
                self.authorvar.set("ksa")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")



            elif x == "The Art of UNIX Programming":
                self.bookidvar.set("140")
                self.booktitlevar.set("The Art of UNIX Programming")
                self.authorvar.set("poqw")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")



            elif x == "Land of Lisp: Learn to Program in Lisp, One Game at a Time!":
                self.bookidvar.set("141")
                self.booktitlevar.set("Land of Lisp: Learn to Program in Lisp, One Game at a Time!")
                self.authorvar.set("mno")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")



            elif x == "The Soul of A New Machine":
                self.bookidvar.set("142")
                self.booktitlevar.set("The Soul of A New Machine")
                self.authorvar.set("mno")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")


            elif x == "Programming Ruby":
                self.bookidvar.set("143")
                self.booktitlevar.set("Programming Ruby")
                self.authorvar.set("powdc")
               
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")



            elif x == "Operating Systems: Principles and Practice":
                self.bookidvar.set("144")
                self.booktitlevar.set("Operating Systems: Principles and Practice")
                self.authorvar.set("mnaac")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")




            elif x == "Understanding Cryptography":
                self.bookidvar.set("145")
                self.booktitlevar.set("Understanding Cryptography")
                self.authorvar.set("akdsd")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")



            elif x == "Win32 Programming":
                self.bookidvar.set("146")
                self.booktitlevar.set("Win32 Programming")
                self.authorvar.set("mnsferfeo")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")




            elif x == "Architecture of Computer Hardware and System Software":
                self.bookidvar.set("147")
                self.booktitlevar.set("Architecture of Computer Hardware and System Software")
                self.authorvar.set("iebfds")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")




            elif x == "Introduction to the Theory of Computation":
                self.bookidvar.set("148")
                self.booktitlevar.set("Introduction to the Theory of Computation")
                self.authorvar.set("yhgbvs")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")



            elif x == "Computer Systems: A Programmer's Perspective":
                self.bookidvar.set("149")
                self.booktitlevar.set("Computer Systems: A Programmer's Perspective")
                self.authorvar.set("fevdvs")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")




            elif x == "The Inmates Are Running the Asylum":
                self.bookidvar.set("150")
                self.booktitlevar.set("The Inmates Are Running the Asylum")
                self.authorvar.set("eoirhfbf")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")





            elif x ==  "Distributed Systems: Principles and Paradigms":
                self.bookidvar.set("151")
                self.booktitlevar.set( "Distributed Systems: Principles and Paradigms")
                self.authorvar.set("eiurfbsc")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")



            elif x == "Domain-Driven Design: Tackling Complexity in the Heart of Software":
                self.bookidvar.set("152")
                self.booktitlevar.set("Domain-Driven Design: Tackling Complexity in the Heart of Software")
                self.authorvar.set("rucsk")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")




            elif x == "Rebel Code: Linux And The Open Source Revolution":
                self.bookidvar.set("153")
                self.booktitlevar.set("Rebel Code: Linux And The Open Source Revolution")
                self.authorvar.set("eiurfcjn")
               
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")




            elif x == "Natural Language Processing with Python":
                self.bookidvar.set("154")
                self.booktitlevar.set("Natural Language Processing with Python")
                self.authorvar.set("rfcbnmx")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")



            elif x == "Programming Massively Parallel Processors":
                self.bookidvar.set("155")
                self.booktitlevar.set("Programming Massively Parallel Processors")
                self.authorvar.set("mno")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")




            elif x == "Database System Concepts":
                self.bookidvar.set("156")
                self.booktitlevar.set("Database System Concepts")
                self.authorvar.set("wioenc")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")




            elif x == "Probability and Computing: Randomized Algorithms and Probabilistic Analysis":
                self.bookidvar.set("157")
                self.booktitlevar.set("Probability and Computing: Randomized Algorithms and Probabilistic Analysis")
                self.authorvar.set("wehdnew")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")




            elif x == "Advanced Programming in the UNIX Environment":
                self.bookidvar.set("158")
                self.booktitlevar.set("Advanced Programming in the UNIX Environment")
                self.authorvar.set("kljfoicnds")
                
                self.daysbookvar.set(15)
                self.latefinevar.set("Rs 50")
                self.dateoverduevar.set("No")
                self.actualpricevar.set("Rs 580")
            

        listScrollbar = Scrollbar(dataframeright)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        listBox = Listbox(dataframeright, font=("times new roman", 12), width=20, height=16, bg="#efe5f7")
        listBox.bind("<<ListboxSelect>>",select_data)
        listBox.grid(row=0, column =0, padx=4)
        for book in booklist:
            listBox.insert(END,book)

        listScrollbar.config(command=listBox.yview)

        def exit_program():
            confirmation = messagebox.askquestion("Exit notification","Are you sure to exit?")
            if confirmation=='yes':
                self.root.quit()
            else:
                return
        
        def reset_data():
            confirmation = messagebox.askquestion("Reset notification","Do you want to erase all the fields?")
            if confirmation=='yes':
                txtfield1.delete(0,END)
                txtfield2.delete(0,END)
                txtfield3.delete(0,END)
                txtfield4.delete(0,END)
                txtfield5.delete(0,END)
                txtfield6.delete(0,END)
                txtfield7.delete(0,END)
                txtfield8.delete(0,END)
                txtfield9.delete(0,END)
                txtfield10.delete(0,END)
                txtfield11.delete(0,END)
                txtfield12.delete(0,END)
                txtfield13.delete(0,END)
                txtfield14.delete(0,END)
                txtfield15.delete(0,END)
                txtfield16.delete(0,END)
                txtfield17.delete(0,END)
                self.txtBox.delete("1.0", END)
            else:
                return

            
            

        def fetch_data():
            conn = mysql.connector.connect(host='localhost',username='root', password='Aditya@03', database='libproj')
            my_cursor = conn.cursor()
            sql = ('''select * from libdata''')
            my_cursor.execute(sql)
            data = my_cursor.fetchall()
            if len(data)!=0:
                self.library_table.delete(*self.library_table.get_children())
                for i in data:
                    self.library_table.insert("",END,values=i)
                    conn.commit()
                conn.close()


        def get_cursor(event=""):
            cursor_row = self.library_table.focus()        
            content = self.library_table.item(cursor_row)
            row = content['values']

            self.membervar.set(row[0])
            self.prnvar.set(row[1])
            self.batchvar.set(row[2])
            self.firstvar.set(row[3])
            self.lastvar.set(row[4])
            self.rollvar.set(row[5])
            self.addressvar.set(row[6])
            self.postvar.set(row[7])
            self.mobilevar.set(row[8])
            self.bookidvar.set(row[9])
            self.booktitlevar.set(row[10])
            self.authorvar.set(row[11])
            self.dateborrowedvar.set(row[12])
            self.duedatevar.set(row[13])
            self.daysbookvar.set(row[14])
            self.latefinevar.set(row[15])
            self.dateoverduevar.set(row[16])
            self.actualpricevar.set(row[17])
            

        def add_data():
            conn = mysql.connector.connect(host='localhost',username='root', password='Aditya@03', database='libproj')
            my_cursor = conn.cursor()
            # my_cursor1 = conn.cursor()
            # my_cursor2 = conn.cursor()
            # prn = self.prnvar.get()
            # book = my_cursor1.execute("select bookid from libdata where prn=%s", (prn,))
            # rol = my_cursor2.execute("select roll from libdata where prn=%s", (prn,))
            # if book == self.bookidvar.get() and rol==self.rollvar.get():
            #     messagebox.showerror("Integrity Constraint error", "You are trying to enter the duplicate information")
            #     conn.close()
            # else:
            # try:
            my_cursor.execute("insert into libdata values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                                                                                   (self.membervar.get(),
                                                                                                    self.prnvar.get(),
                                                                                                    self.batchvar.get(),
                                                                                                    self.firstvar.get(),
                                                                                                    self.lastvar.get(),
                                                                                                    self.rollvar.get(),
                                                                                                    self.addressvar.get(),
                                                                                                    self.postvar.get(),
                                                                                                    self.mobilevar.get(),
                                                                                                    self.bookidvar.get(),
                                                                                                    self.booktitlevar.get(),
                                                                                                    self.authorvar.get(),
                                                                                                    self.dateborrowedvar.get(),
                                                                                                    self.duedatevar.get(),
                                                                                                    self.daysbookvar.get(),
                                                                                                    self.latefinevar.get(),
                                                                                                    self.dateoverduevar.get(),
                                                                                                    self.actualpricevar.get()))
                                                                                                    
                
            # except ValueError: 
            #     messagebox.showerror("Entries Error", "You are trying to enter duplicate values")

            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("success", "Data has been added successfully")
            txtfield1.delete(0,END)
            txtfield2.delete(0,END)
            txtfield3.delete(0,END)
            txtfield4.delete(0,END)
            txtfield5.delete(0,END)
            txtfield6.delete(0,END)
            txtfield7.delete(0,END)
            txtfield8.delete(0,END)
            txtfield9.delete(0,END)
            txtfield10.delete(0,END)
            txtfield11.delete(0,END)
            txtfield12.delete(0,END)
            txtfield13.delete(0,END)
            txtfield14.delete(0,END)
            txtfield15.delete(0,END)
            txtfield16.delete(0,END)
            txtfield17.delete(0,END)
           
            

        def show_data():
            self.txtBox.delete("1.0", END)
            self.txtBox.insert(END,"Member Type:\t\t" + self.membervar.get() + "\n")
            self.txtBox.insert(END,"PRN no:\t\t" + self.prnvar.get() + "\n")
            self.txtBox.insert(END,"Batch(Year):\t\t" + self.batchvar.get() + "\n")
            self.txtBox.insert(END,"First Name:\t\t" + self.firstvar.get() + "\n")
            self.txtBox.insert(END,"Last Name:\t\t" + self.lastvar.get() + "\n")
            self.txtBox.insert(END,"Reg No:\t\t" + self.rollvar.get() + "\n")
            self.txtBox.insert(END,"Address:\t\t" + self.addressvar.get() + "\n")
            self.txtBox.insert(END,"Post Code:\t\t" + self.postvar.get() + "\n")
            self.txtBox.insert(END,"Contact no:\t\t" + self.mobilevar.get() + "\n")
            self.txtBox.insert(END,"BookId:\t\t" + self.bookidvar.get() + "\n")
            self.txtBox.insert(END,"Book Title:\t\t" + self.booktitlevar.get() + "\n")
            self.txtBox.insert(END,"Author name:\t\t" + self.authorvar.get() + "\n")
            self.txtBox.insert(END,"Date Borrowed:\t\t" + self.dateborrowedvar.get() + "\n")
            self.txtBox.insert(END,"Date Due:\t\t" + self.duedatevar.get() + "\n")
            self.txtBox.insert(END,"Days on Book:\t\t" + self.daysbookvar.get() + "\n")
            self.txtBox.insert(END,"Late Fine:\t\t" + self.latefinevar.get() + "\n")
            self.txtBox.insert(END,"Date over Due:\t\t" + self.dateoverduevar.get() + "\n")
            self.txtBox.insert(END,"Actual Price:\t\t" + self.actualpricevar.get() + "\n")


        def update_data():
            conn = mysql.connector.connect(host='localhost',username='root', password='Aditya@03', database='libproj')
            my_cursor = conn.cursor()
            sql = ('''update libdata set  memberType=%s, prn=%s, batch=%s, firstname=%s,
                            lastname=%s, roll=%s, address=%s, post=%s, mobile=%s, bookid=%s,
                            booktitle=%s, author=%s, dateborrowed=%s, duedate=%s, daysbook=%s, latefine=%s, dateoverdue=%s, 
                            actualprice=%s where prn=%s and roll=%s and bookid=%s''')
            my_cursor.execute(sql, 
                                                        (self.membervar.get(),
                                                        self.prnvar.get(),
                                                        self.batchvar.get(),
                                                        self.firstvar.get(),
                                                        self.lastvar.get(),
                                                        self.rollvar.get(),
                                                        self.addressvar.get(),
                                                        self.postvar.get(),
                                                        self.mobilevar.get(),
                                                        self.bookidvar.get(),
                                                        self.booktitlevar.get(),
                                                        self.authorvar.get(),
                                                        self.dateborrowedvar.get(),
                                                        self.duedatevar.get(),
                                                        self.daysbookvar.get(),
                                                        self.latefinevar.get(),
                                                        self.dateoverduevar.get(),
                                                        self.actualpricevar.get(),
                                                        self.prnvar.get(),
                                                        self.rollvar.get(),
                                                        self.bookidvar.get()))
            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("success", "Data has been updated successfully")

        def delete_data():
            sql = (''' delete from libdata where prn=%s and roll=%s and bookid=%s''')
            var = (self.prnvar.get(), self.rollvar.get(), self.bookidvar.get())
            confirm = messagebox.askquestion("askquestion", "Are you sure to delete the record?")
            if confirm=='yes':
                conn = mysql.connector.connect(host='localhost',username='root', password='Aditya@03', database='libproj')
                my_cursor = conn.cursor()
                my_cursor.execute(sql, var)
                conn.commit()
                conn.close()
                messagebox.showinfo("suceess","Your data has been deleted successfully")
            # self.library_table.delete("1.0", END)
            x = self.library_table.selection()[0]
            self.library_table.delete(x)  
            fetch_data()
            
            



        ########################   FRAME FOR BUTTONS HAVING ABILITY TO MODIFY THE DATA ############
        buttonframe = Frame(self.root,  bd = 12, bg='#1F4477', padx= 20)
        buttonframe.place(x=0, y=520, width=1530, height= 60)

        addbutton = Button(buttonframe,command = add_data,text ="Add Borrower ",font=("arial", 12, "bold"), fg="white", bg="#F88B46", width=23)
        addbutton.grid(row=0, column=1)

        showbutton = Button(buttonframe, command=show_data,text="Show Records",font=("arial", 12, "bold"), fg="white", bg="#F88B46", width=23)
        showbutton.grid(row=0, column=2)

        updatebutton = Button(buttonframe, command=update_data,text="Update Record",font=("arial", 12, "bold"), fg="white", bg="#F88B46", width=23)
        updatebutton.grid(row=0, column=3)

        deletebutton = Button(buttonframe, command=delete_data,text="Delete Record",font=("arial", 12, "bold"), fg="white", bg="#F88B46", width=23)
        deletebutton.grid(row=0, column=4)

        resetbutton = Button(buttonframe, command=reset_data,text="Reset Fields", font=("arial", 12, "bold"), fg="white", bg="#F88B46", width=23)
        resetbutton.grid(row=0, column=5)

        exitbutton = Button(buttonframe, command=exit_program ,text="Exit" ,font=("arial", 12, "bold"), fg="white", bg="#F88B46", width=23)
        exitbutton.grid(row=0, column=6)



        ########################  FRAME FOR SHOWING THE DATA FROM DATABASE ########################
        showdata = Frame(self.root,  bd = 12, bg='#008E97', padx= 20)
        showdata.place(x=0, y=580, width=1530, height= 200)

        showdataframe = Frame(showdata,  bd = 6, bg='powder blue')
        showdataframe.place(x=0, y=10, width=1480, height= 160)

        yscroll = ttk.Scrollbar(showdataframe,orient=VERTICAL)
        xscroll = ttk.Scrollbar(showdataframe, orient=HORIZONTAL)
        self.library_table=ttk.Treeview(showdataframe, column=("membertype","prn","batch","firstname",
                                                                "lastname", "roll","address","post", "mobile", "bookid","booktitle","authorname","dateborrowed",
                                                                "duedate", "daysonbook", "latereturnfine", "dateoverdue", "actualprice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prn", text="PRN No")
        self.library_table.heading("batch", text="Batch No")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("roll", text="Reg No")
        self.library_table.heading("address", text="Address2")
        self.library_table.heading("post", text="Post")
        self.library_table.heading("mobile", text="Contact No")
        self.library_table.heading("bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("authorname", text="Author Name")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("duedate", text="Due Date")
        self.library_table.heading("daysonbook", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Fine")
        self.library_table.heading("dateoverdue", text="Date over Due")
        self.library_table.heading("actualprice", text="Actual Price")
        self.library_table.column("membertype", width=120)
        self.library_table.column("prn", width=120)
        self.library_table.column("batch", width=120)
        self.library_table.column("firstname", width=120)
        self.library_table.column("lastname",width=120)
        self.library_table.column("roll", width=120)
        self.library_table.column("address", width=120)
        self.library_table.column("post", width=120)
        self.library_table.column("mobile", width=120)
        self.library_table.column("bookid", width=120)
        self.library_table.column("booktitle",width=120)
        self.library_table.column("authorname", width=120)
        self.library_table.column("dateborrowed", width=120)
        self.library_table.column("duedate", width=120)
        self.library_table.column("daysonbook", width=120)
        self.library_table.column("latereturnfine", width=120)
        self.library_table.column("dateoverdue", width=120)
        self.library_table.column("actualprice", width=120)


        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)
        self.library_table.bind("<ButtonRelease-1>", get_cursor)
        
        fetch_data()
    
        

if __name__ == "__main__":
    # customtkinter.set_appearance_mode("dark")
    # customtkinter.set_default_color_theme("dark-blue")
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()

