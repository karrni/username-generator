import argparse
import bz2
import json
from pathlib import Path

from usergen.markov import MarkovUsernameGenerator

LOCATION = Path(__file__).parent.resolve()
TRANSITIONS_FILE = LOCATION / "transitions.json.bz2"


def main():
    parser = argparse.ArgumentParser(description="Generate usernames using a pre-trained Markov model")
    parser.add_argument("-n", "--num", type=int, default=1, help="Number of usernames to generate")
    parser.add_argument("-l", "--length", type=int, default=8, help="Maximum length of username")

    args = parser.parse_args()

    # Load the transitions from the archive
    with bz2.open(TRANSITIONS_FILE, "r") as fp:
        transitions = json.load(fp)

    generator = MarkovUsernameGenerator(transitions)

    for _ in range(args.num):
        print(generator.generate(max_length=args.length))


if __name__ == "__main__":
    main()
