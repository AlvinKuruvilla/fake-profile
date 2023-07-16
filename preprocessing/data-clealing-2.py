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
users = main_df['user_ids'].unique()
platforms = main_df['platform_ids'].unique()
sessions = main_df['session_ids'].unique()
users.sort()

for user in users[:2]: # traversing through all the users
    for platform in platforms: # traversting through the platform
        for session in sessions:  # traversting through the platform
            cu_cp_df = main_df[(main_df['user_ids'] == user) & (main_df['platform_ids'] == platform) & (main_df['session_ids'] == session)]
            press_index = 0
            release_index = press_index+1
            direction = 1
            key = 2
            time = 3
            cu_cp_df = cu_cp_df.reset_index() # resetting indices
            print(cu_cp_df.iloc[:200].to_string())
            while release_index < cu_cp_df.shape[0]:
                release_row = cu_cp_df.iloc[release_index].tolist()
                press_row = cu_cp_df.iloc[press_index].tolist()
                if release_row[key] == press_row[key] and (release_row[direction]=='R' or release_row[direction]==''R''):
                    press_index = press_index+1
                    release_index = press_index
                    print('--------------------')
                    print(press_row)
                    print(release_row)
                    print(f'press_row: {press_index}')
                    print(f'release_row: {release_index}')
                else:
                    if release_row[key] == press_row[key]:
                        print(f'release_row[key] == press_row[key] failed and skipping {release_index}th row....')
                    if release_row[direction] == 'R':
                        print('release_row[direction]',type(release_row[direction][0]))
                        print(f'release_row[direction] == "R" failed and skipping {release_index}th row....')
                release_index=release_index+1
