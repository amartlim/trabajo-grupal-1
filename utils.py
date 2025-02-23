import math
import random

def distancia(Persona1, Persona2):
        calculo=math.sqrt((Persona2.pos_x-Persona1.pos_x)**2 + (Persona2.pos_y-Persona1.pos_y)**2)
        print(f"La distancia entre {Persona1.nombre} y {Persona2.nombre} es {round(calculo,2)} metro/s")
        if calculo==0:
            print(f"{Persona1.nombre} y {Persona2.nombre} estan en el mismo sitio, cruzan miradas, eso solo significa una cosa: COMBATE POKEMOOONN!!!! ")
            
def mover_todas_las_personas(listas_personas):  
    for i in listas_personas:
        i.pos_x=random.randrange(0,9)
        i.pos_y=random.randrange(0,9)

def persona_recoger_moneda(lista_personas, lista_monedas):
    for p in lista_personas:
        for m in lista_monedas:
            
            if p.pos_x == m.pos_x and p.pos_y == m.pos_y :
                p.monedero +=1
                
def cuantas_monedas_tiene_persona(persona):
    return persona.monedero    
           
def riqueza_total(lista_personas):
    suma=0
    for p in lista_personas:
        suma+=p.monedero 
    return suma    
