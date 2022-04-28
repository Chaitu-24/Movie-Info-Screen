from tkinter import *
import tkinter.messagebox
import back
class movie:

    def __init__(self,root):
        self.root =root
        self.root.title("MOVIE INFO SCREEN")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        MOVIE_ID = StringVar()
        MOVIE_NAME = StringVar()
        RELEASE_DATE = StringVar()
        DIRECTOR= StringVar()
        CAST = StringVar()
        BUDGET = StringVar()
        DURATION = StringVar()
        RATING = StringVar()
# --------------------------------------FUNCTIONS-------------------------------------------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("MOVIE INFO SCREEN", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        def clearData():
            self.txtMOVIE_ID.delete(0, END)
            self.txtMOVIE_NAME.delete(0, END)
            self.txtRELEASE_DATE.delete(0, END)
            self.txtDIRECTOR.delete(0, END)
            self.txtCAST.delete(0, END)
            self.txtBUDGET.delete(0, END)
            self.txtDURATION.delete(0, END)
            self.txtRATING.delete(0, END)
        def addData():
            if(len(MOVIE_ID.get())!=0):
                back.addStdRec(MOVIE_ID.get(), MOVIE_NAME.get(), RELEASE_DATE.get() , DIRECTOR.get() ,CAST.get(), BUDGET.get(), DURATION.get(), RATING.get())
                movielist.delete(0, END)
                movielist.insert(END, (MOVIE_ID.get(), MOVIE_NAME.get(), RELEASE_DATE.get(), DIRECTOR.get(), CAST.get(), BUDGET.get(), DURATION.get(), RATING.get()))

        def DisplayData():
            movielist.delete(0,END)
            for row in back.viewData():
                movielist.insert(END, row, str(""))

        def StudentRec(event):
            # global sd
            searchStd= movielist.curselection()[0]
            sd = movielist.get(searchStd)

            self.txtMOVIE_ID.delete(0, END)
            self.txtMOVIE_ID.insert(END, sd[1])
            self.txtMOVIE_NAME.delete(0, END)
            self.txtMOVIE_NAME.insert(END, sd[2])
            self.txtRELEASE_DATE.delete(0, END)
            self.txtRELEASE_DATE.insert(END, sd[3])
            self.txtDIRECTOR.delete(0, END)
            self.txtDIRECTOR.insert(END, sd[4])
            self.txtCAST.delete(0, END)
            self.txtCAST.insert(END, sd[5])
            self.txtBUDGET.delete(0, END)
            self.txtBUDGET.insert(END, sd[6])
            self.txtDURATION.delete(0, END)
            self.txtDURATION.insert(END, sd[7])
            self.txtRATING.delete(0, END)
            self.txtRATING.insert(END, sd[8])

        def DeleteData():
            if(len(MOVIE_ID.get())!=0):
                back.deleteRec(MOVIE_ID.get())
                clearData()
                DisplayData()

        def searchDatabase():
            movielist.delete(0,END)
            for row in back.searchData(MOVIE_ID.get(), MOVIE_NAME.get(), RELEASE_DATE.get() , DIRECTOR.get() ,CAST.get(), BUDGET.get(), DURATION.get(), RATING.get()):
                movielist.insert(END, row, str(""))

        def update():
            if (len(MOVIE_ID.get()) != 0):
                back.deleteRec(MOVIE_ID.get())
            if (len(MOVIE_ID.get()) != 0):
                back.addStdRec(MOVIE_ID.get(), MOVIE_NAME.get(), RELEASE_DATE.get(), DIRECTOR.get(), CAST.get(), BUDGET.get(),DURATION.get(), RATING.get())
                movielist.delete(0, END)
                movielist.insert(END, (MOVIE_ID.get(), MOVIE_NAME.get(), RELEASE_DATE.get(), DIRECTOR.get(), CAST.get(), BUDGET.get(), DURATION.get(), RATING.get()))
#--------------------------------------Frames-----------------------------------------------------------------------__________________________________________________________
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=54,pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame ,font=('times new roman',48,'bold'),text="MOVIE INFO SCREEN",bg="Ghost White")
        self.lblTit.grid()
        ButtonFrame =Frame(MainFrame,bd=2,width=1350,height=70,padx=19,pady=10,bg="Ghost White",relief =RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,bg="cadet blue")
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20,relief=RIDGE,bg="Ghost White", font=('times new roman',26,'bold'),text="MOVIE Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,bg="Ghost White",font=('times new roman',20,'bold'),text="MOVIE Details\n")
        DataFrameRIGHT.pack(side=RIGHT)
#--------------------------------entries-------------------------------------------------------------------------------------------------
        self.lblMOVIE_ID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="MOVIE ID:",padx=2,pady=2,bg="Ghost White")
        self.lblMOVIE_ID.grid(row=0,column=0,sticky=W)
        self.txtMOVIE_ID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=MOVIE_ID, width=39)
        self.txtMOVIE_ID.grid(row=0, column=1)

        self.lblMOVIE_NAME = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="MOVIE NAME:", padx=2, pady=2,bg="Ghost White")
        self.lblMOVIE_NAME.grid(row=1, column=0, sticky=W)
        self.txtMOVIE_NAME = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=MOVIE_NAME, width=39)
        self.txtMOVIE_NAME.grid(row=1, column=1)

        self.lblRELEASE_DATE = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="RELEASE DATE:", padx=2, pady=2,bg="Ghost White")
        self.lblRELEASE_DATE.grid(row=2, column=0, sticky=W)
        self.txtRELEASE_DATE = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=RELEASE_DATE, width=39)
        self.txtRELEASE_DATE.grid(row=2, column=1)

        self.lblDIRECTOR = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="DIRECTOR:", padx=2, pady=2,bg="Ghost White")
        self.lblDIRECTOR.grid(row=3, column=0, sticky=W)
        self.txtDIRECTOR = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=DIRECTOR, width=39)
        self.txtDIRECTOR.grid(row=3, column=1)

        self.lblCAST = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="CAST:", padx=2, pady=2,bg="Ghost White")
        self.lblCAST.grid(row=4, column=0, sticky=W)
        self.txtCAST = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=CAST, width=39)
        self.txtCAST.grid(row=4, column=1)

        self.lblBUDGET = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="BUDGET(Crores INR):", padx=2, pady=2,bg="Ghost White")
        self.lblBUDGET.grid(row=5, column=0, sticky=W)
        self.txtBUDGET = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=BUDGET, width=39)
        self.txtBUDGET.grid(row=5, column=1)

        self.lblDURATION = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="DURATION(Hrs):", padx=2, pady=2,bg="Ghost White")
        self.lblDURATION.grid(row=6, column=0, sticky=W)
        self.txtDURATION = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=DURATION, width=39)
        self.txtDURATION.grid(row=6, column=1)

        self.lblRATING = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="RATING:", padx=2, pady=2,bg="Ghost White")
        self.lblRATING.grid(row=7, column=0, sticky=W)
        self.txtRATING = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=RATING, width=39)
        self.txtRATING.grid(row=7, column=1)
#--------------------------------------scroll bar and list box----------------------------------------------------------------------------
        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        movielist = Listbox(DataFrameRIGHT, width=41, height=16, font=('times new roman', 12, 'bold'),yscrollcommand=scrollbar.set)
        movielist.bind('<<ListboxSelect>>',StudentRec)
        movielist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=movielist.yview)
#--------------------------------------buttons-----------------------------------------------------------------------------------------------------------
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column =0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)

if __name__=='__main__':
    root = Tk()
    application = movie(root)
    root.mainloop()
