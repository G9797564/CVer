from tkinter import *
import pickle as pk
 
def add(event):
	lb.insert(END,lb.clipboard_get())
	
def delete(event):
	lb.delete("active")
	
def save():
	fw=open("CVData","wb")
	pk.dump(lb.get(0,END),fw)
	fw.close()
	win.destroy()
	
def copy(event):
	lb.clipboard_clear()
	lb.clipboard_append(lb.get("active"))
	
def up(event):
	act=lb.get("active")
	con=lb.get(0,END)
	pos=con.index(act)
	lb.delete(0,END)
	for i in range(0,pos-1):
		lb.insert(END,con[i])
	lb.insert(END,con[pos])
	if pos!=0:
		lb.insert(END,con[pos-1])
	for i in range(pos+1,len(con)):
		lb.insert(END,con[i])
	lb.activate(lb.get(0,END).index(act))
		
def down(event):
	act=lb.get("active")
	con=lb.get(0,END)
	pos=con.index(act)
	lb.delete(0,END)
	for i in range(0,pos):
		lb.insert(END,con[i])	
	if pos!=len(con)-1:
		lb.insert(END,con[pos+1])
	lb.insert(END,con[pos])
	for i in range(pos+2,len(con)):
		lb.insert(END,con[i])
	lb.activate(lb.get(0,END).index(act))
	
win=Tk()
win.title("CtrlC+V")
win.attributes("-topmost",1)
lb=Listbox(win,font=("segoe print",15),width=20,height=30)#可调整窗口大小
lb.bind("<Button-3>",add)
lb.bind("<Double-Button-1>",copy)
lb.bind("<Button-2>",delete)
lb.bind("<BackSpace>",delete)
lb.bind("<F3>",up)
lb.bind("<F2>",down)
lb.bind("<Key-8>",up)
lb.bind("<Key-2>",down)
con=pk.load(open("CVData","rb"))
for i in con:
	lb.insert(END,i)
lb.pack()
win.protocol("WM_DELETE_WINDOW",save)
win.mainloop()
