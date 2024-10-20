import requests

r = requests.get('https://github.com/', auth=('abyssian03', 'look4rewardnewcoder'))
if r.status_code == 200:
    print("OK")
