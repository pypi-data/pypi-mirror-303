import argparse
import json

import requests
from rich import print

from ambientctl.config import settings


def get_parser():
    parser = argparse.ArgumentParser(
        prog="health",
        usage="ambientctl %(prog)s [options] [sub-command]",
        description="Interact with device Health data",
        epilog="Example: ambientctl health backend",
        add_help=False,  # Suppress the default help argument
    )
    parser.add_argument("subcommand", help="Operation to perform")
    return parser


def run(args):
    subcmd = args.subcommand
    if subcmd == "check-in":
        result = check_in()
        print(json.dumps(result, indent=4))
    else:
        print(f"Invalid subcommand: {subcmd}")


def check_in():
    response = requests.request("GET", f"{settings.ambient_server}/health/check-in")
    response.raise_for_status()
    return response.json()
