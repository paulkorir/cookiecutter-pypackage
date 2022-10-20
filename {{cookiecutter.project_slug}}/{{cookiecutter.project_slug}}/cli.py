"""Console script for {{cookiecutter.project_slug}}."""

import argparse
import shlex
import sys


def parse_args() -> argparse.Namespace:
    """Function to parse args"""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    return args


def cli(cmd) -> argparse.Namespace:
    """Simulate a CLI for testing purposes"""
    sys.argv = shlex.split(cmd)
    return parse_args()
