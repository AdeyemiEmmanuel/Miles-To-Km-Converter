from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20)

# label
my_label1 = Label(text="is equal to")
my_label1.grid(column=0, row=1)


entry = Entry(width=10)
entry.grid(column=1, row=0)

my_label2 = Label(text=0)
my_label2.grid(column=1, row=1)


def convert():
    miles = float(entry.get())
    to_km = miles * 1.609
    my_label2.config(text=to_km)


button1 = Button(text="Calculate", command=convert)
button1.grid(column=1, row=2)

my_label3 = Label(text="Miles")
my_label3.grid(column=2, row=0)

my_label4 = Label(text="Km")
my_label4.grid(column=2, row=1)


window.mainloop()
