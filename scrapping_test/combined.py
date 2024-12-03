# import pandas as pd
#
# df = pd.read_csv('test1.csv')
# print(df)
#
# df1 = pd.read_csv('capterra_data1.csv')

# import pandas as pd
# files = ['test1.csv', 'capterra_data1.csv']
# df = pd.DataFrame()
# for file in files:
#     data = pd.read_csv(file)
#     print(data)
#     data = data.dropna(axis=0, how="all")
#     print(data)
#     df = pd.concat([df, data], axis=0)
# # print(df)
# df = df.dropna(axis=1, how="all")
# df.to_csv('merged_files.csv', index=False)






import pandas as pd
# files = ['get_app_1.csv', 'get_app_2.csv', 'get_app_3.csv', 'get_app_4.csv', 'get_app_5.csv']
files = ['get_app_data.csv', 'featured_data.csv', 'merged_files.csv']
df = pd.DataFrame()
for file in files:
    data = pd.read_csv(file)
    # print(data)
    # data = data.dropna(axis=0, how="all")
    print(data)
    df = pd.concat([df, data], axis=0)
# print(df)
df = df.dropna(axis=1, how="all")
df.drop_duplicates(inplace=True)
df.to_csv('all_data.csv', index=False)
