from tkinter import *
import math
def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def c():

    global equation_text

    equation_label.set("")

    equation_text = ""

def squareroot ():
   
    global equation_text

    equation_text = math.sqrt(float(equation_text))

    equation_label.set(equation_text)
   
    equation_text = equation_text
   
def fact():
   
    global equation_text

    equation_text = math.factorial(int(equation_text))

    equation_label.set(equation_text)
   
    equation_text = equation_text
   
   

window = Tk()
window.title("Calculator")
window.geometry("340x400")

equation_text = ""

equation_label = StringVar()

#label = Label(window,textvariable=equation_label,  bg="white",borderwidth=5, width=46,height=2)
#label.pack()

frame = Frame(window)
frame.pack()

label = Label(frame,textvariable=equation_label, anchor=E, bg="white", width=46,height=3)
label.grid(row=0,column=0,columnspan=4)

button1 = Button(frame, text=1, height=2, width=4, font=35,
                 command=lambda: button_press(1))
button1.grid(row=4, column=0)

button2 = Button(frame, text=2, height=2, width=4, font=35,
                 command=lambda: button_press(2))
button2.grid(row=4, column=1)

button3 = Button(frame, text=3, height=2, width=4, font=35,
                 command=lambda: button_press(3))
button3.grid(row=4, column=2)

button4 = Button(frame, text=4, height=2, width=4, font=35,
                 command=lambda: button_press(4))
button4.grid(row=3, column=0)

button5 = Button(frame, text=5, height=2, width=4, font=35,
                 command=lambda: button_press(5))
button5.grid(row=3, column=1)

button6 = Button(frame, text=6, height=2, width=4, font=35,
                 command=lambda: button_press(6))
button6.grid(row=3, column=2)

button7 = Button(frame, text=7, height=2, width=4, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=2, width=4, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=2, width=4, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=2, width=4, font=35,
                 command=lambda: button_press(0))
button0.grid(row=5, column=1)

plus = Button(frame, text='+', height=2, width=4, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=4, column=3)

minus = Button(frame, text='-', height=2, width=4, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=3, column=3)

multiply = Button(frame, text='*', height=2, width=4, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=2, width=4, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=1, column=2)

lessthan = Button(frame, text='<-', height=2, width=4,font=35,
                  command=lambda: button_press('<-'))
lessthan.grid(row=1, column=3)

equal = Button(frame, text='=', height=2, width=4, font=35,
                 command=equals)
equal.grid(row=5, column=3)

decimal = Button(frame, text='.', height=2, width=4, font=35,
                 command=lambda: button_2ress('.'))
decimal.grid(row=5, column=2)

c = Button(frame, text='C', height=2, width=4, font=35,
                 command=c)
c.grid(row=1,column=0)

squareroot = Button(frame, text='√', height=2, width=4, font=35,
                 command=squareroot)
squareroot.grid(row=1,column=1)

fact = Button(frame, text = '!', height=2, width=4,font=35,
                  command = fact)
fact.grid(row=5, column=0)


window.mainloop()