#!/usr/bin/env python

# To be used in conjunction with the passgen shell script under bash scripts folder.
# This script just takes the existing values provided and mangles them. 

import itertools
import sys

j = len(sys.argv)

if j == 3:
	list = [sys.argv[1], sys.argv[2]]
	for x in range(1, len(list) + 1):
		for i in itertools.permutations(list, 2):
			print "".join(i)

if j == 4:
	list = [sys.argv[1], sys.argv[2], sys.argv[3]]
	for x in range(1, len(list) + 1):
		for i in itertools.permutations(list, 2):
			print "".join(i)

if j == 5:
	list = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
	for x in range(1, len(list) + 1):
		for i in itertools.permutations(list, 2):
			print "".join(i)

if j == 6:
	list = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]
	for x in range(1, len(list) + 1):
		for i in itertools.permutations(list, 2):
			print "".join(i)

if j == 7:
	list = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]]
	for x in range(1, len(list) + 1):
		for i in itertools.permutations(list, 2):
			print "".join(i)
if j == 8:
        list = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]]
        for x in range(1, len(list) + 1):
                for i in itertools.permutations(list, 2):
                        print "".join(i)
if j == 9:
        list = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]]
        for x in range(1, len(list) + 1):
                for i in itertools.permutations(list, 2):
                        print "".join(i)
if j == 10:
        list = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9]]
        for x in range(1, len(list) + 1):
                for i in itertools.permutations(list, 2):
                        print "".join(i)
if j == 11:
        list = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]]
        for x in range(1, len(list) + 1):
                for i in itertools.permutations(list, 2):
                        print "".join(i)
