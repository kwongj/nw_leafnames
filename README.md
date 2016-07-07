# nw_rename-leaves
Rename external nodes (leaves) in a newick tree

##Author

Jason Kwong (@kwongjc)

##Dependencies
* Python 2.7.x
* ete2

##Usage

```
$ nw_rename-leaves.py -h

usage: 
  nw_rename-leaves.py [OPTIONS] TREE > new_names.tree

Rename external nodes (leaves) in Newick tree

positional arguments:
  TREE        original tree file in Newick format

optional arguments:
  -h, --help  show this help message and exit
  --tab TAB   specify tab-separated file with [oldnames] [newnames]
  --csv CSV   specify CSV file with [oldnames],[newnames]
  --show      show tree with new leaf names
  --version   show program's version number and exit
```

##Bugs

Please submit via the [GitHub issues page](https://github.com/kwongj/nw_rename-leaves/issues).  

##Software Licence

[GPLv3](https://github.com/kwongj/nw_rename-leaves/blob/master/LICENSE)
