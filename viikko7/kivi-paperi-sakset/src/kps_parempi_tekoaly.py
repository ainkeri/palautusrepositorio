from tekoaly_parannettu import TekoalyParannettu
from kps import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.parempi_tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        parempi_tko_aly_siirto = self.parempi_tekoaly.anna_siirto()
        self.parempi_tekoaly.aseta_siirto(ensimmaisen_siirto)

        print(f"Tietokone valitsi: {parempi_tko_aly_siirto}")

        return parempi_tko_aly_siirto

