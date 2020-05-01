zacatek = ()
konec = ()
prekazky = ()

def nacteni_mapy(pozice):
    with open('map_data_1.json') as soubor:
        import json
        nacteny_soubor = json.loads(soubor)
        zacatek = nacteny_soubor['path']['start']
        konec = nacteny_soubor['path']['end']
    return zacatek, konec

def read_input_file(soubor):
    pocatecni_bod = []
    with open(soubor, 'map_data_0.json') as soubor:
        pocatecni_bod.append((prekazky(x)), prekazky(y))
            vysledne_objekty = ()
            obsah_souboru = soubor.read()
                for objekt in nacteny_soubor
                    vysledne_objekty.append(objekt['coordinates'])
return vysledne_objekty

print('Cílová pozice')
print(konec)