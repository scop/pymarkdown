"""
Module to implement a sample plugin that has an empty string field from get_details.
"""
from plugin_manager import Plugin, PluginDetails


class BadStringDetailIsEmpty(Plugin):
    """
    Class to implement a sample plugin that has an empty string field from get_details.
    """

    def get_details(self):
        """
        Get the details for the plugin.
        """
        return PluginDetails(
            plugin_name="bad-string-detail-is-empty",
            plugin_id="MDE006",
            plugin_enabled_by_default=True,
            plugin_description="",
            plugin_version="0.0.0",
            plugin_interface_version=1,
        )
