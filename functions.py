import math
import numpy as np

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
        #print('Erro: Inseridos dois valores dependentes')
        res[0] = -1
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


# - Orbitas parabólicas ------------------------------------------------------------------------------------------------
#
# 0-p.altitude 1-p.raio 2-semi-latus_rectum 3-p.velocidade   Unidades SI [Km em vez de m]
#
# -> parametros de entrada: (planeta, id do parametro inserido, valor do parametro com determinado id)
# -> parâmetros de saída: (ans[altitude_perigeu, raio_perigeu, p, velocidade_perigeu])
#-----------------------------------------------------------------------------------------------------------------------
def orbita_parabolica (planeta,id,p1):
    planet = Planetas(planeta)
    res = [None]*4
    res[id] = p1
    if id == 0:
        res[1] = p1 + planet.radius
        res[2] = 2 * res[1]
        res[3] = math.sqrt(2 * planet.u/res[1])
    elif id == 1:
        res[0] = res[1] - planet.radius
        res[2] = 2 * res[1]
        res[3] = math.sqrt(2 * planet.u / res[1])
    elif id == 2:
        res[1] = res[2] / 2
        res[0] = res[1] - planet.radius
        res[3] = math.sqrt(2 * planet.u / res[1])
    elif id == 3:
        res[1] = 2 * planet.u / (res[3] ** 2)
        res[0] = res[1] - planet.radius
        res[2] = 2 * res[1]
    return res


# - Orbitas hiperbólicas -----------------------------------------------------------------------------------------------
#
# 0-h.perigeu 1-r.perigeu 2-excentricidade 3-semi.eixo.maior 4-periodo 5-h.apgeu 6-r.apogeu 7-v.perigeu 8-v.apogeu
#
# Unidades SI [Km em vez de m]
#
# -> parametros de entrada: (planeta, id do parametro inserido 1, valor do parametro com id 1, id parametro2, valor do
# parametro com id 2)
# -> parâmetros de saída: (ans[0,1,2,3,4,5,6,7])
#-----------------------------------------------------------------------------------------------------------------------
def orbita_hiperbolica (planeta,id1,p1,id2,p2):
    hp = 0
    rp = 1
    e = 2
    a = 3
    b = 4
    v_p = 5
    v_inf = 6
    c3 = 7
    beta = 8

    planet = Planetas(planeta)

    res = [0,0,0,0,0,0,0,0,0]
    res_available = [0,0,0,0,0,0,0,0,0]

    res[id1] = p1
    res[id2] = p2

    res_available[id1] = 1
    res_available[id2] = 1

    if res_available[beta]:
        res[beta] = math.radians(res[beta])

    i = 0

    while (i < 15) and ( not (np.prod(res_available)) ):
        if not(res_available[hp]):
            if res_available[rp]:
                res[hp] = res[rp] - planet.radius
                res_available[hp] = 1

        if not (res_available[rp]):
            if res_available[hp]:
                res[rp] = res[hp] + planet.radius
                res_available[rp] = 1
            if res_available[e] and res_available[b]:
                res[rp] = res[b] * math.sqrt((res[e] - 1)/(res[e] + 1))
                res_available[rp] = 1
            if res_available[e] and res_available[a]:
                res[rp] = res[a] * (res[e] - 1)
                res_available[rp] = 1
            if res_available[b] and res_available[beta]:
                res[rp] = res[b] * math.tan(res[beta] / 2)
                res_available[rp] = 1
            if res_available[a] and res_available[b]:
                res[rp] = -res[a] + math.sqrt(res[a] ** 2 + res[b] ** 2)
                res_available[rp] = 1
            if res_available[b] and res_available[v_inf]:
                res[rp] = - (planet.u)/(res[v_inf] ** 2) + math.sqrt(((planet.u)/(res[v_inf] ** 2)) ** 2 + res[b] ** 2)
                res_available[rp] = 1

        if not (res_available[e]):
            if res_available[beta]:
                res[e] = 1/(math.cos(res[beta]))
                res_available[e] = 1
            if res_available[rp] and res_available[a]:
                res[e] = 1 + res[rp] / res[a]
                res_available[e] = 1
            if res_available[a] and res_available[b]:
                res[e] = math.sqrt(1 + (res[b] ** 2)/(res[a] ** 2))
                res_available[e] = 1

        if not (res_available[a]):
            if res_available[v_inf]:
                res[a] = planet.u / (res[v_inf] ** 2)
                res_available[a] = 1
            if res_available[e] and res_available[b]:
                res[a] = res[b] / math.sqrt(res[e] ** 2 - 1)
                res_available[a] = 1
            if res_available[rp] and res_available[e]:
                res[a] = res[rp] / (res[e] - 1)
                res_available[a] = 1
            if res_available[rp] and res_available[b]:
                res[a] = (res[b] ** 2 - res[rp] ** 2)/(2 * res[rp])
                res_available[a] = 1
            if res_available[rp] and res_available[v_p]:
                res_available[a] = 0

        if not (res_available[b]):
            if res_available[rp] and res_available[e]:
                res[b] = res[rp] * math.sqrt((res[e] + 1)/(res[e] - 1))
                res_available[b] = 1
            if res_available[e] and res_available[a]:
                res[b] = res[a] * math.sqrt(res[e] ** 2 - 1)
                res_available[b] = 1
            if res_available[rp] and res_available[v_inf]:
                res[b] = res[rp] * math.sqrt((2 * planet.u)/(res[rp] * res[v_inf] ** 2) + 1)
                res_available[b] = 1

        if not (res_available[v_p]):
            if res_available[rp] and res_available[v_inf]:
                res[v_p] = math.sqrt((2 * planet.u)/(res[rp]) + res[v_inf] ** 2)
                res_available[v_p] = 1
            if res_available[rp] and res_available[a]:
                res[v_p] = math.sqrt((2 * planet.u)/(res[rp]) + (planet.u)/(res[a]))
                res_available[v_p] = 1

        if not (res_available[v_inf]):
            if res_available[a]:
                res[v_inf] = math.sqrt(planet.u / res[a])
                res_available[v_inf] = 1
            if res_available[c3]:
                res[v_inf] = math.sqrt(res[c3])
                res_available[v_inf] = 1

        if not (res_available[c3]):
            if res_available[v_inf]:
                res[c3] = res[v_inf] ** 2
                res_available[c3] = 1

        if not (res_available[beta]):
            if res_available[e]:
                res[beta] = math.acos(1/res[e])
                res_available[beta] = 1
            if res_available[a] and res_available[b]:
                res[beta] = math.atan(res[b]/res[a])
                res_available[beta] = 1
            if res_available[rp] and res_available[b]:
                res[beta] = math.atan((2 * res[b] * res[rp])/(res[b] ** 2 - res[rp] ** 2))
                res_available[beta] = 1
            if res_available[b] and res_available[v_inf]:
                res[beta] = math.atan((res[b] * res[v_inf] ** 2)/(planet.u))
                res_available[beta] = 1

        i += 1

    if i == 15:
        res[0] = -1

    if res_available[beta]:
        res[beta] = math.degrees(res[beta])

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
    angle = angle * (2 * math.pi) / (360)
    delta_v = 2 * v * math.sin(angle / 2)
    return delta_v


# - Data Juliana / Gregoriana ------------------------------------------------------------------------------------------
#
# Unidades SI [Km em vez de m]
#
# -> parametros de entrada: (data disponível, elementos) em forma de dicionário
#
# -> parâmetros de saída: (dicionário completo)
#-----------------------------------------------------------------------------------------------------------------------
def julian_date(date):
    if date['input'] == 'gregorian':
        days = date['days']
        months = date['month']
        years = date['years']
        date['julian'] = 367 * years - 7 * ((years + (months + 9) / 12) / 4) + (275 * months) / 9 + days + 1721013.5


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


