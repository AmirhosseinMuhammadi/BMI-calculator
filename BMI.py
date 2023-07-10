from tkinter import *

root = Tk()
root.geometry("800x600")


def BMI():
    height = text1.get()
    weight = text2.get()
    bmi = float(weight) / float(height) ** 2
    label3 = Label(root , text = f"Your BMI is : {bmi}")
    label3.pack()
    if bmi < 18.5:
        label4 = Label(root , text = "You are underweight")
    elif bmi >= 18.5 and bmi <= 24.9:
        label4 = Label(root , text = "You are within the healthy range")
    elif bmi > 24.9 and bmi < 30:
        label4 = Label(root , text = "You are overweight")
    else:
        label4 = Label(root , text = "You are within the obese range")
    label4.pack()

label1 = Label(root , text = "Enter your height(m)")
text1 = Entry(root)
label1.pack()
text1.pack()
label2 = Label(root , text = "Enter your weight(kg)")
text2 = Entry(root)
label2.pack()
text2.pack()

btn1 = Button(root , text = "Calculate BMI" , command = BMI)
btn1.pack()


root.mainloop()
