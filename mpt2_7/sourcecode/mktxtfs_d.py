# -*- encode: utf-8 -*-

__version__ = '0.0.0'
__date__ = '20 March 2019'

'''
$ python mktxtfs_d.py txt1
current_directory
+- txt1
    +- txt1_001.txt
    +- txt1_002.txt
    ...
    +- txt1_010.txt
    +- txt1_011.txt
    ...
    +- txt1_100.txt
    +- txt1_101.txt
    ...
'''


import os.path
import sys
import argparse
import math


def parse(argv):
    parser = argparse.ArgumentParser(description='mkdir and make txt files in')

    parser.add_argument('dirpath', type=str)
    parser.add_argument('-nd', '--num_of_dirs', type=int, default=4, metavar='')
    parser.add_argument('-nf', '--num_of_files', type=int, default=400, metavar='')

    parsed_argv = parser.parse_args(argv)
    return parsed_argv


def mk_txtfs(root_dir, n_dirs , n_files):
    if os.path.isdir(root_dir):
        raise ValueError("Can't make existing directory; {}".format(dirpath))
    os.mkdir(root_dir)
    int_n_files_log10 = int(math.log10(float(n_files)))
    for n_d in range(1, n_dirs+1):
        child_dirname = '{}-{}'.format(os.path.basename(root_dir), n_d)
        child_dirpath = os.path.join(root_dir, child_dirname)
        os.mkdir(child_dirpath)
        for n_f in range(1, n_files+1):
            n_zeros = int_n_files_log10 - int(math.log10(float(n_f)))
            txtname = '{}-{}{}.txt'.format(os.path.basename(child_dirpath), '0' * n_zeros, n_f)
            txtpath = os.path.join(child_dirpath, txtname)
            with open(txtpath, 'w') as f:
                f.write('')


def main(args):
    parsed_args = parse(args)
    mk_txtfs(parsed_args.dirpath, parsed_args.num_of_dirs, parsed_args.num_of_files)


if __name__ == '__main__':
    main(sys.argv[1:])
