"""
Module to provide for an element that can be added to the stack.
"""
from pymarkdown.markdown_token import EndMarkdownToken


class StackToken:
    """
    Class to provide for an element to place on the stack.
    """

    stack_base_document = "document"
    stack_unordered_list = "ulist"
    stack_ordered_list = "olist"
    stack_html_block = "html-block"
    stack_block_quote = "block-quote"
    stack_fenced_code = "fcode-block"
    stack_indented_code = "icode-block"
    stack_paragraph = "para"

    def __init__(self, type_name, extra_data=None):
        self.type_name = type_name
        self.extra_data = extra_data

    def __str__(self):
        add_extra = ""
        if self.extra_data:
            add_extra = ":" + self.extra_data
        return "StackToken(" + self.type_name + add_extra + ")"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """
        Overrides the default implementation
        """
        if isinstance(other, StackToken):
            return (
                self.type_name == other.type_name
                and self.extra_data == other.extra_data
            )
        return NotImplemented

    def generate_close_token(self, extracted_whitespace=None):
        """
        Generate the token emitted to close off the current stack token
        """

        return EndMarkdownToken(self.type_name, extracted_whitespace, None)

    @property
    def is_document(self):
        """
        Is this stack token a document token?
        """
        return self.type_name == self.stack_base_document

    @property
    def is_list(self):
        """
        Is this stack token one of the list tokens?
        """
        return (
            self.type_name == self.stack_ordered_list
            or self.type_name == self.stack_unordered_list
        )

    @property
    def is_html_block(self):
        """
        Is this stack token a html block token?
        """
        return self.type_name == self.stack_html_block

    @property
    def is_code_block(self):
        """
        Is this stack token a fenced code block or indented code block token?
        """
        return self.is_fenced_code_block or self.is_indented_code_block

    @property
    def is_fenced_code_block(self):
        """
        Is this stack token a fenced code block token?
        """
        return self.type_name == self.stack_fenced_code

    @property
    def is_indented_code_block(self):
        """
        Is this stack token an indented code block token?
        """
        return self.type_name == self.stack_indented_code

    @property
    def is_block_quote(self):
        """
        Is this stack token a block quote token?
        """
        return self.type_name == self.stack_block_quote

    @property
    def is_paragraph(self):
        """
        Is this stack token a paragraph token?
        """
        return self.type_name == self.stack_paragraph


# pylint: disable=too-few-public-methods
class DocumentStackToken(StackToken):
    """
    Class to provide for a stack token at the root.
    """

    def __init__(self):
        StackToken.__init__(self, StackToken.stack_base_document)


# pylint: enable=too-few-public-methods


class ParagraphStackToken(StackToken):
    """
    Class to provide for a stack token for a paragraph.
    """

    def __init__(self):
        StackToken.__init__(self, StackToken.stack_paragraph)


class BlockQuoteStackToken(StackToken):
    """
    Class to provide for a stack token for a block quote.
    """

    def __init__(self):
        StackToken.__init__(self, StackToken.stack_block_quote)


class IndentedCodeBlockStackToken(StackToken):
    """
    Class to provide for a stack token for an indented code block.
    """

    def __init__(self):
        StackToken.__init__(self, StackToken.stack_indented_code)


class FencedCodeBlockStackToken(StackToken):
    """
    Class to provide for a stack token for a fenced code block.
    """

    def __init__(self, code_fence_character, fence_character_count):
        self.code_fence_character = code_fence_character
        self.fence_character_count = fence_character_count
        extra_data = code_fence_character + ":" + str(fence_character_count)
        StackToken.__init__(self, StackToken.stack_fenced_code, extra_data)


class ListStackToken(StackToken):
    """
    Class to provide for a stack token for a list.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self, type_name, indent_level, list_character, ws_before_marker, ws_after_marker
    ):
        self.indent_level = indent_level
        self.list_character = list_character
        self.ws_before_marker = ws_before_marker
        self.ws_after_marker = ws_after_marker
        extra_data = (
            str(indent_level)
            + ":"
            + list_character
            + ":"
            + str(ws_before_marker)
            + ":"
            + str(ws_after_marker)
        )
        StackToken.__init__(self, type_name, extra_data)

    # pylint: enable=too-many-arguments


class OrderedListStackToken(ListStackToken):
    """
    Class to provide for a stack token for an ordered list.
    """

    def __init__(self, indent_level, list_character, ws_before_marker, ws_after_marker):
        ListStackToken.__init__(
            self,
            StackToken.stack_ordered_list,
            indent_level,
            list_character,
            ws_before_marker,
            ws_after_marker,
        )


class UnorderedListStackToken(ListStackToken):
    """
    Class to provide for a stack token for an unordered list.
    """

    def __init__(self, indent_level, list_character, ws_before_marker, ws_after_marker):
        ListStackToken.__init__(
            self,
            StackToken.stack_unordered_list,
            indent_level,
            list_character,
            ws_before_marker,
            ws_after_marker,
        )


class HtmlBlockStackToken(StackToken):
    """
    Class to provide for a stack token for a html block.
    """

    def __init__(self, html_block_type, remaining_html_tag):
        self.html_block_type = html_block_type
        self.remaining_html_tag = remaining_html_tag
        extra_data = str(html_block_type) + ":" + str(remaining_html_tag)
        StackToken.__init__(self, StackToken.stack_html_block, extra_data)
