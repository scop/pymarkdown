"""
Module to provide tests related to the MD037 rule.
"""
from test.markdown_scanner import MarkdownScanner

import pytest


@pytest.mark.rules
def test_md037_good_valid_emphasis():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md037/good_valid_emphasis.md",
    ]

    expected_return_code = 0
    expected_output = ""
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md037_bad_surrounding_emphasis():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md037/bad_surrounding_emphasis.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md037/bad_surrounding_emphasis.md:1:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_emphasis.md:3:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_emphasis.md:5:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_emphasis.md:7:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md037_bad_leading_emphasis():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md037/bad_leading_emphasis.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md037/bad_leading_emphasis.md:1:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_leading_emphasis.md:3:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_leading_emphasis.md:5:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_leading_emphasis.md:7:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md037_bad_trailing_emphasis():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md037/bad_trailing_emphasis.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md037/bad_trailing_emphasis.md:1:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_trailing_emphasis.md:3:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_trailing_emphasis.md:5:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_trailing_emphasis.md:7:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md037_bad_surrounding_emphasis_multiline():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md037/bad_surrounding_emphasis_multiline.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md037/bad_surrounding_emphasis_multiline.md:1:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_emphasis_multiline.md:4:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_emphasis_multiline.md:7:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_emphasis_multiline.md:10:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md037_bad_surrounding_empahsis_setext():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md037/bad_surrounding_empahsis_setext.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md037/bad_surrounding_empahsis_setext.md:1:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_empahsis_setext.md:4:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_empahsis_setext.md:7:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_empahsis_setext.md:10:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md037_bad_surrounding_empahsis_atx():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md037/bad_surrounding_empahsis_atx.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md037/bad_surrounding_empahsis_atx.md:1:13: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_empahsis_atx.md:3:14: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_empahsis_atx.md:5:14: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_empahsis_atx.md:7:14: MD037: Spaces inside emphasis markers (no-space-in-emphasis)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md037_bad_surrounding_emphasis_containers():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md037/bad_surrounding_emphasis_containers.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md037/bad_surrounding_emphasis_containers.md:1:12: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_emphasis_containers.md:3:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)\n"
        + "test/resources/rules/md037/bad_surrounding_emphasis_containers.md:5:11: MD037: Spaces inside emphasis markers (no-space-in-emphasis)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md037_good_emphasis_with_code_span():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md037/good_emphasis_with_code_span.md",
    ]

    expected_return_code = 0
    expected_output = ""
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )
