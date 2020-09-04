#!/bin/bash

git pull
cp /users/radarop/test_epfl_2020/quicklooks/2020-08-28/XPOL-20200828-201554_az161_Zdr.png /users/radarop/xpolviewtest/latest.png
cp /users/radarop/lteradar1/webcam/20200904-124602.png /users/radarop/xpolviewtest/latest_webcam.png
git add .
git commit -a --allow-empty-message -m ''
git push
