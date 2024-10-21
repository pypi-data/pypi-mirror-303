import argparse
import json
import subprocess
from typing import Optional

import requests
from rich import print

from ambientctl.config import settings


def get_parser():
    parser = argparse.ArgumentParser(
        prog="daemon",
        usage="ambientctl %(prog)s [options] [command]",
        description="Manage the Ambient Edge Server daemon.",
        epilog="Example: ambientctl %(prog)s restart",
        add_help=False,  # Suppress the default help argument
    )
    parser.add_argument(
        "command",
        help="The command to perform on the service.",
        choices=["install", "start", "stop", "restart", "status", "logs"],
    )
    parser.add_argument(
        "-e",
        "--env-vars",
        help="Environment variables to pass to the service.",
        required=False,
    )
    return parser


def run(args):
    print(f"ARGS: {args}")
    command = args.command
    if command == "install":
        print("Installing service ...")
        print("NOTE: You may be asked for your password.")
        env_vars = args.env_vars
        if env_vars:
            print(f"Environment variables override: {env_vars}")
            install(env_vars)
            return
        install()
    elif command == "start":
        print("Starting service ...")
        start()
    elif command == "stop":
        print("Stopping service ...")
        stop()
    elif command == "restart":
        print("Restarting service ...")
        restart()
    elif command == "status":
        print("Getting service status ...")
        status()
    elif command == "logs":
        print("Getting service logs ...")
        logs()
    else:
        print("Invalid command.")
        exit(1)


def install(env_vars: Optional[str] = None):
    try:
        url = f"{settings.ambient_server}/daemon/install"
        if env_vars:
            print(f"Environment variables: {env_vars}")
            env_dict = {}
            for key_value_pair in env_vars.split(","):
                key, value = key_value_pair.split("=")
                env_dict[key] = value
            print(f"Environment variables dict: {json.dumps(env_dict, indent=4)}")
            response = requests.post(url, json=env_dict)
        else:
            response = requests.post(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Failed to install service: {e}")
        exit(1)


def start():
    try:
        url = f"{settings.ambient_server}/daemon/start"
        response = requests.post(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Failed to start service: {e}")
        exit(1)


def stop():
    try:
        url = f"{settings.ambient_server}/daemon/stop"
        response = requests.post(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Failed to stop service: {e}")
        exit(1)


def restart():
    try:
        url = f"{settings.ambient_server}/daemon/restart"
        response = requests.post(url)
        response.raise_for_status()
        print(json.dumps(response.json(), indent=4))
    except requests.exceptions.RequestException as e:
        print(
            f"Failed to restart service via server: {e}\n\
Restarting via CLI...\nPassword may be required!"
        )
        restart_cmd = ["sudo", "systemctl", "restart", "ambient_edge_server.service"]
        try:
            output = subprocess.run(
                restart_cmd, check=True, text=True, capture_output=True
            )
            print(output.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Failed to restart service via CLI: {e}")
            exit(1)


def status():
    try:
        url = f"{settings.ambient_server}/daemon/status"
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Failed to get service status: {e}")
        exit(1)


def logs():
    try:
        logs_cmd = [
            "journalctl",
            "-u",
            "ambient_edge_server.service",
            "--no-pager",
            "--output",
            "cat",
        ]
        output = subprocess.run(logs_cmd, check=True, text=True, capture_output=True)
        lines = output.stdout.splitlines()[settings.ambient_log_lines * -1 :]  # noqa
        for line in lines:
            print(line)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get logs: {e}")
        exit(1)
