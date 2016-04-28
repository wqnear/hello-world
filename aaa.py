#!/usr/bin/env python2
# -*-encoding:utf-8 -*-

import time
import os


if os.path.exists('/opt/python/projects/text.txt'):
	print("the dir is exists")
	fileinfo = os.stat('text.txt')
	filemtime = fileinfo.st_mtime

	if (time.time() - filemtime) >= 300:
		print("too big ,delete it")
else:
	print("dont have this dir")
