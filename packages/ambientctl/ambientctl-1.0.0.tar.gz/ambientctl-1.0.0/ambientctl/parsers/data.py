import argparse
import json
from typing import Any

import requests
from rich import print

from ambientctl.config import settings


def get_parser():
    parser = argparse.ArgumentParser(
        prog="data",
        usage="ambientctl %(prog)s [options] [operation] [resource]",
        description="Interact with stateful data on the edge node",
        epilog="Example: ambientctl ping backend",
        add_help=False,  # Suppress the default help argument
    )
    parser.add_argument("operation", help="CRUD operation to perform")
    parser.add_argument("resource", help="Data to perform the operation on")
    return parser


def run(args):
    op = args.operation
    resource = args.resource

    rest_method = settings.cred_to_rest_dict.get(op, None)
    if rest_method is None:
        print(f"Invalid operation: {op}")
        return

    result = make_rest_call(resource, rest_method)

    print(json.dumps(result, indent=4))


def make_rest_call(resource: str, method: str) -> Any:
    response = requests.request(method, f"{settings.ambient_server}/data/{resource}")
    response.raise_for_status()
    return response.json()
