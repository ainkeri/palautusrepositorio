from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli(tyyppi):
    if tyyppi == 'a':
        kaksinpeli = KPSPelaajaVsPelaaja()
        kaksinpeli.pelaa()
    if tyyppi == 'b':
        yksinpeli = KPSTekoaly()
        yksinpeli.pelaa()
    if tyyppi == 'c':
        haastava_yksinpeli = KPSParempiTekoaly()
        haastava_yksinpeli.pelaa()

    return None