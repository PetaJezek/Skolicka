#!/usr/bin/env python3

import sys

DAY_NAMES = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

def main():
    try:
        idx = int(sys.argv[1])
        print(DAY_NAMES[idx])


if __name__ == "__main__":
    main()
