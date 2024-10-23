#!/usr/bin/env python3

import readline
import requests
import urllib.parse
import os
import sys
from bs4 import BeautifulSoup
from frshodan import frshodan
def main():
    print("Shodan Search!\n--------------")

    if len(sys.argv) > 1:
        query = sys.argv[1]
        question = "n"
    else:
        question = input("Save output to a file (y/n): ")
        if question == "y":
            filename = input("Filename: ")
            if not os.path.isfile(filename):
                with open(filename, 'w') as file:
                    file.write('')
                print(f'File "{filename}" created.')
            else:
                print(f'File "{filename}" already exists, appending...')
        elif question == "n":
            print("Not Dumping...")
        else:
            print("Skipping...")
        query = input("Search Query: ")

    ip_list = frshodan(query,0)

    if isinstance(ip_list, list):
        for ip in ip_list:
            if question == "y":
                with open(filename, "a") as file:
                    file.write(ip + "\n")
            print(f"IP: {ip}")
    else:
        print(f"Failed to retrieve data. {ip_list}")
