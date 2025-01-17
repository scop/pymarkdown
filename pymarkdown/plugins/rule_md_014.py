"""
Module to implement a plugin that looks for hard tabs in the files.
"""
from pymarkdown.plugin_manager import Plugin, PluginDetails


class RuleMd014(Plugin):
    """
    Class to implement a plugin that looks for hard tabs in the files.
    """

    def __init__(self):
        super().__init__()
        self.__in_code_block = None

    def get_details(self):
        """
        Get the details for the plugin.
        """
        return PluginDetails(
            # code
            plugin_name="commands-show-output",
            plugin_id="MD014",
            plugin_enabled_by_default=True,
            plugin_description="Dollar signs used before commands without showing output",
            plugin_version="0.5.0",
            plugin_interface_version=1,
            plugin_url="https://github.com/jackdewinter/pymarkdown/blob/main/docs/rules/rule_md014.md",
        )  # https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md014---dollar-signs-used-before-commands-without-showing-output

    def starting_new_file(self):
        """
        Event that the a new file to be scanned is starting.
        """
        self.__in_code_block = False

    def next_token(self, context, token):
        """
        Event that a new token is being processed.
        """
        if token.is_code_block:
            self.__in_code_block = True
        elif token.is_code_block_end:
            self.__in_code_block = False
        elif self.__in_code_block and token.is_text:
            are_all_preceded_with_dollar_sign = True
            split_token_text = token.token_text.split("\n")
            for next_line in split_token_text:
                if not next_line.strip().startswith("$"):
                    are_all_preceded_with_dollar_sign = False
                    break
            if are_all_preceded_with_dollar_sign:
                self.report_next_token_error(context, token)
