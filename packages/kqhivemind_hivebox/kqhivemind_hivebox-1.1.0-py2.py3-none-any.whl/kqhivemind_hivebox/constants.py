POSITION_NAME = {
    1: 'Queen',
    2: 'Queen',
    3: 'Stripes',
    4: 'Stripes',
    5: 'Abs',
    6: 'Abs',
    7: 'Skulls',
    8: 'Skulls',
    9: 'Checks',
    10: 'Checks',
}

POSITION_BY_TEAM = {
    "gold": { POSITION_NAME[i].lower(): i for i in [1, 3, 5, 7, 9] },
    "blue": { POSITION_NAME[i].lower(): i for i in [2, 4, 6, 8, 10] },
}

PIN_ORDER = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 4,
    8: 4,
    9: 5,
    10: 5,
}

HOLD_TIME = 0.8
