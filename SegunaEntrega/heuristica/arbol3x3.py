class Nodo():
    padre = None
    hijos = None
    dato  = None
    coste = None

    #constructor 

    def __init__(self, dato, hijos = None):
        self.hijos = None
        self.padre = None
        self.dato  = dato
        self.asignar_hijos(hijos)

    #obtener datos
    def obtener_datos(self):
        return self.dato
    
    #asignar datos
    def asignar_datos(self, dato):
        self.dato = dato

    #obtener coste
    def obtener_coste(self):
        return self.coste
    
    #asignar coste
    def asignar_coste(self, coste):
        self.coste = coste

    #asignar hijos
    def asignar_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos != None:
            for hijito in self,hijos:
                hijito.padre = self

    #obtener hijos
    def obtener_hijos(self):
        return self.hijos
    
    #obtener padre
    def obtener_padre(self):
        return self.padre
    
    #asignar padre
    def asignar_padre(self, padre):
        self.padre = padre
    
    def igual(self, nodo):
        if self.obtener_datos()== nodo.obtener_datos():
            return True
        else:
            return False
        
    def en_lista(self, lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista=True
        return en_la_lista
