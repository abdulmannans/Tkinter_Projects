#Created By Abdul Mannan
#Form Ver 1.0
#16-10-2019 23:57 

#Importing
from tkinter import *
import sqlite3 

#Screen
screen = Tk()
screen.title("Feedback Form")
#Creating Function
def save():
	s_fname = fname.get()
	s_lname = lname.get()
	s_age = age.get()
	s_age = str(s_age)
	s_adress = adress.get()
	s_review = review.get()
	s_null = "      "

	file = open("registeration.txt", "w")
	file.write(s_fname)
	file.write(s_null)
	file.write(s_lname)
	file.write(s_null)
	file.write(s_age)
	file.write(s_null)
	file.write(s_adress)
	file.write(s_null)
	file.write(s_review)
	file.close()
#Clear text box
	fname_text.delete(0, END)
	lname_text.delete(0, END)
	age_text.delete(0, END)
	adress_text.delete(0, END)
	review_text.delete(0, END)

#creating a sumbit Function
def sumbit():
	#Connecting Database
	conn= sqlite3.connect('registeration.db')
	
	#Creating cursor
	c = conn.cursor()
	
	#Insert into Table
	c.execute("INSERT INTO entry VALUES(:d_fname, :d_lname, :d_age, :d_adress, :d_review)",
 			{
 				'd_fname':fname_text.get(),
 				'd_lname':lname_text.get(),
 				'd_age':age_text.get(),
 				'd_adress':adress_text.get(),
 				'd_review':review_text.get()})
	#Clear text box
	fname_text.delete(0, END)
	lname_text.delete(0, END)
	age_text.delete(0, END)
	adress_text.delete(0, END)
	review_text.delete(0, END)



	#Comit changes
	conn.commit()
	
	#Closing Connection
	conn.close()
#Creating View Function
def view():
	#Connecting Database
	conn= sqlite3.connect('registeration.db')

	#Creating cursor
	c = conn.cursor()

	#Query 
	c.execute("SELECT *, oid FROM entry")
	records = c.fetchall()
	print(records)

	#loop
	print_records = ''
	for record in records:
		print_records += str(record) + "\n"

	query_label = Label(screen, text=print_records)
	query_label.grid(row=7 ,column=, columnspan=4)
	query_label.config(font=("Cooper Black", 15))





	#Comit changes
	conn.commit()

	#Closing Connection
	conn.close()

#Connecting Database
conn= sqlite3.connect('registeration.db')

#Creating cursor
c = conn.cursor()

#Create Changes
'''c.execute("""CREATE TABLE entry (
			e_fname text,
			e_lname text,
			e_age integer,
			e_adress text,
			e_review text)""")'''

#Comit changes
conn.commit()
#Closing Connection
conn.close()

#Declaring Variable 
fname = StringVar()
lname = StringVar()
age = IntVar()
adress = StringVar()
review = StringVar()

#Creating Labels 
fname_label = Label(screen, text="First Name:")
fname_label.config(font=("Cooper Black", 10))
lname_label = Label(screen, text="Last Name:")
lname_label.config(font=("Cooper Black", 10))
age_label = Label(screen, text="Age:")
age_label.config(font=("Cooper Black", 10))
adress_label = Label(screen, text="Adress:")
adress_label.config(font=("Cooper Black", 10))
review_label = Label(screen, text="Review:")
review_label.config(font=("Cooper Black", 10))
fname_label.grid(row=1, column=1)
lname_label.grid(row=2, column=1)
age_label.grid(row=3, column=1)
adress_label.grid(row=4, column=1)
review_label.grid(row=5, column=1)

#Creatinggg Text-Box
fname_text = Entry(textvariable = fname )
lname_text = Entry(textvariable = lname )
age_text = Entry(textvariable = age )
adress_text = Entry(textvariable = adress)
review_text = Entry(textvariable = review )
fname_text.grid(row=1, column=2)
lname_text.grid(row=2, column=2)
age_text.grid(row=3, column=2)
adress_text.grid(row=4, column=2)
review_text.grid(row=5, column=2)

#Creating Button 
exit_button = Button(screen, text="EXIT", command=screen.destroy)
exit_button.grid(row=6, column=3)
save_button = Button(screen, text="Save Entry" ,command=sumbit)
save_button.grid(row=6, column=1)
view_button = Button(screen, text="View All Entry", command=view)
view_button.grid(row=6, column=2)



screen.mainloop()
