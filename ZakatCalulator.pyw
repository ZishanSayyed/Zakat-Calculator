from tkinter import Tk,Button,Label,DoubleVar,Entry   #DoubleVar is a data type in this case its a boolean

window=Tk()
window.title("Zakat Calculator")
window.configure(background="green")
window.geometry("320x220")
window.resizable(width=False,height=False)



def calulate():
    value=float(Amt_entry.get())   # value get enter
    Zakat=value*0.025         #value converted
    Zakat_value.set(Zakat) # value displayed


def clear():
    Amt_value.set("")
    Zakat_value.set("")



Amt_lbl=Label(window,text="Amount",bg="black",fg="white",width=14) #fg is forground property
Amt_lbl.grid(column=0,row=0,padx=15,pady=15)   #the lable tab be at 0 column and 0 row posstion pad use for spaceing form x and y


Amt_value=DoubleVar()  # Value which be in window is boolean
Amt_entry=Entry(window,textvariable=Amt_value,width=14)
Amt_entry.grid(column=1,row=0)
Amt_entry.delete(0,"end") #we get empty window every time we open the app

Zakat_lbl=Label(window,text="Zakat",bg="black",fg="white",width=14)
Zakat_lbl.grid(column=0,row=1,padx=15,pady=15)

Zakat_value=DoubleVar()  # Value which be in window is boolean
Zakat_entry=Entry(window,textvariable=Zakat_value,width=14)
Zakat_entry.grid(column=1,row=1)
Zakat_entry.delete(0,"end")

Calculate_btn=Button(window,text="Calculate",bg="black",fg="white",width=14,command=calulate)
Calculate_btn.grid(column=0,row=3,padx=15)

clear_btn=Button(window,text="Clear",bg="black",fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=15)



















window.mainloop()  #run App
