class carros:
    color="Rojo"
    Marca="Audi"
    modelo= "1"
    potencia=180
    tamaño="Grande"

    def correr(self):
        print ("brum")
    
    def  prender(self):
        print ("no está prendido")
    
    def colorxd (self):
        return self.modelo
     
    def que_color_es(self):
        if self.modelo == "1":
            print("el color es azul")
        elif self.modelo== "2":
            print("el color es rojo")
        elif self.modelo== "3":
            print("el color es negro")

audir8=carros()
audir8.modelo="2"
audir8.color="azul"
audir8.que_color_es()