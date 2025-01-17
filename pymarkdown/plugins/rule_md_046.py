"""
Module to implement a plugin that looks for hard tabs in the files.
"""
from pymarkdown.plugin_manager import Plugin, PluginDetails


class RuleMd046(Plugin):
    """
    Class to implement a plugin that looks for hard tabs in the files.
    """

    __consistent_style = "consistent"
    __fenced_style = "fenced"
    __indented_style = "indented"
    __valid_styles = [
        __consistent_style,
        __fenced_style,
        __indented_style,
    ]

    def __init__(self):
        super().__init__()
        self.__style_type = None
        self.__actual_style_type = None

    def get_details(self):
        """
        Get the details for the plugin.
        """
        return PluginDetails(
            # code
            plugin_name="code-block-style",
            plugin_id="MD046",
            plugin_enabled_by_default=True,
            plugin_description="Code block style",
            plugin_version="0.5.0",
            plugin_interface_version=1,
        )  # https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md045---images-should-have-alternate-text-alt-text
        # Parameters: style ("consistent", "fenced", "indented"; default "consistent")

    @classmethod
    def __validate_configuration_style(cls, found_value):
        if found_value not in RuleMd046.__valid_styles:
            raise ValueError(f"Allowable values: {str(RuleMd046.__valid_styles)}")

    def initialize_from_config(self):
        """
        Event to allow the plugin to load configuration information.
        """
        self.__style_type = self.plugin_configuration.get_string_property(
            "style",
            default_value=RuleMd046.__consistent_style,
            valid_value_fn=self.__validate_configuration_style,
        )

    def starting_new_file(self):
        """
        Event that the a new file to be scanned is starting.
        """
        self.__actual_style_type = None
        if self.__style_type != RuleMd046.__consistent_style:
            self.__actual_style_type = self.__style_type

    def next_token(self, context, token):
        """
        Event that a new token is being processed.
        """
        if token.is_code_block:
            current_style = (
                RuleMd046.__fenced_style
                if token.is_fenced_code_block
                else RuleMd046.__indented_style
            )
            if not self.__actual_style_type:
                self.__actual_style_type = current_style
            if self.__actual_style_type != current_style:
                extra_data = (
                    "Expected: "
                    + str(self.__actual_style_type)
                    + "; Actual: "
                    + str(current_style)
                )
                self.report_next_token_error(
                    context, token, extra_error_information=extra_data
                )
