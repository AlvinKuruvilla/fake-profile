import math
from decimal import Decimal, ROUND_HALF_UP
from classifiers.template_generator import read_compact_format
from tabulate import tabulate


def force_round_up(value):
    return Decimal(value).to_integral_value(rounding=ROUND_HALF_UP)


def mean_samples_for_user(user_id):
    df = read_compact_format()
    # A "keystroke" is a press and release event together, so we want to divide
    # final answer by 2 because we get both press and release events
    return math.ceil(len(df[df["user_ids"] == user_id]) / 3) / 2


def mean_samples_for_platform(platform):
    df = read_compact_format()
    # A "keystroke" is a press and release event together, so we want to divide
    # final answer by 2 because we get both press and release events
    return math.ceil(len(df[df["platform_id"] == platform])) / 2


def mean_samples_per_session(session_id):
    df = read_compact_format()
    # A "keystroke" is a press and release event together, so we want to divide
    # final answer by 2 because we get both press and release events
    return math.ceil(len(df[df["session_id"] == session_id]) / 6) / 2


def keystrokes_per_platform():
    rows = []
    df = read_compact_format()
    ids = sorted(list(df["platform_id"].unique()))
    for _id in ids:
        # The decimal conversion here is to force round to the nearest integer
        rows.append([_id, force_round_up(mean_samples_for_platform(_id))])
    table = tabulate(
        rows,
        headers=["ID", "Mean Sample Count Across all Platforms"],
        tablefmt="plain",
    )
    print(table)


def keystrokes_per_user():
    rows = []
    df = read_compact_format()
    ids = sorted(list(df["user_ids"].unique()))
    for _id in ids:
        # The decimal conversion here is to force round to the nearest integer
        rows.append([_id, force_round_up(mean_samples_for_user(_id))])
    table = tabulate(
        rows,
        headers=["ID", "Mean Sample Count Across all Platforms"],
        tablefmt="plain",
    )
    print(table)


def keystrokes_per_session():
    rows = []
    # NOTE: There seems to be an extra session 7 that occurs for one user, since its only 52 raw samples (press+ released)
    # executive decision to just ignore it
    ids = [i for i in range(1, 7)]
    for _id in ids:
        # The decimal conversion here is to force round to the nearest integer
        rows.append([_id, force_round_up(mean_samples_per_session(_id))])
    table = tabulate(
        rows,
        headers=["ID", "Mean Sample Count Across all Sessions"],
        tablefmt="plain",
    )
    print(table)


if __name__ == "__main__":
    keystrokes_per_session()
