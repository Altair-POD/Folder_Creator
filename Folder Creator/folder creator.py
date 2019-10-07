from tkinter import *
from tkinter import messagebox
import os




root = Tk()
root.title('Folder Maker')
root.geometry("270x200")



	
def Make():
	url = str(urle.get())
	startnumber = int(noe1.get())
	finishingnumber = int(noe2.get())

	os.chdir(url)

	for i in range(startnumber, finishingnumber+1):

		os.mkdir(str(i))

	ret = messagebox.showinfo("Info", "Operation succeeded")

	if ret == 'ok':
		urle.delete(0, END)
		noe1.delete(0, END)
		noe2.delete(0, END)







urll = Label(root, text = "Path").grid(row = 0, column = 0, padx = 10, pady = 10)

urle = Entry(root)
urle.grid(row = 0, column = 1, padx = 10, pady = 10)



nol1 = Label(root, text = "starting number").grid(row = 1, column = 0, padx = 10, pady = 10)
noe1 = Entry(root)
noe1.grid(row = 1, column = 1)

nol2 = Label(root, text = "finishing number").grid(row = 2, column = 0, padx = 10, pady = 10)
noe2 = Entry(root)
noe2.grid(row = 2, column = 1)

Button(root, text = "Make", command = Make).grid(row = 3, column = 0, columnspan = 2, ipadx = 40, pady = 10)







root.mainloop()