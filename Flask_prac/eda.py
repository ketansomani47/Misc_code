# from sklearn import datasets
# import pandas as pd
# data = datasets.load_iris()
# df = pd.DataFrame(data.data,columns=data.feature_names)
# df['target'] = pd.Series(data.target)
# df.head()
# import pandas_profiling
# import pandas as pd
# df = pd.read_excel("C:\\Users\\ketansomani\\Downloads\\sample.xlsx")
# print(df)
# report = pandas_profiling.ProfileReport(df)
# # report.html
# # print(report.html)
# file = open("sample.html", "w", encoding='utf-8')
# file.write(report.html)
# file.close()

from numpy import array_split
x = array_split([1,2,3,4,5,6,7],2)
print(x)
print(type(x))
for i in x:
    print(i)
    print(type(i))
    print(i.any())
    y = [i]
    print(y)
    print(type(y))
