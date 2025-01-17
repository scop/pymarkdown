# Rule - MD044

| Aliases |
| --- |
| `md044` |
| `proper-names` |

## Summary

Fenced code blocks should have a language specified.

## Reasoning

The main reason for this rule is consistency. Quite often, when writing
groups of documents, there are certain proper nouns that have specific
capitalization.  A good example of this is this project, the
[PyMarkdown](https://github.com/jackdewinter/pymarkdown).  It very specifically
has the `P` and `M` characters captialized.  This rule enforces that
captialization.

## Examples

### Failure Scenarios

This rule triggers when this rule finds any standalone instance of a
word specified in the `names` configuration value that does not have
a correct capitalization.  Assuming `names` is set to `ParaGraph`, then
the following example will trigger this rule:

````Markdown
this is a paragraph.
````

There are also special rules for how this rule triggers on links and
images.  For inline links and inline images, this rule triggers on
matching text in the link label and the link title, but not the link URI:

````Markdown
this is a [paragraph](/paragraph "a paragraph item") link.
````

For that example, the rule triggers on the first occurence of
paragraph (link label) and the last occurrence (link title).

For every other type of link and image, this rule triggers on
any occurence in the link label.

![collapsed
paragraph][]
link

[collapsed
paragraph]: /url "a paragraph title"

Since any link title is physically
associated with the Link Reference Definition, any occurence found
in the link title triggers this rule.

### Correct Scenarios

This rule does not trigger if it cannot find any of the words present
in the the `names` configuration value.  This rule also does not trigger
if any of those words are found, but are correctly capitalized.
Assuming `names` is set to `ParaGraph`, then the following example will not trigger this rule:

````Markdown
this is a ParaGraph.
````

In addition, this rule does not trigger if the found text is not an
isolated word within the text.  For example, even if `names` is set to
`ParaGraph`, the following lines of text will not trigger this rule:

````Markdown
this is a paragraphing
this is a reparagraph
````

## Configuration

| Prefixes |
| --- |
| `plugins.md044.` |
| `plugins.proper-names.` |

| Value Name | Type | Default | Description |
| -- | -- | -- | -- |
| `enabled` | `boolean` | `True` | Whether the plugin rule is enabled by default. |
| `names`   | `string` | None | Comma-seperated list of proper nouns to preserve capitalization on. |
| `code_blocks` | `boolean` | `True` | Search in Fenced Code Block elements and Indented Code Block elements. |

## Origination of Rule

This rule is largely inspired by the MarkdownLint rule
[MD044](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md044---proper-names-should-have-the-correct-capitalization).
