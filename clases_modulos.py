from utils import *
import matplotlib.pyplot as plt

# Clase Persona
class Persona:
    def __init__(self, nombre, año_nacimiento, nacionalidad, hobby, cantante_favorito,genero, pos_x=0, pos_y=0):
        self.nombre = nombre
        self.año_nacimiento = año_nacimiento
        self.edad = 2025 - año_nacimiento
        self.nacionalidad = nacionalidad
        self.hobby = hobby
        self.cantante_favorito = cantante_favorito
        self.genero=genero
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.monedero = 0 

    # Método para saludar
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y nací en el año {self.año_nacimiento} y tengo {self.edad} años.")


   

# Clase Moneda
class Moneda: 
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x 
        self.pos_y = pos_y

# Clase Espacio
class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_personas = []
        self.lista_monedas=[]

    # Método para agregar una persona al espacio
    def agregar_persona(self, persona):
        self.lista_personas.append(persona)
        print(f"{persona.nombre} ha sido añadido/a al espacio '{self.nombre}'.")
    
    def agregar_monedas(self, moneda):
        self.lista_monedas.append(moneda)
        
    
    def devolver_lista_personas(self):
        return self.lista_personas
    def devolver_lista_monedas(self):
        return self.lista_monedas

    # Método para listar las personas que están en el espacio
    def listar_personas(self):
        if self.lista_personas:
            print(f"Personas en el espacio '{self.nombre}':")
            for persona in self.lista_personas:
                print(f"- {persona.nombre} en la posición ({persona.coord_x}, {persona.coord_y})")
        else:
            print(f"No hay personas en el espacio '{self.nombre}'.")




# Función para calcular la distancia euclidiana entre dos personas

#def calcular_distancia(persona1, persona2, persona3, persona4):
#    distancia_1_3 = math.sqrt((persona1.coord_x - persona3.coord_x) ** 2 + (persona1.coord_y - persona3.coord_y) ** 2)
#    distancia_2_4 =  math.sqrt((persona2.coord_x - persona4.coord_x) ** 2 + (persona2.coord_y - persona4.coord_y) ** 2)
#    return distancia_1_3, distancia_2_4
   

# Función para verificar si dos personas están en la misma posición
'''
def estan_en_misma_posicion(persona1, persona2, persona3, persona4):
    return persona1.coord_x == persona2.coord_x and persona1.coord_y == persona2.coord_y
'''

# Función para contar cuántas personas hay en un espacio
def contar_personas_en_espacio(espacio):
    return len(espacio.lista_personas) 

# Ejemplo de uso:

# Crear personas
persona1 = Persona("Adriana", 2006, "Española", "Tenis", "Melendi","F", 0, 0)
persona2 = Persona("Manuel", 2004, "Español", "Fútbol", "Estopa","M", 5, 5)
persona3=Persona("Fran", 2006, "Epañola", "Badmington", "Depol", "M", 8,2  )
persona4=Persona("Paula", 2006,"Española", "Baile", "Quevedo", "F", 4, 6)

moneda1=Moneda(3,6)
moneda2=Moneda(7,2)
moneda3=Moneda(4,9)
moneda4=Moneda(8,2)
moneda5=Moneda(6,5)



# Crear un espacio y agregar personas
'''parque = Espacio("Parque")
parque.agregar_persona(persona1)
parque.agregar_persona(persona2)

parque.repartir_monedas(5, 10, 10)
persona1.mover_a(3, 7)
persona2.mover_a(3, 7)

persona1.recoger_moneda(parque.monedas)
persona2.recoger_moneda(parque.monedas)

'''
'''
parque.agregar_persona(persona3)
parque.agregar_persona(persona4)
# Listar personas en el espacio
parque.listar_personas()

# Calcular la distancia entre dos personas
distancia = calcular_distancia(persona1, persona2)
print(f"La distancia entre {persona1.nombre} y {persona2.nombre} es {distancia:.2f} unidades.")

# Verificar si están en la misma posición
if estan_en_misma_posicion(persona1, persona2):
    print(f"{persona1.nombre} y {persona2.nombre} están en la misma posición.")
else:
    print(f"{persona1.nombre} y {persona2.nombre} están en posiciones diferentes.")

# Contar personas en el espacio
total_personas = contar_personas_en_espacio(parque)
print(f"El número de personas en el espacio '{parque.nombre}' es {total_personas}.")
'''

Espacio1=Espacio("Parque")
Espacio1.agregar_persona(persona1)
Espacio1.agregar_persona(persona2)
Espacio1.agregar_persona(persona3)
Espacio1.agregar_persona(persona4)

Espacio1.agregar_monedas(moneda1)
Espacio1.agregar_monedas(moneda2)
Espacio1.agregar_monedas(moneda3)
Espacio1.agregar_monedas(moneda4)
Espacio1.agregar_monedas(moneda5)
#lista_personas=Espacio1.devolver_lista_personas()
#print(lista_personas)
#print(Espacio1.devolver_lista_monedas())
persona_recoger_moneda(Espacio1.devolver_lista_personas(), Espacio1.devolver_lista_monedas())
datos_riqueza=[]
M=[]
F=[]
for x in range(0,10):
    mover_todas_las_personas(Espacio1.devolver_lista_personas())
    persona_recoger_moneda(Espacio1.devolver_lista_personas(), Espacio1.devolver_lista_monedas())
    print("riqueza total :",riqueza_total(Espacio1.devolver_lista_personas()))
    combate(persona1,persona2)
    combate(persona1,persona3)
    combate(persona1,persona4)
    combate(persona2,persona3)
    combate(persona2,persona4)
    combate(persona3,persona4)
    datos_riqueza.append(riqueza_total(Espacio1.devolver_lista_personas()))
    masculino,femenino= riqueza_total_genero(Espacio1.devolver_lista_personas())
    M.append(masculino)
    F.append(femenino)

print(f"los hombres:{M}")
print(f"las mujeres:{F}")
    
print(datos_riqueza)
# Crear la figura
plt.figure(figsize=(6, 4))

# Graficar la secuencia de valores en el array
plt.plot(range(1, len(datos_riqueza) + 1), datos_riqueza, marker='o', linestyle='-', color='blue', label="Riqueza Total x Turno")

# Configurar el gráfico
plt.xticks(range(1, len(datos_riqueza) + 1))
plt.xlabel("Nº de Turnos")
plt.ylabel("Valor Monedas")
plt.title("Evolución de la Riqueza")
plt.legend()
plt.grid()

# Mostrar el gráfico
plt.show()



#print("el monedero de la persona 3 es :",persona3.monedero)
#print("el monedero de la perona 1 es :",cuantas_monedas_tiene_persona(persona1))
#print("riqueza total :",riqueza_total(Espacio1.devolver_lista_personas()))
#mover_todas_las_personas(Espacio1.devolver_lista_personas())
#distancia(persona1,persona2)
#distancia(persona1,persona3)
#distancia(persona1,persona4)
#distancia(persona2,persona3)
