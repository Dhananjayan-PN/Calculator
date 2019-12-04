from tkinter import *

def calc():
    try:
        value = eval(entry.get())
        entry.delete(0,END)
        Entry.insert(entry,0,'= '+str(value))
     
    except:
        entry.delete(0,END)
        Entry.insert(entry,0,"ERROR")
        
def clr():
    entry.delete(0,END)

def insert(txt):
    if freeze:
        entry.delete(0,END)
    Entry.insert(entry,END,txt)


top = Tk()
top.configure(background='black')
top.iconbitmap(r'Data/calc.ico')
top.title("Basic Calculator")
top.geometry('340x325+100+100')
l1 = Label(top, text="CALCULATOR", font=('Agency FB', 30, 'bold'), bg='black',fg='deep sky blue')
l1.grid(row=0,column=0, pady=5,columnspan=4)

global entry
entry = Entry(top, bd=4, width=30, font=('Helvetica', 15, 'bold'), bg='black',fg='deep sky blue')
entry.grid(row=1,column=0,pady=5 ,columnspan=4)
fnt = ('Helvetica', 15, 'bold')

# NUMBER BUTTONS
b9 = Button(top, text='9', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b9.cget('text')
b9.bind('<Button-1>', lambda event, txt=text: insert(txt))
b9.grid(row=2, column=0)
b8 = Button(top, text='8', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b8.cget('text')
b8.bind('<Button-1>', lambda event, txt=text: insert(txt))
b8.grid(row=2, column=1)
b7 = Button(top, text='7', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b7.cget('text')
b7.bind('<Button-1>', lambda event, txt=text: insert(txt))
b7.grid(row=2, column=2)
b6 = Button(top, text='6', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b6.cget('text')
b6.bind('<Button-1>', lambda event, txt=text: insert(txt))
b6.grid(row=3, column=0)
b5 = Button(top, text='5', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b5.cget('text')
b5.bind('<Button-1>', lambda event, txt=text: insert(txt))
b5.grid(row=3, column=1)
b4 = Button(top, text='4', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b4.cget('text')
b4.bind('<Button-1>', lambda event, txt=text: insert(txt))
b4.grid(row=3, column=2)
b3 = Button(top, text='3', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b3.cget('text')
b3.bind('<Button-1>', lambda event, txt=text: insert(txt))
b3.grid(row=4, column=0)
b2 = Button(top, text='2', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b2.cget('text')
b2.bind('<Button-1>', lambda event, txt=text: insert(txt))
b2.grid(row=4, column=1)
b1 = Button(top, text='1', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b1.cget('text')
b1.bind('<Button-1>', lambda event, txt=text: insert(txt))
b1.grid(row=4, column=2)
b = Button(top, text='.', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b.cget('text')
b.bind('<Button-1>', lambda event, txt=text: insert(txt))
b.grid(row=5, column=0)
b0 = Button(top, text='0', font=fnt, width=6, bg='black', fg='deep sky blue')
text = b0.cget('text')
b0.bind('<Button-1>', lambda event, txt=text: insert(txt))
b0.grid(row=5, column=1)


# OPERATION BUTTONS
fnt = ('Helvetica', 15)
bpower= Button(top, text='^', font=('Helvetica', 15, 'bold'), width=6, bg='black', fg='deep sky blue')
text = '**'
bpower.bind('<Button-1>', lambda event, txt=text: insert(txt))
bpower.grid(row=5, column=2)
add = Button(top, text='+', font=fnt, width=6, bg='black', fg='deep sky blue')
text = add.cget('text')
add.bind('<Button-1>', lambda event, txt=text: insert(txt))
add.grid(row=2, column=3)
sub = Button(top, text='-', font=fnt, width=6, bg='black', fg='deep sky blue')
text = sub.cget('text')
sub.bind('<Button-1>', lambda event, txt=text: insert(txt))
sub.grid(row=3, column=3)
mult = Button(top, text='*', font=fnt, width=6, bg='black', fg='deep sky blue')
text = mult.cget('text')
mult.bind('<Button-1>', lambda event, txt=text: insert(txt))
mult.grid(row=4, column=3)
div = Button(top, text='/', font=fnt, width=6, bg='black', fg='deep sky blue')
text = div.cget('text')
div.bind('<Button-1>', lambda event, txt=text: insert(txt))
div.grid(row=5, column=3)

# RESULT BUTTON
fnt = ('Helvetica', 15,'bold')
res = Button(top, text='=', font=fnt, width=13, bg='black', fg='deep sky blue')
res.grid(row=6, column=2,columnspan=2)

# ALL CLEAR BUTTON
clr = Button(top, text='AC', font=fnt, command=clr,width=13, bg='black', fg='deep sky blue')
clr.grid(row=6, column=0,columnspan=2)
    
top.mainloop()
