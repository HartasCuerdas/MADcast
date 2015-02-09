#!/usr/bin/python

import sys
import os
from datetime import datetime

verbose = False

if verbose:
  print 'Number of arguments:', len(sys.argv), 'arguments.'
  print 'Argument List:', str(sys.argv)

path = 'audios'
year = '2013'
month = sys.argv[1]
day = sys.argv[2]

thisdir = path + '/' + year + '/' + month +'/' + day + '/'
fileshere = os.listdir(thisdir)
segments = len(fileshere)
lengths = []

for i in range (1, segments+1):
  statinfo = os.stat( thisdir + 'parte-' + str(i) + '.mp3')
  lengths.append(statinfo.st_size)

if verbose:
  print 'dir: \'' + thisdir + '\''
  print 'files: ' + str(fileshere)
print '---'
print 'segments: ' + str(segments)
print 'lengths: ' + str(lengths)
print 'pubDate: ' + str(datetime.utcnow())
print '---'
