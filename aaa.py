#!/usr/bin/env python2
# -*-encoding:utf-8 -*-

import time
import os


def firstrun():
	if os.path.exists('/opt/python/projects/text.txt'):
		print("the dir is exists")
		fileinfo = os.stat('text.txt')
		filemtime = fileinfo.st_mtime

		if (time.time() - filemtime) >= 300:
			print("too old!")
			os.remove("/opt/python/projects/text.txt")
			print("create a new text.txt")
	else:
		print("dont have this dir")

	while True:
		global gotime
		gotime = int(str(time.time())[:10])
		if gotime % 5 == 0:
		#if int(time.time()[:10]) % 300  == 0:
			break
		time.sleep(1)

	print(gotime)
	print("OK")

def main():
	firstrun()

if __name__ == '__main__':
	main()