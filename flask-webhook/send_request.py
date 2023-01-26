import requests

# Let's call the webhook from here
url = 'http://127.0.0.1:5000/webhookcallback'

response = requests.post(url)

print(response)
print(response.text)