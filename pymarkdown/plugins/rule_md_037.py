"""
Module to implement a plugin that looks for hard tabs in the files.
"""
from pymarkdown.plugin_manager import Plugin, PluginDetails


class RuleMd037(Plugin):
    """
    Class to implement a plugin that looks for hard tabs in the files.
    """

    def __init__(self):
        super().__init__()
        self.__block_stack = None
        self.__start_emphasis_token = None
        self.__emphasis_token_list = []

    def get_details(self):
        """
        Get the details for the plugin.
        """
        return PluginDetails(
            # whitespace, emphasis
            plugin_name="no-space-in-emphasis",
            plugin_id="MD037",
            plugin_enabled_by_default=True,
            plugin_description="Spaces inside emphasis markers",
            plugin_version="0.5.0",
            plugin_interface_version=1,
            plugin_url="https://github.com/jackdewinter/pymarkdown/blob/main/docs/rules/rule_md037.md",
        )  # https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md037---spaces-inside-emphasis-markers

    def starting_new_file(self):
        """
        Event that the a new file to be scanned is starting.
        """
        self.__block_stack = []
        self.__start_emphasis_token = None
        self.__emphasis_token_list = []

    def next_token(self, context, token):
        """
        Event that a new token is being processed.
        """
        if self.__start_emphasis_token:
            if (
                token.is_paragraph_end
                or token.is_setext_heading_end
                or token.is_atx_heading_end
            ):
                del self.__block_stack[-1]
                self.__start_emphasis_token = None
                self.__emphasis_token_list = []
            elif (
                token.is_text
                and token.token_text == self.__start_emphasis_token.token_text
            ):
                # if (
                #     # len(self.__emphasis_token_list) == 1
                #     # and self.__emphasis_token_list[0].is_text and
                #     #self.__emphasis_token_list[0].token_text
                #     #!= self.__emphasis_token_list[0].token_text.strip()
                #     True
                # ):
                self.report_next_token_error(context, self.__start_emphasis_token)

                self.__start_emphasis_token = None
                self.__emphasis_token_list = []
            else:
                self.__emphasis_token_list.append(token)
        elif token.is_paragraph or token.is_setext_heading or token.is_atx_heading:
            self.__block_stack.append(token)
        elif token.is_paragraph_end or token.is_setext_heading_end:
            del self.__block_stack[-1]
        elif (
            token.is_text
            and self.__block_stack
            and (
                self.__block_stack[-1].is_paragraph
                or self.__block_stack[-1].is_setext_heading
                or self.__block_stack[-1].is_atx_heading
            )
        ):
            if token.token_text in ("*", "**", "_", "__"):
                self.__start_emphasis_token = token
