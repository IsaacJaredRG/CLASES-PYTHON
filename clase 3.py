class animales:
    color="marron"
    raza="fina"
    cantidad_patas="si"
    tipo="hominido"
    alimentacion="carnivoro"
    nacimiento="oviparo"

    def comer(self):
        print("esta comiendo")

coyote=animales()
coyote.tipo="cuadrupedo"
coyote.comer()
print(coyote.tipo)
