import datetime

from selenium.webdriver.remote.webdriver import WebDriver
from typing_extensions import Unpack

from .get_violations import get_violations
from .report.origin_page_reporter import generate_origin_page_filename
from .report.reporter import save_report_artifacts
from .report.screenshot_reporter import save_screenshots
from .static_analysis import execute_static_analysis
from .types import AnalyzeWebPageConfig, UserwayAnalysisException, UserwayAnalysisResult
from .utils.is_ignore_url import is_ignore_url


def analyze_web_page(
    web_driver: WebDriver,
    **config: Unpack[AnalyzeWebPageConfig],
) -> UserwayAnalysisResult:
    if is_ignore_url(web_driver.current_url, config.get("ignore_urls", [])):
        return {
            "report": {"result": {}, "config": {}},
            "screenshots_meta": None,
            "violations": [],
        }

    html_content = web_driver.page_source

    (report, analyze_errors) = execute_static_analysis(web_driver, **config)

    violations = get_violations(
        report["result"], config.get("report_incomplete", False)
    )

    screenshots_meta = save_screenshots(web_driver, violations, config)

    url = web_driver.current_url
    viewport = web_driver.get_window_rect()

    save_report_artifacts(
        meta={
            "config": report["config"],
            "framework": "Selenium",
            "version": "2",
            "browser": web_driver.capabilities["browserName"],
            "mode": config["mode"],
            "date": datetime.datetime.now(datetime.UTC).isoformat(),
            "htmlOrigin": f"../pages/{generate_origin_page_filename(url)}",
            "device": "mobile" if viewport["width"] < 768 else "desktop",
            "pageScreenshot": screenshots_meta.get("page", {}).get("pageScreenshot"),
            "customTags": config.get("custom_tags", []),
            "test": [],
            "relativePath": "",
            "viewport": viewport,
            "url": url,
        },
        report=list(report["result"].values()),
        html_content=html_content,
        screenshots_meta=screenshots_meta,
        errors=analyze_errors,
    )

    if config.get("strict", False) and violations:
        raise UserwayAnalysisException(f"[Userway]: Found {len(violations)} violations")

    return {
        "report": report,
        "screenshots_meta": screenshots_meta,
        "violations": violations,
    }
