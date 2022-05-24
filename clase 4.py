
class computadora:
    color="azul"
    marca=""
    procesador=""
    ram=""
    memoria=""

    def prender(self):
        print("no funciona")
    
    def correr_videojuego(self):
        print("MINECRAFT")

lenovo_ideapad_3=computadora()
lenovo_ideapad_3.color="azul"
lenovo_ideapad_3.procesador="ryzen 5 5500U"
lenovo_ideapad_3.ram="8GB"
lenovo_ideapad_3.memoria="256GB"
print("Lenovo Ideapad 3")
print(lenovo_ideapad_3)
print(lenovo_ideapad_3.procesador)
print(lenovo_ideapad_3.ram)
print(lenovo_ideapad_3.memoria)
lenovo_ideapad_3.prender()
lenovo_ideapad_3.correr_videojuego()
