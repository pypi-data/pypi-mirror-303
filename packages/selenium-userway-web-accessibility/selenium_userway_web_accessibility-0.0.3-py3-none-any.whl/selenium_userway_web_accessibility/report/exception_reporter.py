import os

from ..utils.get_formatted_date import get_formatted_date


def report_runtime_exception(
    report_path: str, method_name: str, exception: Exception
) -> None:
    timestamp = get_formatted_date()

    folder_path = os.path.join(report_path, "errors")
    os.makedirs(folder_path, exist_ok=True)

    log_file_path = os.path.join(report_path, f"errors/userway-debug-{timestamp}.log")
    exception_message = f'{timestamp}:: {method_name} failed with: "{exception}"'

    with open(log_file_path, "w") as file:
        file.write(exception_message)
