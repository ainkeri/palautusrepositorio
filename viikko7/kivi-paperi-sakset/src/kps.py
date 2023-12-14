from tuomari import Tuomari

class KiviPaperiSakset:
    def __init__(self):
        self.ekan_siirto = None
        self.tokan_siirto = None

    def pelaa(self):
        tuomari = Tuomari()

        self.ekan_siirto = self._ensimmaisen_siirto()
        self.tokan_siirto = self._toisen_siirto(self.ekan_siirto)

        while self._onko_ok_siirto(self.ekan_siirto) and self._onko_ok_siirto(self.tokan_siirto):
            tuomari.kirjaa_siirto(self.ekan_siirto, self.tokan_siirto)
            print(tuomari)

            self.ekan_siirto = self._ensimmaisen_siirto()
            self.tokan_siirto = self._toisen_siirto(self.ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
