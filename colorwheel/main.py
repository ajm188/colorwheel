import argparse
import sys
from pathlib import Path


def collect_files(path):
    if path.is_file():
        return [path]

    return path.glob('**/*.py')


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('module')
    return parser


def _main(argv):
    parser = build_parser()
    parsed_args = parser.parse_args(argv)
    files = collect_files(Path(parsed_args.module))
    print(list(files))
    return 0


def main():
    sys.exit(_main(sys.argv[1:]))


if __name__ == '__main__':
    main()
