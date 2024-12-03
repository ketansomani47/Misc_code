# import pandas as pd
#
# df = pd.read_csv('US_Heart_Patients.csv', index_col=0)
# # print(df)
# df.info()
# print(df.describe().T)
#
from jsonbender import K, S
from jsonbender.control_flow import Switch

b = Switch(S('service'),
           {'twitter': S('handle'),
            'mastodon': S('handle') + K('@') + S('server')},
           default=S('email'))

x = b({'service': 'twitter', 'handle': 'etandel'})  #  -> 'etandel'
print(x)
y = b({'service': 'mastodon', 'handle': 'etandel', 'server': 'mastodon.social'})  #  -> 'etandel@mastodon.social'
print(y)
# b({'service': 'facebook',
#    'email': 'email@whatever.com'})  #  -> 'emai
