#!/usr/bin/python

import sys
import requests

def save_data(day):
    url = f"https://adventofcode.com/2022/day/{day}/input"
    response = requests.get(url).text

    with open(f"{day}.txt",'w',encoding = 'utf-8') as f:
        f.write(response)

if __name__ == "__main__":
    day = sys.argv[0]
    save_data(day)
