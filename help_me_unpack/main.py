import base64
import struct
import requests

def main():
    # url = "https://hackattic.com/challenges/help_me_unpack/problem?access_token=xxx"
    # response = requests.get(url)
    # problem_json = response.json()
    # problem_data = problem_json["bytes"]
    # print(f"the encoded data is {problem_data}")

    base64string = "H3pwi9KLQf3SsgAAsTocRO7DtWdOXmZAQGZeTme1w+4="
    t=base64string.encode("ascii")
    decoded = base64.decodebytes(t)

    print(f"{decoded}\n")
    print(f'"int" : {int.from_bytes(decoded[:4], byteorder='little', signed=True)},')
    print(f'"uint" : {int.from_bytes(decoded[4:8], byteorder='little', signed=False)},')
    print(f'"short" : {int.from_bytes(decoded[8:10], byteorder='little', signed=True)},')
    print(f'"float" : {struct.unpack('<f', decoded[12:16])[0]},')
    print(f'"double" : {struct.unpack('d', decoded[16:24])[0]},')
    print(f'"big_endian_double" : {struct.unpack('!d', decoded[24:32])[0]}')


if __name__=="__main__":
    main()
