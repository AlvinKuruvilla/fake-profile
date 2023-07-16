# New Session Folder
# The name of the files in the output should be looked at later on ..
# Those files need to be fixed so we can use the data... those files contain EID, and 0/1 for P/R which does not make any sense!
# This needs more work to preprocess the New Session folder... some work is alredy done!
# Import pandas library
import pandas as pd
import os
import csv
from io import StringIO
# format of the dataframe
# cols: [userid, platformid, sessionid, 'key', 'event', timestamp]
# userid: [1, 2, 3, ..., N]
# platformid: [1, 2, 3], 1: Facebook, 2: Instagram, 3: Twitter
# sessionid: [1, 2], there were two sessions of data collection
# sampledata = {'userid':1, 'platformid':1, 'sessionid':1, 'key': 'h', 'event': 'P', 'timestamp':1653420520533530000}
child_problem= [356, 567]
user_id_dict = {'1':1, '11':2, '13':3, '17':4, '18':5, '19':6, '2':7, '22':8, '23':9, '24':10, '25':11, '26':12, '27':13, '28':14, '29':15, '31':16, '319':17, '32':18, '33':19, '34':20, '3456':21, '98':22, '4':23, '419':24, '5':25, '567':26, '356':27}
final_df = pd.DataFrame(columns=['direction', 'key', 'time', 'platform_ids', 'user_ids', 'session_ids'])
sess_path = f"/Users/rajeshkumar/PycharmProjects/fake-profile/data/new_session_data"
user_list = os.listdir(sess_path)
user_list.sort()
print('sorted list of users',user_list)
user_list = [item for item in user_list if len(item)<5] # excluding those with problems
# print('----------', platforms)

print('------------------------Data cleaning in progress-----------------')

rows = 0
cols = 0
for user_folder in user_list:
  session_list = os.listdir(os.path.join(sess_path, user_folder))
  session_list.sort()
  user_id = user_id_dict[user_folder]
  for session_file in session_list:
    # getting platform id from file name
    if session_file != ".ipynb_checkpoints":
      if "f_" in session_file:
        platform_id = 1
      elif 'i_' in session_file:
        platform_id = 2
      elif 't_' in session_file:
        platform_id = 3
      else:
        raise ValueError('Unknown session!')

      session_file_path = os.path.join(sess_path, user_folder, session_file)
      # print('current file: ', session_file_path)
      session_id = session_file_path[-5:-4] # getting the session id from the filename, safest!
      # fixing the format to make it readable by pandas
      text = open(session_file_path).read()
      text = text.replace("\"EID","EID") # clearning the header line
      text = text.replace("time\"\n\"","time\n") # clearning the header line
      text = text.replace(f'"EID,key,direction,time"\n"', "") # removing the first line
      text = text.replace('\n\",\"', "\n") # there was a patter "\n ","" after everyline which should just be \n
      text = text.replace("','", "comma")
      text = text.replace('","', "comma")
      # which is making it difficult for pandas to read because format had changed
      text = text.replace("\n,", "\n")
      text = text[:-2] # removing the last line which had only 1 character i.e. "
      # changing text to pandas dataframe
      # Convert String into StringIO
      csvStringIO = StringIO(text)
      try:
        temp_df = pd.read_csv(csvStringIO, sep=",", header=0, index_col=None, quoting=csv.QUOTE_NONE)
      except:
        print('session_file with error:',session_file_path)

      # check if the file has any header or not, if not add it.
      # this code may fail miserably if the column names dont match the expected values


      # create columns for the following so you can cancatenate to the temp_df and then to the final_df
      temp_df['platform_ids'] = platform_id # adding a column with default value
      temp_df['user_ids'] = user_id # adding a column with default value
      temp_df['session_ids']  = session_id # adding a column with default value
      # stack the two DataFrames
      temp_col_names = list(temp_df.columns)
      final_col_names = list(final_df.columns)

      should_concatenate = True
      if final_col_names != temp_col_names: # files need to be fixed manually
      # A quick fix is to rename the columns but it will overwrite on of the FIRST row.
        if len(temp_col_names) == len(final_col_names):
          temp_df.set_axis(final_col_names, axis=1, inplace=True)
        else:
          # temp_df.set_axis(final_col_names, axis=1, inplace=True)
          should_concatenate = False # you should not concatenate
          # This affect one folder t_22 so switch it on if that gets fixed, else just ignore it.
          print(f'file with different number of columns: {session_file_path}')
        # The above of course would not work if we have different number of columns
        # Which unfortunately is the case for some files.

      if should_concatenate:
        rows+= temp_df.shape[0]
        cols= temp_df.shape[1]
        final_df = pd.concat([final_df,  temp_df], ignore_index=True, axis=0)
      # print(f'final_df.shape: {final_df.shape} temp_df.shape: {temp_df.shape}')

# print(f'----original: ({rows},{cols})')
# print(f'----created: ({final_df.shape[0]},{final_df.shape[1]})')

outpath = f"/Users/rajeshkumar/PycharmProjects/fake-profile/data"
final_df = final_df.dropna() ## rows with NaNs because of the no values for KeyEvent and KeyPresses
final_df.to_csv(os.path.join(outpath,'fpd_new_session_no_nans2.csv'))
print('----------------Data cleaning done!-----------------------')

