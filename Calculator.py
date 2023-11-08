import tkinter as tk
root = tk.Tk()
root.title('Calculator')
s = ''
def enternum(n):
    global s
    s = s + str(n)
    display.config(text=s)

def cleardisp():
    global s
    if s=="ERROR":
        s = ''
    else:
        w = ''
        w = w + s[0:len(s)-1]
        s = w
    display.config(text=s)

def calculate():

    global s
    try:
        res  = eval(s)
    except:
        res = 'ERROR'
    finally:
        s = str(res)
        display.config(text=res)

def clearfun():
    global s
    s = ''
    display.config(text=s)

dispframe = tk.Frame(root,bg='lightgreen')
dispframe.rowconfigure(0,weight=1)
dispframe.columnconfigure(0,weight=1)


display = tk.Label(dispframe,width=20,height=2,bg='white',font=('Arial',20))
display.grid(row=0,column=0,pady=1,padx=1)
dispframe.grid(row=0,column=0,sticky='NEWS')

btnframe = tk.Frame(root,bg='black')

btnframe.rowconfigure(0,weight=1)
btnframe.columnconfigure(0,weight=1)
btnframe.rowconfigure(1,weight=1)
btnframe.columnconfigure(1,weight=1)
btnframe.rowconfigure(1,weight=1)
btnframe.columnconfigure(1,weight=1)
btnframe.rowconfigure(2,weight=1)
btnframe.columnconfigure(2,weight=1)
btnframe.rowconfigure(3,weight=1)
btnframe.columnconfigure(3,weight=1)


but1 = tk.Button(btnframe,text='1',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(1))
but2 = tk.Button(btnframe,text='2',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(2))
but3 = tk.Button(btnframe,text='3',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(3))
but4 = tk.Button(btnframe,text='4',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(4))
but5 = tk.Button(btnframe,text='5',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(5))
but6 = tk.Button(btnframe,text='6',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(6))
but7 = tk.Button(btnframe,text='7',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(7))
but8 = tk.Button(btnframe,text='8',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(8))
but9 = tk.Button(btnframe,text='9',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(9))
but0 = tk.Button(btnframe,text='0',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(0))
buta = tk.Button(btnframe,text='+',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum('+'))
buts = tk.Button(btnframe,text='-',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum('-'))
butm = tk.Button(btnframe,text='*',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum('*'))
butd = tk.Button(btnframe,text='/',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum('/'))
butb = tk.Button(btnframe,text='<-',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=cleardisp)
bute = tk.Button(btnframe,text='=',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=calculate)
butc = tk.Button(btnframe,text='CLEAR',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=clearfun)
butbr2 = tk.Button(btnframe,text=')',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum(')'))
butbr1 = tk.Button(btnframe,text='(',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum('('))
butexp = tk.Button(btnframe,text='^',width=5,height=2,borderwidth=4,bg='grey',fg='white',command=lambda: enternum('**'))

tk.Grid.columnconfigure(root,0,weight=1)
tk.Grid.rowconfigure(root,0,weight=1)

but7.grid(row=0,column=0,padx=2,pady=2,sticky='NEWS')
but8.grid(row=0,column=1,padx=2,pady=2,sticky='NEWS')
but9.grid(row=0,column=2,padx=2,pady=2,sticky='NEWS')
but4.grid(row=1,column=0,padx=2,pady=2,sticky='NEWS')
but5.grid(row=1,column=1,padx=2,pady=2,sticky='NEWS')
but6.grid(row=1,column=2,padx=2,pady=2,sticky='NEWS')
but1.grid(row=2,column=0,padx=2,pady=2,sticky='NEWS')
but2.grid(row=2,column=1,padx=2,pady=2,sticky='NEWS')
but3.grid(row=2,column=2,padx=2,pady=2,sticky='NEWS')
but0.grid(row=3,column=1,padx=2,pady=2,sticky='NEWS')
buta.grid(row=0,column=3,padx=2,pady=2,sticky='NEWS')
buts.grid(row=1,column=3,padx=2,pady=2,sticky='NEWS')
butd.grid(row=2,column=3,padx=2,pady=2,sticky='NEWS')
butm.grid(row=3,column=0,padx=2,pady=2,sticky='NEWS')
butb.grid(row=3,column=2,padx=2,pady=2,sticky='NEWS')
bute.grid(row=3,column=3,padx=2,pady=2,sticky='NEWS')
butc.grid(row=4,column=0,padx=2,pady=2,sticky='NEWS')
butbr1.grid(row=4,column=1,padx=2,pady=2,sticky='NEWS')
butbr2.grid(row=4,column=2,padx=2,pady=2,sticky='NEWS')
butexp.grid(row=4,column=3,padx=2,pady=2,sticky='NEWS')


btnframe.grid(row=1,column=0,sticky='NEWS')






















root.mainloop()