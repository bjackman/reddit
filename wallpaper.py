#!/usr/bin/python

from urllib import urlopen
from json import load as decode_json
from sys import argv, exit

if len(argv) != 2:
  print("please provide a filename to save to as an argument")
  exit(1)
out_file_name = argv[1]

json_io = urlopen("http://www.reddit.com/r/wallpapers/top/.json")
listing = decode_json(json_io)
image_url = listing["data"]["children"][0]["data"]["url"] #lol
image_io = urlopen(image_url)
out_file = open(out_file_name, "w")
out_file.write(image_io.read())
out_file.close()
