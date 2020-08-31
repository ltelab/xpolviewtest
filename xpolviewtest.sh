#!/bin/bash

cp /users/radarop/test_epfl_2020/quicklooks/2020-08-28/XPOL-20200828-201554_az161_Zdr.png /users/radarop/xpolviewtest/latest.png
git pull
git add .
git commit -a --allow-empty-message -m ''
git push
