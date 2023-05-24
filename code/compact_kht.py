import pandas as pd
from collections import defaultdict
import statistics
import numpy as np

def get_kht():
    df = pd.read_csv("cleaned.csv")
    return df["release_time"]  - df["press_time"] 
def kht_dictionary(user_id):
    df = pd.read_csv("cleaned.csv")
    df = df.loc[df['user_ids'] == user_id]
    unique_keys = df["key"].unique()
    print(unique_keys)
    kht_dict = defaultdict(list)
    for i, row in df.iterrows():
        kht_dict[row["key"]].append(row["release_time"]  - row["press_time"])
    return kht_dict
def kit():
    df = pd.read_csv("cleaned.csv")
    flight1 = []
    flight2 = []
    flight3 = []
    flight4 = []
    for i, g in df.groupby(df.index // 2):
        if g.shape[0] == 1:
            continue
        initial_press = g.iloc[0]["press_time"]
        second_press = g.iloc[1]["press_time"]
        initial_release = g.iloc[0]["release_time"]

        second_release = g.iloc[1]["release_time"]

        flight1.append(float(second_press) - float(initial_release))
        flight2.append(float(second_release) - float(initial_release))
        flight3.append(float(second_press) - float(initial_press))
        flight4.append(float(second_release) - float(initial_press))
    print(len(flight1))
    print(sum(i < 0 for i in flight1))
    print(len(flight2))
    print(sum(i < 0 for i in flight2))
    print(len(flight3))
    print(sum(i < 0 for i in flight3))
    print(len(flight4))
    print(sum(i < 0 for i in flight4))

def find_max_feature_set_length(value_set):
    current_max_length = 0
    for feature_set in value_set:
        if len(feature_set) > current_max_length:
            current_max_length = len(feature_set)
        current_max_length +=1
    return current_max_length

def pad_feature_vector(fp_kht_feature_dict):
    value_set = list(fp_kht_feature_dict.values())
    max_feature_length = find_max_feature_set_length(value_set)
    print("Max length is:", max_feature_length)
    kht_keys = list(fp_kht_feature_dict.keys())
    for key in kht_keys:
        nested_value_list = fp_kht_feature_dict.get(key)
        if len(nested_value_list) < max_feature_length:
            nested_value_list += [0] * (max_feature_length - len(nested_value_list))
def kht_feature_df(kht_dict):
    kht_keys = kht_dict.keys()
    holder= defaultdict(list)
    for key in kht_keys:
        raw = list(kht_dict.get(key))
        if len(raw) ==1:
            holder[key+"mean"].append(raw[0])
            holder[key+"median"].append(raw[0])
            holder[key+"stdev"].append(raw[0])
            holder[key+"first_quartile"].append(raw[0])
            holder[key+"third_quartile"].append(raw[0])
        else:
            holder[key+"mean"].append(statistics.mean(raw))
            holder[key+"median"].append(statistics.median(raw))
            holder[key+"stdev"].append(statistics.stdev(raw))
            holder[key+"first_quartile"].append(np.quantile(raw, [0.25]))
            holder[key+"third_quartile"].append(np.quantile(raw, [0.75]))

    return pd.DataFrame(holder)
def kit_feature_df(kit_dict):
    kit_keys = kit_dict.keys()
    holder= defaultdict(list)
    for key in kit_keys:
        raw = list(kit_dict.get(key))
        if len(raw) ==1:
            holder[key+"mean"].append(raw[0])
            holder[key+"median"].append(raw[0])
            holder[key+"stdev"].append(raw[0])
            holder[key+"first_quartile"].append(raw[0])
            holder[key+"third_quartile"].append(raw[0])
        else:
            holder[key+"mean"].append(statistics.mean(raw))
            holder[key+"median"].append(statistics.median(raw))
            holder[key+"stdev"].append(statistics.stdev(raw))
            holder[key+"first_quartile"].append(np.quantile(raw, [0.25]))
            holder[key+"third_quartile"].append(np.quantile(raw, [0.75]))

    return pd.DataFrame(holder)

if __name__ == "__main__":
    raw = get_kht()
    raw = raw.to_frame()
    cleaned = raw[(raw != 0).all(1)]
    features = []
    print(cleaned)
    input()
    for i in range(1,28):
        kht = kht_dictionary(i)
        kht_features = kht_feature_df(kht)
        print(kht_features)
        features.append(kht_features)
    df = pd.concat(features)
    # count = (kht < 0).sum().sum()
    # print(count)
    print(df)
    # kit_features = kit_feature_df(kit())
    # print(kit_features)
