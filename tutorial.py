from tkinter import *

myroot = Tk()

#myl1 = Label(myroot,  text = 'Label1',bd =  8,relief = 'groove')
#myl1.pack()

myb1 = Button(myroot, text = 'Without highlight Thickness')
myb1.grid(row=0,column=1)

myb2=Button(myroot,text='With highlight Thickness',highlightthickness=10)
myb2.grid(row=1,column=1,padx=10,pady=10)
myroot.mainloop()
