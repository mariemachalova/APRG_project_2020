import json
import konvexni_obalky


def nacteni_mapy(pozice):
    soubor = open(pozice, encoding='utf-8')
    obsah = soubor.read()
    soubor.close()

    data = json.loads(obsah)
    zacatek = konvexni_obalky.Bod(data['path'][2]['start'][0], data['path'][2]['start'][1])
    konec = konvexni_obalky.Bod(data['path'][2]['end'][0], data['path'][2]['end'][1])
    return zacatek, konec


def read_input_file(soubor):
    soubor = open(soubor, encoding='utf-8')
    obsah = soubor.read()
    soubor.close()

    data = json.loads(obsah)

    nactene_objekty = []
    for json_object in data['object']:
        nacteny_objekt = []
        for bod in json_object['coordinates']:
            nacteny_objekt.append(bod)
        nactene_objekty.append(nacteny_objekt)

    return nactene_objekty