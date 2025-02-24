import math
import random

def distancia(persona1, persona2):
        calculo=math.sqrt((persona2.pos_x-persona1.pos_x)**2 + (persona2.pos_y-persona1.pos_y)**2)
        print(f"La distancia entre {persona1.nombre} y {persona2.nombre} es {round(calculo,2)} metro/s")
        if calculo==0:
            print(f"{persona1.nombre} y {persona2.nombre} estan en el mismo sitio, cruzan miradas, eso solo significa una cosa: COMBATE POKEMOOONN!!!! ")
            
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

def combate(persona1,persona2):
    if persona1.pos_x==persona2.pos_x and persona1.pos_y==persona2.pos_y:
        print("combate a muerte")
        
def riqueza_total_genero(lista_personas):
    m=0
    f=0
    for p in lista_personas:
        if p.genero== "M":
            m+=p.monedero 
        else:
            f+=p.monedero
    return m,f
    