
zacatecni_bod = (15, 15)
koncovy_bod = (50, 50)
# nase_usecka = n_u
n_u = (zacatecni_bod[0], zacatecni_bod[1], koncovy_bod[0], koncovy_bod[1])
# polygon_usecka
# p_u = (20, 50, 45, 20)

objekty = [[(14, 46), (7.7, 77), (18.7, 89.4), (36.6, 80.3), (32.8, 54.9), (22.3, 59.9)], [(51.7, 52.0), (54.4, 22.8), (43.8, 7.9), (34.7, 10.2), (32.2, 17.4), (23.2, 11.1), (15.6, 17.4), (22.2, 42.3), (37.1, 27.2), (44.4, 30.4), (41.6, 37.4)]
, [(63.4, 45.1), (88.0, 54.9), (72.6, 20.6), (65.7, 27.7), (63.4, 45.1)], [(47.3, 81.2), (58.5, 77.4), (62.8, 86.3), (88.2, 86.3), (71.1, 60.5), (66.2, 75.2), (51.7, 68.8)]]


# n_u[0] = bodA.x
# n_u[1] = bodA.y
# n_u[2] = bodB.x
# n_u[3] = bodB.y
# p_u[0] = bodC.x
# p_u[1] = bodC.y
# p_u[2] = bodD.x
# p_u[3] = bodD.y


def vytvor_usecky(objekty):
    for polygon in objekty:
        p_u = []
        pruseciky = []
        posledni_souradnice = len(polygon) - 1
        for idx, point in enumerate(polygon):
            if idx == posledni_souradnice:
                p_u.append((point, polygon[0]))
            else:
                p_u.append((point, polygon[idx + 1]))
        najdi_prusecik(n_u, p_u)
        if najdi_prusecik(n_u, p_u) == True:
            return x, y
        else:
            p_u.pop(p_u)


def najdi_prusecik(n_u, p_u):
    pruseciky = []
    x_help1 = (n_u[3] - n_u[1]) * (p_u[2] - p_u[0]) * n_u[0] + (n_u[2] - n_u[0]) * (p_u[2] - p_u[0]) * (p_u[1] - n_u[1]) - (p_u[3] - p_u[1]) * (n_u[2] - n_u[0]) * p_u[0]
    x_help2 = (n_u[3] - n_u[1]) * (p_u[2] - p_u[0]) - (n_u[2] - n_u[0]) * (p_u[3] - p_u[1])
    x = x_help1 / x_help2
    y_help1 = x * (n_u[3] - n_u[1]) + n_u[1] * (n_u[2] - n_u[0]) - n_u[0] * (n_u[3] - n_u[1])
    y_help2 = (n_u[2] - n_u[0])
    y = y_help1 / y_help2
    if (n_u[0] <= x <= n_u[2]) or (p_u[0] <= x <= p_u[2]) and (n_u[1] <= y <= n_u[3]) or (p_u[1] <= y <= p_u[3]):
        print(x, y)
        pruseciky.append(x, y)


    # usecka = vytvor_usecky(objekty)
    # for usecka in usecky:
    #     pruseciky.append(najdi_prusecik(n_u, usecka))
vytvor_usecky(objekty)
