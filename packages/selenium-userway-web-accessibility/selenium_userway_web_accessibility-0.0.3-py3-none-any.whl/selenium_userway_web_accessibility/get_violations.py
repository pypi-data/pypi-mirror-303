from typing import Any, Dict


def is_violated(issue_type: str, report_incomplete: bool = False) -> bool:
    return issue_type == "violation" or (
        report_incomplete and issue_type in ["inapplicable", "incomplete"]
    )


def get_violations(full_report: Dict[str, Any], report_incomplete: bool = False):
    violations = []

    for record in full_report.values():
        filtered_issues = [
            issue
            for issue in record["issues"]
            if is_violated(issue["type"], report_incomplete)
        ]

        filtered_issues_group = {}
        for group, issues in record["issuesGroup"].items():
            issues_in_group = [
                issue
                for issue in issues
                if is_violated(issue["type"], report_incomplete)
            ]
            if issues_in_group:
                filtered_issues_group[group] = issues_in_group

        if filtered_issues or filtered_issues_group:
            issues_count = {
                **record["count"],
                "violation": (
                    (
                        record["count"]["violation"]
                        + record["count"]["inapplicable"]
                        + record["count"]["incomplete"]
                    )
                    if report_incomplete
                    else record["count"]["violation"]
                ),
            }

            violations.append(
                {
                    **record,
                    "count": issues_count,
                    "issues": filtered_issues,
                    "issuesGroup": filtered_issues_group,
                }
            )

    return violations
