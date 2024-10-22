from typing import Any, Dict, List, Literal, Optional, TypedDict

from typing_extensions import NotRequired


class UserwayAnalysisException(Exception):
    pass


class RuleSpecificOptions(TypedDict):
    empty_alt_as_presentational_role: NotRequired[bool]


class UserwayAnalysisConfig(TypedDict):
    report_path: str
    strict: NotRequired[bool]
    element_screenshots: NotRequired[bool]
    page_screenshot: NotRequired[bool]
    report_incomplete: NotRequired[bool]
    include_rules: NotRequired[List[str]]
    exclude_rules: NotRequired[List[str]]
    level: NotRequired[Literal["A", "AA", "AAA"]]
    include_best_practices: NotRequired[bool]
    include_experimental: NotRequired[bool]
    ignore_urls: NotRequired[List[str]]
    ignore_selectors: NotRequired[List[str]]
    custom_tags: NotRequired[List[str]]
    root_selector: NotRequired[str]
    switch_off: NotRequired[bool]
    rule_specific_options: NotRequired[RuleSpecificOptions]
    on_rule_error: NotRequired[str]


class AnalyzeWebPageConfig(UserwayAnalysisConfig):
    mode: Literal["manual", "background"]


class UserwayAnalysisResult(TypedDict):
    report: Dict[str, Any]
    screenshots_meta: Optional[Dict[str, Any]]
    violations: List[Dict[str, Any]]
