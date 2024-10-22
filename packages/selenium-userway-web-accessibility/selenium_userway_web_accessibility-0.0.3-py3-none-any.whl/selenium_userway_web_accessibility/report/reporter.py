from os import makedirs, path

from .exception_reporter import report_runtime_exception
from .json_reporter import save_analysis_result_as_json
from .origin_page_reporter import save_origin_page_html


def save_report_artifacts(meta, report, html_content, screenshots_meta, errors) -> None:
    report_path = meta["config"]["reportPath"]

    try:
        prepare_report_folder(report_path)

        page_path = meta["htmlOrigin"].replace("..", report_path)
        save_origin_page_html(page_path, html_content)

        for report_item in report:
            for issue in report_item["issues"]:
                remove_issue_element(issue)
            for group in report_item["issuesGroup"].values():
                for issue in group:
                    remove_issue_element(issue)

        save_analysis_result_as_json(
            {"meta": meta, "violations": report, "errors": errors},
            report_path,
            screenshots_meta,
        )

    except Exception as exception:
        print("Exception during save_report_artifacts execution")
        report_runtime_exception(
            report_path=report_path,
            method_name="save_report_artifacts",
            exception=exception,
        )


def remove_issue_element(issue: dict) -> None:
    if "element" in issue:
        del issue["element"]


def prepare_report_folder(report_path: str) -> None:
    for folder in ["pages", "reports", "screenshots"]:
        folder_path = path.join(report_path, folder)
        makedirs(folder_path, exist_ok=True)
