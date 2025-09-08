import requests
import os

from dotenv import load_dotenv

load_dotenv()

def main():
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    url = f"https://hackattic.com/challenges/reading_qr/problem?access_token={ACCESS_TOKEN}"
    

if __name__ == "__main__":
    main()
