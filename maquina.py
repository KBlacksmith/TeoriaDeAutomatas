class TuringMachine(): 
    def __init__(self) -> None:
        self.pos: int = ''
        self.cadena: str = ''
        self.lenguaje: str = ''
        self.reglas = ['{ a^(n+1)(aba)^n c² | n>=0 }', 'Ejemplos válidos: ', 'acc', 'aaabacc', 'aaaabaabacc']
        self.font: tuple = ('bold', 15)
        pass
    def reemplazar(self, simbolo: str)->None: 
        self.cadena = self.cadena[:self.pos] + simbolo + self.cadena[self.pos+1:]
    def q0(self, cad: str)->bool:
        print('q0')
        self.cadena = '#' + cad + '#'
        self.pos = 1
        print(self.cadena)
        v: bool
        if self.cadena[self.pos] == 'a': 
            v = self.q1()
        else: 
            v = False
        if v: 
            print('Cadena válida')
        else: 
            print('Cadena inválida')
        print('-'*20)
        return v
    def q1(self)->bool: 
        self.reemplazar('#')
        print('q1')
        print(self.cadena)
        self.pos += 1
        if self.cadena[self.pos] == 'a': 
            return self.q2()
        elif self.cadena[self.pos] == 'c':
            return self.q8()
        return False
    def q2(self): 
        self.reemplazar('#')
        print('q2')
        print(self.cadena)
        self.pos += 1
        while self.cadena[self.pos] != 'b':
            if self.cadena[self.pos] != '#': 
                self.pos += 1
                continue
            return False
        else: 
            self.pos -= 1
            if self.cadena[self.pos] == 'a': 
                return self.q3()
            return False
    def q3(self): 
        print('q3')
        self.reemplazar('X')
        print(self.cadena)
        self.pos += 1
        self.reemplazar('Y')
        print(self.cadena)
        self.pos += 1
        if self.cadena[self.pos] == 'a': 
            return self.q4()
        return False
    def q4(self): 
        self.reemplazar('X')
        print('q4')
        print(self.cadena)
        self.pos -= 1
        while self.cadena[self.pos] != '#': 
            self.pos -= 1
        else: 
            self.pos += 1
            if self.cadena[self.pos] == 'a': 
                return self.q2()
            elif self.cadena[self.pos] == 'X': 
                return self.q5()
        return False
    def q5(self): 
        self.reemplazar('#')
        print('q5')
        print(self.cadena)
        self.pos += 1
        if self.cadena[self.pos] == 'Y': 
            return self.q6()
        return False
    def q6(self): 
        self.reemplazar('#')
        print('q6')
        print(self.cadena)
        self.pos += 1
        if self.cadena[self.pos] == 'X': 
            return self.q7()
        return False

    def q7(self): 
        self.reemplazar('#')
        print('q7')
        print(self.cadena)
        self.pos += 1
        if self.cadena[self.pos] == 'X': 
            return self.q5()
        elif self.cadena[self.pos] == 'c': 
            return self.q8()
        return False

    def q8(self): 
        self.reemplazar('#')
        print('q8')
        print(self.cadena)
        self.pos += 1
        if self.cadena[self.pos] == 'c': 
            return self.q9()
        return False

    def q9(self): 
        self.reemplazar('#')
        print('q9')
        print(self.cadena)
        self.pos += 1
        return self.cadena[self.pos] == '#'
    
if __name__=='__main__': 
    print('Este archivo no debe ser utilizado de manera directa')
    print('Intente con el archivo \'TA032 PIA E1.py\'')