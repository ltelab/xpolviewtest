#!/usr/bin/env python

import glob
import subprocess

quicklook_dir = '/users/radarop/test_epfl_2020/quicklooks/'
list_profiles = sorted(glob.glob(quicklook_dir+'2020*/*profile.png'))
latest_profile = list_profiles[-1]
list_rhis = sorted(glob.glob(quicklook_dir+'2020*/*rhi.png'))
latest_rhis = list_profiles[-1]

subprocess.Popen(["cp",latest_profile,'/users/radarop/xpolviewtest/latest_profile.png'], stdout=subprocess.PIPE)
subprocess.Popen(["cp",latest_profile,'/users/radarop/xpolviewtest/latest_rhi.png'], stdout=subprocess.PIPE)
