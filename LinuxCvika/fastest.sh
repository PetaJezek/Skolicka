#!/bin/sh
sort -n -t , -k 2 | head -n 1 | cut -d , -f 1
