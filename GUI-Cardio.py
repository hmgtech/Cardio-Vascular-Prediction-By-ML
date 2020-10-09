from tkinter import *
import tkinter as tk

from tkinter import filedialog
from tkinter import messagebox  

from sklearn.externals import joblib 
import skimage
from skimage.io import imread
from skimage.transform import resize
import numpy as np

from PIL import ImageTk, Image

classifier = joblib.load('cardio2.h5') 

global a


def filedreq():
	if Name.get() == "":
		print("Name Field is Empty!!")
		user = "Name Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=610)	
	elif age.get() == 0:
		print("Age Field is Empty!!")
		user = "Age Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=610)

	elif height.get() == 0:
		print("Height Field is Empty!!")
		user = "Height Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=610)

	elif weight.get() == 0:
		print("Weight Field is Empty!!")
		user = "Weight Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=610)

	elif ap_hi.get() == 0:
		print("Systolic blood pressure:  is Empty!!")
		user = "Systolic blood pressure:  is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=610)

	elif ap_lo.get() == 0:
		print("Diastolic blood pressure:  is Empty!!")
		user = "Diastolic blood pressure:  is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=610)


	else:
		test()


def test():
	print("Testing...")
	# Test code will go here....
	a = age.get()
	h = height.get()
	w = weight.get()
	aphi = ap_hi.get()
	aplo = ap_lo.get()
	g = gender.get()
	c = cholesterol.get()
	gl = gluc.get()
	s = smoke.get()
	al = alcohol.get()
	ac = active.get()

	bmi = ((w/h)/h)*10000
	pressure = aphi - aplo
	bmit = "BMI: "+str(bmi)
	pret = "Blood Pressure: "+str(pressure)
	Label(win,text=bmit,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=300,y=260)
	Label(win,text=pret,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=300,y=340)
	
	Prediction = [[a,g,h,w,aphi,aplo,c,gl,s,al,ac,bmi,pressure]]

	result = classifier.predict(Prediction)
	print(result)

	if result[0] == 1:
	    print("Infected")
	    person = Name.get()
	    user = person + ' having Cardio-Vascular Problem!!!'
	    a = user
	    Label(win,text="                                                              ",fg="red",bg="white",font = ("Calibri 12 bold")).place(x=12,y=610)
	    Label(win,text=user,fg="red",bg="white",font = ("Calibri 12 bold")).place(x=12,y=610)
	    MsgBox = tk.messagebox.showwarning ('warning','Cardio-Vascular Problem Found!! \nEat Vegetables, Fruits, Milk Products, Fish, Sugar With Honey!! \nReport is saved by Persons Name',icon = 'warning')
	
	else:
	    print("Uninfected")
	    person = Name.get()
	    user = person + ' not having Cardio-Vascular Problem!!!'
	    a = user
	    Label(win,text=". ",fg="red",bg="white",font = ("Calibri 12 bold")).place(x=12,y=610)
	    Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 12 bold")).place(x=12,y=610)
	    MsgBox = tk.messagebox.showinfo ('information','Cardio-Vascular Problem Not Found!! \nPateint is at Less Risk!! \nEat Vegetables, Fruits, Milk Products, Fish, Sugar With Honey!! \nReport is saved by Persons Name', icon = 'info')

	# After Test, save() will execute
	# save(a)

def save(a):
	
	Name = Name.get()
	Last = Lname.get()
	gender = str(radio.get())
	save_name = Name+".txt"

	file = open(save_name,"a")
	file.write("\nName: "+First+"\n")
	file.write("Gender: "+gender+"\n")
	file.write("Report: "+ a +"\n")
	file.close()
	report = First + "'s Health Detection have successfully done and Report is saved in "+First+".txt"
	Label(win,text=report,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=500)
	# print("Printing Data: ")
	# print(First,Last,phone,email,address,gender)

def reset():
	Name.set("")
	entry_Address.delete(1.0,END)

win =  Tk()

# win.geometry("600x650")
win.geometry("{0}x{1}+0+0".format(500, win.winfo_screenheight()))
win.configure(background="cyan")
win.title("Cardio Disease Prediction By Hitesh")
win.iconbitmap('1.ico')

title = Label(win,text="Cardio Disease Prediction",bg="gray",width="30",height="2",fg="White",font = ("Calibri 20 bold italic underline"))
title.place(x=0,y=0)

my_img = ImageTk.PhotoImage(Image.open("2.png"))
my_label = Label(image=my_img)
my_label.place(x=400,y=0)


Name = StringVar()
gender = IntVar()
age = IntVar()
height = DoubleVar()
weight = DoubleVar()
ap_hi = DoubleVar()
ap_lo = DoubleVar()
cholesterol = IntVar()
gluc = IntVar()
smoke = IntVar()
alcohol = IntVar()
active = IntVar()


Name = Label(win, text="Name: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=100)
Name = Entry(win,textvariable = Name,width=30)
Name.insert(0, 'Name of Person')
Name.place(x=120,y=100)

Age = Label(win, text="Age: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=140)
Age = Entry(win,textvariable = age,width=30)
Age.insert(0, 'Age of Person: ')
Age.place(x=120,y=140)


Gender = Label(win, text="Gender: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=180)
Male = Radiobutton(win, text="Male",bg="cyan",variable=gender,value=1,font = ("Verdana 12")).place(x=120,y=180)
Female = Radiobutton(win, text="Female",bg="cyan",variable=gender,value=0,font = ("Verdana 12")).place(x=220,y=180)

Height = Label(win, text="Height (in CMs): ",bg="cyan",font = ("Verdana 12")).place(x=12,y=220)
Height = Entry(win,textvariable = height,width=30)
Height.place(x=220,y=220)

Weight = Label(win, text="Weight (in KGs): ",bg="cyan",font = ("Verdana 12")).place(x=12,y=260)
Weight = Entry(win,textvariable = weight,width=30)
Weight.place(x=220,y=260)

aphi = Label(win, text="Systolic blood pressure: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=300)
aphi = Entry(win,textvariable = ap_hi,width=30)
aphi.insert(0, 'Between: 90 to 250:  ')
aphi.place(x=220,y=300)

aplo = Label(win, text="Diastolic blood pressure: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=340)
aplo = Entry(win,textvariable = ap_lo,width=30)
aplo.insert(0, 'Between: 60 to 140:  ')
aplo.place(x=220,y=340)

Cholesterol = Label(win, text="Cholesterol: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=380)
Normal = Radiobutton(win, text="Normal",bg="cyan",variable=cholesterol,value=1,font = ("Verdana 12")).place(x=12,y=400)
Above_Normal = Radiobutton(win, text="Above_Normal",bg="cyan",variable=cholesterol,value=2,font = ("Verdana 12")).place(x=100,y=400)
Well_Above_Normal = Radiobutton(win, text="Well_Above_Normal",bg="cyan",variable=cholesterol,value=3,font = ("Verdana 12")).place(x=250,y=400)

Glucose = Label(win, text="Glucose: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=440)
Normal = Radiobutton(win, text="Normal",bg="cyan",variable=gluc,value=1,font = ("Verdana 12")).place(x=12,y=460)
Above_Normal = Radiobutton(win, text="Above_Normal",bg="cyan",variable=gluc,value=2,font = ("Verdana 12")).place(x=100,y=460)
Well_Above_Normal = Radiobutton(win, text="Well_Above_Normal",bg="cyan",variable=gluc,value=3,font = ("Verdana 12")).place(x=250,y=460)


Smoke = Label(win, text="Smoke: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=500)
Yes = Radiobutton(win, text="Yes",bg="cyan",variable=smoke,value=1,font = ("Verdana 12")).place(x=120,y=500)
No = Radiobutton(win, text="No",bg="cyan",variable=smoke,value=0,font = ("Verdana 12")).place(x=220,y=500)

Alcohol = Label(win, text="Alcohol: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=540)
Yes = Radiobutton(win, text="Yes",bg="cyan",variable=alcohol,value=1,font = ("Verdana 12")).place(x=120,y=540)
No = Radiobutton(win, text="No",bg="cyan",variable=alcohol,value=0,font = ("Verdana 12")).place(x=220,y=540)

Active = Label(win, text="Active: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=580)
Yes = Radiobutton(win, text="Yes",bg="cyan",variable=active,value=1,font = ("Verdana 12")).place(x=120,y=580)
No = Radiobutton(win, text="No",bg="cyan",variable=active,value=0,font = ("Verdana 12")).place(x=220,y=580)


path = Label(win,bg="cyan",font = ("Verdana 8"))
path.place(x=140,y=600)

reset = Button(win, text="Reset", width="12",height="1",activebackground="red", bg="Pink",font = ("Calibri 12 "),command = reset).place(x=20, y=640)
submit = Button(win, text="Test", width="12",height="1",activebackground="violet", bg="Pink",command = filedreq,font = ("Calibri 12 ")).place(x=240, y=640)

win.mainloop()


