from argparse import ArgumentParser, Namespace
from wsgiref import headers

from requests import Response
from requests import get

def get_argparse() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="SSL Metrics GitHub Repository Information",
        usage="Gather information about GitHub repositories by leveraging the GitHub REST and GraphQL libraries",
    )
    parser.add_argument(
        "-l",
        "--list",
        help="List of repositories to analyze",
        type=str,
        required=False,
        default=None,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="JSON file to dump data to",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-r",
        "--repository",
        help="A specific repository to be analyzed. Must be in format OWNER/REPO",
        type=str,
        required=False,
        default=None,
    )
    parser.add_argument(
        "--min-stars",
        help="Minimum number of stars a repository must have",
        type=int,
        required=False,
        default=0,
    )

    return parser.parse_args()

def call_REST(topic: str, stars: int, token: str)    ->  Response:
    url: str = "https://api.github.com/search/repositories?q=topic:{} + stars:>={}&sort=stars&order=asc&per_page=100&page={}"
    headers: dict

    return get()

def call_GraphQL(owner: str, repo: str, stars: int, token: str)    ->  Response:
    pass

def main() -> None:
    args: Namespace = get_argparse()

    if (args.list is None) and (args.repository is None):
        print("Please input a TXT file of reposorities or a specific repository to analyze")
        quit(1)

    if args.output[-5::] != ".json":
            print("Invalid output file type. Output file must be JSON")
            quit(2)

    try:
        if args.list[-4::] != ".txt":
            print("Invalid input file type. Input file must be TXT")
            quit(3)
    except TypeError:
        pass

    if (args.list is not None) and (args.repository is not None):
        print("A list of repositories and a specific repository have been inputted. The list of repositories will be analyzed")

    if args.min_stars < 0:
        args.min_stars = 0




if __name__ == "__main__":
    main()
