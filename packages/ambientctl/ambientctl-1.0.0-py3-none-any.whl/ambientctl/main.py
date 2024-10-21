import argparse

from ambientctl.parsers import auth, daemon, data, health, ping, ports


def main():
    parser = argparse.ArgumentParser(prog="ambientctl")
    subparsers = parser.add_subparsers(dest="command")

    # add parsers to the list below
    parsers = [ping, ports, auth, daemon, data, health]

    # this loops through the parsers and adds them to the subparsers
    for _parser in parsers:
        parser_ = _parser.get_parser()
        parser_name = _parser.__name__.split(".")[-1]
        subparser = subparsers.add_parser(parser_name, parents=[parser_], add_help=True)
        subparser.set_defaults(func=_parser.run)

    args = parser.parse_args()

    if "func" in args:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
