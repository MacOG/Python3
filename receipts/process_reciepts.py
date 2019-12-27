#!/usr/bin/env python3

import os
import glob
import shutil
import json

## Make sure the Processed Folder exist ##
try:
    os.mkdir('./processed')
except OSError:
    print("'./processed' directory already exists")

## Collect all receipts in the ./new Folder
receipts = glob.glob('./new/receipt-[0-9]*.json')


## Start the subtotal at $0.00
subtotal = 0.0

## Processes the receipts, moves them to the processed directory, and gives a subtotal of all receipts ##

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    receipt_name = path.split('/')[-1]
    destination = f"./processed/{receipt_name}"
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")

print("Python2: Receipt subtotal: $%.2f" % subtotal)
print(f"Python 3: Receipt subtotal: ${round(subtotal, 2)}")
