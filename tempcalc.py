from tkinter import *

def tempfc():
	def die2():
		roo.destroy()
	deg =float(e1.get())
	var=((deg-32)/1.8)
	roo =Tk()
	mes = Label(roo,text = var)
	die = Button(roo,text="Quit",command = lambda:die2())
	mes.pack()
	die.pack(side = RIGHT)
	roo.mainloop()
	
def tempcf():
	def die2():
		roo.destroy()
	deg =float(e1.get())
	var=((deg*1.8)+32)
	roo= Tk()
	mes = Label(roo,text= var)
	die = Button(roo,text="Quit",command = lambda:die2())
	die.pack(side = RIGHT)
	mes.pack()
	roo.mainloop()
def die():
	root.destroy()
root =Tk()

f = Frame(root, height =65, width =65)
bfc = Button(root, text= "Farenheit to celsius", command = lambda: tempfc())
bcf = Button(root,text ="celsius to Farenheit", command = lambda: tempcf())
bd = Button(root,text="Quit",command = lambda:die())
bd.pack(side = RIGHT)
e1 =Entry(root)
e1.pack()
f.pack()
bfc.pack(side = RIGHT)
bcf.pack(side = RIGHT)
root.mainloop()
