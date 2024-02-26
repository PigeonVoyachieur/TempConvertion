import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.title("Temp convertion")

label = ttk.Label(fenetre, text="Enter the temperature in Farenheit")
label.grid(column=0, row=0, sticky=tk.E, padx=5 , pady= 5)

entry  = ttk.Entry(fenetre)
entry.grid(column=1, row=0, sticky=tk.E, padx=5 , pady= 5)

def convertir():
    temperature= entry.get()
    calcul= (float(temperature) - 32)* 5/9
    Resultat= f"Here is the conversion to degrees Celsius {calcul} °C"
    messagebox.showinfo("Celsius temperature",Resultat)

bouton = ttk.Button(fenetre, text="convert", command=convertir)
bouton.grid(column=1, row=1, sticky=tk.E , padx=5,pady=5)

fenetre.mainloop()