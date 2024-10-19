from parser import get_args
from make import make_dir
from check import check_dir


if __name__ == '__main__':
    args = get_args()

    if args.command == "make":
        make_dir(args)
    elif args.command == "check":
        check_dir(args)
    else:
        print(f"Not supported command: {args.command}")

