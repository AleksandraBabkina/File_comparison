import os
import pandas as pd
import time

# Path to the folder with the files
# folder_path = r'For Sasha'
folder_path = os.path.dirname(__file__)

# Get a list of xlsx files in the folder
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Sort files by name (numbers)
# files.sort(key=lambda x: int(x.split('.')[0]))
files_4021 = os.path.join(folder_path, files[0])
files_4081 = os.path.join(folder_path, files[1])

df1 = pd.read_excel(files_4021)
print('First file read')
df2 = pd.read_excel(files_4081)
print('Second file read')

df1.index = df1.index + 2
df2.index = df2.index + 2

unique_in_df1 = df1[~df1.apply(tuple, 1).isin(df2.apply(tuple, 1))]
unique_in_df2 = df2[~df2.apply(tuple, 1).isin(df1.apply(tuple, 1))]

unique_in_df1 = unique_in_df1.drop_duplicates()
unique_in_df2 = unique_in_df2.drop_duplicates()

unique_in_df1['File'] = os.path.basename(files_4021)
unique_in_df2['File'] = os.path.basename(files_4081)

unique_in_df = pd.concat([unique_in_df1, unique_in_df2]).drop_duplicates(keep=False)

if unique_in_df.empty:
    print("NO CHANGED ROWS!!!")
    time.sleep(15)
else:
    unique_in_df.to_excel('Changed_Rows.xlsx', index=True)