from tkinter import *

KM = 1.609344

def action():
    result = round(int(entry.get()) * KM, 2)
    label_3.config(text= str(result))

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady= 20)


entry = Entry(width=10)
entry.pack()
entry.grid(column=1, row= 0)

label_1 = Label(text="Miles")
label_1.grid(column=2, row= 0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row= 1)

label_3 = Label(text="Km")
label_3.grid(column=2, row= 1)

label_3 = Label(text="0")
label_3.grid(column=1, row= 1)
 
button = Button(text="Caculate", command=action)
button.grid(column=1, row= 2)

window.mainloop()