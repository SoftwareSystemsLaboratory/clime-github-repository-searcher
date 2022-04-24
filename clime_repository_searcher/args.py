from argparse import ArgumentParser, Namespace
from datetime import datetime

name: str = "CLIME"
authors: list = [
    "Nicholas M. Synovic",
    "Matthew Hyatt",
    "George K. Thiruvathukal",
]


def mainArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{name} GitHub Repository Searcher",
        description="A utility to perform advanced searching on GitHub using both the REST and GraphQL APIs",
        epilog=f"Author(s): {', '.join(authors)}",
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
        "--topic",
        help="Topic to scrape (up to) the top 1000 repositories from",
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
        "-t",
        "--token",
        help="GitHub personal access token",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--min-stars",
        help="Minimum number of stars a repository must have",
        type=int,
        required=False,
        default=0,
    )
    parser.add_argument(
        "--max-stars",
        help="Maximum number of stars a repository must have",
        type=int,
        required=False,
        default=1000000000,
    )
    parser.add_argument(
        "--min-commits",
        help="Minimum number of commits a repository must have",
        type=int,
        required=False,
        default=0,
    )
    parser.add_argument(
        "--max-commits",
        help="Maximum number of commits a repository must have",
        type=int,
        required=False,
        default=1000000000,
    )
    parser.add_argument(
        "--min-issues",
        help="Minimum number of issues a repository must have",
        type=int,
        required=False,
        default=0,
    )
    parser.add_argument(
        "--max-issues",
        help="Maximum number of issues a repository must have",
        type=int,
        required=False,
        default=1000000000,
    )
    parser.add_argument(
        "--min-pull-requests",
        help="Minimum number of pull requests a repository must have",
        type=int,
        required=False,
        default=0,
    )
    parser.add_argument(
        "--max-pull-requests",
        help="Maximum number of pull requests a repository must have",
        type=int,
        required=False,
        default=1000000000,
    )
    parser.add_argument(
        "--min-forks",
        help="Minimum number of forks a repository must have",
        type=int,
        required=False,
        default=0,
    )
    parser.add_argument(
        "--max-forks",
        help="Maximum number of forks a repository must have",
        type=int,
        required=False,
        default=1000000000,
    )
    parser.add_argument(
        "--min-watchers",
        help="Minimum number of watchers a repository must have",
        type=int,
        required=False,
        default=0,
    )
    parser.add_argument(
        "--max-watchers",
        help="Maximum number of watchers a repository must have",
        type=int,
        required=False,
        default=1000000000,
    )
    parser.add_argument(
        "--min-created-date",
        help="Minimum date of creation a repository must have",
        type=str,
        required=False,
        default="1970-01-01",
    )
    parser.add_argument(
        "--max-created-date",
        help="Maximum date of creation a repository must have",
        type=str,
        required=False,
        default=datetime.now().strftime("%Y-%m-%d"),
    )
    parser.add_argument(
        "--min-pushed-date",
        help="Minimum date of the latest push a repository must have",
        type=str,
        required=False,
        default="1970-01-01",
    )
    parser.add_argument(
        "--max-pushed-date",
        help="Maximum date of the latest push a repository must have",
        type=str,
        required=False,
        default=datetime.now().strftime("%Y-%m-%d"),
    )
    parser.add_argument(
        "-v",
        "--version",
        help="Display version of the tool",
        action="store_true",
        default=False,
    )

    return parser.parse_args()
