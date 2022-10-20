"""Main module."""
import sys

from {{ cookiecutter.project_slug }}.cli import parse_args

def main() -> int:
    # main entry point code goes here
    args = parse_args()
    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_slug}}.__main__")
    return 0


if __name__ == "__main__":
    sys.exit(main())
