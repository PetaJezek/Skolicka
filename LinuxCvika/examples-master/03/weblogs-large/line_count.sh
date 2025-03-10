#!/bin/sh

cat *.txt | uniq -c | paste -s -d | bc
