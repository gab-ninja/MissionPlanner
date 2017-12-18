import math


def functions():
    file = open('planet_data.txt', 'r')
    read = file.readline().split(';')
    planet_names =[]
    planet_radius = []
    planet_u = []
    while read[1] != 'end':
        planet_names.append(read[0])
        planet_radius.append(float(read[1]))
        planet_u.append(float(read[2]))
        read = file.readline().split(';')
    return planet_radius, planet_names, planet_u


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
    res[id] = p1
    if id == 0:
        res[1] = p1 + planet.radius
        res[2] = 2*math.pi*math.sqrt((res[1]**3)/planet.u)
        res[3] = math.sqrt(planet.u/res[1])
    elif id == 1:
        res[0] = res[1] - planet.radius
        res[2] = 2 * math.pi * math.sqrt((res[1] ** 3) / planet.u)
        res[3] = math.sqrt(planet.u / res[1])
    elif id == 2:
        res[1] = ((res[2] * math.sqrt(planet.u))/(2 * math.pi)) ** (2/3)
        res[0] = res[1] - planet.radius
        res[3] = math.sqrt(planet.u / res[1])
    elif id == 3:
        res[1] = planet.u / (res[3] ** 2)
        res[0] = res[1] - planet.radius
        res[2] = 2*math.pi*math.sqrt((res[1]**3)/planet.u)
    return res


# - Orbitas elípticas --------------------------------------------------------------------------------------------------
#
# 0-h.perigeu 1-r.perigeu 2-excentricidade 3-semi.eixo.maior 4-periodo 5-h.apgeu 6-r.apogeu 7-v.perigeu 8-v.apogeu
#
# Unidades SI [Km em vez de m]
#
# -> parametros de entrada: (planeta, id do parametro inserido 1, valor do parametro com id 1, id parametro2, valor do
# parametro com id 2)
# -> parâmetros de saída: (ans[0,1,2,3,4,5,6,7])
#-----------------------------------------------------------------------------------------------------------------------
def orbita_eliptica (planeta,id1,p1,id2,p2):
    planet = Planetas(planeta)
    res = [0,0,0,0,0,0,0,0,0]
    if (id1 == 0 and id2 == 1) or (id1 == 3 and id2 == 4) or  (id1 == 5 and id2 == 6):
        print('Erro: Inseridos dois valores dependentes')
    else:
        res[id1] = p1
        res[id2] = p2
        #determinação dos parametros dependentes
        if id1 == 0:
            res[1] = res[0] + planet.radius
        elif id1 == 1:
            res[0] = res[1] - planet.radius
        elif id1 == 3:
            res[4] = ((2 * math.pi)/ math.sqrt(planet.u)) * res[3] ** (3 / 2)
        elif id1 == 4:
            res[3] = ((res[4] * math.sqrt(planet.u)) / (2 * math.pi)) ** (2 / 3)
        elif id1 == 5:
            res[6] = res[5] + planet.radius
        elif id1 == 6:
            res[5] = res[6] - planet.radius

        if id2 == 3:
            res[4] = ((2 * math.pi)/ math.sqrt(planet.u)) * res[3] ** (3 / 2)
        elif id2 == 4:
            res[3] = ((res[4] * math.sqrt(planet.u)) / (2 * math.pi)) ** (2 / 3)
        elif id2 == 5:
            res[6] = res[5] + planet.radius
        elif id2 == 6:
            res[5] = res[6] - planet.radius

        #determinação de rp, e, a, ra. É suposto ter 2 destes parâmetros
        if res[2] != 0:
            if res[1] != 0: # e rp
                res[3] = res[1]/(1 - res[2])
                res[6] = res[1] * (1 + res[2])/(1 - res[2])
            elif res[3] != 0: # e a
                res[1] = res[3] * (1 - res[2])
                res[6] = res[3] * (1 + res[2])
            elif res[6] != 0: # e ra (n usei o else para prevenir erros)
                res[1] = res[6] * (1 - res[2])/(1 + res[2])
                res[3] = res[6]/(1 + res[2])
        else:
            if res[1] != 0:
                if res[3] != 0: # rp a
                    res[2] = 1 - res[1]/res[3]
                    res[6] = 2 * res[3] - res[1]
                else: # rp ra
                    res[2] = (res[6] - res[1])/(res[6] + res[1])
                    res[3] = (res[1] + res[6])/2
            else: # a ra
                res[1] = 2 * res[3] - res[6]
                res[2] = res[6]/res[3] - 1

        if res[0] == 0:
            res[0] = res[1] - planet.radius
        if res[5] == 0:
            res[5] = res[6] - planet.radius
        if res[4] == 0:
            res[4] = (2 * math.pi)/ math.sqrt(planet.u) * res[3] ** (3/2)

        res[7] = math.sqrt(2 * planet.u * (1/res[1] - 1/(2 * res[3])))
        res[8] = math.sqrt(2 * planet.u * (1 / res[6] - 1 / (2 * res[3])))

    return res


# - Tipo de Orbita Desconhecido ----------------------------------------------------------------------------------------
#
# Unidades SI [Km em vez de m]
#
# -> parametros de entrada: (astrocentral, r0, v0, gama0)
#
# -> parâmetros de saída: ([a, e])
#-----------------------------------------------------------------------------------------------------------------------
def orbita_desconhecida (planeta,r0,v0,gama0):
    planet = Planetas(planeta)
    a = r0 / (2 - (r0 * v0 ** 2)/planet.u)
    e = math.sqrt(((r0 * v0 ** 2)/planet.u -1) ** 2 * (math.cos(gama0) ** 2 + (math.sin(gama0)) ** 2))
    return [a,e]


# - Mudanças de Plano Orbital ------------------------------------------------------------------------------------------
#
# Unidades SI [Km em vez de m]
#
# -> parametros de entrada: (v, plane change angle)
#
# -> parâmetros de saída: (lta velocity)
#-----------------------------------------------------------------------------------------------------------------------
def plane_changes(v, angle):
    delta_v = 2 * v * math.sin(angle / 2)
    return delta_v


# - Parametros Planetas-------------------------------------------------------------------------------------------------
#
# 0-Earth 1-Moon 2-Sun 3-Mercury 4-Venus 5-Mars 6-Jupiter 7-Saturn 8-Uranus 9-Neptune 10-Pluto 11-Other
#
#-----------------------------------------------------------------------------------------------------------------------
class Planetas:

    def __init__(self, num):
        self.astro = num
        #planet_names = ['Earth', 'Moon', 'Sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune',
        #                'Pluto', 'Other']
        #self.name = planet_names[self.astro]
        #planet_radius = [6378.14, 1737.4, 696000, 2439.7, 6051.8, 3397, 71492, 60268, 25559, 24764, 1195, 0]
        #self.radius = planet_radius[self.astro]
        #planet_u = [398600.4, 4902.8, 132712439925.5, 22032.1, 324858.8, 42828.3, 126711995.4, 37939519.7, 578158.5,
        #            6871307.8, 1020.9, 0]
        #self.u = planet_u[self.astro]
        planet_radius, planet_names, planet_u = functions()
        self.name = planet_names[self.astro]
        self.radius = planet_radius[self.astro]
        self.u = planet_u[self.astro]


#print(orbita_circular(0,2,5400))
#print(['%.10f' % elem for elem in orbita_eliptica(0,0,593,5,39770)])
#print(orbita_desconhecida(0,6652.555468783185, 7.740599773454766, 0))
#print(orbita_desconhecida(0,46148.14, 1.5056796288, 0))


