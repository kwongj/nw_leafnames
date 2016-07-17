#!/usr/bin/env python

# Use modern print function from python 3.x
from __future__ import print_function

# Usage
import argparse
from argparse import RawTextHelpFormatter
import csv
from ete2 import Tree
import sys

def tab2dict(tab, sep):
    with open(tab, mode='r') as file:
        table = csv.reader(file, delimiter=sep)
        dict = {rows[0]:rows[1] for rows in table}
    return dict

parser = argparse.ArgumentParser(
    formatter_class=RawTextHelpFormatter,
    description='Rename or display external node names (leaves) in Newick tree file\n'
		'If list of new names is not specified, output will use existing names\n'
		'\nOutput formats :\n'
		'\tnewick : newick format\n'
		'\t  tree : show tree topology\n'
		'\t  list : print list of leaf names\n',
    usage='\n  %(prog)s [OPTIONS] TREE > new_names.tree')
parser.add_argument('tree', metavar='TREE', nargs=1, help='original tree file in Newick format')
parser.add_argument('--tab', metavar='TAB', nargs=1, help='specify tab-separated file with [oldnames] [newnames]')
parser.add_argument('--csv', metavar='CSV', nargs=1, help='specify CSV file with [oldnames],[newnames]')
parser.add_argument('--output', metavar='FORMAT', nargs=1, help='newick (default) | tree | list')
parser.add_argument('--version', action='version', version=
    '=====================================\n'
    '%(prog)s v0.1\n'
    'Updated 17-Jul-2016 by Jason Kwong\n'
    'Dependencies: ete2, csv\n'
    '=====================================')
args = parser.parse_args()

# Load tree
t = Tree(args.tree[0])

# Rename leaf nodes
if args.tab:
	new_names = tab2dict(args.tab[0], '\t')
	for leaf in t.iter_leaves():
	    leaf.name = new_names[leaf.name]
elif args.csv:
	new_names = tab2dict(args.csv[0], ',')
	for leaf in t.iter_leaves():
	    leaf.name = new_names[leaf.name]

# Print output to stdout
if args.output[0] == 'list':
	for leaf in t.iter_leaves():
		print(leaf.name)
elif args.output[0] == 'tree':
	print(t)
else:
	print(t.write(format=1))

sys.exit(0)
