import os
import pandas as pd
import numpy as np


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
