zacatecni_bod = (17, 15)
koncovy_bod = (50, 75)
n_u = (zacatecni_bod[0], zacatecni_bod[1], koncovy_bod[0], koncovy_bod[1])

objekty = [[(14, 46), (7.7, 77), (18.7, 89.4), (36.6, 80.3), (32.8, 54.9), (22.3, 59.9)], [(51.7, 52.0), (54.4, 22.8), (43.8, 7.9), (34.7, 10.2), (32.2, 17.4), (23.2, 11.1), (15.6, 17.4), (22.2, 42.3), (37.1, 27.2), (44.4, 30.4), (41.6, 37.4)]
, [(63.4, 45.1), (88.0, 54.9), (72.6, 20.6), (65.7, 27.7), (63.4, 45.1)], [(47.3, 81.2), (58.5, 77.4), (62.8, 86.3), (88.2, 86.3), (71.1, 60.5), (66.2, 75.2), (51.7, 68.8)]]

c = - ((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
# print(c)

point = []
for polygon in objekty:
    # c = - ((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
    # pocet_objektu = len(objekty) - 1
    # gut_body = []
    for point in polygon:
        bodik = [point[0], point[1]]
        gut_body = []
        c = - ((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
        x = ((n_u[3] - n_u[1]) * bodik[0] + (n_u[0] - n_u[2]) * bodik[1] + c)
        if (c > 0) and (x > 0) or (c < 0) and (x < 0):
            gut_body.append(bodik)
        else:
            continue
        # print(gut_body)
        return gut_body

# def pridej_body_polygonu_v_polorovine(objekty, n_u):
#     c = - ((n_u[3] - n_u[1]) * n_u[0] + (n_u[0] - n_u[2]) * n_u[1])
#     print(c)
#     point = []
#     for polygon in objekty:
#         # posledni_souradnice = len(polygon) - 1
#         for idx, point in enumerate(polygon):
#             x = - ((n_u[3] - n_u[1]) * point[0] + (n_u[0] - n_u[2]) * point[1] (idx + 1)
#             if ((c > 0) and (x > 0) or (c < 0) and (x < 0)):
#                 point.append
#             else:
#                 continue
#     return point