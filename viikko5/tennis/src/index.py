from tennis_game import TennisGame


def main():
    game = TennisGame("Player 1", "Player 2")

    print(game.get_score())

    game.won_point("Player 1")
    print(game.get_score())

    game.won_point("Player 1")
    print(game.get_score())

    game.won_point("Player 2")
    print(game.get_score())

    game.won_point("Player 1")
    print(game.get_score())

    game.won_point("Player 1")
    print(game.get_score())


if __name__ == "__main__":
    main()
