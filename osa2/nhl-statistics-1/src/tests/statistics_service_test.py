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
        self.stats = StatisticsService(PlayerReaderStub())


    def test_loyda_pelaaja(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_ei_loytynyt_pelaajaa(self):
        player = self.stats.search("Error")
        self.assertIsNone(player)

    def test_joukkue_loytyi(self):
        joukkueen_pelaajat = self.stats.team("EDM")
        self.assertEqual(len(joukkueen_pelaajat), 3)

    def test_tehokkain_pelaaja(self):
        tehokkain = self.stats.top(1)
        self.assertEqual(tehokkain[0].name, "Gretzky")


    
