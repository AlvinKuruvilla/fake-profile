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
import utility


preprocessed_data = f"/Users/rajeshkumar/PycharmProjects/fake-profile/data/fpd_new_session_no_nans.csv"
userful_cols = ['direction', 'key', 'time', 'platform_ids', 'user_ids', 'session_ids']
main_df = pd.read_csv(preprocessed_data, sep=",", header=0, index_col=None, quoting=csv.QUOTE_NONE, low_memory=False,
                      usecols=userful_cols)
# dtype={'direction': str, 'key':object, 'time':int, 'platform_ids':int, 'user_ids':int, 'session_ids':int}
### User 12 does not have platform3 data
# print(main_df.columns)
users = main_df['user_ids'].unique()
print(f'users: {users}')
platforms = main_df['platform_ids'].unique()
print(f'platforms: {platforms}')
# main_df['key'] = main_df['key'].astype(str)
keys = main_df['key'].unique()
print(f'keys: {keys}')
# keys = [item[1] for item in keys]  # gets the keys in string format but then some keys like tab has Key.tab and are captured as Key.tab
# print(f'keys: {keys}')
press = {}
release = {}
kht = {}
kit_pp = {}
kit_pr = {}
kit_rp = {}
kit_rr = {}
for user in users[:5]: # traversing through all the users
    for platform in platforms: # traversting through the platform
        for key in keys[:6]: # just running for first few keys to verify
            press_df = main_df[(main_df['user_ids'] == user) & (main_df['platform_ids'] == platform) & (key == main_df['key']) & (main_df['direction'] == 'P')]
            release_df = main_df[(main_df['user_ids'] == user) & (main_df['platform_ids'] == platform) & (key == main_df['key']) & (main_df['direction'] == 'R')]
            # print(f'press_df: {press_df.head()}')
            # print(f'press_df: {press_df.tail()}')
            # print(f'release_df: {release_df.head()}')
            # print(f'release_df: {release_df.tail()}')
            press_times = press_df['time'].tolist()
            release_times = release_df['time'].tolist()
            # print(f'press_times:{press_times}')
            # print(f'release_times:{release_times}')
            correct_timing_pairs, _, _ = utility.find_pairs(press_times, release_times)
            print(f'for user: {user}, platfrom: {platform}, letter: {key}, correct_timing_pairs: {correct_timing_pairs}') # dig in this further.
            khtimings = [pair[1]-pair[0] for pair in correct_timing_pairs] # release: pair[1], press: pair[0]
            kht[key] = khtimings
            print(f'number of ocurrences: {len(khtimings)}, kht:{kht[key]}')


# main_df.key = main_df.key.astype(str)
# users = main_df['user_ids'].unique()
# print(f'users:{users}')
# platforms = main_df['platform_ids'].unique()
# keys = main_df['key'].unique()
# print(keys)
# # users.sort()
# # # populating kht dict with blank list
# # press = {}
# # release = {}
# # kht = {}
# #
# # kit_pp = {}
# # kit_pr = {}
# # kit_rp = {}
# # kit_rr = {}
# # for key1 in keys:
# #     for key2 in keys:
# #         if (key1,key2) not in kht:
# #             kit_pp[(key1, key2)] = []
# #             kit_pr[(key1, key2)] = []
# #             kit_rp[(key1, key2)] = []
# #             kit_rr[(key1, key2)] = []
# #
# # for user in users:
# #     for platform in platforms:
# #         # Slicing the dataframe for the current user
# #         df = main_df[(main_df['user_ids'] == user) & (main_df['platform_ids'] == platform)]
# #         for key in keys[:6]:
# #             press_frames = df[(df['key'] == key) & (df['direction'] == 'P')]
# #             release_frames = df[(df['key'] == key) & (df['direction'] == 'R')]
# #             # print(press_frames.to_string())
# #             # print(release_frames.to_string())
# #             print(type(press_frames['time']))
# #             press[(user, platform, key)] = press_frames['time'].to_list()
# #             release[(user, platform, key)] = release_frames['time'].to_list()
# #         print(press)
# #         print(release)
#
#         # # just in case we dont have the press time for the first key, we will ignore the key
#         # if df['direction'][0] == 'P':
#         #     pos = 0
#         # else:
#         #     pos = 1
#         #
#         # window = 3
#         # slide = window
#         # for pos in range(pos, df.shape[0] - window - pos, slide):
#         #     df_window = df.iloc[pos:pos + window, :]
#         #     print(df_window.head())
#         #     event = df_window['direction'][0]
#         #     key = df_window['key'][0]
#         #
#         #     main_df[(main_df['direction'] == user) & (main_df['key'] == platform)]
#
#         # events = df['direction'].unique()
#         # unique_keys = df['key'].unique()
#         # for key in unique_keys:
#         #   df_keys = df[df['key']==key]
#         #   # print(df_keys.to_string())
#         #   press_df_keys = df_keys[df_keys['direction']=='P']
#         #   # print(press_df_keys.head())
#         #   release_df_keys = df_keys[df_keys['direction']=='R']
#         #   # print(release_df_keys.head())
#         #   # print(release_df_keys.index.to_list())
#         #   release_timings = release_df_keys['time'].values
#         #   press_timings= press_df_keys['time'].values
#         #   if len(release_timings) < len(press_timings):
#         #     useful = len(release_timings)
#         #   else:
#         #     useful = len(press_timings)
#
#         #   index_difference = np.array(release_df_keys.index.to_list()[:useful]) - np.array(press_df_keys.index.to_list()[:useful])
#         #   greater_than_one = [val for val in index_difference if val>1]
#         #   print(f'------greater_than_one:{greater_than_one}')
#
#         #   # kht[(user, platform, key)] = release_timings[:useful]-press_timings[:userful]
#         #   # print(kht)
#
#         #   # P1
#         #   # P2
#         #   # R1
#         #   # R2
#
#         #   # P
#         #   # R
#         #   # P
#         #   # R
#
#         #   # P
#         #   # R
#         #   # P
#
#         #   # P
#         #   # R
#         #   # R
#
#         #   # P
#         #   # P
#         #   # R
#
#
#
#
#
#
#
