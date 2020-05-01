
objekty = [[(14, 46), (7.7, 77), (18.7, 89.4), (36.6, 80.3), (32.8, 54.9), (22.3, 59.9)], [(51.7, 52.0), (54.4, 22.8), (43.8, 7.9), (34.7, 10.2), (32.2, 17.4), (23.2, 11.1), (15.6, 17.4), (22.2, 42.3), (37.1, 27.2), (44.4, 30.4), (41.6, 37.4)]
, [(63.4, 45.1), (88.0, 54.9), (72.6, 20.6), (65.7, 27.7), (63.4, 45.1)], [(47.3, 81.2), (58.5, 77.4), (62.8, 86.3), (88.2, 86.3), (71.1, 60.5), (66.2, 75.2), (51.7, 68.8)]]

pam = []
def spravna_datova_struktura(objekty):
    pam = []
    for polygon in objekty:
        for body in polygon:
            body = [body[0], body[1]]
            for souradnice in body:
                # souradnice = [body[0], body[1]]
                pam.append(souradnice)
    return pam


def zjisti_pocet_vrcholu(objekty):
    for polygon in objekty:
        for vrcholy in polygon:
            pocet_vrcholu = len(vrcholy) - 1
            if pocet_vrcholu > 3:
                continue
            else:
                if pocet_vrcholu == 2:
                    print("Pridej jeste jeden bod, jeden objekt je jen usecka.")
                    break
                if pocet_vrcholu == 1:
                    print("Objekt je jen jeden bod.")
                    break
