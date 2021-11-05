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
    
if __name__=='__main__': 
    print('Este archivo no debe ser utilizado de manera directa')
    print('Intente con el archivo \'TA032 PIA E1.py\'')