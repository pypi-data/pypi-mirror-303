import argparse

from pratac.definitions import person_offset


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Cleaning schedule tool.')
        self.add_arguments()

    @staticmethod
    def valid_person(person: str) -> str:
        valid_people = ', '.join([f"{k}" for k in person_offset.keys()])
        value = person.lower()
        if value in valid_people:
            return value
        else:
            raise argparse.ArgumentTypeError(
                f"Invalid person: {person}.\nValid people are: {valid_people}")


    def add_arguments(self):
        self.parser.add_argument("person", type=self.valid_person, help="Person to generate schedule for.")
        self.parser.add_argument("week_offset", type=int, help="Week offset from current week.", nargs='?', default=0)
    def parse_args(self):
        return self.parser.parse_args()
