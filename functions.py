import math



# - Orbitas circulares -------------------------------------------------------------------------------------------------
#
# 0-altitude 1-raio 2-periodo 3-velocidade   Unidades SI [Km em vez de m]
#
# -> parametros de entrada: (planeta, id do parametro inserido, valor do parametro com determinado id)
# -> parâmetros de saída: (ans[altitude, raio, periodo, velocidade])
#-----------------------------------------------------------------------------------------------------------------------
def orbita_circular (planeta,id,p1):
    planet = Planetas(planeta)
    res = [None]*4
    if id == 0:
        res[0] = p1
        res[1] = p1 + planet.radius
        res[2] = 2*math.pi*math.sqrt((res[1]**3)/planet.u)
        res[3] = math.sqrt(planet.u/res[1])
    elif id == 1:
        res[1] = p1
        res[0] = res[1] - planet.radius
        res[2] = 2 * math.pi * math.sqrt((res[1] ** 3) / planet.u)
        res[3] = math.sqrt(planet.u / res[1])
    elif id == 2:
        res[2] = p1
        res[1] = ((res[2] * math.sqrt(planet.u))/(2 * math.pi)) ** (2/3)
        res[0] = res[1] - planet.radius
        res[3] = math.sqrt(planet.u / res[1])
    elif id == 3:
        res[3] = p1
        res[1] = planet.u / (res[3] ** 2)
        res[0] = res[1] - planet.radius
        res[2] = 2*math.pi*math.sqrt((res[1]**3)/planet.u)
    return res


# - Orbitas elípticas --------------------------------------------------------------------------------------------------
#
# 0-h.perigeu 1-r.perigeu 2-excentricidade 3-semi.eixo.maior 4-periodo 5-h.apgeu 6-r.apogeu 7-v.perogeu 8-v.apogeu
#
# Unidades SI [Km em vez de m]
#
# -> parametros de entrada: (planeta, id do parametro inserido 1, id parametro2, valor do parametro com id 1, valor do
# parametro com id 2)
# -> parâmetros de saída: (ans[0,1,2,3,4,5,6,7])
#-----------------------------------------------------------------------------------------------------------------------
def orbita_eliptica (planeta,id1,id2,p1,p2):
    planet = Planetas(planeta)
    res = [None]*8
    if (p1 == 1 and p2 == 2) or (p1 == 3 and p2 == 4) or  (p1 == 5 and p2 == 6):
        print('Erro: Inseridos dois valores dependentes')
    elif
        d

    return res



# - Parametros Planetas-------------------------------------------------------------------------------------------------
#
# 0-Earth 1-Moon 2-Sun 3-Mercury 4-Venus 5-Mars 6-Jupiter 7-Saturn 8-Uranus 9-Neptune 10-Pluto 11-Other
#
#-----------------------------------------------------------------------------------------------------------------------
class Planetas:

    def __init__(self, num):
        self.astro = num
        planet_names = ['Earth', 'Moon', 'Sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune',
                        'Pluto', 'Other']
        self.name = planet_names[self.astro]
        planet_radius = [6378.14, 1737.4, 696000, 2439.7, 6051.8, 3397, 71492, 60268, 25559, 24764, 1195, 0]
        self.radius = planet_radius[self.astro]
        planet_u = [398600.4, 4902.8, 132712439925.5, 22032.1, 324858.8, 42828.3, 126711995.4, 37939519.7, 578158.5,
                    6871307.8, 1020.9, 0]
        self.u = planet_u[self.astro]



print(orbita_circular(0,0,200))
print(orbita_circular(0,1,6578.14))
print(orbita_circular(0,2,5309.647275945052))
print(orbita_circular(0,3,7.784259565380226))