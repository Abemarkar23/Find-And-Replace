#!/bin/python
import os

print("copying script to /usr/bin")
os.system("sudo cp far /usr/bin/")
os.system("sudo chmod +x /usr/bin/far")

try:
	import pathlib
	import argparse
	print("sucess!")
	sys.exit()

except ImportError:
	print("isntalling pathlib and argparse")
	os.system("pip install pathlib")
	os.system("pip install argparse")




