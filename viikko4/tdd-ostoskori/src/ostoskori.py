from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self.ostokset)

    def hinta(self):
        loppu_hinta = sum(ostos.hinta() for ostos in self.ostokset)
        return loppu_hinta

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostokset:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                break
        else:
            ostos = Ostos(lisattava)
            self.ostokset.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostokset:
            if ostos.tuote == poistettava:
                self.ostokset.remove(ostos)

    def tyhjenna(self):
        self.ostokset.clear()

    def ostokset(self):
        return self.ostokset

    def tulosta_ostokset(self):
        for ostos in self.ostokset:
            print(f'Tuote: {ostos.tuote.nimi()}, Lukumäärä: {ostos.lukumaara()}')


ostoskori = Ostoskori()
tuote1 = Tuote("Maito", 2.5)
#tuote2 = Tuote("Juusto", 5.0)
tuote3 = Tuote("Maito", 2.5)

ostoskori.lisaa_tuote(tuote1)
#ostoskori.lisaa_tuote(tuote2)
ostoskori.lisaa_tuote(tuote3)

print(f'Tavaroita korissa: {ostoskori.tavaroita_korissa()}')
print(f'Kokonaishinta: {ostoskori.hinta()}')

ostoskori.tulosta_ostokset()