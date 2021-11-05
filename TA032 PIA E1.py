from tkinter import *
from maquina import TuringMachine
def iniciar(frame: Frame, e: Entry, b:Button, maquina: TuringMachine): 
    x=20
    y=20
    Label(frame, text=maquina.lenguaje, padx=x, pady=y, font=maquina.font).grid(row=0, column=1)
    for r in maquina.reglas: 
        Label(frame, text=r, pady=5, font=maquina.font).grid(columnspan=2)
    Label(frame, text="\nIngrese una cadena para validar: ", pady=y/2, font=maquina.font).grid(columnspan=2)
    e.grid(columnspan=2, pady=y)
    b.grid(columnspan=2)
def continuar(resultado: Label, si: Button, no: Button, pregunta: Label, b: Button): 
    e.configure(state='normal')
    b.configure(state="active")
    resultado.configure(text="")
    si.destroy()
    no.destroy()
    pregunta.destroy()

def click(e: Entry, resultado: Label, frame: Frame, b: Button, root: Tk, maquina: TuringMachine):
    if maquina.q0(e.get()): 
        resultado.configure(text="Cadena válida")
    else: 
        resultado.configure(text="Cadena inválida")
    resultado.grid(columnspan=2)
    e.configure(state='disabled')
    b.configure(state="disabled")
    si = Button(frame, text="Sí", padx=20, font=maquina.font)
    no = Button(frame, text="No", padx=20, font=maquina.font)
    pregunta = Label(frame, text="¿Desea continuar?", font=maquina.font)
    pregunta.grid(columnspan=2)
    si.grid(row= 16,column=0, pady=10)
    no.grid(row=16, column=1, pady=10)

    si.configure(command=lambda: continuar(resultado, si, no, pregunta, b))
    no.configure(command=lambda: root.destroy())

    pass
if __name__=="__main__": 
    maquina = TuringMachine()
    root = Tk()
    root.title("PIA")
    Label(root, text="Esta maquina de Turing acepta una cadena y determina si es válida o no para el siguiente lenguaje: ", font=maquina.font, pady=10).pack()
    frame = Frame(root)
    frame.pack()
    e=Entry(frame, font=maquina.font)
    resultado = Label(frame, font=maquina.font)
    b=Button(frame, text="Ingresar cadena", font=maquina.font, command=lambda: click(e, resultado, frame, b, root, maquina), pady=10, padx=10)
    iniciar(frame, e, b, maquina)
    resultado.grid(columnspan=2)
    root.mainloop()