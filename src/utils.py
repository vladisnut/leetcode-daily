import os.path
from datetime import datetime

from requests import HTTPError, ConnectionError
from winotify import Notification, audio

from src.api import (
    get_daily_problem,
    get_daily_problem_url,
    get_user_recent_submissions,
)
from src.config import APP_ID, ICON_PATH, DATA_PATH, DATE_FORMAT


def notify(message: str, launch: str = ""):
    toast = Notification(
        app_id=APP_ID,
        title=APP_ID,
        msg=message,
        icon=ICON_PATH,
        launch=launch,
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def check_daily_problem(username: str):
    today = datetime.utcnow().date()
    today_str = today.strftime(DATE_FORMAT)

    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, encoding="utf-8") as f:
            data = f.read()
        if today_str == data:
            return

    try:
        problem = get_daily_problem()
        submissions = get_user_recent_submissions(username)
    except ConnectionError:
        notify("Не удалось установить соединение с сервером")
        return
    except HTTPError as e:
        notify(str(e))
        return

    if not submissions:
        notify("Невозможно получить список решенных задач, либо он пустой")
        return

    url = get_daily_problem_url(problem)
    daily_slug = problem["question"]["titleSlug"]

    for submission in submissions:
        timestamp = int(submission["timestamp"])
        date = datetime.utcfromtimestamp(timestamp).date()

        if date == today:
            if submission["titleSlug"] == daily_slug:
                with open(DATA_PATH, "w", encoding="utf-8") as f:
                    f.write(today_str)
                return

        elif date < today:
            notify("Сегодня не было решено ни одной задачи", launch=url)
            return

    timestamp = int(submissions[-1]["timestamp"])
    date = datetime.utcfromtimestamp(timestamp).date()
    if date == today:
        notify("Ежедневная задача, возможно, не решена", launch=url)
