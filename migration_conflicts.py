#!/usr/bin/env python
import os
import sys

known_overlaps = {}
all_prefixes = {}
# walks through the migrations folder and checks there are no files starting with the same number
for file in os.listdir("db/migrations"):
    prefix = file.split("_")[0]
    if prefix:
        if prefix in all_prefixes and prefix not in known_overlaps:
            print("A migration conflict was found for", prefix)
            sys.exit(1)
        all_prefixes[prefix] = True

print("No migration conflicts found.")
