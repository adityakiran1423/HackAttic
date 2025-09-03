import json
import pprint
import requests

def main():
    url = "https://hackattic.com/challenges/the_redis_one/problem?access_token=xxx"
    response = requests.get(url)
    data = response.json()
    data = json.dumps(data, indent = 2)
    print(data)

if __name__ == "__main__":
    main()
