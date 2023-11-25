import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen_hinta(self):
        juusto = Tuote("Juusto", 4)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.hinta(), 4)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jälkeen_korin_hinta_sama_kun_tuotteiden_summa(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.hinta(), 7)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_kaksi_kertaa_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)

        ostos1 = self.kori.ostokset[0]
        ostos2 = self.kori.ostokset[1]  

        self.assertEqual(ostos1.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos2.tuotteen_nimi(), "Juusto")
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
    
        ostos = self.kori.ostokset[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(len(self.kori.ostokset), 2)