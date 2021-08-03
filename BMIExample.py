from tkinter import *
import math

def leftClickButton(event):
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    format_result = "{:.2f}".format(result)
    labelResult.configure(text=format_result)
    if float(format_result) <= 18.5:
        labelResultExplain.configure(text="Underweight")
    elif float(format_result) > 18.5 and float(format_result) < 25:
        labelResultExplain.configure(text="Normal Weight")
    elif float(format_result) >= 25 and float(format_result) < 29.9:
        labelResultExplain.configure(text="Overweight")
    else:
        labelResultExplain.configure(text="Obesity")

MainWindow = Tk()
labelHead = Label(MainWindow, text="Let's BMI!!!", fg="red", bg="orange", font=("Helvetica",12), anchor="center")
labelHead.grid(row=0, column=0)
labelHeight = Label(MainWindow, text="Height (cm.)")
labelHeight.grid(row=1, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=1, column=1)
labelWeight = Label(MainWindow, text="Weight (kg.)")
labelWeight.grid(row=2, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=2, column=1)
calculateButton = Button(MainWindow, text="Submit")
calculateButton.grid(row=3, column=0)
calculateButton.bind('<Button-1>', leftClickButton)
labelResult = Label(MainWindow, text="Result")
labelResult.grid(row=3, column=1)
labelResultExplain = Label(MainWindow, text="")
labelResultExplain.grid(row=4, column=1)
MainWindow.mainloop()