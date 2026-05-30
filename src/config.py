import os
import sys

APP_ID = "LeetCode"

PROJECT_DIR = (
    os.path.dirname(sys.executable)
    if getattr(sys, "frozen", False)
    else os.path.dirname(os.path.dirname(__file__))
)
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")

ICON_PATH = os.path.join(PROJECT_DIR, "icon.ico")
DATA_PATH = os.path.join(PROJECT_DIR, "data")

DAILY_PROBLEM_QUERY_PATH = os.path.join(
    ASSETS_DIR, "graphql", "questionOfToday.graphql"
)
USER_RECENT_SUBMISSIONS_QUERY_PATH = os.path.join(
    ASSETS_DIR, "graphql", "recentAcSubmissions.graphql"
)

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql/"
LEETCODE_DAILY_PROBLEM_URL = (
    "https://leetcode.com/problems/{slug}/?envType=daily-question"
)

HEADERS = {
    "Content-Type": "application/json",
}

DATE_FORMAT = "%Y-%m-%d"
