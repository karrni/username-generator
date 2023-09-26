import random
from collections import Counter, defaultdict

TRANSITIONS = dict[
    str,  # the current string
    dict[
        str,  # possible next character
        int,  # weight of the character
    ],
]


class MarkovUsernameGenerator:
    """
    This class implements a Markov chain model to generate realistic usernames.
    """

    def __init__(
        self,
        transitions: TRANSITIONS | None = None,
        order: int = 3,
        padding_char: str = "~",
    ):
        if transitions is None:
            transitions = {}

        self.transitions = transitions
        self.order = order
        self.padding_char = padding_char

    def train(self, usernames: list[str]):
        """
        Trains the Markov model using the provided list of usernames.
        """

        transitions = defaultdict(Counter)

        for name in usernames:
            padded_name = self.padding_char * self.order + name

            # Go through the name character by character and create 'states'
            # that are 'order' characters long from each position. Then record
            # the next character for each state.
            #
            # For example the name 'foobar' would first be padded and then
            # yield the following states and next characters:
            #
            # ~~~foobar
            # ~~~       -> f
            #  ~~f      -> o
            #   ~fo     -> o
            #    foo    -> b
            #     oob   -> a
            #      oba  -> r
            for i in range(len(name)):
                state = padded_name[i : i + self.order]
                next_char = padded_name[i + self.order]

                # Increase the weight for the next character
                transitions[state][next_char] += 1

        self.transitions = dict(transitions)

    def generate(self, max_length: int = 8) -> str:
        """
        Generates a pronounceable username using the trained Markov model.
        """

        # Start with a padded string
        name = self.padding_char * self.order

        while True:
            # Get the current state, which is the last 'order' characters
            # of the generated name
            state = name[-self.order :]

            # Get the list of next possible characters or stop if there are none
            next_chars = self.transitions.get(state)
            if not next_chars:
                break

            # Split the next possible characters and their weights into lists
            # and choose a random next character based on their weights
            chars, weights = zip(*next_chars.items())
            name += random.choices(chars, weights=weights)[0]

            # Check if we have reached the maximum length
            if len(name) - self.order >= max_length:
                break

        # Return the generated username without the padding
        return name[self.order :]
