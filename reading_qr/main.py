import requests
import os

from PIL import Image
from pyzbar.pyzbar import decode

from dotenv import load_dotenv

load_dotenv()

def main():
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    CHALLENGE_NAME = os.getenv("CHALLENGE_NAME")
    IMAGE_DOWNLOAD_PATH = os.getenv("IMAGE_DOWNLOAD_PATH")
    payload = {"access_token" : ACCESS_TOKEN}
    
    try:
        challenge_url = f"https://hackattic.com/challenges/{CHALLENGE_NAME}/problem"
        d = requests.get(url= challenge_url, params = payload)
        problem_json = d.json()
        image_url = problem_json.get('image_url')
        print(image_url)
        image = requests.get(image_url)
        print(image.status_code)

        if image.status_code == 200:
            with open(IMAGE_DOWNLOAD_PATH, "wb") as fp:
                fp.write(image.content)

        else:
            print("Error, status code not 200")

        data = decode(Image.open('image.jpg'))
        data = data[0].data
        string_data = data.decode("utf-8")

        response = {'code' : string_data}

        solution_url = f"https://hackattic.com/challenges/{CHALLENGE_NAME}/solve"
        r = requests.post(url=solution_url, params=payload, json = response)
        print(r.content)


    except requests.exceptions.ConnectionError:
        print("HTTPSConnectionPool(host='hackattic.com', port=443): Max retries exceeded with url: /challenges/reading_qr/problem?access_token=a36030441954f10d")
    

if __name__ == "__main__":
    main()
