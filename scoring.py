def score_fundamental(main_diff, change_diff):
    score_main, score_diff = main_diff * 2, change_diff * 2
    if score_main < -8:
        score_main = -8
    elif score_main > 8:
        score_main = 8
    if score_diff < -2:
        score_diff = -2
    elif score_diff > 2:
        score_diff = 2
    return round(score_main + score_diff, 1)


def score_cot(base, quote):
    if base["long"] + quote["short"] - 100 > 0:
        return round((base["long"] + quote["short"] - 100) / 5, 1)
    elif quote["long"] + base["short"] - 100 > 0:
        return round((quote["long"] + base["short"] - 100) / -5, 1)
    else:
        return 0



def score_retail(long, short):
    if long - 50 > 0:
        return round((long - 50) * -2 / 10, 1)
    elif short - 50 > 0:
        return round((short - 50) * 2 / 10, 1)
    else:
        return 0