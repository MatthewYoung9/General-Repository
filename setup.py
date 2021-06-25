from tkinter import *
from tkinter import messagebox
import pyperclip


# BUG: warrant overpayment is temp. faulty

def basic(name, franchise):
    return ("Dear {}, \n".format(name)+"Please can you advise when we can expect to receive payment for the attached outstanding invoices for Evans Halshaw {}".format(franchise) +". If you require any further information or have any queries then please let me know. \nThank you,")

def warranty_overpayment(name, franchise):
    return ("Hello {}, \n".format(name)+ "I’ve just processing your warranty SBIs and have attached the overpayment(s)for the handling charge for the part. Would you like to leave them in write-off or are you going to invoice them? \nThank you,")

def refused_warranty_claim(name):
    return ("Hi {}, \n".format(name) + "I’m just doing the warranty SBIs and I’ve come across a claim refused for the attached job(s). Have we queried these? \nThanks,")
def warranty_dne(name):
    return "Hi {}, \n".format(name)+ "Please find attached a file of jobs for which there is no debt on the warranty account and I would like to know if they have been invoiced. \nThanks,"
def warranty_all(name,location):
    return ("Hi {}, \n".format(name)+" \nI’ve just processing your warranty SBIs and have attached the overpayment(s)for the handling charge for the part. Would you like to leave them in write-off or are you going to invoice them? \n \n I have also coome across a/some refused claim(s) which you shall also find attached. Have we queried these? \n \n Additionally, please find attached a file of jobs for which there is no debt on the warranty account ({}_DNE.pdf) I would like to know if they have been invoiced.\nThank you,".format(location))

        
#key down function
def click():
    name = nameEntry.get()
    franchise = franchiseEntry.get()
    location = locationEntry.get()
    output.delete(0.0, END)
    if dropDown.get()== "Basic":
        email = basic(name, franchise)
    elif dropDown.get() == "Warranty overpayment":
        email = warranty_overpayment(name, franchise)
    elif dropDown.get() == "Refused warranty claim":
        email = refused_warranty_claim(name)
    elif dropDown.get() == "Warranty invoice DNE":
        email = warranty_dne(name)
    elif dropDown.get() == "Warranty (all)":
        email = warranty_all(name,location)
    pyperclip.copy(email)
    output.insert(END, email)
    messagebox.showinfo("Information","email text copied to clipboard")


#main

fields = 4

window = Tk()
window.title("Email text generator")
window.configure(bg = "white")


# Photo

photo1 = PhotoImage(file = "logo.gif")
Label(window, image=photo1, bg= "white").grid(row=0, column = 0 , sticky = W)



# drop down
OPTIONS = ["Basic", "Warranty overpayment", "Refused warranty claim", "Warranty invoice DNE", "Warranty (all)"]

Label(window, text= "Email type:", bg= "white", fg = "black", font = "none 12 bold").grid(row=1,column =0,sticky = W)

dropDown = StringVar(window)
dropDown.set(OPTIONS[0]) # default value

w = OptionMenu(window, dropDown, *OPTIONS)
w.grid(row=1, column=0, sticky = E )



# Label (name)

Label(window, text= "Name:", bg= "white", fg = "black", font = "none 12 bold").grid(row=2,column =0,sticky = W)

#text entry box (name)

nameEntry = Entry(window, width = 40, bg = "white")
nameEntry.grid(row =2,column =0,sticky =E)

# Label (franchise)

Label(window, text= "Franchise:", bg= "white", fg = "black", font = "none 12 bold").grid(row=3,column =0,sticky = W)

#text entry box (franchise)

franchiseEntry = Entry(window, width = 40, bg = "white")
franchiseEntry.grid(row =3,column =0,sticky =E)

# Label (location)

Label(window, text= "Location:", bg= "white", fg = "black", font = "none 12 bold").grid(row=4,column =0,sticky = W)

#text entry box (location)

locationEntry = Entry(window, width = 40, bg = "white")
locationEntry.grid(row =4,column =0,sticky =E)
# add submit

Button(window, text= "Submit", width = 6, command = click).grid(row = fields+1, column = 0, sticky = W)

# output box

output = Text(window, width =75, height = 6, wrap = WORD, bg = "white")
output.grid(row = fields +2, column = 0 , sticky = W)
window.mainloop()

