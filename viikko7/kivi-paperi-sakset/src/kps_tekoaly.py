from tekoaly import Tekoaly
from kps import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        teko_alyn_siirto = self.tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {teko_alyn_siirto}")

        return teko_alyn_siirto
