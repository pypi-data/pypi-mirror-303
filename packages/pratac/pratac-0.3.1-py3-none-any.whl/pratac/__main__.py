from argparse import Namespace
from datetime import datetime

from pratac.argparser import ArgParser
from pratac.definitions import get_persons_offset, person_offset, room_offset


def calculate_week_offset(offset: int) -> int:
    start_date = "2022-09-14"
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    current_datetime = datetime.now()
    week_offset = (((current_datetime - start_datetime).days) + (offset * 7)) // 7
    return week_offset

def process_args(args: Namespace) -> None:
    week_num = calculate_week_offset(args.week_offset)
    get_schedule(args.person, week_num)

def get_schedule(person: str, week_num: int) -> None:
    room_type = week_num % (len(room_offset))
    if person == "all":
        for key in person_offset:
            if key != "all":
                persons_offset = get_persons_offset(key[0])
                print(f"For week {week_num} the schedule for {key[0]} is: {room_offset.get((room_type + persons_offset) % len(room_offset))}")
        return
    persons_offset = get_persons_offset(person)
    print(f"For week {week_num} the schedule for {person} is: {room_offset.get((room_type + persons_offset) % len(room_offset))}") 

def main():
    args = ArgParser().parse_args()
    process_args(args)

if __name__ == "__main__":
    main()