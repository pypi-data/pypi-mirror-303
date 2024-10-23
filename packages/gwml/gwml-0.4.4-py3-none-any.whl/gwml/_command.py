import argparse


class CommandParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(prog="gwml")
        self.subparser = self.parser.add_subparsers(
            dest="command", help="Available commands"
        )

    def get_args(self) -> argparse.Namespace:
        pull_parser = self.subparser.add_parser(
            "pull", help="You can download ML writing samples."
        )
        push_parser = self.subparser.add_parser(
            "push", help="You can deploy the model you wrote in GreenWales"
        )

        pull_option = pull_parser.add_mutually_exclusive_group(required=False)
        pull_option.add_argument(
            "-l",
            "-list",
            help=f"Displays a list of available samples",
        )
        pull_option.add_argument("-n", help=f"Choose a sample name")

        push_option = push_parser.add_mutually_exclusive_group(required=False)
        push_option.add_argument(
            "-H",
            "--host",
            help=f"* Enter your Green Wales address.",
        )
        push_option.add_argument(
            "-U",
            "--user",
            help=f"* Enter your Green Wales login ID",
        )
        push_option.add_argument(
            "-P",
            help=f"* Enter your Green Wales login Password",
        )
        push_option.add_argument(
            "-m",
            help=f"Select when you don't need automatic generation of the setting.yaml file.",
        )

        return self.parser.parse_args()
