from tkinter import Tk, Frame, Entry, Label, Button

class TuringMachine(): 
    def __init__(self) -> None:
        self.pos: int = ''
        self.cadena: str = ''
        self.lenguaje: str = 'L = { a^(n+1)(aba)^n c² | n>=0 }'
        self.reglas = ['Ejemplos válidos: ', 'n = 0 => acc', 'n = 1 => aaabacc', 'n = 2 => aaaabaabacc']
        self.font: tuple = ('bold', 15)
        pass
    def reemplazar(self, simbolo: str)->None: 
        self.cadena = self.cadena[:self.pos] + simbolo + self.cadena[self.pos+1:]
    def q0(self, cad: str)->bool:
        self.cadena = '#' + cad + '#'
        print('q0')
        print(self.cadena)
        self.pos = 1
        return self.q1()
    def q1(self)->bool: 
        print('q1')
        print(self.cadena)
        if self.cadena[self.pos] == 'a': 
            self.reemplazar('#')
            self.pos += 1
            return self.q2()
        return False
    def q2(self)->bool: 
        if self.cadena[self.pos] != '#': 
            self.pos += 1
            return self.q2()
        else: 
            self.pos -= 1
            return self.q3()
    def q3(self)->bool: 
        print('q3')
        print(self.cadena)
        if self.cadena[self.pos] == 'c': 
            self.reemplazar('#')
            self.pos -=1
            return self.q4()
        return False
    def q4(self)->bool: 
        print('q4')
        print(self.cadena)
        if self.cadena[self.pos] == 'c': 
            self.reemplazar('#')
            self.pos -= 1
            return self.q5()
        return False
    def q5(self)->bool: 
        print('q5')
        print(self.cadena)
        if self.cadena[self.pos] == '#': 
            return True
        elif self.cadena[self.pos] == 'a':
            self.reemplazar('#')
            self.pos -= 1 
            return self.q6()
        return False
    def q6(self)->bool: 
        print('q6')
        print(self.cadena)
        if self.cadena[self.pos] == 'b': 
            self.reemplazar('#')
            self.pos -= 1
            return self.q7()
        return False
    def q7(self)->bool: 
        print('q7')
        print(self.cadena)
        if self.cadena[self.pos] == 'a': 
            self.reemplazar('#')
            self.pos -= 1
            return self.q8()
        return False
    def q8(self)->bool: 
        print('q8')
        print(self.cadena)
        if self.cadena[self.pos] != '#': 
            self.pos -= 1
            return self.q8()
        else: 
            self.pos += 1
            return self.q9()
    def q9(self)->bool: 
        print('q9')
        print(self.cadena)
        if self.cadena[self.pos] == 'a': 
            self.reemplazar('#')
            self.pos += 1
            return self.q10()
        return False
    def q10(self)->bool: 
        print('q10')
        print(self.cadena)
        if self.cadena[self.pos] != '#': 
            self.pos += 1
            return self.q10()
        else: 
            self.pos -= 1
            return self.q5()

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