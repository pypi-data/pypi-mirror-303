from selenium.webdriver.remote.webdriver import WebDriver
from typing_extensions import Unpack

from .analysis import analyze_web_page
from .types import UserwayAnalysisConfig, UserwayAnalysisResult


def userway_analysis(
    web_driver: WebDriver, **config: Unpack[UserwayAnalysisConfig]
) -> UserwayAnalysisResult:
    return analyze_web_page(web_driver, mode="manual", **config)
