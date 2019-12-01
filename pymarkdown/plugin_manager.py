"""
Module to provide classes to deal with plugins.
"""
import inspect
import os
import sys
from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class ScanContext:
    """
    Class to provide context when reporting any errors.
    """

    def __init__(self, owning_manager, scan_file):
        self.owning_manager = owning_manager
        self.scan_file = scan_file

        self.line_number = 0


class BadPluginError(Exception):
    """
    Class to allow for a critical error within a plugin to be encapsulated
    and reported.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        plugin_id=None,
        plugin_action=None,
        file_name=None,
        class_name=None,
        field_name=None,
        is_constructor=False,
        is_empty=False,
    ):

        if file_name:
            if class_name:
                if is_constructor:
                    formatted_message = (
                        "Plugin file named '"
                        + file_name
                        + "' threw an exception in the constructor for the class '"
                        + class_name
                        + "'."
                    )
                else:
                    formatted_message = (
                        "Plugin file named '"
                        + file_name
                        + "' does not contain a class named '"
                        + class_name
                        + "'."
                    )
            else:
                formatted_message = (
                    "Plugin file named '" + file_name + "' cannot be loaded."
                )
        elif class_name:
            if field_name:
                if is_empty:
                    formatted_message = (
                        "Plugin class '"
                        + class_name
                        + "' returned an empty value for field name '"
                        + field_name
                        + "'."
                    )
                else:
                    formatted_message = (
                        "Plugin class '"
                        + class_name
                        + "' returned an improperly typed value for field name '"
                        + field_name
                        + "'."
                    )
            else:
                formatted_message = (
                    "Plugin class '"
                    + class_name
                    + "' had a critical failure loading the plugin details."
                )
        else:
            formatted_message = (
                "Plugin id '"
                + plugin_id
                + "' had a critical failure during the '"
                + plugin_action
                + "' action."
            )
        Exception.__init__(self, formatted_message)


class Plugin(ABC):
    """
    Class to provide structure to scan through a file.
    """

    def __init__(self):
        self.__scan_context = None

    @abstractmethod
    def get_details(self):
        """
        Get the details for the plugin.
        """

    def set_context(self, context):
        """
        Set the context to use for any error reporting.
        """
        self.__scan_context = context

    def report_error(self, column_number, line_number_delta=0):
        """
        Fix this up.
        """
        self.__scan_context.owning_manager.log_scan_failure(
            self.__scan_context.scan_file,
            self.__scan_context.line_number + line_number_delta,
            column_number,
            self.get_details().plugin_id,
            self.get_details().plugin_name,
            self.get_details().plugin_description,
        )

    def initialize_from_config(self):
        """
        Event to allow the plugin to load configuration.
        """

    def starting_new_file(self):
        """
        Event that the a new file to be scanned is starting.
        """

    def completed_file(self):
        """
        Event that the file being currently scanned is now completed.
        """

    def next_line(self, line):
        """
        Event that a new line is being processed.
        """


class PluginDetails:
    """
    Class to provide details about a plugin, supplied by the plugin.
    """

    def __init__(
        self, plugin_id, plugin_name, plugin_description, plugin_enabled_by_default
    ):
        self.plugin_id = plugin_id
        self.plugin_name = plugin_name
        self.plugin_description = plugin_description
        self.plugin_enabled_by_default = plugin_enabled_by_default


class FoundPlugin:
    """
    Encapsulation of a plugin that was discovered.  While similar to the PluginDetails
    class, this is meant for an internal representation of the plugin, and not the
    external information provided.
    """

    def __init__(self, plugin_id, plugin_name, plugin_description, plugin_instance):
        self.plugin_id = plugin_id
        self.plugin_name = plugin_name
        self.plugin_description = plugin_description
        self.plugin_instance = plugin_instance


class PluginManager:
    """
    Manager object to take care of load and accessing plugin modules.
    """

    def __init__(self):
        self.__registered_plugins = None
        self.__enabled_plugins = None
        self.__loaded_classes = None
        self.number_of_scan_failures = None

    def initialize(
        self, directory_to_search, additional_paths, enable_rules, disable_rules
    ):
        """
        Initializes the manager by scanning for plugins, loading them, and registering them.
        """
        self.number_of_scan_failures = 0

        self.__loaded_classes = []

        plugin_files = self.__find_eligible_plugins_in_directory(directory_to_search)
        self.__load_plugins(directory_to_search, plugin_files)

        if additional_paths:
            for next_additional_plugin in additional_paths:
                if not os.path.exists(next_additional_plugin):
                    print(
                        "Plugin path '" + next_additional_plugin + "' does not exist.",
                        file=sys.stderr,
                    )
                    sys.exit(1)
                if os.path.isdir(next_additional_plugin):
                    plugin_files = self.__find_eligible_plugins_in_directory(
                        next_additional_plugin
                    )
                    self.__load_plugins(next_additional_plugin, plugin_files)
                else:
                    self.__load_plugins(
                        os.path.dirname(next_additional_plugin),
                        [os.path.basename(next_additional_plugin)],
                    )

        self.__register_plugins(enable_rules, disable_rules)

    # pylint: disable=too-many-arguments
    def log_scan_failure(
        self,
        scan_file,
        line_number,
        column_number,
        rule_id,
        rule_name,
        rule_description,
    ):
        """
        Log the scan failure in the appropriate format.
        """
        print(
            "{0}:{1}:{2}: {3}: {4} ({5})".format(
                scan_file,
                line_number,
                column_number,
                rule_id,
                rule_description,
                rule_name,
            )
        )
        self.number_of_scan_failures = self.number_of_scan_failures + 1

    @classmethod
    def __find_eligible_plugins_in_directory(cls, directory_to_search):
        """
        Given a directory to search, scan for eligible modules to load later.
        """

        plugin_files = [
            x
            for x in os.listdir(directory_to_search)
            if x.endswith(".py") and x[0:-3] != "__init__"
        ]
        return plugin_files

    @classmethod
    def __snake_to_camel(cls, word):

        return "".join(x.capitalize() or "_" for x in word.split("_"))

    def __attempt_to_load_plugin(
        self, next_plugin_module, plugin_class_name, next_plugin_file
    ):
        """
        Attempt to cleanly load the specified plugin.
        """
        try:
            try:
                mod = __import__(next_plugin_module)
            except Exception:
                raise BadPluginError(file_name=next_plugin_file)

            if not hasattr(mod, plugin_class_name):
                raise BadPluginError(
                    file_name=next_plugin_file, class_name=plugin_class_name
                )
            my_class = getattr(mod, plugin_class_name)

            try:
                plugin_class_instance = my_class()
            except Exception:
                raise BadPluginError(
                    file_name=next_plugin_file,
                    class_name=plugin_class_name,
                    is_constructor=True,
                )
            self.__loaded_classes.append(plugin_class_instance)
        except BadPluginError as this_exception:
            print("BadPluginError: " + str(this_exception), file=sys.stderr)
            sys.exit(1)

    # pylint: disable=broad-except
    def __load_plugins(self, directory_to_search, plugin_files):
        """
        Given an array of discovered modules, load them into the global namespace.
        """

        if os.path.abspath(directory_to_search) not in sys.path:
            sys.path.insert(0, os.path.abspath(directory_to_search))

        for next_plugin_file in plugin_files:
            next_plugin_module = next_plugin_file[0:-3]
            plugin_class_name = self.__snake_to_camel(next_plugin_module)
            self.__attempt_to_load_plugin(
                next_plugin_module, plugin_class_name, next_plugin_file
            )

    @classmethod
    def __determine_if_plugin_enabled(
        cls,
        plugin_enabled,
        plugin_object,
        command_line_enabled_rules,
        command_line_disabled_rules,
    ):
        """
        Given the enable and disable rules values, evaluate the enabled or disabled
        state of the plugin in proper order.
        """

        if (
            plugin_object.plugin_id in command_line_disabled_rules
            or plugin_object.plugin_name in command_line_disabled_rules
        ):
            plugin_enabled = False
        if (
            plugin_object.plugin_id in command_line_enabled_rules
            or plugin_object.plugin_name in command_line_enabled_rules
        ):
            plugin_enabled = True

        return plugin_enabled

    @classmethod
    def __verify_string_field(cls, plugin_instance, field_name, field_value):
        """
        Verify that the detail field is a valid string.
        """

        if not isinstance(field_value, str):
            raise BadPluginError(
                class_name=type(plugin_instance).__name__, field_name=field_name
            )
        if not field_value:
            raise BadPluginError(
                class_name=type(plugin_instance).__name__,
                field_name=field_name,
                is_empty=True,
            )

    @classmethod
    def __verify_boolean_field(cls, plugin_instance, field_name, field_value):
        """
        Verify that the detail field is a valid boolean.
        """

        if not isinstance(field_value, bool):
            raise BadPluginError(
                class_name=type(plugin_instance).__name__, field_name=field_name
            )

    def __get_plugin_details(self, plugin_instance):
        """
        Query the plugin for details and verify that they are reasonable.
        """

        try:
            instance_details = plugin_instance.get_details()
            plugin_id = instance_details.plugin_id
            plugin_name = instance_details.plugin_name
            plugin_description = instance_details.plugin_description
            plugin_enabled_by_default = instance_details.plugin_enabled_by_default
        except Exception:
            raise BadPluginError(class_name=type(plugin_instance).__name__,)

        self.__verify_string_field(plugin_instance, "plugin_id", plugin_id)
        self.__verify_string_field(plugin_instance, "plugin_name", plugin_name)
        self.__verify_string_field(
            plugin_instance, "plugin_description", plugin_description
        )
        self.__verify_boolean_field(
            plugin_instance, "plugin_enabled_by_default", plugin_enabled_by_default
        )

        plugin_object = FoundPlugin(
            plugin_id, plugin_name, plugin_description, plugin_instance
        )
        return plugin_object, plugin_enabled_by_default

    # pylint: disable=broad-except
    def __register_individual_plugin(
        self, plugin_instance, command_line_enabled_rules, command_line_disabled_rules
    ):
        """
        Register an individual plugin for use.
        """

        plugin_object, plugin_enabled_by_default = self.__get_plugin_details(
            plugin_instance
        )
        self.__registered_plugins.append(plugin_object)
        if self.__determine_if_plugin_enabled(
            plugin_enabled_by_default,
            plugin_object,
            command_line_enabled_rules,
            command_line_disabled_rules,
        ):
            self.__enabled_plugins.append(plugin_object)
            plugin_instance.initialize_from_config()

    def __register_plugins(self, enable_rules, disable_rules):
        """
        Scan the global namespace for all subclasses of the 'Plugin' class to use as
        plugins.
        """

        command_line_enabled_rules = set()
        command_line_disabled_rules = set()
        if enable_rules:
            for i in enable_rules.split(","):
                command_line_enabled_rules.add(i)
        if disable_rules:
            for i in disable_rules.split(","):
                command_line_disabled_rules.add(i)

        self.__registered_plugins = []
        self.__enabled_plugins = []
        for plugin_instance in self.__loaded_classes:
            self.__register_individual_plugin(
                plugin_instance, command_line_enabled_rules, command_line_disabled_rules
            )

    def starting_new_file(self, file_being_started):
        """
        Inform any listeners that a new current file has been started.
        """
        for next_plugin in self.__enabled_plugins:
            try:
                next_plugin.plugin_instance.starting_new_file()
            except Exception:
                raise BadPluginError(next_plugin.plugin_id, inspect.stack()[0][3])

        return ScanContext(self, file_being_started)

    def completed_file(self, context, line_number):
        """
        Inform any listeners that the current file has been completed.
        """
        context.line_number = line_number
        for next_plugin in self.__enabled_plugins:
            try:
                next_plugin.plugin_instance.set_context(context)
                next_plugin.plugin_instance.completed_file()
            except Exception:
                raise BadPluginError(next_plugin.plugin_id, inspect.stack()[0][3])

    def next_line(self, context, line_number, line):
        """
        Inform any listeners that a new line has been loaded.
        """
        context.line_number = line_number
        for next_plugin in self.__enabled_plugins:
            try:
                next_plugin.plugin_instance.set_context(context)
                next_plugin.plugin_instance.next_line(line)
            except Exception:
                raise BadPluginError(next_plugin.plugin_id, inspect.stack()[0][3])