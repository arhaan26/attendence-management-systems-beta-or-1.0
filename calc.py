from tkinter import *

def btnCilck (numbers) :
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnC_display () :
    global operator 
    operator = ""
    text_Input.set("")

def btneql_Input () :
    global operator 
    sumUp = str(eval(operator))
    text_Input.set(sumUp)
    operator = ""

cal = Tk()
cal.title("RainbowCalculator")
operator=""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

#========================================================================================================================================================================

btn7 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "7", bg="dark blue", command = lambda: btnCilck(7) ).grid(row = 1, column = 0)

btn8= Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "8", bg="light green", command = lambda: btnCilck(8) ).grid(row = 1, column = 1)

btn9= Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "9", bg="white",command = lambda: btnCilck(9) ).grid(row = 1, column = 2)                      

Addition = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "+", bg="grey", command = lambda: btnCilck("+") ).grid(row = 1, column = 3)
#============================================================================================
btn4 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "4", bg="dark red", command = lambda: btnCilck(4) ).grid(row = 2, column = 0)
                    
btn5= Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "5", bg="powder blue", command = lambda: btnCilck(5) ).grid(row = 2, column = 1)

btn6= Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "6", bg="dark orange", command = lambda: btnCilck(6) ).grid(row = 2, column = 2)                      

Subtraction = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "-", bg="hot pink", command = lambda: btnCilck("-") ).grid(row = 2, column = 3)                                      
#============================================================================================
btn1 = Button(cal,padx = 16, pady = 16,bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "1", bg="brown", command = lambda: btnCilck(1) ).grid(row = 3, column = 0)
                    
btn2= Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "2", bg="yellow", command = lambda: btnCilck(2) ).grid(row = 3, column = 1)

btn3= Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "3", bg="blue", command = lambda: btnCilck(3) ).grid(row = 3, column = 2)                      

Multiplication = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "*", bg="orange", command = lambda: btnCilck("*") ).grid(row = 3, column = 3) 

#============================================================================================
btn0 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "0", bg="pink", command = lambda: btnCilck(0) ).grid(row = 4, column = 0)
                    
btnC= Button(cal,padx = 16, pady = 16,bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "C", bg="green", command = btnC_display).grid(row = 4, column = 1)

btneql= Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "=", bg="indigo", command = btneql_Input).grid(row = 4, column = 2)                      

Division = Button(cal,padx = 16, pady = 16,bd = 8, fg = "black", font=('arial', 20, 'bold'),
                    text = "/", bg="red", command = lambda: btnCilck("/") ).grid(row = 4, column = 3)                         

cal.mainloop()