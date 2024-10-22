from contextlib import contextmanager
from copy import copy
from functools import wraps

from selenium.webdriver.remote.webdriver import WebDriver
from typing_extensions import Unpack

from .analysis import analyze_web_page
from .types import UserwayAnalysisConfig


def userway_analysis_background_watcher(
    web_driver: WebDriver, **config: Unpack[UserwayAnalysisConfig]
):
    def userway_analysis_background_decorator(function):

        @wraps(function)
        def helper(*args, **kwargs):
            if web_driver.current_url != "data:,":
                analyze_web_page(web_driver, mode="background", **config)
            return function(*args, **kwargs)

        return helper

    return userway_analysis_background_decorator


@contextmanager
def userway_analysis_background_watch(
    web_driver: WebDriver, **config: Unpack[UserwayAnalysisConfig]
):
    userway_analysis_background_decorator = userway_analysis_background_watcher(
        web_driver, **config
    )

    watched_web_driver = copy(web_driver)

    watched_execute = userway_analysis_background_decorator(web_driver.execute)
    setattr(watched_web_driver, "execute", watched_execute)

    yield watched_web_driver

    analyze_web_page(web_driver, mode="background", **config)
