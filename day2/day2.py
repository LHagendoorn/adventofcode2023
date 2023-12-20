import dataclasses
import re


@dataclasses.dataclass
class DrawCounts:
    red: int = 0
    green: int = 0
    blue: int = 0


@dataclasses.dataclass
class GameDescription:
    game_id: int
    draws: list[DrawCounts]

    def max_colour(self, colour):
        return max([d.__getattribute__(colour) for d in self.draws])


def parse_input():
    with open("./input.txt") as f:
        inputlines = f.readlines()

    games = []

    for line in inputlines:
        gamebit, draws = line.split(": ")
        _, game_id = gamebit.split(" ")
        parsed_draws = []
        for draw in draws.split("; "):
            drawcounts = DrawCounts()
            for d in draw.split(", "):
                match d.strip().split(" "):
                    case (x, "red"):
                        drawcounts.red = int(x)
                    case (x, "green"):
                        drawcounts.green = int(x)
                    case (x, "blue"):
                        drawcounts.blue = int(x)
            parsed_draws.append(drawcounts)
        games.append(GameDescription(game_id=int(game_id), draws=parsed_draws))

    return games


def solve_part_1(games):
    red_thresh = 12
    green_thresh = 13
    blue_thresh = 14

    real_games = 0
    for game in games:
        if (
                (game.max_colour("red") <= red_thresh) and
                (game.max_colour("green") <= green_thresh) and
                (game.max_colour("blue") <= blue_thresh)
        ):
            real_games += game.game_id
            print(game.game_id, "Is real!")
    print(real_games)


def solve_part_2(games):
    total_power = 0
    for game in games:
        total_power += game.max_colour("red") * game.max_colour("green") * game.max_colour("blue")
    print(total_power)

if __name__ == "__main__":
    t = parse_input()
    solve_part_2(t)
    print("done!")