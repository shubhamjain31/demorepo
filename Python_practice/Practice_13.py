import requests
url = input("Enter url :")
full_url = 'http://'+url
new_url = full_url.replace("www.", "")
page = requests.get(url)
print(page)