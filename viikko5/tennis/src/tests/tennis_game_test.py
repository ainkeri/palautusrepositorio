import unittest

from tennis_game import TennisGame

test_cases = [
    (0, 0, "Love-All"),
    (1, 1, "Fifteen-All"),
    (2, 2, "Thirty-All"),
    (3, 3, "Deuce"),
    (4, 4, "Deuce"),

    (1, 0, "Fifteen-Love"),
    (0, 1, "Love-Fifteen"),
    (2, 0, "Thirty-Love"),
    (0, 2, "Love-Thirty"),
    (3, 0, "Forty-Love"),
    (0, 3, "Love-Forty"),
    (4, 0, "Win for Player 1"),
    (0, 4, "Win for Player 2"),

    (2, 1, "Thirty-Fifteen"),
    (1, 2, "Fifteen-Thirty"),
    (3, 1, "Forty-Fifteen"),
    (1, 3, "Fifteen-Forty"),
    (4, 1, "Win for Player 1"),
    (1, 4, "Win for Player 2"),

    (3, 2, "Forty-Thirty"),
    (2, 3, "Thirty-Forty"),
    (4, 2, "Win for Player 1"),
    (2, 4, "Win for Player 2"),

    (4, 3, "Advantage Player 1"),
    (3, 4, "Advantage Player 2"),
    (5, 4, "Advantage Player 1"),
    (4, 5, "Advantage Player 2"),
    (15, 14, "Advantage Player 1"),
    (14, 15, "Advantage Player 2"),

    (6, 4, "Win for Player 1"),
    (4, 6, "Win for Player 2"),
    (16, 14, "Win for Player 1"),
    (14, 16, "Win for Player 2"),
]


def play_game(p1_points, p2_points):
    game = TennisGame("Player 1", "Player 2")
    for i in range(max(p1_points, p2_points)):
        if i < p1_points:
            game.won_point("Player 1")
        if i < p2_points:
            game.won_point("Player 2")
    return game


class TestTennis(unittest.TestCase):
    def test_score(self):
        for test_case in test_cases:
            (p1_points, p2_points, score) = test_case
            game = play_game(p1_points, p2_points)
            self.assertEqual(score, game.get_score())
