import json
from difflib import SequenceMatcher
from typing import Any, Dict, List

import pytest
from deepdiff import DeepDiff

AllowedJSON = Dict[str, Any] | str | List[Dict[str, Any]] | List[str] | None

Result = Dict[str, Any]


def validate_field_match(expected: Result, actual: Result, field: str) -> None:
    expected_value = expected.get(field, None)
    actual_value = actual.get(field, None)

    # Treat empty string as none
    if actual_value == "":
        actual_value = None

    if expected_value is None and actual_value is None:
        pytest.skip(
            f"Field {field} is None in both expected and actual. Skipping this test."
        )

    if not check_match(expected_value, actual_value):
        raise ValueError(f"{expected_value} != {actual_value}")


def trim_strings(value: AllowedJSON) -> AllowedJSON:
    """Recursively trim strings in the given JSON structure."""
    if isinstance(value, dict):
        return {k: trim_strings(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [trim_strings(elem) for elem in value]  # type: ignore[return-value]
    elif isinstance(value, str):
        return value.strip()
    else:
        return value


def replace_empty_strings_with_none(value: AllowedJSON) -> AllowedJSON:
    """Recursively replace empty strings with None in the given JSON structure."""
    if isinstance(value, dict):
        return {k: replace_empty_strings_with_none(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [replace_empty_strings_with_none(elem) for elem in value]  # type: ignore[return-value]
    elif isinstance(value, str) and value == "":
        return None
    else:
        return value


def pre_process(value: AllowedJSON) -> AllowedJSON:
    value = format_new_lines(value)
    value = trim_strings(value)
    value = replace_empty_strings_with_none(value)
    return value


def validate_json_match(expected: AllowedJSON, actual: AllowedJSON) -> None:
    expected = pre_process(expected)
    actual = pre_process(actual)

    if isinstance(expected, Dict) and isinstance(actual, Dict):
        # TODO: Pass in schema in the backend and handle this OUTSIDE of tests
        # Adding missing keys in actual with None if they are expected to be None
        if isinstance(expected, dict) and isinstance(actual, dict):
            for key, value in expected.items():
                if value is None and key not in actual:
                    actual[key] = None

    diff = DeepDiff(
        expected,
        actual,
        ignore_order=True,
        report_repetition=True,
    )
    if diff:
        pretty_expected = json.dumps(expected, indent=4)
        pretty_actual = json.dumps(actual, indent=4)

        diff_msg = f"Actual: {pretty_actual}\nExpected: {pretty_expected}"
        raise ValueError(f"JSONEval mismatch!\n{diff_msg}")


def validate_end_url_match(expected: str, actual: str) -> None:
    if actual != expected:
        diff_msg = f"Actual URL:\t{actual}\nExpected URL:\t{expected}"
        pytest.fail(f"URLEval mismatch!\n{diff_msg}")


def format_new_lines(value: AllowedJSON) -> AllowedJSON:
    """Recursively replace newlines in strings with spaces."""
    if isinstance(value, dict):
        return {k: format_new_lines(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [format_new_lines(elem) for elem in value]  # type: ignore[return-value]
    elif isinstance(value, str):
        return value.replace("\n", " ")
    else:
        return value


def sanitize_string(input_str: str) -> str:
    return "".join(char for char in input_str if char.isalnum()).lower()


def is_string_similar(actual: str, expected: str, tolerance: int = 2) -> bool:
    if tolerance == 0:
        return actual == expected

    sanitized_actual = sanitize_string(actual)
    sanitized_expected = sanitize_string(expected)

    # Check if alphanumeric content matches
    if sanitized_actual != sanitized_expected:
        return False

    diff_count = native_count_differences(actual, expected)
    if diff_count <= tolerance:
        return True

    return SequenceMatcher(None, actual, expected).ratio() >= 0.8


def native_count_differences(actual: str, expected: str) -> int:
    non_alnum_actual = "".join(char for char in actual if not char.isalnum())
    non_alnum_expected = "".join(char for char in expected if not char.isalnum())
    # Compare the sequence of non-alphanumeric characters with a tolerance for
    # additional/missing characters
    diff_count = 0
    for char1, char2 in zip(non_alnum_actual, non_alnum_expected):
        if char1 != char2:
            diff_count += 1
    # Account for length difference if one sequence is longer than the other
    length_diff = abs(len(non_alnum_actual) - len(non_alnum_expected))
    diff_count += length_diff
    return diff_count


def check_match(expected_value: Any, actual_value: Any) -> bool:
    if isinstance(expected_value, str) and isinstance(actual_value, str):
        return is_string_similar(expected_value, actual_value)
    else:
        return expected_value == actual_value
