from argparse import ArgumentParser
from itertools import product

import diffy


def main():
    parser = ArgumentParser(
        description="Find diffy squares that produce long sequences.",
        prog="python -m diffy",
    )
    parser.add_argument("bound", type=int, help="Upper bound for initial values")
    args = parser.parse_args()

    high_score = 0
    for seq in product(range(1, args.bound + 1), repeat=4):
        diff = diffy.diffy(seq)
        if diff > high_score:
            high_score = diff
            high_scorers = set()
        if diff >= high_score:
            high_scorers.add(diffy._canon(seq))
    print(high_score)
    for scorer in sorted(high_scorers):
        print(scorer)


if __name__ == "__main__":
    main()
