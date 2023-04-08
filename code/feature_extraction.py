# user_df
# KHTdict = {}
# key, event, time
# 'h', 'P', 123
# 'h', 'R', 128
# 'o', 'P', 132
# 'o', 'R', 139
# 'h', 'P', 143
# 'h', 'R', 148
# 'o', 'P', 152
# 'o', 'R', 159
# for key in user_df:
#   if event == P:
#     press_time = time
#   if event == R:
#     release_time = time
#     new_kht = release_time-press_time
#     if key not in KHTdict:
#       KHTdict[key] = [new_kht]
#     else:
#       KHTdict[key].append(new_kht)

# # Output:
# KHTdict = {'h':[5, 7], 'o':[7, 7]}
# KITdict1 = [] # just use one of them now, maybe first P to the last R!!
# # see the literature to figure out which one people use
# # KITdict2
# # KITdict3
# # KITdict4
import pandas as pd
import numpy as np
import csv

preprocessed_data = f"/Users/rajeshkumar/PycharmProjects/fake-profile/data/fpd_new_session_no_nans.csv"
userful_cols = ['direction', 'key', 'time', 'platform_ids', 'user_ids', 'session_ids']
main_df = pd.read_csv(preprocessed_data, sep=",", header=0, index_col=None, quoting=csv.QUOTE_NONE, low_memory=False,
                      usecols=userful_cols)
### USer 12 does not have platform3 data
# print(main_df.columns)
users = main_df['user_ids'].unique()
platforms = main_df['platform_ids'].unique()
users.sort()
kht = {}
kit_pp = {}
kit_pr = {}
kit_rp = {}
kit_rr = {}
for user in users:
    for platform in platforms:
        # Slicing the dataframe for the current user
        df = main_df[(main_df['user_ids'] == user) & (main_df['platform_ids'] == platform)]
        if df['direction'][0] == 'P':
            pos = 0
        else:
            pos = 1
        window = 4
        slide = window//2
        for pos in range(pos, df.shape[0] - window - pos, slide):
            df_window = df.iloc[pos:pos + window, :]
            print(df_window.head())

        # events = df['direction'].unique()
        # unique_keys = df['key'].unique()
        # for key in unique_keys:
        #   df_keys = df[df['key']==key]
        #   # print(df_keys.to_string())
        #   press_df_keys = df_keys[df_keys['direction']=='P']
        #   # print(press_df_keys.head())
        #   release_df_keys = df_keys[df_keys['direction']=='R']
        #   # print(release_df_keys.head())
        #   # print(release_df_keys.index.to_list())
        #   release_timings = release_df_keys['time'].values
        #   press_timings= press_df_keys['time'].values
        #   if len(release_timings) < len(press_timings):
        #     useful = len(release_timings)
        #   else:
        #     useful = len(press_timings)

        #   index_difference = np.array(release_df_keys.index.to_list()[:useful]) - np.array(press_df_keys.index.to_list()[:useful])
        #   greater_than_one = [val for val in index_difference if val>1]
        #   print(f'------greater_than_one:{greater_than_one}')

        #   # kht[(user, platform, key)] = release_timings[:useful]-press_timings[:userful]
        #   # print(kht)

        #   # P1
        #   # P2
        #   # R1
        #   # R2

        #   # P
        #   # R
        #   # P
        #   # R

        #   # P
        #   # R
        #   # P

        #   # P
        #   # R
        #   # R

        #   # P
        #   # P
        #   # R







