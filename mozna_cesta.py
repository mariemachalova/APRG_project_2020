
zacatecni_bod = (17, 15)
koncovy_bod = (50, 75)
# nase_usecka = n_u
n_u = (zacatecni_bod[0], zacatecni_bod[1], koncovy_bod[0], koncovy_bod[1])
# polygon_usecka
# p_u = (20, 50, 45, 20)

objekty = [[(14, 46), (7.7, 77), (18.7, 89.4), (36.6, 80.3), (32.8, 54.9), (22.3, 59.9)], [(51.7, 52.0), (54.4, 22.8), (43.8, 7.9), (34.7, 10.2), (32.2, 17.4), (23.2, 11.1), (15.6, 17.4), (22.2, 42.3), (37.1, 27.2), (44.4, 30.4), (41.6, 37.4)]
, [(63.4, 45.1), (88.0, 54.9), (72.6, 20.6), (65.7, 27.7), (63.4, 45.1)], [(47.3, 81.2), (58.5, 77.4), (62.8, 86.3), (88.2, 86.3), (71.1, 60.5), (66.2, 75.2), (51.7, 68.8)]]

# c = -((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
# print(c)

# n_u[0] = bodA.x
# n_u[1] = bodA.y
# n_u[2] = bodB.x
# n_u[3] = bodB.y
# p_u[0] = bodC.x
# p_u[1] = bodC.y
# p_u[2] = bodD.x
# p_u[3] = bodD.y


def vytvor_usecky(polygon):
    p_u = []
    posledni_souradnice = len(polygon) - 1
    for idx, point in enumerate(polygon):
        if idx == posledni_souradnice:
            p_u.append((point, polygon[0]))
        else:
            p_u.append((point, polygon[idx + 1]))
    return p_u

        # muj_prusecik = najdi_prusecik(n_u, p_u)
        # if muj_prusecik == True:
        #     return muj_prusecik


def najdi_prusecik(n_u, p_u):
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
        return (x, y)



def pridej_body_polygonu_v_polorovine(polygon, n_u):
    c = - ((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
    gut_body = []
    for point in polygon:
        bodik = [point[0], point[1]]
        c = - ((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
        x = ((n_u[3] - n_u[1]) * bodik[0] + (n_u[0] - n_u[2]) * bodik[1] + c)
        if (c > 0) and (x > 0) or (c < 0) and (x < 0):
            gut_body.append(bodik)
        else:
            continue
    return gut_body

pruseciky = []
    # print(pruseciky)
vysledne_body = []
for polygon in objekty:

    moje_usecky_v_polygonu = vytvor_usecky(polygon)



    for p_u in moje_usecky_v_polygonu:
        p_u = (p_u[0][0], p_u[0][1], p_u[1][0], p_u[1][1])
        prusecik = najdi_prusecik(n_u, p_u)
        if prusecik != None:
            pruseciky.append(najdi_prusecik(n_u, p_u))

    if len(pruseciky) > 0:
        ty_spravne_body_polygonu = pridej_body_polygonu_v_polorovine(polygon, n_u)
        vysledne_body.append([pruseciky, ty_spravne_body_polygonu])

# print(pruseciky)
print(vysledne_body)

# def pridej_body_polygonu_v_polorovine(objekty, polygon):
#     c = - ((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
#     for polygon in objekty:
#         gut_body = []
#         print(gut_body)
#         for point in polygon:
#             bodik = [point[0], point[1]]
#             gut_body = []
#             c = - ((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
#             x = ((n_u[3] - n_u[1]) * bodik[0] + (n_u[0] - n_u[2]) * bodik[1] + c)
#             if (c > 0) and (x > 0) or (c < 0) and (x < 0):
#                 gut_body.append(bodik)
#             else:
#                 continue
#         return gut_body

moje_hrkhrk = vytvor_usecky(polygon)
# print(moje_hrkhrk)
pruseciky = []
# for p_u in moje_hrkhrk:
#     p_u = (p_u[0][0], p_u[0][1], p_u[1][0], p_u[1][1])
#     najdi_prusecik(n_u, p_u)
#     pruseciky.append(najdi_prusecik(n_u, p_u))
#
# print(pruseciky)