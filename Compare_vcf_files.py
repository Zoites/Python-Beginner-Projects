#!/usr/bin/env python

#Purpose: Find similar rows in 2 vcf files
#Usage: ./Compare_Specific_Columns_v5.py file1.vcf file2.vcf
#Author: Ousman Mahmud -> ousman.mahmud@gmail.com
#Date: June 20, 2019

import sys

f1=open(sys.argv[1],'r')
f2=open(sys.argv[2],'r')


d = {}

#Read file 1 and store columns
while True:
  line = f1.readline()
  if not line:
    break
  c0,c1,c2,c3,c4 = line.split("\t", 4)
  d[(c0,c1,c2,c3,c4)] = (c0,c1,c2,c3,c4)
	
#Read file 2 and store columns
while True:
  line = f2.readline()
  if not line:
    break
  c0,c1,c2,c3,c4 = line.split("\t", 4)
  
  '''compare to the 2 files and print similar rows'''
  if (c0,c1,c2,c3,c4) in d:
  	print (c0,c1,c2,c3,c4, sep='\t', end='')

f1.close()
f2.close()