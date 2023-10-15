from collections import defaultdict


def create_kht_data_from_df(df):
    # Compute KHT as the difference between the press and release times for the instance of the key
    kht_dict = defaultdict(list)
    for i, row in df.iterrows():
        kht_dict[row["key"]].append(row["release_time"] - row["press_time"])
    return kht_dict


def create_kit_data_from_df(df, kit_feature_type):
    kit_dict = defaultdict(list)
    if df.empty:
        # print("dig deeper: dataframe is empty!")
        return kit_dict
    num_rows = len(df.index)
    for i in range(num_rows):
        if i < num_rows - 1:
            current_row = df.iloc[i]
            next_row = df.iloc[i + 1]
            key = current_row["key"] + next_row["key"]
            initial_press = float(current_row["press_time"])
            second_press = float(next_row["press_time"])
            initial_release = float(current_row["release_time"])
            second_release = float(next_row["release_time"])
            if kit_feature_type == 1:
                kit_dict[key].append(second_press - initial_release)
            elif kit_feature_type == 2:
                kit_dict[key].append(second_release - initial_release)
            elif kit_feature_type == 3:
                kit_dict[key].append(second_press - initial_press)
            elif kit_feature_type == 4:
                kit_dict[key].append(second_release - initial_press)
    return kit_dict


def word_hold(word_list, raw_df):
    wh = defaultdict(list)
    # The word_list needs to be in the same order as they would
    # sequentially appear in the dataframe
    raw_df["visited"] = False
    for word in word_list:
        first_letter = word[0]
        # print(first_letter)
        potential_release_matches = raw_df[
            (~raw_df["visited"]) & (raw_df["key"].str.strip("'") == first_letter)
        ]
        if len(potential_release_matches) > 0:
            first_row = potential_release_matches.iloc[0]
            first_row_index = first_row.name
            # print(first_row_index)
            # print(raw_df.loc[first_row_index])
            # input()
            # TODO: How to account for shift and other non-printing keys that could appear in between?
            # The ending bound is exclusive
            press_time = raw_df.loc[first_row_index]["press_time"]
            try:
                release_time = raw_df.loc[first_row_index + len(word) - 1][
                    "release_time"
                ]
                raw_df.loc[
                    first_row_index : first_row_index + len(word) - 1, "visited"
                ] = True
            except KeyError:
                release_time = raw_df.loc[first_row_index + len(word) - 2][
                    "release_time"
                ]
                raw_df.loc[
                    first_row_index : first_row_index + len(word) - 2, "visited"
                ] = True
            wh[word].append(release_time - press_time)
    return wh
