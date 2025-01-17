"""
Module to provide tests related to the MD044 rule.
"""
from test.markdown_scanner import MarkdownScanner

import pytest

# pylint: disable=too-many-lines


@pytest.mark.rules
def test_md044_bad_configuration_names():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=$#1",
        "--strict-config",
        "scan",
        "test/resources/rules/md044/good_paragraph_text.md",
    ]

    expected_return_code = 1
    expected_output = ""
    expected_error = (
        "BadPluginError encountered while configuring plugins:\n"
        + "The value for property 'plugins.md044.names' must be of type 'str'."
    )

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bad_configuration_names_empty_elements():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=,,",
        "--strict-config",
        "scan",
        "test/resources/rules/md044/good_paragraph_text.md",
    ]

    expected_return_code = 1
    expected_output = ""
    expected_error = (
        "BadPluginError encountered while configuring plugins:\n"
        + "Elements in the comma-separated list cannot be empty."
    )

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bad_configuration_names_repeated_elements():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=one,two,One",
        "--strict-config",
        "scan",
        "test/resources/rules/md044/good_paragraph_text.md",
    ]

    expected_return_code = 1
    expected_output = ""
    expected_error = (
        "BadPluginError encountered while configuring plugins:\n"
        + "Element `One` is already present in the list as `one`."
    )

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bad_configuration_code_blocks():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.code_blocks=one",
        "--strict-config",
        "scan",
        "test/resources/rules/md044/good_paragraph_text.md",
    ]

    expected_return_code = 1
    expected_output = ""
    expected_error = (
        "BadPluginError encountered while configuring plugins:\n"
        + "The value for property 'plugins.md044.code_blocks' must be of type 'bool'."
    )

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_paragraph_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=paragraph",
        "scan",
        "test/resources/rules/md044/good_paragraph_text.md",
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
def test_md044_bad_paragraph_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_paragraph_text.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_paragraph_text.md:1:11: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_paragraph_text_prefix():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_paragraph_text_prefix.md",
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
def test_md044_good_paragraph_text_suffix():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_paragraph_text_suffix.md",
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
def test_md044_bad_paragraph_text_start():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_paragraph_text_start.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_paragraph_text_start.md:1:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bad_paragraph_text_end():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_paragraph_text_end.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_paragraph_text_end.md:1:20: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bad_paragraph_text_followed_non_alpha():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_paragraph_text_followed_non_alpha.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_paragraph_text_followed_non_alpha.md:1:11: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bar_paragraph_text_multiples():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_paragraph_text_multiples.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_paragraph_text_multiples.md:1:11: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_paragraph_text_multiples.md:1:26: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bar_paragraph_text_multiples_on_multiple_lines():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_paragraph_text_multiples_on_multiple_lines.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_paragraph_text_multiples_on_multiple_lines.md:1:33: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_paragraph_text_multiples_on_multiple_lines.md:3:39: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bar_atx_heading_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_atx_heading_text.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_atx_heading_text.md:1:27: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_atx_heading_text.md:3:8: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bad_setext_heading_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_setext_heading_text.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_setext_heading_text.md:1:25: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_setext_heading_text.md:4:8: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bad_indented_code_block_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_indented_code_block_text.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_indented_code_block_text.md:1:27: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_indented_code_block_text.md:3:12: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_bad_fenced_code_block_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_fenced_code_block_text.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_fenced_code_block_text.md:1:27: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_fenced_code_block_text.md:4:8: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_indented_code_block_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "--set",
        "plugins.md044.code_blocks=$!False",
        "--strict-config",
        "scan",
        "test/resources/rules/md044/good_indented_code_block_text.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_indented_code_block_text.md:1:27: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_fenced_code_block_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "--set",
        "plugins.md044.code_blocks=$!False",
        "--strict-config",
        "scan",
        "test/resources/rules/md044/good_fenced_code_block_text.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_fenced_code_block_text.md:1:27: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_html_block_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_html_block_text.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_html_block_text.md:1:27: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_html_block_text.md:4:8: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_block_quote_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_block_quote_text.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_block_quote_text.md:1:27: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_block_quote_text.md:3:10: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_code_span_text():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_code_span_text.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_code_span_text.md:1:27: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_code_span_text.md:3:7: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_code_span_text_multiple_lines():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_code_span_text_multiple_lines.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_code_span_text_multiple_lines.md:1:27: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_code_span_text_multiple_lines.md:3:7: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_code_span_text_multiple_lines.md:4:6: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_inline_link():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_inline_link.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_inline_link.md:1:4: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_inline_link.md:1:41: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_inline_link_multiple_lines_x():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_inline_link_multiple_lines.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_inline_link_multiple_lines.md:1:4: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_inline_link_multiple_lines.md:3:2: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_inline_link_multiple_lines_two():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_inline_link_multiple_lines_two.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_inline_link_multiple_lines_two.md:1:4: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_inline_link_multiple_lines_two.md:4:13: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_inline_image():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_inline_image.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_inline_image.md:1:5: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_inline_image.md:1:42: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_inline_image_multiple_lines():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_inline_image_multiple_lines.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_inline_image_multiple_lines.md:1:5: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_inline_image_multiple_lines.md:3:2: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_inline_image_multiple_lines_two():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_inline_image_multiple_lines_two.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_inline_image_multiple_lines_two.md:1:5: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_inline_image_multiple_lines_two.md:4:13: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_full_link():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_full_link.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_full_link.md:2:4: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_full_link.md:5:16: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_full_link_multiple():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_full_link_multiple.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_full_link_multiple.md:3:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_full_link_multiple.md:9:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_full_image():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_full_image.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_full_image.md:2:5: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_full_image.md:5:16: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_full_image_multiple():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_full_image_multiple.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_full_image_multiple.md:3:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_full_image_multiple.md:9:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_collapsed_link():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_collapsed_link.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_collapsed_link.md:3:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_collapsed_link.md:7:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_collapsed_link.md:7:21: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_collapsed_link_multiple():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_collapsed_link_multiple.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_collapsed_link_multiple.md:3:6: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_collapsed_link_multiple.md:7:6: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_collapsed_link_multiple.md:8:5: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_collapsed_image():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_collapsed_image.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_collapsed_image.md:3:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_collapsed_image.md:7:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_collapsed_image.md:7:21: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )


@pytest.mark.rules
def test_md044_good_collapsed_image_multiple():
    """
    Test to make sure we get the expected behavior after scanning a good file from the
    test/resources/rules/md004 directory that has consistent asterisk usage on a single
    level list.
    """

    # Arrange
    scanner = MarkdownScanner()
    supplied_arguments = [
        "--set",
        "plugins.md044.names=ParaGraph",
        "scan",
        "test/resources/rules/md044/good_collapsed_image_multiple.md",
    ]

    expected_return_code = 1
    expected_output = (
        "test/resources/rules/md044/good_collapsed_image_multiple.md:3:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_collapsed_image_multiple.md:7:1: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)\n"
        + "test/resources/rules/md044/good_collapsed_image_multiple.md:8:5: "
        + "MD044: Proper names should have the correct capitalization "
        + "[Expected: ParaGraph; Actual: paragraph] (proper-names)"
    )
    expected_error = ""

    # Act
    execute_results = scanner.invoke_main(arguments=supplied_arguments)

    # Assert
    execute_results.assert_results(
        expected_output, expected_error, expected_return_code
    )
