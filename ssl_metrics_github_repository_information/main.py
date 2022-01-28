from argparse import ArgumentParser, Namespace

from pandas import DataFrame
from requests import Response, get, post


def get_argparse() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="SSL Metrics GitHub Repository Information",
        usage="Gather information about a GitHub from the GitHub GraphQL API",
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
        "--topic",
        help="Topic to scrape (up to) the top 1000 repositories from",
        type=str,
        required=False,
        default=None,
    )

    return parser.parse_args()


def callREST(stars: int, topic: str, token: str, page: int = 1) -> Response:
    apiURL: str = f"https://api.github.com/search/repositories?q=stars:{stars}+topic:{topic}&sort=stars&order=asc&per_page=100&page={page}"
    requestHeaders: dict = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "ssl-metrics-github-repository-information",
        "Authorization": f"token {token}",
    }

    return get(url=apiURL, headers=requestHeaders)


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
            owner {
                login
            }
            name
            url
            repositoryTopics(first: 100) {
                totalCount
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


def flattenJSON(json: dict, df: DataFrame) -> DataFrame:
    root: dict = json["data"]["repository"]

    data: list = [
        root["owner"]["login"],
        root["name"],
        root["url"],
        root["repositoryTopics"]["totalCount"],
        ",".join([x["topic"]["name"] for x in root["repositoryTopics"]["nodes"]]),
        root["object"]["history"]["totalCount"],
        root["issues"]["totalCount"],
        root["pullRequests"]["totalCount"],
        root["stargazerCount"],
        root["forkCount"],
        root["watchers"]["totalCount"],
        root["licenseInfo"]["name"].strip(),
        root["licenseInfo"]["pseudoLicense"],
    ]

    df.loc[len(df)] = data

    return df


def main() -> None:
    args: Namespace = get_argparse()

    if (args.repository is None) and (args.topic is None):
        print("Input either a repository or a topic to analyze")
        quit(1)

    if (args.repository is not None) and (args.topic is not None):
        print("Input either a repository or a topic to analyze")
        quit(2)

    if args.output[-5::] != ".json":
        print("Invalid output file type. Output file must be JSON")
        quit(3)

    if args.min_stars < 0:
        args.min_stars = 0

    columns: list = [
        "owner",
        "repository",
        "url",
        "topicCount",
        "topics",
        "totalCommits",
        "totalIssues",
        "totalPullRequests",
        "stargazerCount",
        "forkCount",
        "watchers",
        "licenseName",
        "isPseudoLicense",
    ]
    df: DataFrame = DataFrame(columns=columns)

    if args.repository is None:
        splitRepository: list = args.repository.split("/")
        owner: str = splitRepository[0]
        repo: str = splitRepository[1]

        response: Response = callGraphQL(owner=owner, repo=repo, token=args.token)
        json = response.json()

        flat: DataFrame = flattenJSON(json=json)
        flat.T.to_json(args.output)


if __name__ == "__main__":
    main()
