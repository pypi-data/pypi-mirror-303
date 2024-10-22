import importlib.resources as pkg_resources
from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing_extensions import Unpack

from .report.reporter import report_runtime_exception
from .types import AnalyzeWebPageConfig
from .utils.snake_to_camel_dict import snake_to_camel_dict


def static_analysis_exists(web_driver: WebDriver) -> bool:
    return any(
        "StaticAnalysis" in (script.get_attribute("innerHTML") or "")
        for script in web_driver.find_elements(By.TAG_NAME, "script")
    )


def inject_static_analysis(web_driver: WebDriver, report_path: str) -> None:
    try:
        with pkg_resources.path(
            "selenium_userway_web_accessibility.assets", "static_analysis.iife.js"
        ) as static_analysis_iife_path:
            with open(static_analysis_iife_path, "r") as file:
                static_analysis_iife = file.read()

        web_driver.execute_script(
            """
            var script = document.createElement('script');
            script.textContent = arguments[0];
            document.head.appendChild(script);
            """,
            static_analysis_iife,
        )
    except Exception as exception:
        print("Exception during inject_static_analysis execution")
        report_runtime_exception(
            report_path=report_path,
            method_name="inject_static_analysis",
            exception=exception,
        )


def execute_static_analysis(
    web_driver: WebDriver, **config: Unpack[AnalyzeWebPageConfig]
) -> Tuple[dict, list]:
    if not static_analysis_exists(web_driver):
        inject_static_analysis(web_driver, config["report_path"])

    (report, analyze_errors, fatal_error) = web_driver.execute_script(
        """
        var staticAnalysisConfig = arguments[0];

        try {
            var analyze = window.StaticAnalysis.analyze;

            var analyzeErrors = [];
            staticAnalysisConfig.onRuleError = function(error) {
                analyzeErrors.push(error);
            };

            var report = await analyze(staticAnalysisConfig);

            return [report, analyzeErrors, undefined];
        } catch (fatalError) {
            return [{}, undefined, String(fatalError)];
        }
        """,
        snake_to_camel_dict(config),
    )

    if fatal_error:
        print("Fatal exception during static_analysis execution")
        report_runtime_exception(
            report_path=config["report_path"],
            method_name="static_analysis",
            exception=fatal_error,
        )

    return report, analyze_errors
