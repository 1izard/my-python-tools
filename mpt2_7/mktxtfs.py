'''
$ python mktxtfs.py txt1
current_directory
+- txt1
    +- txt1_1.txt
    +- txt1_2.txt
    ...
    +- txt1_10.txt
'''


import os.path
import sys
import argparse


def parse(argv):
    parser = argparse.ArgumentParser(description='mkdir and make txt files in')

    parser.add_argument('dirpath', type=str)
    parser.add_argument('-n', '--number', type=int, default=10, metavar='')

    parsed_argv = parser.parse_args(argv[:])
    return parsed_argv


def mk_txtfs(dirpath, num):
    if os.path.isdir(dirpath):
        raise ValueError("Can't make existing directory; {}".format(dirpath))
    os.mkdir(dirpath)
    for i in range(1, num+1):
        txtname = '{}_{}.txt'.format(os.path.basename(dirpath), i)
        txtpath = os.path.join(dirpath, txtname)
        with open(txtpath, 'w') as f:
            f.write('')


def main(args):
    parsed_args = parse(args)
    mk_txtfs(parsed_args.dirpath, parsed_args.number)


if __name__ == '__main__':
    main(sys.argv[1:])
