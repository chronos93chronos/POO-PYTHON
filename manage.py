#APRENDIENDO PROGRAMACION ORIENTADA A OBJETOS EN PYTHON


class humano():#CREACION DE CLASE HUMANO

    #FUNCION __INIT__ INICIALIZA LOS ATRIBUTOS DE LA CLASE
    #SELF SIRVE PARA USAR LAS VARIABLES EN TODOS LOS METODOS 
    def __init__(self,nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
    
    #FUNCION __STR__ SIRVE PARA TRANSFORMAR LOS ATRIBUTOS DE LA CLASE EN UNA CADENA DE CARACTERES
    def __str__(self):
        return f"nombre:{self.nombre}, Edad:{self.edad},Pais:{self.pais}"
    
    #SE CREA UN METODO QUE IMPRIME EL ATRIBUTO NOMBRE (CON SELF PUEDO USAR EN LA FUNCION CUALQUIER VARIABLE QUE SE INICIALIZA EN __INIT__)
    def imprimir(self):
        print("El nombre de usuario es",self.nombre )

    

#SE CREA UNA INSTANCIA DE LA CLASE HUMANO
#SE LE ENTREGA LOS VALORES SOLICITADOS Y ASI SE CREA UN OBJETO DE LA CLASE HUMANO
humano_1 = humano("chronos", 30, "chile")

# SE ACTUALIZA EL VALOR DEL ATRIBUTO NOMBRE
humano_1.nombre = "Alexander"

#DEL ELIMINA EL ATRIBUTO PAIS DEL OBJETO HUMANO_1
#SE PUEDE ELIMINAR EL OBJETO TAMBIEN CON DEL
#del humano_1.pais 
#del humano_1

print(humano_1)
#___________________________________________________________
#           HERENCIA

class persona():
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def imprimir(self):
        print(self.fname, self.lname)

persona_1 = persona("alexander", "hernandez")
persona_1.imprimir()
    

        
        

