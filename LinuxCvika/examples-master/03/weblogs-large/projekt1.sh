#!/bin/sh

echo "Podíváme se na následující soubory: " logs/*.csv

cat logs/*.csv | cut -d , -f 5 | sort | uniq -c | sort -nr | head -n 3
