import itertools


class Vagonas():
    """
        Vagonas turi unikalų numerį, masę, vežamą krovinio masę ir
        maksimalią masę.
    """
    numerio_generatorius = itertools.count(100)

    def __init__(self, vmase, vvezama, vmaksimali):
        self.vmase = vmase
        self.vvezama = vvezama
        self.vmaksimali = vmaksimali
        self.vnumeris = next(self.numerio_generatorius)


class Lokomotyvas():
    """
        Lokomotyvas teturi savo masę ir
        maksimalią tempiamą masę
    """
    def __init__(self, lmase, lmaksimali):
        self.lmase = lmase
        self.lmaksimali = lmaksimali


class Traukinys():
    """
    Traukini sudaro lokomotyvas ir n vagonu
    Ar jis vaziuoja = lmaksimali - mase - mase ...
    """
    id_generatorius = itertools.count(10)

    def __init__(self, pav, lok):
        """
            Traukinys sukuriamas su pav, num, tuščiu vagonų sąrašu
        """

        self.lokomotyvas = lok
        self.trvagonai = []
        self.pav = pav
        self.id = next(self.id_generatorius)

    def __add__(self, vagonas):
        """
            Metodas vagonų pridėjimui į traukinį.
            Paduodamas objektas iš vagonų klasės.
        """
        self.trvagonai.append(vagonas)

    def __sub__(self, vid):
        """
            Metodas vagonų pašalinimui iš traukinio
        """
        for v in self.trvagonai:
            if v.vnumeris == vid:
                self.trvagonai.pop(self.trvagonai.index(v))

    def __str__(self):
        """
            Metodas skirtas spausdinti detalia informacija apie traukini,
            spausdinamas traukinio pavadinimas, priskirtas lokomotyvas
            ir visi priskirti vagonai
        """
        print("Traukinys: '"+self.pav+"'")
        print('Lokomotyvas:')
        print(' Mase: ', self.lokomotyvas.lmase)
        print(' Tempiama mase: ', self.lokomotyvas.lmaksimali)

        print('Vagonai:')

        if len(self.trvagonai) == 0:
            print('Traukinys neturi vagonų')
        for vagonas in self.trvagonai:
            print(' Vagono mase: ', vagonas.vmase)
            print(' Vagono vazamo krovinio mase: ', vagonas.vvezama)
            print(' Vagono numeris: ', vagonas.vnumeris)
            print('\n')

    def __len__(self):
        """
            Metodas skirtas apskaičiuoti realią tempiamą masę
        """
        suma = int(self.lokomotyvas.lmase)
        for vagon in self.trvagonai:
            suma += int(vagon.vmase)
            suma += int(vagon.vvezama)
        return suma
