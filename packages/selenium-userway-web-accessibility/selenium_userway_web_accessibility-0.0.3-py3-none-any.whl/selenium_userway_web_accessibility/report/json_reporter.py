import json
import os
import time
from typing import Any, Dict, Optional

from ..utils.base36_encode import base36_encode


def generate_json_report_filename() -> str:
    timestamp_base36 = base36_encode(int(time.time()))
    return f"uw-a11y-report-{timestamp_base36}.json"


def get_screenshot_path(
    rule_id: str, selector: str, screenshots_metadata: Optional[Dict[str, Any]]
) -> Optional[str]:
    if screenshots_metadata and rule_id in screenshots_metadata:
        return screenshots_metadata[rule_id].get(selector)
    return None


def get_json_report(
    report_fields: Dict[str, Any], screenshots_metadata: Optional[Dict[str, Any]] = None
) -> dict:
    meta = report_fields["meta"]
    violations = report_fields["violations"]
    errors = report_fields["errors"]

    for violation in violations:
        grouped_issues = []
        for group in violation["issuesGroup"].values():
            grouped_issues.extend(group)
        for issue in violation["issues"] + grouped_issues:
            screenshot_path = get_screenshot_path(
                violation["ruleId"], issue["selector"], screenshots_metadata
            )

            if screenshot_path:
                issue["screenshotPath"] = screenshot_path

    return {
        "meta": meta,
        "violations": violations,
        "errors": errors,
    }


def save_analysis_result_as_json(
    report_source: dict, report_path: str, screenshots_meta: Optional[dict] = None
) -> None:
    path = os.path.join(report_path, "reports", generate_json_report_filename())
    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            get_json_report(report_source, screenshots_meta),
            file,
            ensure_ascii=False,
            indent=2,
        )
