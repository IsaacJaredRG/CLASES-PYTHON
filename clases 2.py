
class alumno:
    edad=19
    grupo="A"
    carrera="tics"
    promedio=7

    def asistir_a_clases(self):
        print ("está asisitiendo a clases jaja")
    
    def poner_atenciom(self):
        print("jaja alumnos poner atención")
    
    def equisde(self):
        print("a")
    
    def pasar_maateria(self):
        return self.promedio
    def pasarMateria(self):
        if self.promedio > 7:
            print("no le sabe")
        else:
            print("le sabe poquito")

paola=alumno()
paola.asistir_a_clases()
paola.edad=21
print(paola.edad)
paola.promedio=6
