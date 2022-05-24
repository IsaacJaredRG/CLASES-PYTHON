from pickle import FALSE, TRUE


class zapatos:
    precio=""
    tipo=""
    talla=""
    color=""
    abujetas=FALSE

    def desabrocharse(self):
        print("ahhhhh me caigo")


tennis=zapatos()
tennis.precio="1000"
tennis.tipo="deportivo"
tennis.talla="28"
tennis.color="azul"
tennis.abujetas=TRUE

print(tennis.precio)
tennis.desabrocharse()