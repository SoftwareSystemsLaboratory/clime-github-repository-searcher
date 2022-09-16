# PRIME GitHub Repository Searcher

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6480691.svg)](https://doi.org/10.5281/zenodo.6480691)
[![Release Project](https://github.com/SoftwareSystemsLaboratory/prime-github-repository-searcher/actions/workflows/release.yml/badge.svg)](https://github.com/SoftwareSystemsLaboratory/prime-github-repository-searcher/actions/workflows/release.yml)

> A utility to perform advanced searching on GitHub using both the REST and GraphQL APIs

## Table of Contents

- [PRIME GitHub Repository Searcher](#prime-github-repository-searcher)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
    - [Licensing](#licensing)
  - [How To Use](#how-to-use)
    - [Installation](#installation)
    - [Command Line Arguements](#command-line-arguements)

## About

The Software Systems Laboratory (SSL) GitHub Repository Searcher is an installable Python project that utilizes both the GitHub REST and GraphQL APIs to allow for the advanced searching of repositories hosted on GitHub.

### Licensing

This project is licensed under the BSD-3-Clause. See the [LICENSE](LICENSE) for more information.

## How To Use

### Installation

You can install the tool from PyPi with one of the following one liners:

- `pip install prime-metrics`
- `pip install prime-github-repository-searcher`

### Command Line Arguements

`prime-github-repository-searcher -h`

``` shell
usage: PRIME GitHub Repository Searcher [-h] [-r REPOSITORY] [--topic TOPIC]
                                        -o OUTPUT -t TOKEN
                                        [--min-stars MIN_STARS]
                                        [--max-stars MAX_STARS]
                                        [--min-commits MIN_COMMITS]
                                        [--max-commits MAX_COMMITS]
                                        [--min-issues MIN_ISSUES]
                                        [--max-issues MAX_ISSUES]
                                        [--min-pull-requests MIN_PULL_REQUESTS]
                                        [--max-pull-requests MAX_PULL_REQUESTS]
                                        [--min-forks MIN_FORKS]
                                        [--max-forks MAX_FORKS]
                                        [--min-watchers MIN_WATCHERS]
                                        [--max-watchers MAX_WATCHERS]
                                        [--min-created-date MIN_CREATED_DATE]
                                        [--max-created-date MAX_CREATED_DATE]
                                        [--min-pushed-date MIN_PUSHED_DATE]
                                        [--max-pushed-date MAX_PUSHED_DATE]
                                        [-v]

A utility to perform advanced searching on GitHub using both the REST and
GraphQL APIs

options:
  -h, --help            show this help message and exit
  -r REPOSITORY, --repository REPOSITORY
                        A specific repository to be analyzed. Must be in
                        format OWNER/REPO
  --topic TOPIC         Topic to scrape (up to) the top 1000 repositories from
  -o OUTPUT, --output OUTPUT
                        JSON file to dump data to
  -t TOKEN, --token TOKEN
                        GitHub personal access token
  --min-stars MIN_STARS
                        Minimum number of stars a repository must have
  --max-stars MAX_STARS
                        Maximum number of stars a repository must have
  --min-commits MIN_COMMITS
                        Minimum number of commits a repository must have
  --max-commits MAX_COMMITS
                        Maximum number of commits a repository must have
  --min-issues MIN_ISSUES
                        Minimum number of issues a repository must have
  --max-issues MAX_ISSUES
                        Maximum number of issues a repository must have
  --min-pull-requests MIN_PULL_REQUESTS
                        Minimum number of pull requests a repository must have
  --max-pull-requests MAX_PULL_REQUESTS
                        Maximum number of pull requests a repository must have
  --min-forks MIN_FORKS
                        Minimum number of forks a repository must have
  --max-forks MAX_FORKS
                        Maximum number of forks a repository must have
  --min-watchers MIN_WATCHERS
                        Minimum number of watchers a repository must have
  --max-watchers MAX_WATCHERS
                        Maximum number of watchers a repository must have
  --min-created-date MIN_CREATED_DATE
                        Minimum date of creation a repository must have
  --max-created-date MAX_CREATED_DATE
                        Maximum date of creation a repository must have
  --min-pushed-date MIN_PUSHED_DATE
                        Minimum date of the latest push a repository must have
  --max-pushed-date MAX_PUSHED_DATE
                        Maximum date of the latest push a repository must have
  -v, --version         Display version of the tool

Author(s): Nicholas M. Synovic, Matthew Hyatt, George K. Thiruvathukal
```
