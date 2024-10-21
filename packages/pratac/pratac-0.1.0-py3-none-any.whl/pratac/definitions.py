person_offset = {
    ("martin", "mato"): 0,
    ("adam", "trumtulus"): 1,
    ("dano", "danko"): 2,
    ("simona", "simi"): 3,
    ("all"): 4
}
room_offset = {
    0: "shower",
    1: "toilet",
    2: "floor",
    3: "kitchen",
}


def get_persons_offset(person_name: str) -> int:
    for key in person_offset:
        if person_name in key:
            return person_offset[key]
