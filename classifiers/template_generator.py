import os
import json
import pandas as pd
import numpy as np


class Genders:
    @staticmethod
    def ALL():
        return "all"

    @staticmethod
    def MALE():
        return "male"

    @staticmethod
    def FEMALE():
        return "female"

    @staticmethod
    def OTHER():
        return "other"


def read_compact_format():
    df = pd.read_csv(
        os.path.join(os.getcwd(), "cleaned2.csv"),
        dtype={
            "key": str,
            "press_time": np.float64,
            "release_time": np.float64,
            "platform_id": np.uint8,
            "session_id": np.uint8,
            "user_ids": np.uint8,
        },
    )
    # print(df.head())
    return df


def all_ids():
    with open(os.path.join(os.getcwd(), "classifier_config.json"), "r") as f:
        config = json.load(f)
    gender_type = str(config["gender"])
    if gender_type.lower() == Genders.ALL().lower():
        return [num for num in range(1, 26) if num != 22]
    elif gender_type.lower() == Genders.MALE().lower():
        return [9, 12, 14, 15, 16, 17, 18, 20, 21, 26, 27]
    elif gender_type.lower() == Genders.FEMALE().lower():
        return [1, 3, 4, 5, 6, 8, 10, 11, 13, 19, 22, 23, 24]
    elif gender_type.lower() == Genders.OTHER().lower():
        return [2, 7, 25]
    else:
        raise ValueError(f"Unknown gender type {gender_type}")
