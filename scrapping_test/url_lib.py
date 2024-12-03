from urllib.request import urlopen

response = urlopen('https://www.google.com')
print("response :::", response.read())
print("response :::", response)
