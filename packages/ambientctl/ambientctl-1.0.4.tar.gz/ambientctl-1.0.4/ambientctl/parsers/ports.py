import argparse
import base64

import requests

from ambientctl.config import settings


def get_parser():
    parser = argparse.ArgumentParser(
        prog="ports",
        usage="ambientctl %(prog)s [options] command [args]",
        description="Interact with the host ports.",
        epilog="Example: ambientctl ports forward",
        add_help=False,  # Suppress the default help argument
    )
    parser.add_argument("command", help="The command to run", choices=["forward"])
    # add flags for forward command
    parser.add_argument("--ws-uri", help="The websocket URI to forward to")
    parser.add_argument("--port", help="The port to forward")
    return parser


def run(args):
    # print(f"args: {args}")
    command = args.command
    print(f"Running command: {command}...")

    if command == "forward":
        ws_uri = args.ws_uri
        port = args.port
        forward_ports(ws_uri, port)
        return
    # elif command == 'list':
    #     list_ports()
    #     return

    print("error: command not found")


def forward_ports(ws_uri: str, port: int):
    url = f"{settings.ambient_server}/ports/port-forwards/{port}"
    # add ws_url to query params
    base_64_encoded_ws_uri = base64.b64encode(ws_uri.encode()).decode()
    url = f"{url}?ws_url={base_64_encoded_ws_uri}"
    try:
        response = requests.post(url)
        response.raise_for_status()
        print(response.json())
    except Exception as e:
        print(f"error: {e}")
        return
