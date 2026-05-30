import requests

from src.config import (
    DAILY_PROBLEM_QUERY_PATH,
    LEETCODE_GRAPHQL_URL,
    HEADERS,
    USER_RECENT_SUBMISSIONS_QUERY_PATH,
    LEETCODE_DAILY_PROBLEM_URL,
)


def get_daily_problem():
    with open(DAILY_PROBLEM_QUERY_PATH, encoding="utf-8") as f:
        query = f.read()

    response = requests.get(
        LEETCODE_GRAPHQL_URL,
        headers=HEADERS,
        json={"query": query},
    )
    response.raise_for_status()
    data = response.json()["data"]["activeDailyCodingChallengeQuestion"]
    return data


def get_user_recent_submissions(username: str):
    with open(USER_RECENT_SUBMISSIONS_QUERY_PATH, encoding="utf-8") as f:
        query = f.read()

    response = requests.get(
        LEETCODE_GRAPHQL_URL,
        headers=HEADERS,
        json={
            "query": query,
            "variables": {
                "username": username,
                "limit": 20,
            },
        },
    )
    response.raise_for_status()
    data = response.json()["data"]["recentAcSubmissionList"]
    return data


def get_daily_problem_url(problem: dict | None = None):
    problem = problem or get_daily_problem()
    slug = problem["question"]["titleSlug"]
    url = LEETCODE_DAILY_PROBLEM_URL.format(slug=slug, date=problem["date"])
    return url
