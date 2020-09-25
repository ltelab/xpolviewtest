#!/bin/bash
while true
do
git pull
python3 find_latest_quicklook.py
git add .
git commit -a --allow-empty-message -m ''
git push
sleep 30
done