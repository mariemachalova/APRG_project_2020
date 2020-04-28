
zacatecni_bod = (15, 15)
koncovy_bod = (50, 50)
# nase_usecka = n_u
n_u = (zacatecni_bod[0], zacatecni_bod[1], koncovy_bod[0], koncovy_bod[1])
# polygon_usecka
# je potreba vyzkouset se vsemi useckami z konvexni obalky - objekt 1 nejnizsi x (seradit si x) dokud se nevrati ke start pointu - append a pop?
p_u = (20, 50, 45, 20)


def vytvor_usecky(polygony):
    for polygon in polygony:
        usecky = []
        posledni_souradnice = len(polygon)
        for point in polygon:
            if point == posledni_souradnice:
                # point[0].append ???
                usecky.append
            else
                point





# pod class?
def najdi_prusecik(n_u, p_u):
    x_help1 = (n_u[3] - n_u[1]) * (p_u[2] - p_u[0]) * n_u[0] + (n_u[2] - n_u[0]) * (p_u[2] - p_u[0]) * (p_u[1] - n_u[1]) - (p_u[3] - p_u[1]) * (n_u[2] - n_u[0]) * p_u[0]
    x_help2 = (n_u[3] - n_u[1]) * (p_u[2] - p_u[0]) - (n_u[2] - n_u[0]) * (p_u[3] - p_u[1])
    x = x_help1 / x_help2
    y_help1 = x * (n_u[3] - n_u[1]) + n_u[1] * (n_u[2] - n_u[0]) - n_u[0] * (n_u[3] - n_u[1])
    y_help2 = (n_u[2] - n_u[0])
    y = y_help1 / y_help2
    # print(x, y)
    if (n_u[0] <= x <= n_u[2]) or (p_u[0] <= x <= p_u[2]) and (n_u[1] <= y <= n_u[3]) or (p_u[1] <= y <= p_u[3]):
        print(x, y)
        return x, y

najdi_prusecik(n_u, p_u)
