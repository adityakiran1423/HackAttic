import requests
import os

from dotenv import load_dotenv

load_dotenv()

def main():
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    CHALLENGE_NAME = os.getenv("CHALLENGE_NAME")
    payload = {"access_token" : ACCESS_TOKEN}
    
    try:
        challenge_url = f"https://hackattic.com/challenges/{CHALLENGE_NAME}/problem"
        d = requests.get(url= challenge_url, params = payload)
        print(d.content)
        # problem_json = d.json()

    except requests.exceptions.ConnectionError:
        print("HTTPSConnectionPool(host='hackattic.com', port=443): Max retries exceeded with url: /challenges/")

if __name__ == "__main__":
    main()