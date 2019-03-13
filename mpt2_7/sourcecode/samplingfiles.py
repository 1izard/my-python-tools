import argparse
import os.path
import sys
import glob


def parse(argv):
    parser = argparse.ArgumentParser(
        description='Sampling files in src_dir and output the files in dst_dir')

    parser.add_argument('src_dir', type='str')
    parser.add_argument('dst_dir', type='str')
    parser.add_argument('unit', type=int)
    parser.add_argument('step', type=int)

    parsed_argv = parser.parse_args(argv)
    return parsed_argv


def sampling(src_dir, dst_dir, unit, step):
    if os.path.isdir(dst_dir):
        raise ValueError("Can't apply existing directory; {}".format(dst_dir))
    txt_lst = glob.glob(os.path.join(src_dir, '*.txt'))
    sample_txts = [x for i, x in enumerate(txt_lst, 1) if i % step <= unit]
    sample_txts.extend()



def main(args):
    parsed_args = parse(args)
    sampling(parsed_args.src_dir, parsed_args.dst_dir, parsed_args.unit, parsed_args.step)


if __name__ == '__main__':
    main(sys.argv[1:])
