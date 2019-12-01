"""
https://github.github.com/gfm/#thematic-breaks
"""
from pymarkdown.tokenized_markdown import TokenizedMarkdown

from .utils import assert_if_lists_different


def test_thematic_breaks_013():
    """
    Test case 013:  A line consisting of 0-3 spaces of indentation, followed by a sequence of three or more matching -, _, or * characters, each followed optionally by any number of spaces or tabs, forms a thematic break.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """***
---
___"""
    expected_tokens = ["[tbreak:*::***]", "[tbreak:-::---]", "[tbreak:_::___]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_014():
    """
    Test case 014:  (part a) Wrong characters:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """+++"""
    expected_tokens = ["[para:]", "[text:+++:]", "[end-para]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_015():
    """
    Test case 015:  (part b) Wrong characters:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """==="""
    expected_tokens = ["[para:]", "[text:===:]", "[end-para]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_016():
    """
    Test case 016:  Not enough characters:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """--
**
__"""
    expected_tokens = [
        "[para:]",
        "[text:--:]",
        "[text:**:]",
        "[text:__:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_017():
    """
    Test case 017:  One to three spaces indent are allowed:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """ ***
  ***
   ***"""
    expected_tokens = ["[tbreak:*: :***]", "[tbreak:*:  :***]", "[tbreak:*:   :***]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_018():
    """
    Test case 018:  (part a) Four spaces is too many:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """    ***"""
    expected_tokens = ["[para:    ]", "[text:***:]", "[end-para]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when code blocks are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_019():
    """
    Test case 019:  (part b) Four spaces is too many:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """Foo
    ***"""
    expected_tokens = ["[para:]", "[text:Foo:]", "[text:***:    ]", "[end-para]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when code blocks are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_020():
    """
    Test case 020:  More than three characters may be used:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """_____________________________________"""
    expected_tokens = ["[tbreak:_::_____________________________________]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_021():
    """
    Test case 021:  (part a) Spaces are allowed between the characters:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """ - - -"""
    expected_tokens = ["[tbreak:-: :- - -]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_022():
    """
    Test case 022:  (part b) Spaces are allowed between the characters:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """ **  * ** * ** * **"""
    expected_tokens = ["[tbreak:*: :**  * ** * ** * **]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_023():
    """
    Test case 023:  (part c) Spaces are allowed between the characters:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """-     -      -      -"""
    expected_tokens = ["[tbreak:-::-     -      -      -]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_024():
    """
    Test case 024:  Spaces are allowed at the end:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """- - - -    """
    expected_tokens = ["[tbreak:-::- - - -    ]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_025():
    """
    Test case 025:  However, no other characters may occur in the line:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """_ _ _ _ a

a------

---a---"""
    expected_tokens = [
        "[para:]",
        "[text:_ _ _ _ a:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:a------:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:---a---:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_026():
    """
    Test case 026:  It is required that all of the non-whitespace characters be the same. So, this is not a thematic break:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """ *-*"""
    expected_tokens = ["[para: ]", "[text:*-*:]", "[end-para]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when inlining-emphasis are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_027():
    """
    Test case 027:  Thematic breaks do not need blank lines before or after:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """- foo
***
- bar"""
    expected_tokens = [
        "[para:]",
        "[text:- foo:]",
        "[end-para]",
        "[tbreak:*::***]",
        "[para:]",
        "[text:- bar:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when lists are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_028():
    """
    Test case 028:  Thematic breaks can interrupt a paragraph:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """Foo
***
bar"""
    expected_tokens = [
        "[para:]",
        "[text:Foo:]",
        "[end-para]",
        "[tbreak:*::***]",
        "[para:]",
        "[text:bar:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_029():
    """
    Test case 029:  If a line of dashes that meets the above conditions for being a thematic break could also be interpreted as the underline of a setext heading, the interpretation as a setext heading takes precedence. Thus, for example, this is a setext heading, not a paragraph followed by a thematic break:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """Foo
---
bar"""
    expected_tokens = [
        "[para:]",
        "[text:Foo:]",
        "[end-para]",
        "[tbreak:-::---]",
        "[para:]",
        "[text:bar:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when setext are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_030():
    """
    Test case 030:  When both a thematic break and a list item are possible interpretations of a line, the thematic break takes precedence:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """* Foo
* * *
* Bar"""
    expected_tokens = [
        "[para:]",
        "[text:* Foo:]",
        "[end-para]",
        "[tbreak:*::* * *]",
        "[para:]",
        "[text:* Bar:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when lists are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


def test_thematic_breaks_031():
    """
    Test case 031:  If you want a thematic break in a list item, use a different bullet:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """- Foo
- * * *"""
    expected_tokens = ["[para:]", "[text:- Foo:]", "[text:- * * *:]", "[end-para]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when lists are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)