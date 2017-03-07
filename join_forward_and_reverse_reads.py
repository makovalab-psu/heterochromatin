import sys
import os
from os.path import basename
import numpy as np
import itertools
from itertools import izip

######################################
#python join_forward_and_reverse_reads.py forwardReads reverseReads
######################################

forward=sys.argv[1]
reverse=sys.argv[1]

fRepeats=[]
rRepeats=[]

f = open(forward)
r = open(reverse)
print(f.readline())
print(r.readline())
headerF=f.readline()
print("headerF: " + headerF)
while True:
    lineR=r.readline()
    print("lineR: " + lineR)
    if (headerF==lineR):
	    last_pos = r.tell()
	    while ("@" not in lineR):
	    	lineR=r.readline()
	    	print lineR
	    print("match")
	    break
r.seek(last_pos)