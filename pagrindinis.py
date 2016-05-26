from klases import Vagonas, Lokomotyvas, Traukinys
import json
import sys
from operator import itemgetter
import doctest


def vagonuIrasymas(vag):
    """
        Metodas irašo esamų vagonų sąrašą
        į vagon.json failą
        Kūrimo metu tai buvo vagonai.json
        Tačiau naudojimo metu geriau atskirti
        Įrašymo ir nuskaitymo failus
    """
    with open('vagon.json', 'w')as f:
        f.write('[')
    for i in range(len(vag)):
        json_str = json.dumps(vag[i].__dict__)
        if i == (len(vag)-1):
            with open('vagon.json', 'a')as f:
                f.write(json_str)
                f.write(']')
        else:
            with open('vagon.json', 'a')as f:
                f.write(json_str)
                f.write(',\n')
    print("Vagonai įrašyti")


def lokomotyvuIrasymas(lok):
    """
        Metodas irašo esamus laisvus lokomotyvus
    """
    with open('lokomot.json', 'w')as f:
        f.write('[')
    for i in range(len(lok)):
        json_str = json.dumps(lok[i].__dict__)
        if i == (len(lok)-1):
            with open('lokomot.json', 'a')as f:
                f.write(json_str)
                f.write(']')
        else:
            with open('lokomot.json', 'a')as f:
                f.write(json_str)
                f.write(',\n')
    print("Lokomotyvai įrašyti")


def traukiniuIrasymas(trauk):
    """
        Metodas įrašo esamų lokomotyvų sąrašą
    """
    traukinioVagonai = []
    traukin = {}
    with open('traukiniai.json', 'w')as f:
        f.write('')
    for traukinys in trauk:
        try:
            for vagonas in traukinys.trvagonai:
                traukinioVagonai.append({"vagonas":
                                        {"vagonoMase": vagonas.vmase,
                                         "vezamoKrovinioMase": vagonas.vvezama,
                                         "id": vagonas.vnumeris}})
        except AttributeError:
            pass
        try:
            traukinioLokomotyvas = ({'lokomotyvoMase':
                                     traukinys.lokomotyvas.lmase,
                                     'maksimaliTempiamaMase':
                                     traukinys.lokomotyvas.lmaksimali}
                                    )
        except AttributeError:
            pass
        traukin['traukinys'] = ({'pavadinimas': traukinys.pav,
                                 'id': traukinys.id,
                                 'lokomotyvas': traukinioLokomotyvas,
                                 'vagonai': [i for vag in traukinioVagonai]})

        with open("traukiniai.json", 'a') as f:
            jsonString = json.dumps(traukin)
            f.write(jsonString)
            f.write('\n')
        traukin.clear()
        traukinioVagonai[:] = []
    print("Traukinys įrašytas")


def vagonuNuskaitymas(vag):
    """
        Metodas is failo vagonai.json
        nuskaito įrašytus vagonus ir
        prideda juos į vagonų sąrašą
    """
    with open('vagonai.json', 'r') as f:
        kiek = len(f.readlines())

    with open('vagonai.json', 'r') as f:
        v = json.loads(f.read())

    for i in range(kiek):
        vag.append(Vagonas(v[i]['vmase'], v[i]['vvezama'], v[i]['vmaksimali']))
    print("Vagonai nuskaityti")
    return vag


def lokomotyvuNuskaitymas(lok):
    """
        Metodas iš failo lokomoto.json
        nuskaito įrašytus vagonus ir
        prideda juos į vagonų sąrašą
    """
    with open('lokomoto.json', 'r') as f:
        kiek = len(f.readlines())

    with open('lokomoto.json', 'r') as f:
        v = json.loads(f.read())

    for i in range(kiek):
        lok.append(Lokomotyvas(v[i]['lmase'], v[i]['lmaksimali']))
    print("Lokomotyvai nuskaityti")
    return lok


def vagonuSarasas(vag):
    """
        Metodas atspausdina vagonų sąrašą
        Jei jis nėra tuščias
    """
    if len(vag) == 0:
        print("Nėra vagonų")
        return
    else:
        for i in range(len(vag)):
            print(vag[i].__dict__)


def lokomotyvuSarasas(lok):
    """
        Metodas atspausdina lokomotyvų sąrašą
        Jei jis nėra tuščias
    """
    if len(lok) == 0:
        print("Nėra lokomotyvų")
        return
    else:
        for i in range(len(lok)):
            print(lok[i].__dict__)


def traukiniuSarasas(trauk):
    """
        Metodas spausdins traukinių sąrašą
    """
    if len(trauk) == 0:
        print("Nėra traukinių")
    else:
        for i in range(len(trauk)):
            traukinys = trauk[i]
            traukinys.__str__()


def traukiniaiRusiuoti(trauk):
    """
       Metodas isrusiuoja ir atspausdina traukinius
    """
    if len(trauk) == 0:
        print("Nėra traukinių")
    else:
        trauk.sort(key=lambda x: x.pav, reverse=True)
        for i in range(len(trauk)):
            traukinys = trauk[i]
            traukinys.__str__()


def sukurtiVagona(vag):
    """
        Metodas skirtas sukurti vagona,
        Paima vagonu sarasa, prideda prie jo ir
        Gražina naują, papildytą vagonų sąrašą
    """
    print('Įveskite naujo Vagono masę: ')
    try:
        vmase = int(input())
    except ValueError:
        print("Vagono masė privalo būti skaičius")
        print("Naujo vagono sukurti nepavyko")
        return vag

    print('Įveskite naujo vagono vežamo krovinio masę: ')
    try:
        vvezama = int(input())
    except ValueError:
        print("Vagono vezamo krovinio masė privalo būti skaičius")
        print("Naujo vagono sukurti nepavyko")
        return vag

    print('Įveskite naujo vagono maksimalią krovinio masę: ')
    try:
        vmaksimali = int(input())
    except ValueError:
        print("Vagono maksimali važama masė privalo būti skaičius")
        print("Naujo vagono sukurti nepavyko")
        return vag

    if vmaksimali < vvezama:
        print("Vagono vežama masė negali būti didesnė už maksimalią")
        print("Vagonas nesukurtas")
        return vag

    vag.append(Vagonas(vmase, vvezama, vmaksimali))
    print("Naujas vagonas sukurtas")
    return vag


def sukurtiLokomotyva(lok):
    """
        Metodas skirtas sukurti lokomotyvą,
        Paima lokomotyvų sarasa, prideda prie jo ir
        Gražina naują, papildytą lokomotyvų sąrašą
    """
    print('Įveskite naujo lokomotyvo masę: ')
    try:
        lmase = int(input())
    except ValueError:
        print("Lokomotyvo masė privalo būti skaičius")
        print("Naujo lokomotyvo sukurti nepavyko")
        return lok

    print('Įveskite naujo lokomotyvo maksimalią tempiamą masę: ')
    try:
        lmaksimali = int(input())
    except ValueError:
        print("Lokomotyvo maksimali masė privalo būti skaičius")
        print("Naujo lokomotyvo sukurti nepavyko")
        return lok

    lok.append(Lokomotyvas(lmase, lmaksimali))
    print("Naujas Lokomotyvas sukurtas")
    return lok


def sukurtiTraukini(trauk, lok):
    """
        Metodas kuriantis traukini.
        Traukinių kūrimui reikalingi lokomotyvai
    """
    print("Įveskite traukinio pavadinimą")
    pav = input()

    if len(lok) == 0:
        print("Nėra lokomotyvų")
        print("Pirma pridėkite lokomotyvą")
        print("Traukinys nesukurtas")
        return trauk, lok
    else:
        print("Turimų lokomotyvų sąrašas:")
        for i in range(len(lok)):
            print(lok[i].__dict__)

    print("Kelintą lokomotyvą iš sąrašo priskirti traukiniui?")
    try:
        i = (int(input())-1)
    except ValueError:
        print("Turėjo būti skaičius")
        print("Traukinio sukurti nepavyko")
        return trauk, lok

    trauk.append(Traukinys(pav, lok[i]))
    del lok[i]
    print("Naujas traukinys sukurtas")
    return trauk, lok


def pridetiVagona(trauk, vag):
    """
        Metodas leidžiantis pridėti vagonus
        Prie traukinio
    """
    if len(trauk) == 0:
        print("Nėra traukinių")
        return trauk, vag
    elif len(vag) == 0:
        print("Nėra laisvų vagonų")
        return trauk, vag
    else:
        print("Esami traukiniai:")
        for i in range(len(trauk)):
            print(trauk[i].id, trauk[i].pav)
        print("Įveskite pasirinkto traukinio id")
        try:
            tid = (int(input()))
        except ValueError:
            print("Turėjo būti skaičius")
            print("Vagono pridėti nepavyko")
            return trauk, vag

        print("Turimi laisvi vagonai:")
        for i in range(len(vag)):
            print(vag[i].__dict__)
        print("Įveskite pasirinkto vagono numerį")
        try:
            vid = (int(input()))
        except ValueError:
            print("Turėjo būti skaičius")
            print("Vagono nepavyko pridėti")
            return trauk, vag

        for i in range(len(vag)):
            if vag[i].vnumeris == vid:
                kelintas = i

        for traukinys in trauk:
            if traukinys.id == tid:
                traukinys.__add__(vag[kelintas])
                print("Vagonas pridėtas sėkmingai")
                suma = traukinys.__len__()
                if suma > traukinys.lokomotyvas.lmaksimali:
                    print("Traukinys perkrautas, nepajudės iš vietos")
                    print("Ar atkabinti vagoną? (taip/ne)")
                    atkabinti = input()
                    if atkabinti == 'taip':
                        traukinys.__sub__(vid)
                        print("Vagonas atkabintas")
                        return trauk, vag
                    elif atkabinti == 'ne':
                        del vag[kelintas]
                        return trauk, vag
                    else:
                        print("Neteisinga komanda.")
                        print("Vagonas liko prikabintas")
                        del vag[kelintas]
                        return trauk, vag
                del vag[kelintas]
                return trauk, vag
            else:
                print("Nepavyko pridėti vagono")
                return trauk, vag


def meniu():
    """
        Spausdina galimu veiksmu sarasa
    """
    print("1 - Sukurti vagoną")
    print("2 - Įkelti vagonus iš failo")
    print("3 - Įrašyti vagonus į failą")
    print("4 - Spausdinti vagonų sąrašą")
    print("5 - Sukurti lokomotyvą")
    print("6 - Įkelti lokomotyvus iš failo")
    print("7 - Įrašyti lokomotyvus į failą")
    print("8 - Spausdinti lokomotyvų sąrašą")
    print("9 - Sukurti traukinį")
    print("10 - Spausdinti traukinius")
    print("11 - Pridėti vagoną prie traukinio")
    print("12 - Spausdinti išrūšiuotus traukinius")
    print("13 - Traukinių Įrašymas")
    print("meniu - spausdinti meniu")
    print("iki - išeiti iš programos")


if __name__ == "__main__":
    doctest.testmod()
    vag = []
    lok = []
    trauk = []
    meniu()
    while True:
        pasirinkimas = input()
        if pasirinkimas == '1':
            vag = sukurtiVagona(vag)
        elif pasirinkimas == '2':
            vag = vagonuNuskaitymas(vag)
        elif pasirinkimas == '3':
            vagonuIrasymas(vag)
        elif pasirinkimas == '4':
            vagonuSarasas(vag)
        elif pasirinkimas == '5':
            lok = sukurtiLokomotyva(lok)
        elif pasirinkimas == '6':
            lok = lokomotyvuNuskaitymas(lok)
        elif pasirinkimas == '7':
            lokomotyvuIrasymas(lok)
        elif pasirinkimas == '8':
            lokomotyvuSarasas(lok)
        elif pasirinkimas == '9':
            trauk, lok = sukurtiTraukini(trauk, lok)
        elif pasirinkimas == '10':
            traukiniuSarasas(trauk)
        elif pasirinkimas == '11':
            trauk, vag == pridetiVagona(trauk, vag)
        elif pasirinkimas == '12':
            traukiniaiRusiuoti(trauk)
        elif pasirinkimas == '13':
            traukiniuIrasymas(trauk)
        elif pasirinkimas == 'meniu':
            meniu()
        elif pasirinkimas == 'iki':
            sys.exit()
        else:
            print("Tokio pasirinkimo nėra")
            meniu()
