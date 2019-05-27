import requests

token = 'token=2a354c0830c7149d56c02b3e99e29fe4a10ed096'
url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?'

res = requests.get(url, token)
data = res.json()