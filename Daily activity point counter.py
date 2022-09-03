from tkinter import *                          #importing tkinter module
from datetime import date                      #importing datetime module for date

def get_data():
    result = data_entry.get()                   #this is the data collecting box to get data from user
    f = open("Data.txt", "r+")           #opend the file 
    f.read()                               #first read so that data enter in correct order
    f.writelines(str(today())+"    :    "+result+"\n") #adding data with date
    f.close()
    data_entry.delete(0 , 'end')

def today():                            #Getting todays date
    today = date.today()
    return today

root = Tk()
root.geometry("500x600")          #Main window configerations
root.minsize(500,600)
root.maxsize(500,600)

top_frame = Frame(root, bg="grey", borderwidth=6)
top_frame.pack(side=TOP, fill="x")                                           #welcome frame
l_welcome = Label(top_frame, text="Welcome To Point counter", fg="red")
l_welcome.pack()

data_f = Frame(root, bg="powder blue", width="600")
data_f.pack(fill="x")
entry_date = Label(data_f, text=today())                       #data entry field layout
entry_date.pack()
data_entry = Entry(data_f, width=20,font=("Arial", 18))
data_entry.pack()
entry_btn = Button(data_f, text="Submit", command=lambda:get_data())
entry_btn.pack()

show_data = Frame(root, borderwidth=6, relief=SUNKEN)           #stored data viewer title
show_data.pack(fill="x")
data_label = Label(show_data, text="Your privious data are here")
data_label.pack()

f = open("Data.txt", "r+")    #reading data and positioning them in window
fr = Frame(root)
fr.place(x=5,y=160)
for line in reversed(list(f)):    
    lable = Label(fr, text=line)
    lable.pack()

root.mainloop()                 #running the programme in mainloop