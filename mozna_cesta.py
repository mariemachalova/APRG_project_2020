import math
import konvexni_obalky


#funkce tvorici usecky z konvexnich obalu
def vytvor_usecky(polygon):
    p_u = []
    posledni_souradnice = len(polygon) - 1
    for idx, point in enumerate(polygon):
        if idx == posledni_souradnice:
            p_u.append((point, polygon[0]))
        else:
            p_u.append((point, polygon[idx + 1]))
    return p_u


# funkce hledajici prusecik usecek obalu a prime cesty mezi zacatecnim a koncovym bodem
def najdi_prusecik(n_u, p_u):
    if n_u[0] > n_u[2]:
        n_u = [n_u[2], n_u[3], n_u[0], n_u[1]]

    if p_u[0] > p_u[2]:
        p_u = [p_u[2], p_u[3], p_u[0], p_u[1]]

    x_help1 = (n_u[3] - n_u[1]) * (p_u[2] - p_u[0]) * n_u[0] + (n_u[2] - n_u[0]) * (p_u[2] - p_u[0]) * (p_u[1] - n_u[1]) - (p_u[3] - p_u[1]) * (n_u[2] - n_u[0]) * p_u[0]
    x_help2 = (n_u[3] - n_u[1]) * (p_u[2] - p_u[0]) - (n_u[2] - n_u[0]) * (p_u[3] - p_u[1])
    if x_help2 == 0:
        return
    x = x_help1 / x_help2
    y_help1 = x * (n_u[3] - n_u[1]) + n_u[1] * (n_u[2] - n_u[0]) - n_u[0] * (n_u[3] - n_u[1])
    y_help2 = (n_u[2] - n_u[0])

    if y_help2 == 0:
        return
    y = y_help1 / y_help2

    if ((n_u[0] <= x <= n_u[2]) and (p_u[0] <= x <= p_u[2])) or ((n_u[1] <= y <= n_u[3]) and (p_u[1] <= y <= p_u[3])):
        # print(x, y)
        return konvexni_obalky.Bod(x, y)


#prida body z jedne pulky konvexniho obalu do trasy
def pridej_body_polygonu_v_polorovine(polygon, n_u):
    c = - ((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
    gut_body = []
    obratit = False
    for idx, point in enumerate(polygon):

        # c = - ((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
        x = ((n_u[3] - n_u[1]) * point.x + (n_u[0] - n_u[2]) * point.y + c)
        if (c > 0) and (x > 0) or (c < 0) and (x < 0):
            gut_body.append(point)
            if idx == 0:
                obratit = True
        else:
            continue
    if obratit:
        gut_body.reverse()
    return gut_body

def najdi_trasu(zacatecni_bod, koncovy_bod, objekty):

    vysledne_body = [zacatecni_bod]

    n_u = (zacatecni_bod.x, zacatecni_bod.y, koncovy_bod.x, koncovy_bod.y)

    for polygon in objekty:
        pruseciky = []
        moje_usecky_v_polygonu = vytvor_usecky(polygon)
        for p_u in moje_usecky_v_polygonu:
            p_u = (p_u[0].x, p_u[0].y, p_u[1].x, p_u[1].y)
            prusecik = najdi_prusecik(n_u, p_u)

            if prusecik != None:
                pruseciky.append(prusecik)

        if len(pruseciky) == 1:
            vysledne_body.append(pruseciky[0])

        if len(pruseciky) == 2:
            predvysledne_body = []
            predvysledne_body.append(pruseciky[0])
            ty_spravne_body_polygonu = pridej_body_polygonu_v_polorovine(polygon, n_u)
            for bod_polygonu in ty_spravne_body_polygonu:
                predvysledne_body.append(bod_polygonu)
            predvysledne_body.append(pruseciky[1])
            vzdalenost_bodu_1 = math.sqrt((pruseciky[0].x - zacatecni_bod.x)**2 + (pruseciky[0].y - zacatecni_bod.y)**2)
            vzdalenost_bodu_2 = math.sqrt((pruseciky[1].x - zacatecni_bod.x)**2 + (pruseciky[1].y - zacatecni_bod.y)**2)
            if vzdalenost_bodu_2 < vzdalenost_bodu_1:
                predvysledne_body.reverse()
            vysledne_body += predvysledne_body

    vysledne_body.append(koncovy_bod)

    return vysledne_body
