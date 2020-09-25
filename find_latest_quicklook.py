#!/usr/bin/env python

import glob
import subprocess

quicklook_dir = '/users/radarop/test_epfl_2020/quicklooks/'
list_quicklooks = sorted(quicklook_dir+'*/*')
latest = list_quicklooks[-1]
