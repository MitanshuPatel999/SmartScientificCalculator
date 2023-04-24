from tkinter import *
import math
from pygame import mixer
import speech_recognition

root = Tk()
entryField = Entry(root, font=('arial', 20, 'bold'), bg="dodgerblue1", fg='white', bd=10,justify="right",
                   relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def sqrt(*a):
    return math.sqrt(a[0])


def power(a,b):
    return math.pow(a,b)


def fact(*a):
    return math.factorial(a[0])


def cube(*a):
    return math.pow(a[0],3)


def square(*a):
    return math.pow(a[0],2)


def log10(*a):
    return math.log(a[0],10)


def ln(*a):
    return math.log(a[0],math.e)


operations = {"ADD": add, "SUM": add, "ADDITION": add, "PLUS": add,
              "SUBTRACT": sub, "DIFFERENCE": sub, "SUBTRACTION": sub, "MINUS": sub,
              "MULTIPLY": mul, "MULTIPLY BY": mul, "MULTIPLICATION": mul, "INTO": mul, "PRODUCT": mul,
              "DIVIDE": div, "DIVISION": div, "DIV": div, "BY": div,
              "MOD": mod, "MODULUS": mod, "REMAINDER": mod,
              "ROOT":sqrt,"SQUARE ROOT":sqrt,
              "POWER":power,"RAISE TO":power,
              "SQUARE":square,"CUBE":cube,
              "LOG":log10,"LN":ln,"NATURAL":ln,
              "FACTORIAL":fact
              }


def findnumbers(s):
    ab = []
    for num in s:
        try:
            ab.append(float(num))
        except ValueError:
            pass
    if len(ab)==1:
        ab.append(0)
    if len(ab)>2:
        raise ValueError
    return ab


def audio():
    mixer.music.load("music1.mp3")
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        try:
            sr.adjust_for_ambient_noise(m, duration=0.2)
            voice = sr.listen(m)
            text = sr.recognize_google(voice)
            text_list = text.split(" ")
            for word in text_list:
                if word.upper() in operations.keys():
                    nums=findnumbers(text_list)
                    result=operations[word.upper()](nums[0],nums[1])
                    entryField.delete(0,END)
                    entryField.insert(END,result)
                else:
                    pass
            mixer.music.load("music2.mp3")
            mixer.music.play()
        except:
            pass


def main():
    root.title("SMART SCIENTIFIC CALCULATOR")
    root.config(bg="dodgerblue1")
    root.geometry("680x486+100+100")
    mixer.init()

    logoImg = PhotoImage(file="logo.png")
    logoLbl = Label(root, image=logoImg, bg="dodgerblue2")
    logoLbl.grid(row=0, column=0)

    micImg = PhotoImage(file="microphone.png")
    micLbl = Button(root, image=micImg, bd=0, bg="dodgerblue1", activebackground="dodgerblue1",
                    command=audio)
    micLbl.grid(row=0, column=7)

    button_text_list = ['C', 'CE', '√', '+', 'π', 'cosθ', 'tanθ', 'sinθ',
                        '1', '2', '3', '-', '2π', 'cosh', 'tanh', 'sinh',
                        '4', '5', '6', '*', chr(8731), 'x\u02b8', 'x\u00B3', 'x\u00B2',
                        '7', '8', '9', chr(247), 'ln', 'deg', 'rad', 'e',
                        '0', '.', '%', '=', 'log₁₀', '(', ')', 'x!']

    rv, cv = 1, 0
    for i in button_text_list:
        button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, command=lambda bttn=i: click(bttn),
                        bg="dodgerblue1", fg='white', font=('arial', 18, 'bold'),
                        activebackground="dodgerblue2")
        button.grid(row=rv, column=cv)
        cv += 1
        if cv > 7:
            cv = 0
            rv += 1
    root.mainloop()


def click(value):
    try:
        ex = entryField.get()
        ans = ""
        if value == 'C':
            ans = ex[0:len(ex) - 1]
        elif value == 'CE':
            entryField.delete(0, END)
        elif value == '√':
            ans = math.sqrt(eval(ex))
        elif value == 'π':
            ans = math.pi
            entryField.insert(END, str(ans))
            return
        elif value == '2π':
            ans = math.pi * 2
            entryField.insert(END, str(ans))
            return
        elif value == 'cosθ':
            ans = math.cos(math.radians(eval(ex)))
        elif value == 'tanθ':
            ans = math.tan(math.radians(eval(ex)))
        elif value == 'sinθ':
            ans = math.sin(math.radians(eval(ex)))
        elif value == 'cosh':
            ans = math.cosh(eval(ex))
        elif value == 'tanh':
            ans = math.tanh(eval(ex))
        elif value == 'sinh':
            ans = math.sinh(eval(ex))
        elif value == chr(8731):
            ans = eval(ex) ** (1 / 3)
        elif value == 'x\u02b8':
            entryField.insert(END, "**")
            return
        elif value == 'x\u00B3':
            ans = eval(ex) ** 3
        elif value == 'x\u00B2':
            ans = eval(ex) ** 2
        elif value == 'ln':
            ans = math.log(eval(ex), math.e)
        elif value == 'log₁₀':
            ans = math.log(eval(ex), 10)
        elif value == 'deg':
            ans = math.degrees(eval(ex))
        elif value == 'rad':
            ans = math.radians(eval(ex))
        elif value == '%':
            entryField.insert(END, "%")
            return
        elif value == 'e':
            ans = math.e
            entryField.insert(END, str(ans))
            return
        elif value == 'x!':
            ans = math.factorial(eval(ex))
        elif value == chr(247):
            entryField.insert(END, "/")
            return
        elif value == "=":
            ans = eval(ex)
        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, ans)

    except SyntaxError:
        pass


if __name__=="__main__":
    main()
