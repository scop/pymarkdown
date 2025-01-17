"""
Module to provide for recognizing a strikethrough sequence.
"""

from pymarkdown.extension_impl import ExtensionDetails


# pylint: disable=too-few-public-methods
class MarkdownStrikeThroughExtension:
    """
    Extension to implement the strikethrough extension.
    """

    @classmethod
    def get_details(cls):
        """
        Get the details for the extension.
        """
        return ExtensionDetails(
            extension_id="markdown-strikethrough",
            extension_name="Markdown Strikethrough",
            extension_description="Allows parsing of Markdown strikethrough.",
            extension_enabled_by_default=False,
            extension_version="0.0.0",
            extension_interface_version=1,
            extension_url="https://github.github.com/gfm/#strikethrough-extension-",
            extension_configuration=None,
        )


# pylint: enable=too-few-public-methods
