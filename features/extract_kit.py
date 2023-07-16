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

### USer 12 does not have platform3 data
# print(main_df.columns)
users = main_df['user_ids'].unique()
platforms = main_df['platform_ids'].unique()
users.sort()
kit_pp = {}
kit_pr = {}
kit_rp = {}
kit_rr = {}
for user in users[:5]: # traversing through all the users
    for platform in platforms: # traversting through the platform
        press_df = main_df[(main_df['user_ids'] == user) & (main_df['platform_ids'] == platform) & (main_df['direction'] == 'P')]
        release_df = main_df[(main_df['user_ids'] == user) & (main_df['platform_ids'] == platform) & (main_df['direction'] == 'R')]
        print(f'press_df---------{press_df}')
        print(f'release_df---------{release_df}')



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

# for user in users:
#     for platform in platforms:
#         # Slicing the dataframe for the current user
#         df = main_df[(main_df['user_ids'] == user) & (main_df['platform_ids'] == platform)]
#         if df['direction'][0] == 'P':
#             pos = 0
#         else:
#             pos = 1
#         window = 4
#         slide = window//2
#         for pos in range(pos, df.shape[0] - window - pos, slide):
#             df_window = df.iloc[pos:pos + window, :]
#             print(df_window.head())

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
