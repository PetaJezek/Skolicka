#!/bin/sh

echo "Sečteme byty následujících souborů:" logs/*.csv

cat *.txt | cut -d , -f 4 | paste -s -d + | bc
