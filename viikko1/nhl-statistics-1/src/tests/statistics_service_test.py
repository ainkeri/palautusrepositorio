import unittest
from statistics_service import StatisticsService, SortBy
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

    def test_konstruktori_luo_pelaajat(self):
        self.assertAlmostEqual(len(self.stats._players), 5)
    
    def test_pelaajan_haku_toimii(self):
        pelaaja = self.stats.search("Semenko")

        self.assertEqual(pelaaja.name, "Semenko")
    
    def test_pelaajan_haku_none(self):
        pelaaja = self.stats.search("Mksks")

        self.assertEqual(pelaaja, None)
    
    def test_list_of_players(self):
        joukkue = self.stats.team("EDM")

        pelaajat = ["Semenko", "Kurri", "Gretzky"]

        self.assertAlmostEqual([pelaaja.name for pelaaja in joukkue], pelaajat)
    
    def test_top_three_highest_points(self):
        top_three = self.stats.top(3)

        points = top_three[0]

        self.assertAlmostEqual(points.name, "Gretzky")
    
    def test_top_three_most_goals(self):
        top_three = self.stats.top(3, SortBy.GOALS)

        goals = top_three[0]

        self.assertAlmostEqual(goals.name, "Lemieux")
    
    def test_top_three_most_assists(self):
        top_three = self.stats.top(3, SortBy.ASSISTS)

        assists = top_three[0]

        self.assertAlmostEqual(assists.name, "Gretzky")
    
    
