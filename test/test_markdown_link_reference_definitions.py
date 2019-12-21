"""
https://github.github.com/gfm/#link-reference-definitions
"""
import pytest

from pymarkdown.tokenized_markdown import TokenizedMarkdown

from .utils import assert_if_lists_different


@pytest.mark.skip
def test_link_reference_definitions_161():
    """
    Test case 161:  (part 1) A link reference definition does not correspond to a structural element of a document.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /url "title"

[foo]"""
    expected_tokens = [
        "[para:]",
        '[text:[foo]: /url "title":]',
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_162():
    """
    Test case 162:  (part 2) A link reference definition does not correspond to a structural element of a document.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    # pylint: disable=trailing-whitespace
    source_markdown = """   [foo]: 
      /url  
           'the title'  

[foo]"""
    expected_tokens = [
        "[para:   ]",
        "[text:[foo]: :]",
        "[text:/url  :      ]",
        "[text:'the title'  :           ]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_163():
    """
    Test case 163:  (part 3) A link reference definition does not correspond to a structural element of a document.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[Foo*bar\\]]:my_(url) 'title (with parens)'

[Foo*bar\\]]"""
    expected_tokens = [
        "[para:]",
        "[text:[Foo*bar\\]]:my_(url) 'title (with parens)':]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[Foo*bar\\]]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_164():
    """
    Test case 164:  (part 4) A link reference definition does not correspond to a structural element of a document.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[Foo bar]:
<my url>
'title'

[Foo bar]"""
    expected_tokens = [
        "[para:]",
        "[text:[Foo bar]::]",
        "[text:<my url>:]",
        "[text:'title':]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[Foo bar]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_165():
    """
    Test case 165:  The title may extend over multiple lines:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /url '
title
line1
line2
'

[foo]"""
    expected_tokens = [
        "[para:]",
        "[text:[foo]: /url ':]",
        "[text:title:]",
        "[text:line1:]",
        "[text:line2:]",
        "[text:':]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_166():
    """
    Test case 166:  However, it may not contain a blank line:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /url 'title

with blank line'

[foo]"""
    expected_tokens = [
        "[para:]",
        "[text:[foo]: /url 'title:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:with blank line':]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_167():
    """
    Test case 167:  The title may be omitted:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]:
/url

[foo]"""
    expected_tokens = [
        "[para:]",
        "[text:[foo]::]",
        "[text:/url:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_168():
    """
    Test case 168:  The link destination may not be omitted:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]:

[foo]"""
    expected_tokens = [
        "[para:]",
        "[text:[foo]::]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_169():
    """
    Test case 169:  However, an empty link destination may be specified using angle brackets:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: <>

[foo]"""
    expected_tokens = [
        "[para:]",
        "[text:[foo]: <>:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_170():
    """
    Test case 170:  The title must be separated from the link destination by whitespace:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: <>

[foo]"""
    expected_tokens = [
        "[para:]",
        "[text:[foo]: <>:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_171():
    """
    Test case 171:  Both title and destination can contain backslash escapes and literal backslashes:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /url\\bar\\*baz "foo\\"bar\\baz"

[foo]"""
    expected_tokens = [
        "[para:]",
        '[text:[foo]: /url\\bar\\*baz "foo\\"bar\\baz":]',
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_172():
    """
    Test case 172:  A link can come before its corresponding definition:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]

[foo]: url"""
    expected_tokens = [
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]: url:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_173():
    """
    Test case 173:  If there are several matching definitions, the first one takes precedence:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]

[foo]: first
[foo]: second"""
    expected_tokens = [
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]: first:]",
        "[text:[foo]: second:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_174():
    """
    Test case 174:  (part 1) As noted in the section on Links, matching of labels is case-insensitive (see matches).
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[FOO]: /url

[Foo]"""
    expected_tokens = [
        "[para:]",
        "[text:[FOO]: /url:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[Foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_175():
    """
    Test case 175:  (part 2) As noted in the section on Links, matching of labels is case-insensitive (see matches).
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[ΑΓΩ]: /φου

[αγω]"""
    expected_tokens = [
        "[para:]",
        "[text:[ΑΓΩ]: /φου:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[αγω]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_176():
    """
    Test case 176:  Here is a link reference definition with no corresponding link. It contributes nothing to the document.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /url"""
    expected_tokens = ["[para:]", "[text:[foo]: /url:]", "[end-para]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_177():
    """
    Test case 177:  Here is another one:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[
foo
]: /url
bar"""
    expected_tokens = [
        "[para:]",
        "[text:[:]",
        "[text:foo:]",
        "[text:]: /url:]",
        "[text:bar:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_178():
    """
    Test case 178:  This is not a link reference definition, because there are non-whitespace characters after the title:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /url "title" ok"""
    expected_tokens = ["[para:]", '[text:[foo]: /url "title" ok:]', "[end-para]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_179():
    """
    Test case 179:  This is a link reference definition, but it has no title:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /url
"title" ok"""
    expected_tokens = [
        "[para:]",
        "[text:[foo]: /url:]",
        '[text:"title" ok:]',
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_180():
    """
    Test case 180:  This is not a link reference definition, because it is indented four spaces:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """    [foo]: /url "title"

[foo]"""
    expected_tokens = [
        "[icode-block:    ]",
        '[text:[foo]: /url "title":]',
        "[end-icode-block]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_181():
    """
    Test case 181:  This is not a link reference definition, because it occurs inside a code block:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """```
[foo]: /url
```

[foo]"""
    expected_tokens = [
        "[fcode-block:`:3::::]",
        "[text:[foo]: /url:]",
        "[end-fcode-block:]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_182():
    """
    Test case 182:  A link reference definition cannot interrupt a paragraph.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """Foo
[bar]: /baz

[bar]"""
    expected_tokens = [
        "[para:]",
        "[text:Foo:]",
        "[text:[bar]: /baz:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[bar]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_183():
    """
    Test case 183:  (part 1) However, it can directly follow other block elements, such as headings and thematic breaks, and it need not be followed by a blank line.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """# [Foo]
[foo]: /url
> bar"""
    expected_tokens = [
        "[atx:1:[Foo]:: ::]",
        "[para:]",
        "[text:[foo]: /url:]",
        "[end-para]",
        "[block-quote:]",
        "[para:]",
        "[text:bar:]",
        "[end-para]",
        "[end-block-quote]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_184():
    """
    Test case 184:  (part 2) However, it can directly follow other block elements, such as headings and thematic breaks, and it need not be followed by a blank line.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /url
bar
===
[foo]"""
    expected_tokens = [
        "[setext:=:]",
        "[text:[foo]: /url:]",
        "[text:bar:]",
        "[end-setext::]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_185():
    """
    Test case 185:  (part 3) However, it can directly follow other block elements, such as headings and thematic breaks, and it need not be followed by a blank line.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /url
===
[foo]"""
    expected_tokens = [
        "[setext:=:]",
        "[text:[foo]: /url:]",
        "[end-setext::]",
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_186():
    """
    Test case 186:  Several link reference definitions can occur one after another, without intervening blank lines.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /foo-url "foo"
[bar]: /bar-url
  "bar"
[baz]: /baz-url

[foo],
[bar],
[baz]"""
    expected_tokens = [
        "[para:]",
        '[text:[foo]: /foo-url "foo":]',
        "[text:[bar]: /bar-url:]",
        '[text:"bar":  ]',
        "[text:[baz]: /baz-url:]",
        "[end-para]",
        "[BLANK:]",
        "[para:]",
        "[text:[foo],:]",
        "[text:[bar],:]",
        "[text:[baz]:]",
        "[end-para]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_187():
    """
    Test case 187:  Link reference definitions can occur inside block containers, like lists and block quotations. They affect the entire document, not just the container in which they are defined:
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]

> [foo]: /url"""
    expected_tokens = [
        "[para:]",
        "[text:[foo]:]",
        "[end-para]",
        "[BLANK:]",
        "[block-quote:]",
        "[para:]",
        "[text:[foo]: /url:]",
        "[end-para]",
        "[end-block-quote]",
    ]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)


@pytest.mark.skip
def test_link_reference_definitions_188():
    """
    Test case 188:  Whether something is a link reference definition is independent of whether the link reference it defines is used in the document.
    """

    # Arrange
    tokenizer = TokenizedMarkdown()
    source_markdown = """[foo]: /url"""
    expected_tokens = ["[para:]", "[text:[foo]: /url:]", "[end-para]"]

    # Act
    actual_tokens = tokenizer.transform(source_markdown)

    # Assert
    # TODO Expect this to fail when link references are implemented
    assert_if_lists_different(expected_tokens, actual_tokens)