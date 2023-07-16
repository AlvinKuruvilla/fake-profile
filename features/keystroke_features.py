from collections import defaultdict
def create_kht_data_from_df(df):
    kht_dict = defaultdict(list)
    for i, row in df.iterrows():
        kht_dict[row["key"]].append(row["release_time"] - row["press_time"])
    return kht_dict

def create_kit_data_from_df(df, kit_feature_type):
    kit_dict = defaultdict(list)
    if df.empty:
        print('dig deeper: dataframe is empty!')
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
