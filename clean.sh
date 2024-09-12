#!/usr/bin/env bash

# FInd and delete all __pycache__ directories
result=$(find . -type d -name '__pycache__')

# Check if any __pycache__ directories were found
if [ -n "$result" ]; then
    # If directories are found, delete them
    echo "$result" | xargs rm -rf
    echo "All __pycache__ directories have been deleted."
else
    # If no directories are found, inform the user
    echo "No __pycache__ directory found."
fi
