""" Website Blocker Module
This script will block websites by redirecting blocked website to localhost.
Make a backup copy of your hosts file before running this script.
"""

import time
import sys
from datetime import datetime as dt

hosts_temp = "hosts"
redirect = "127.0.0.1"
hosts_path = "/etc/hosts"

# Adjusting hosts file path for windows based computers.
# Default value is for posix based systems.
if sys.platform.startswith("win"):
  hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"

# List of websites to block.
website_list = [
  "www.facebook.com",
  "facebook.com",
  "www.gmail.com",
  "gmail.com"
]

working_hours_start = 9
working_hours_end = 17
loop_interval_seconds = 5

while True:
    d = dt.now()
    if d.isoweekday() < 6 and d.hour >= working_hours_start and d.hour <= working_hours_end:
        print("Work time!")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Free time ....")

    time.sleep(loop_interval_seconds)

if __name__ == "__main__":
  print("Website blocker is active.")