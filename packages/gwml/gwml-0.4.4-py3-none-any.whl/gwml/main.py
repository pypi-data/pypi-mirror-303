import argparse
from gwml.command import handle_pull, handle_push


def main():
    parser = argparse.ArgumentParser(description="CLI for pull and push commands")

    subparsers = parser.add_subparsers(dest="command")

    pull_parser = subparsers.add_parser("pull", help="Execute pull command")

    push_parser = subparsers.add_parser("push", help="Execute push command")
    push_parser.add_argument("-s", "--string1", type=str, help="First string option")
    push_parser.add_argument("-j", "--string2", type=str, help="Second string option")

    args = parser.parse_args()

    if args.command == "pull":
        handle_pull()
    elif args.command == "push":
        handle_push()
    else:
        parser.print_help()


# if __name__ == '__main__':
#     main()
