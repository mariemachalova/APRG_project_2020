import mozna_cesta
import konvexni_obalky
import nacteni_dat1
import zobrazeni_dat


def main():
    objekty = nacteni_dat1.read_input_file('map_data_1.json')
    zacatecni_bod, koncovy_bod = nacteni_dat1.nacteni_mapy('test_path.json')

    konvexni_polygony = []
    puvodni_polygony = []
    for objekt in objekty:
        body_polygonu = []
        novy_polygon = []
        for bod in objekt:
            body_polygonu.append(konvexni_obalky.Bod(bod[0], bod[1]))
            novy_polygon.append(konvexni_obalky.Bod(bod[0], bod[1]))
        puvodni_polygony.append(novy_polygon)

        konvexni_polygon = konvexni_obalky.graham_scan(body_polygonu)

        konvexni_polygony.append(konvexni_polygon)

    vysledne_seskupeni = mozna_cesta.najdi_trasu(zacatecni_bod, koncovy_bod, konvexni_polygony)

    zobrazeni_dat.vykreslovani_objektu(puvodni_polygony, konvexni_polygony, vysledne_seskupeni, zacatecni_bod, koncovy_bod)


main()
