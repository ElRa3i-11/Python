from random import *
from tkinter import *




window = Tk()
test=True

Dif=0

#fonctions
def Easy_button() :
    Dif=1
    HardDiff.place_forget()
    EasyDiff.place_forget()
    DifficultyLabel.place_forget()
    return (Dif)

def Hard_button() :
    Dif=2
    HardDiff.place_forget()
    EasyDiff.place_forget()
    DifficultyLabel.place_forget()
    return(Dif)
def start_button() :
    startbutton.place_forget()
    label_citysim.pack_forget()
    userentry.place(relx=0.5, rely=0.5, anchor="center")
    Usubmit.place(relx=0.75, rely=0.45, anchor="center")
    Udelete.place(relx=0.75, rely=0.55, anchor="center")
def UsubmitF() :
    username = userentry.get()
    print(username)
    Udelete.place_forget()
    Usubmit.place_forget()
    userentry.place_forget()
    DifficultyLabel.place(relx=0.5, rely=0.4, anchor="center")
    EasyDiff.place(relx=0.4, rely=0.55, anchor="center")
    HardDiff.place(relx=0.6, rely=0.55, anchor="center")

def UdeleteF() :
    userentry.delete(11,END)
## declaring variables

## declaring label button etc
DifficultyLabel= Label(window)
userentry= Entry()
Usubmit= Button(window,text="Submit")
Udelete= Button(window,text="Delete")
startbutton= Button(window,text="Start the game")
mainmenu= PhotoImage(file="288256.png")
mainlabel= Label(image=mainmenu)
EasyDiff= Button(window,text="Easy")
HardDiff= Button(window,text="Hard")
## Lables and button etc config

window.title("CITYSIM")
window.geometry("1280x720")
window.config(background="black")
userentry.config(font=("Arial",30,"bold",),
              fg="white",
              bg="grey",)
userentry.insert(0,"User Name: ")


DifficultyLabel.config(text="Choose Difficulty",
              font=("Arial",30,"bold",),
              fg="white",
              bg="grey",
              bd=10,
              relief=RAISED,
              padx=10,
              pady=10,)

EasyDiff.config(text="Easy",
              font=("Arial",20,"bold",),
              fg="white",
              bg="grey",
              bd=10,
              relief=RAISED,
              )

HardDiff.config(font=("Arial",20,"bold",),
              fg="white",
              bg="grey",
              bd=10,
              relief=RAISED,
              )
EasyDiff.config(command=Easy_button)
HardDiff.config(command=Hard_button)
Udelete.config(command=UdeleteF)
Udelete.config(text="Delete",
              font=("Arial",20,"bold",),
              fg="white",
              bg="grey",
              bd=10,
              relief=RAISED,
              )

Usubmit.config(command=UsubmitF)
Usubmit.config(text="Submit",
              font=("Arial",20,"bold",),
              fg="white",
              bg="grey",
              bd=10,
              relief=RAISED,
              )
startbutton.config(command=start_button)
startbutton.config(text="Start",
              font=("Arial",30,"bold",),
              fg="white",
              bg="grey",
              bd=10,
              relief=RAISED,
              padx=10,
              pady=10,)
label_citysim = Label(window,
              text="The citysim",
              font=("Arial",50,"bold",),
              fg="white",
              bg="grey",
              bd=10,
              relief=RAISED,
              padx=10,
              pady=10,
              )

## Printing labels and others

mainlabel.place(x=0, y=0, relwidth=1, relheight=1)
mainlabel.lower()
startbutton.place(relx=0.5, rely=0.5, anchor="center")
label_citysim.pack()
window.mainloop()