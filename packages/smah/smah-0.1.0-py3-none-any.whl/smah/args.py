import argparse
import sys
import logging

def initialize_argument_parser():
    """
    Initialize the argument parser with basic configurations.

    Returns:
        ArgumentParser: A configured argument parser.
    """
    return argparse.ArgumentParser(
        description="SMAH Command Line Tool",
        formatter_class=argparse.RawTextHelpFormatter
    )


def add_general_arguments(parser: argparse.ArgumentParser) -> None:
    """
    Add general command-line arguments to the parser.

    Args:
        parser (ArgumentParser): The argument parser to which general arguments are added.
    """
    parser.add_argument('-q', '--query', type=str, help='The Query to process')
    parser.add_argument('-i', '--instructions', type=str, help='The Instruction File to process')
    parser.add_argument('--profile', type=str, help='Path to alternative config file')
    parser.add_argument('-v', '--verbose', action='count', default=0, help="Set Verbosity Level, such as -vv")

def add_ai_arguments(parser: argparse.ArgumentParser) -> None:
    """
    Add specific AI-related command-line arguments to the parser.

    Args:
        parser (ArgumentParser): The argument parser to which AI-related arguments are added.
    """
    parser.add_argument('--openai-api-tier', type=int, help='OpenAI Tier')
    parser.add_argument('--openai-api-key', type=str, help='OpenAI Api Key')
    parser.add_argument('--openai-api-org', type=str, help='OpenAI Api Org')

def add_gui_arguments(parser: argparse.ArgumentParser) -> None:
    """
    Add GUI-related command-line arguments to the parser.

    Args:
        parser (ArgumentParser): The argument parser to which GUI-related arguments are added.
    """
    parser.add_argument('--gui', action=argparse.BooleanOptionalAction, help='Run in GUI mode', default=True)

def extract_args() -> tuple[argparse.Namespace, str | None]:
    """
    Parses and extracts command-line arguments for the SMAH CLI tool.

    Returns:
        parser (ArgumentParser): The argument parser with configured options.
        args (Namespace): Parsed arguments and options.
        pipe (str or None): Content read from standard input if available.
    """
    parser = initialize_argument_parser()
    add_general_arguments(parser)
    add_ai_arguments(parser)
    add_gui_arguments(parser)
    args = parser.parse_args()
    return args, get_pipe()


def get_pipe():
    """
    Reads data from standard input if present and available.

    Returns:
        str or None: The content available from standard input; otherwise, None if input is not a TTY.
    """
    if sys.stdin.isatty():
        return None
    else:
        return sys.stdin.read()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    args, pipe = extract_args()
    logging.debug("Parsed arguments: %s", args)
    logging.debug("Pipe content: %s", pipe)