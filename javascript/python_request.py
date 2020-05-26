import requests

res = requests.get('https://')
data = res.json()
post_content = data[0].get('content')
print(post_content)