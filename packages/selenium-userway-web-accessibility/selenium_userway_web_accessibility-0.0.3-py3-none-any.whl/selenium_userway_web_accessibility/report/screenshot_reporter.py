import os
import time
from typing import Any, Dict, List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from ..utils.base36_encode import base36_encode
from .reporter import prepare_report_folder, report_runtime_exception


def generate_screenshot_filename(rule_id: str, idx: int) -> str:
    timestamp_base36 = base36_encode(int(time.time()))
    return f"{rule_id}-{idx}-{timestamp_base36}.jpg"


def save_page_screenshot(web_driver: WebDriver, report_path: str) -> dict[str, str]:
    timestamp_base36 = base36_encode(int(time.time()))
    screenshot_name = f"screenshots/page-screenshot-{timestamp_base36}.jpg"

    screenshot_path = os.path.join(report_path, screenshot_name)

    try:
        web_driver.save_screenshot(screenshot_path)
    except Exception as exception:
        print("Exception during save_screenshot execution")
        report_runtime_exception(
            report_path=report_path,
            method_name="save_screenshot",
            exception=exception,
        )

    return {"pageScreenshot": f"../{screenshot_name}"}


def save_screenshots(
    web_driver: WebDriver,
    violations: List[Dict[str, Any]],
    config: dict,
):
    prepare_report_folder(config["report_path"])
    metadata = {}

    if config.get("page_screenshot", False):
        metadata["page"] = save_page_screenshot(web_driver, config["report_path"])

    if config.get("element_screenshots", False):
        for violation in violations:
            idx = 1
            selectors = [issue["selector"] for issue in violation["issues"]]

            for group in violation["issuesGroup"].values():
                for issue in group:
                    selectors.append(issue["selector"])

            for selector in selectors:
                if ">>>" in selector:
                    continue

                element = web_driver.find_element(By.CSS_SELECTOR, selector)

                if element.rect["width"] > 0 and element.rect["height"] > 0:
                    screenshot_name = generate_screenshot_filename(
                        violation["ruleId"], idx
                    )
                    idx += 1

                    file_path = f"screenshots/{screenshot_name}"

                    if violation["ruleId"] not in metadata:
                        metadata[violation["ruleId"]] = {}

                    metadata[violation["ruleId"]][selector] = f"../{file_path}"
                    screenshot_path = os.path.join(config["report_path"], file_path)

                    try:
                        element.screenshot(screenshot_path)
                    except Exception as exception:
                        print("Exception during save_screenshot execution")
                        report_runtime_exception(
                            report_path=config["report_path"],
                            method_name="save_screenshot",
                            exception=exception,
                        )

    return metadata
