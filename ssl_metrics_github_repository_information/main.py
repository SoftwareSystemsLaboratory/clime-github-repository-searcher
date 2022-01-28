from argparse import ArgumentParser, Namespace

import pandas
from pandas import DataFrame
from requests import Response, get, post


def get_argparse() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="SSL Metrics GitHub Repository Information",
        usage="Gather information about a GitHub from the GitHub GraphQL API",
    )
    parser.add_argument(
        "-i",
        "--input",
        help="A specific repository to be analyzed. Must be in format OWNER/REPO",
        type=str,
        required=True,
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

    return parser.parse_args()


def callGraphQL(owner: str, repo: str, token: str) -> Response:
    apiURL: str = f"https://api.github.com/graphql"
    requestHeaders: dict = {
        "Authorization": f"bearer {token}",
    }
    query: str = (
        '{repository(owner: "'
        + owner
        + '", name: "'
        + repo
        + """") {
        ... on Repository {
            nameWithOwner
            url
            repositoryTopics(first: 100) {
                nodes {
                    topic {
                        name
                        }
                    }
                }
            object(expression: "HEAD") {
                ... on Commit {
                    history {
                        totalCount
                        }
                    }
                }
            issues {
                totalCount
                }
            pullRequests {
                totalCount
            }
            stargazerCount
            forkCount
            watchers {
                totalCount
            }
            licenseInfo {
                name
                pseudoLicense
            }
        }
    }
}"""
    )

    json: dict = {"query": query, "variables": ""}

    return post(url=apiURL, headers=requestHeaders, json=json)


def flattenJSON(json: dict) -> DataFrame:
    pass


def main() -> None:
    args: Namespace = get_argparse()

    if args.output[-5::] != ".json":
        print("Invalid output file type. Output file must be JSON")
        quit(1)

    if args.min_stars < 0:
        args.min_stars = 0

    r: Response = callGraphQL("numpy", "numpy", token=args.token)
    print(type(r.json()))


if __name__ == "__main__":
    main()
