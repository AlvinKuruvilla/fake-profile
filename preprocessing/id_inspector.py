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


def get_user_by_platform(user_id, platform_id, session_id=None):
    # print(f"user_id:{user_id}", end=" | ")
    df = read_compact_format()
    if session_id is None:
        if isinstance(platform_id, list):
            # Should only contain an inclusive range of the starting id and ending id
            assert len(platform_id) == 2
            return df[
                (df["user_ids"] == user_id)
                & (df["platform_id"].between(platform_id[0], platform_id[1]))
            ]

        return df[(df["user_ids"] == user_id) & (df["platform_id"] == platform_id)]
    if isinstance(session_id, list):
        # Should only contain an inclusive range of the starting id and ending id
        assert len(session_id) == 2
        return df[
            (df["user_ids"] == user_id)
            & (df["platform_id"] == platform_id)
            & (df["session_id"].between(session_id[0], session_id[1]))
        ]

    return df[
        (df["user_ids"] == user_id)
        & (df["platform_id"] == platform_id)
        & (df["session_id"] == session_id)
    ]


if __name__ == "__main__":
    fb_missing_ids = []
    insta_missing_ids = []
    twitter_missing_ids = []
    ids = [num for num in range(1, 26) if num != 22]
    for id in ids:
        df = get_user_by_platform(id, 1)
        df2 = get_user_by_platform(id, 2)
        df3 = get_user_by_platform(id, 3)
        if df.empty:
            fb_missing_ids.append(id)
        if df2.empty:
            insta_missing_ids.append(id)
        if df3.empty:
            twitter_missing_ids.append(id)
    print(fb_missing_ids)
    print(insta_missing_ids)
    print(twitter_missing_ids)
