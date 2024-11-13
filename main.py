from tkinter import *
from tkinter import ttk
import creatSlovar
import accuracy

root = Tk()

setHamEmail=set([])
setSpamEmail=set([])
P_spam=1
P_ham=1


def clicked():
    if not creatSlovar.CreateSlovarSpamAndHamEmail():
        label["text"] = "Dictionaries have been created successfully"
    else:
        label["text"] = "Error"

def setLebelText(text):
    label["text"] = text

def clicked2():
   he,ph = creatSlovar.readSet("slovarHam")
   se, ps = creatSlovar.readSet("slovarSpam")
   global setHamEmail
   global setSpamEmail
   global P_ham
   global P_spam
   setHamEmail = he
   setSpamEmail = se
   P_ham=ph
   P_spam=ps
   if len(setHamEmail)!=0 and len(setSpamEmail)!=0:
       setLebelText("dictionaries have been successfully read")

   return 0

def clicTest():
    ac=0
    if len(setHamEmail)==0 and len(setSpamEmail)==0:
        setLebelText("You must crete or red dictionaries")
    else:
        ac = accuracy.TEST("spam", setSpamEmail, setHamEmail, P_spam, P_ham)
        setLebelText("accuracy = " + str(ac))


#-----MAIN-----
root.title("METANIT.COM")
root.geometry("400x400")


label = ttk.Label(text="Hello Tkinter", background="#FFCDD2", foreground="#B71C1C", padding=8)
label.grid(row=0, column=0, columnspan=2, ipadx=100, ipady=6, padx=5, pady=5)

for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)


btnStartGeniration = ttk.Button(text="Create dictionaries",command=clicked)
btnStartGeniration.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)

btn4 = ttk.Button(text="Read dictionaries",command=clicked2)
btn4.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)

btnTest = ttk.Button(text="Numbering accuracy",command=clicTest)
btnTest.grid(row=1, column=2, ipadx=6, ipady=6, padx=5, pady=5)

root.mainloop()