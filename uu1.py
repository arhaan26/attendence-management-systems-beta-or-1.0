from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk
import time
import datetime

root = Tk()
root.title("Attendance Management Systems 1.0")
Label(text = "Attendence Management Systems 1.0", font = ("arial", 30, "bold"), fg = "blue").pack()
root.geometry("1350x650+0+0")
root.configure(background = "#d4d4d4")

leftmay = Frame(root, width = 1000, height = 650, bd = 8, relief = "raise")
leftmay.pack(side = LEFT)

rightmay = Frame(root, width = 350, height = 650, bd = 8, relief = "raise")
rightmay.pack(side = RIGHT)

rightmay1 = Frame(rightmay, width = 350, height = 650, bd = 8, relief = "raise")
rightmay1.pack(side = TOP)

cont1 = Canvas(rightmay1, width=350, height=650, bg="red")
cont1.grid(row = 0, column = 0)
img1 = PhotoImage(file="school.png")
cont1.create_image(200,200, image = img1)

DateOfOrder = StringVar()
value0 = StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()

def Mark_Register():
    if value0.get() == "Present Today":
        value1.set("Present Today")
        value2.set("Present Today")
        value3.set("Present Today")
        value4.set("Present Today")
        value5.set("Present Today")
        value6.set("Present Today")
        value7.set("Present Today")

    if value0.get() == "Late Today":
        value1.set("Late Today")
        value2.set("Late Today")
        value3.set("Late Today")
        value4.set("Late Today")
        value5.set("Late Today")
        value6.set("Late Today")
        value7.set("Late Today")


def Reset():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")

def qExit():
    qExit = messagebox.askyesno("Exit System", "Are You Sure To Exit???")
    if qExit > 0:
        root.destroy()
        return

DateOfOrder.set(time.strftime("%d/%m/%Y"))

lblno = Label(leftmay, font = ('arial', 10, 'bold'), text = "No:", bd = 16)
lblno.grid(row = 0, column = 0, sticky = W)
lblStudentsNo = Label(leftmay, font = ('arial', 10, 'bold'), text = "Student No:", bd = 16)
lblStudentsNo.grid(row = 0, column = 1, sticky = W)
lblStudentsName = Label(leftmay, font = ('arial', 10, 'bold'), text = "Student Name:", bd = 16)
lblStudentsName.grid(row = 0, column = 2, sticky = W)
lblCourseCode = Label(leftmay, font = ('arial', 10, 'bold'), text = "Course Code:", bd = 16)
lblCourseCode.grid(row = 0, column = 3, sticky = W)
box = ttk.Combobox(leftmay, textvariable = value0, state = "readonly")
box["values"] = (' ', 'Present Today', 'Late Today', 'Early Today', 'Absent Today', 'Sick Today')
box.current(0)
box.grid( row = 0, column = 4)
Fill = Button(leftmay, text = "Fill Form", padx = 2, pady = 2, bd = 2, fg = "red", 
font = ('arial', 10, 'bold'), width = 12, height = 1, command = Mark_Register).grid(row = 0, column = 5)
Reset = Button(leftmay, text = "Reset Form", padx = 2, pady = 2, bd = 2, fg = "red", 
font = ('arial', 10, 'bold'), width = 12, height = 1, command = Reset).grid(row = 0, column = 6)
Quit = Button(leftmay, text = "Quit Application", padx = 2, pady = 2, bd = 2, fg = "red", 
font = ('arial', 10, 'bold'), width = 12, height = 1, command = qExit).grid(row = 0, column = 7)
Date = Label(leftmay, font = ('arial', 10, 'bold'), textvariable = DateOfOrder, padx = 2, pady = 2, bd = 2, fg = "red", bg = "blue", relief = "sunken",
width = 12, height = 1).grid(row = 0, column = 8, sticky = W)

lblno = Label(leftmay, font = ('arial', 10, 'bold'), text = "1:", bd = 16)
lblno.grid(row = 1, column = 0, sticky = W)
lblStudents1 = Label(leftmay, font = ('arial', 10, 'bold'), text = "4569", bd = 16)
lblStudents1.grid(row = 1, column = 1, sticky = W)
lblStudentsName = Label(leftmay, font = ('arial', 10, 'bold'), text = "James Anatube", bd = 16)
lblStudentsName.grid(row = 1, column = 2, sticky = W)
lblCourseCode = Label(leftmay, font = ('arial', 10, 'bold'), text = "3494", bd = 16)
lblCourseCode.grid(row = 1, column = 3, sticky = W)
box = ttk.Combobox(leftmay, textvariable = value1, state = "readonly")
box["values"] = (' ', 'Present Today', 'Late Today', 'Early Today', 'Absent Today', 'Sick Today')
box.current(0)
box.grid( row = 1, column = 4)
# Fill = Button(leftmay, ''''text = Fill Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 5)
# Reset = Button(leftmay, '''text = Reset Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 6)
# Quit = Button(leftmay, '''text = Quit Application''', padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 7)
# # Date = Label(leftmay, font = ('arial', 10, 'bold'), textvariable = DateOfOrder, padx = 2, pady = 2, bd = 2, fg = "rd", bg = "blue", relief = "sunken",
# # width = 12, height = 1).grid(row = 0, column = 8, sticky = W)

lblno = Label(leftmay, font = ('arial', 10, 'bold'), text = "2:", bd = 16)
lblno.grid(row = 2, column = 0, sticky = W)
lblStudents1 = Label(leftmay, font = ('arial', 10, 'bold'), text = "4557", bd = 16)
lblStudents1.grid(row = 2, column = 1, sticky = W)
lblStudentsName = Label(leftmay, font = ('arial', 10, 'bold'), text = "Zackory Xaimcius", bd = 16)
lblStudentsName.grid(row = 2, column = 2, sticky = W)
lblCourseCode = Label(leftmay, font = ('arial', 10, 'bold'), text = "311", bd = 16)
lblCourseCode.grid(row = 2, column = 3, sticky = W)
box = ttk.Combobox(leftmay, textvariable = value2, state = "readonly")
box["values"] = (' ', 'Present Today', 'Late Today', 'Early Today', 'Absent Today', 'Sick Today')
box.current(0)
box.grid( row = 2, column = 4)
# Fill = Button(leftmay, ''''text = Fill Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 5)
# Reset = Button(leftmay, '''text = Reset Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 6)
# Quit = Button(leftmay, '''text = Quit Application''', padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 7)
# # Date = Label(leftmay, font = ('arial', 10, 'bold'), textvariable = DateOfOrder, padx = 2, pady = 2, bd = 2, fg = "rd", bg = "blue", relief = "sunken",
# # width = 12, height = 1).grid(row = 0, column = 8, sticky = W)

lblno = Label(leftmay, font = ('arial', 10, 'bold'), text = "3:", bd = 16)
lblno.grid(row = 3, column = 0, sticky = W)
lblStudents1 = Label(leftmay, font = ('arial', 10, 'bold'), text = "4995", bd = 16)
lblStudents1.grid(row = 3, column = 1, sticky = W)
lblStudentsName = Label(leftmay, font = ('arial', 10, 'bold'), text = "Xavier Mortons", bd = 16)
lblStudentsName.grid(row = 3, column = 2, sticky = W)
lblCourseCode = Label(leftmay, font = ('arial', 10, 'bold'), text = "3", bd = 16)
lblCourseCode.grid(row = 3, column = 3, sticky = W)
box = ttk.Combobox(leftmay, textvariable = value3, state = "readonly")
box["values"] = (' ', 'Present Today', 'Late Today', 'Early Today', 'Absent Today', 'Sick Today')
box.current(0)
box.grid( row = 3, column = 4)
# Fill = Button(leftmay, ''''text = Fill Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 5)
# Reset = Button(leftmay, '''text = Reset Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 6)
# Quit = Button(leftmay, '''text = Quit Application''', padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 7)
# # Date = Label(leftmay, font = ('arial', 10, 'bold'), textvariable = DateOfOrder, padx = 2, pady = 2, bd = 2, fg = "rd", bg = "blue", relief = "sunken",
# # width = 12, height = 1).grid(row = 0, column = 8, sticky = W)

lblno = Label(leftmay, font = ('arial', 10, 'bold'), text = "4:", bd = 16)
lblno.grid(row = 4, column = 0, sticky = W)
lblStudents1 = Label(leftmay, font = ('arial', 10, 'bold'), text = "2334", bd = 16)
lblStudents1.grid(row = 4, column = 1, sticky = W)
lblStudentsName = Label(leftmay, font = ('arial', 10, 'bold'), text = "Rahul Pondekerei", bd = 16)
lblStudentsName.grid(row = 4, column = 2, sticky = W)
lblCourseCode = Label(leftmay, font = ('arial', 10, 'bold'), text = "2889", bd = 16)
lblCourseCode.grid(row = 4, column = 3, sticky = W)
box = ttk.Combobox(leftmay, textvariable = value4, state = "readonly")
box["values"] = ('  ', 'Present Today', 'Late Today', 'Early Today', 'Absent Today', 'Sick Today')
box.current(0)
box.grid( row = 4, column = 4)
# Fill = Button(leftmay, ''''text = Fill Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 5)
# Reset = Button(leftmay, '''text = Reset Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 6)
# Quit = Button(leftmay, '''text = Quit Application''', padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 7)
# # Date = Label(leftmay, font = ('arial', 10, 'bold'), textvariable = DateOfOrder, padx = 2, pady = 2, bd = 2, fg = "rd", bg = "blue", relief = "sunken",
# # width = 12, height = 1).grid(row = 0, column = 8, sticky = W)

lblno = Label(leftmay, font = ('arial', 10, 'bold'), text = "5:", bd = 16)
lblno.grid(row = 5, column = 0, sticky = W)
lblStudentsNo = Label(leftmay, font = ('arial', 10, 'bold'), text = "3558", bd = 16)
lblStudentsNo.grid(row = 5, column = 1, sticky = W)
lblStudentsName = Label(leftmay, font = ('arial', 10, 'bold'), text = "Mouhammamd Sainshuid", bd = 16)
lblStudentsName.grid(row = 5, column = 2, sticky = W)
lblCourseCode = Label(leftmay, font = ('arial', 10, 'bold'), text = "7793", bd = 16)
lblCourseCode.grid(row = 5, column = 3, sticky = W)
box = ttk.Combobox(leftmay, textvariable = value5, state = "readonly")
box["values"] = (' ', 'Present Today', 'Late Today', 'Early Today', 'Absent Today', 'Sick Today')
box.current(0)
box.grid( row = 5, column = 4)
# Fill = Button(leftmay, text = "Fill Form", padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 5)
# Reset = Button(leftmay, text = "Reset Form", padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 6)
# Quit = Button(leftmay, text = "Quit Application", padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 7)
# Date = Label(leftmay, font = ('arial', 10, 'bold'), textvariable = DateOfOrder, padx = 2, pady = 2, bd = 2, fg = "red", bg = "blue", relief = "sunken",
# width = 12, height = 1).grid(row = 0, column = 8, sticky = W)

lblno = Label(leftmay, font = ('arial', 10, 'bold'), text = "1:", bd = 16)
lblno.grid(row = 6, column = 0, sticky = W)
lblStudents1 = Label(leftmay, font = ('arial', 10, 'bold'), text = "4558", bd = 16)
lblStudents1.grid(row = 6, column = 1, sticky = W)
lblStudentsName = Label(leftmay, font = ('arial', 10, 'bold'), text = "Sandy Huniskisishaxinng", bd = 16)
lblStudentsName.grid(row = 6, column = 2, sticky = W)
lblCourseCode = Label(leftmay, font = ('arial', 10, 'bold'), text = "8775", bd = 16)
lblCourseCode.grid(row = 6, column = 3, sticky = W)
box = ttk.Combobox(leftmay, textvariable = value6, state = "readonly")
box["values"] = (' ', 'Present Today', 'Late Today', 'Early Today', 'Absent Today', 'Sick Today')
box.current(0)
box.grid( row = 6, column = 4)
# Fill = Button(leftmay, ''''text = Fill Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 5)
# Reset = Button(leftmay, '''text = Reset Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 6)
# Quit = Button(leftmay, '''text = Quit Application''', padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 7)
# # Date = Label(leftmay, font = ('arial', 10, 'bold'), textvariable = DateOfOrder, padx = 2, pady = 2, bd = 2, fg = "rd", bg = "blue", relief = "sunken",
# # width = 12, height = 1).grid(row = 0, column = 8, sticky = W)

lblno = Label(leftmay, font = ('arial', 10, 'bold'), text = "7:", bd = 16)
lblno.grid(row = 7, column = 0, sticky = W)
lblStudents1 = Label(leftmay, font = ('arial', 10, 'bold'), text = "1335", bd = 16)
lblStudents1.grid(row = 7, column = 1, sticky = W)
lblStudentsName = Label(leftmay, font = ('arial', 10, 'bold'), text = "Steven Hotshot", bd = 16)
lblStudentsName.grid(row = 7, column = 2, sticky = W)
lblCourseCode = Label(leftmay, font = ('arial', 10, 'bold'), text = "1112467", bd = 16)
lblCourseCode.grid(row = 7, column = 3, sticky = W)
box = ttk.Combobox(leftmay, textvariable = value7, state = "readonly")
box["values"] = (' ', 'Present Today', 'Late Today', 'Early Today', 'Absent Today', 'Sick Today')
box.current(0)
box.grid( row = 7, column = 4)
# Fill = Button(leftmay, ''''text = Fill Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 5)
# Reset = Button(leftmay, '''text = Reset Form''' padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 6)
# Quit = Button(leftmay, '''text = Quit Application''', padx = 2, pady = 2, bd = 2, fg = "red", 
# font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 7)
# # Date = Label(leftmay, font = ('arial', 10, 'bold'), textvariable = DateOfOrder, padx = 2, pady = 2, bd = 2, fg = "rd", bg = "blue", relief = "sunken",
# # width = 12, height = 1).grid(row = 0, column = 8, sticky = W)

root.mainloop()
