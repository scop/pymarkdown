"""
Module to provide tests related to the MD039 rule.
"""
from test.markdown_scanner import MarkdownScanner

import pytest


@pytest.mark.rules
def test_md039_good_inline_link():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/good_inline_link.md",
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
def test_md039_bad_inline_link_trailing_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_inline_link_trailing_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_inline_link_trailing_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_bad_inline_link_leading_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_inline_link_leading_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_inline_link_leading_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_bad_inline_link_both_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_inline_link_both_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_inline_link_both_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_good_full_link():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/good_full_link.md",
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
def test_md039_bad_full_link_both_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_full_link_both_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_full_link_both_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_good_collapsed_link():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/good_collapsed_link.md",
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
def test_md039_bad_collapsed_link_both_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_collapsed_link_both_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_collapsed_link_both_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_good_shortcut_link():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/good_shortcut_link.md",
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
def test_md039_bad_shortcut_link_both_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_shortcut_link_both_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_shortcut_link_both_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_good_inline_image():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/good_inline_image.md",
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
def test_md039_bad_inline_image_trailing_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_inline_image_trailing_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_inline_image_trailing_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_bad_inline_image_leading_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_inline_image_leading_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_inline_image_leading_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_bad_inline_image_both_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_inline_image_both_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_inline_image_both_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_good_full_image():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/good_full_image.md",
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
def test_md039_bad_full_image_both_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_full_image_both_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_full_image_both_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_good_collapsed_image():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/good_collapsed_image.md",
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
def test_md039_bad_collapsed_image_both_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_collapsed_image_both_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_collapsed_image_both_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md039_good_shortcut_image():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/good_shortcut_image.md",
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
def test_md039_bad_shortcut_image_both_space():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "scan",
        "test/resources/rules/md039/bad_shortcut_image_both_space.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md039/bad_shortcut_image_both_space.md:2:1: "
        + "MD039: Spaces inside link text (no-space-in-links)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )
