import re
from pathlib import Path
import requests
import json
import time
import sys
import random
import subprocess
from colorama import init, Fore, Style
# Define the input and output file names
path = Path("/mnt/c/Users/RReaist12/Downloads")
input_file = path / 'hits.txt'
output_file = path / 'links.txt'

# Define the regex pattern to match the desired link format
pattern = r'discord\.gift/[^\s|]+'

# Read the content of the input file
with open(input_file, 'r') as file:
    content = file.read()

# Find all matching links
links = re.findall(pattern, content)

# Write the found links to the output file
with open(output_file, 'w') as file:
    for link in links:
        file.write(link + '\n')

print(f"Extracted {len(links)} links and saved them to {output_file}.")
file_path = output_file
def check_nitro_code(code, webhook_url, valid_file):
    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"

    response = requests.get(url)

    if response.status_code == 200:
        result = f"{Fore.GREEN}[VALID]{Style.RESET_ALL} {code}"
        send_webhook(webhook_url, result)
        valid_file.write(f"{code}\n")
        return True
    else:
        result = f"{Fore.RED}[INVALID]{Style.RESET_ALL} {code}"
        print(result)
        return False
def check_nitro_codes_from_file(file_path):
    with open(file_path, "r") as file:
        nitro_codes = file.read().splitlines()

    num_codes = len(nitro_codes)
    valid_codes = []

    webhook_url = input("Enter the Discord webhook URL: ")

    add_codes_input = input("Have you added your codes to the 'Nitro Codes.txt' file? (y/n): ")

    if add_codes_input.lower() == "y":
        print("Press Enter to perform the check...")
        input()
    elif add_codes_input.lower() == "n":
        print("Please add your codes to the 'Nitro Codes.txt' file and restart the program.")
        return
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return
    linxx = path / 'links.txt'
    with open(linxx, "w") as valid_file:
        for code in nitro_codes:
            if check_nitro_code(code, webhook_url, valid_file):
                valid_codes.append(code)

    valid_count = len(valid_codes)
    invalid_count = num_codes - valid_count

    print(f"Valid Codes: {valid_count}")
    print(f"Invalid Codes: {invalid_count}")
check_nitro_codes_from_file(file_path)
