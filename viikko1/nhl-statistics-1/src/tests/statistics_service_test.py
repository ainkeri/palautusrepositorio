import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_return_correct_points(self):
        pelaaja = self.sort_by_points("Lemieux")

        self.assertAlmostEqual(pelaaja, 45+54)

    def test_konstruktori_luo_pelaajat(self):
        self.assertAlmostEqual(self.stats)
    
    def test_pelaajan_haku_toimii(self):
        pelaaja = self.stats.search("Semenko")

        self.assertAlmostEqual(pelaaja, "Semenko")
    
    def test_pelaajan_haku_none(self):
        pelaaja = self.stats.search("Mksks")

        self.assertAlmostEqual(pelaaja, None)
    
    def test_list_of_players(self):
        joukkue = self.stats.team("EDM")

        pelaajat = [Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)]

        self.assertAlmostEqual(joukkue, pelaajat)
    
    def test_top_players(self):
        pass


        
    
    
