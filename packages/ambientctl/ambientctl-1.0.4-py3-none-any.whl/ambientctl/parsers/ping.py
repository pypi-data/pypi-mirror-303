import argparse

import requests

from ambientctl.config import settings


def get_parser():
    parser = argparse.ArgumentParser(
        prog="ping",
        usage="ambientctl %(prog)s [options] [endpoint]",
        description="Ping an endpoint to check if it is reachable.",
        epilog="Example: ambientctl ping backend",
        add_help=False,  # Suppress the default help argument
    )
    parser.add_argument("endpoint", help="The endpoint to ping")
    return parser


def run(args):
    # print(f"args: {args}")
    endpoint = args.endpoint
    print(f"Pinging {endpoint}...")

    if endpoint == "self":
        print("Pong!")
        return
    elif endpoint == "backend" or endpoint == "server":
        ping_server(endpoint)
        return

    print("error: endpoint not found")


def ping_server(endpoint: str):
    url = f"{settings.ambient_server}/ping?endpoint={endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.json())
    except Exception as e:
        print(f"error: {e}")
        return
