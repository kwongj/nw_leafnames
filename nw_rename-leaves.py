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
    description='Rename external nodes (leaves) in Newick tree\n',
    usage='\n  %(prog)s [OPTIONS] TREE > new_names.tree')
parser.add_argument('tree', metavar='TREE', nargs=1, help='original tree file in Newick format')
parser.add_argument('--tab', metavar='TAB', help='specify tab-separated file with [oldnames] [newnames]')
parser.add_argument('--csv', metavar='CSV', help='specify CSV file with [oldnames],[newnames]')
parser.add_argument('--show', action='store_true', help='show tree with new leaf names')
parser.add_argument('--version', action='version', version=
    '=====================================\n'
    '%(prog)s v0.1\n'
    'Updated 7-Jul-2016 by Jason Kwong\n'
    'Dependencies: ete2, csv\n'
    '=====================================')
args = parser.parse_args()

# Load tree
t = Tree(args.tree[0])

# Set delimiter options
if args.tab:
    tab = args.tab
    sep = '\t'
elif args.csv:
    tab = args.csv
    sep = ','
else:
    print(t.write(format=1))
    sys.exit(0)

# Setup dictionary of oldnames, newnames
new_names = tab2dict(tab, sep)

# Rename leaf nodes
for leaf in t.iter_leaves():
    leaf.name = new_names[leaf.name]
if args.show:
    print(t)
else:
    print(t.write(format=1))
sys.exit(0)
