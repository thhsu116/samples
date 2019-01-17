import argparse

def parse_args(args):
    parser = argparse.ArgumentParser(description="someting")
    parser.add_argument("-t", required=True, dest='test', help="something")
    return parser.parse_args(args)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
