#!/usr/bin/env python3

from datetime import datetime
import time

def main():
 	current_datetime = datetime.now()
 	print(current_datetime)

while True:
    time.sleep(5)
    main()
