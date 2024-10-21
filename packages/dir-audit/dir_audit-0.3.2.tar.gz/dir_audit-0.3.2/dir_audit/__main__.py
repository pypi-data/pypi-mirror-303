import sys
from parser import get_args
from make import make_dir
from check import check_dir
from __init__ import __version__


if __name__ == "__main__":
    args = get_args()

    if args.version:
        print(__version__)
        sys.exit(0)

    if args.command == "make":
        make_dir(args)
    elif args.command == "check":
        check_dir(args)
    else:
        print(f"Not supported command: {args.command}")
