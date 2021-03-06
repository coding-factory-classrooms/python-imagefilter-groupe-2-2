import configparser
import re

# Read config.ini file

def get_general_settings(ini_file):
    '''

    :param ini_file:
    :return: an iterable dictionary we call general since it contains all [general] settings in the ini file
    '''
    config_object = configparser.ConfigParser()
    config_object.read(ini_file)
    general = config_object["general"]
    return general


def get_input_directory(general_settings):
    '''

    :param general_settings: a dict containing all the infos we need
    :return: the input directory path
    '''
    input_directory_path = general_settings["input_dir"]
    return input_directory_path + '/'


def get_output_directory(general_settings):
    '''

    :param general_settings: a dict containing all the infos we need
    :return: the output directory path
    '''
    output_directory_path = general_settings["output_dir"]
    return output_directory_path + '/'


def get_log_file(general_settings):
    '''

    :param general_settings:
    :return: the log file
    '''
    log_file = general_settings["log_file"]
    return log_file


def get_filter_dict(ini_file):
    '''

    :param ini_file:
    :return: a dict_of_filters with the filters as keys and the filters value as value.
    '''
    config_object = configparser.ConfigParser()
    config_object.read(ini_file)

    # Get a dict in the form of "content=filter"
    content = config_object["filters"]

    # Get the value from key content. Returns a string with all filters
    filters = content["content"]

    # Get all the filters inside a list
    list_of_filters = filters.split('|')

    # Get all the filters in a dict as key = name_of_filter and value = value of filter
    dict_filters = {}
    for effect in list_of_filters:
        effect_parameters = effect.split(':')
        effect_name = effect_parameters[0]

        # Check if the effect is a message. We do this before the regex check to avoid errors
        if effect_name == "message":
            dict_filters[effect_name] = effect_parameters[1]
        else:
            try:
                # Do a regex check to make sure we give an int
                if re.match('[\+\-]?[0-9]+', effect_parameters[1]):
                    effect_value = int(effect_parameters[1])

                    # Manage negative error
                    if effect_value < 0:
                        print(
                            f"Expected value for {effect_name} has to be positive (>0), so we changed your value from {effect_value} to {effect_value * -1} ")
                        effect_value *= -1

                    # Manage pair value error
                    if effect_value % 2 == 0:
                        print(
                            f"Expected value for {effect_name} has to be odd, so we changed your value from {effect_value} to {effect_value + 1} ")
                        effect_value += 1

                    # Input values in dict as key = effect_name and value = effect_value
                    dict_filters[effect_name] = effect_value

                else:
                    print(f'Value : "{effect_parameters[1]}" for {effect_name} is incorrect. A number is required')

            # Handle index out of bond error
            except IndexError as e:
                dict_filters[effect_name] = 0
    return dict_filters


def get_filter_list():
    '''

    :return: print all the effects available at the time
    '''
    config_object = configparser.ConfigParser()
    config_object.read('imagefilter.ini')

    # Get a dict in the form of "filters=filters_list"
    filter_list = config_object["filters_list"]
    filters = filter_list["list"]

    # Get all the filters inside a list
    list_of_filters = filters.split(',')
    print("Here's the filter list currently available:")

    # Print all filters wrote in .ini file
    for effect in list_of_filters:
        print(effect)
    print()

def get_message(ini_file):
    '''

    :param ini_file: a config .ini file
    :return: a function to get the message contained in the .ini file
    '''
    config_object = configparser.ConfigParser()
    config_object.read(ini_file)

    # Get a dict in the form of "content=filter"
    content = config_object["filters"]

    # Get the value from key content. Returns a string with all filters
    filters = content["content"]

    # Get all the filters inside a list
    list_of_filters = filters.split('|')

    # Get all the filters in a dict as key = name_of_filter and value = value of filter
    dict_filters = {}
    for effect in list_of_filters:
        effect_parameters = effect.split(':')
        effect_name = effect_parameters[0]
        if effect_name == "message":
            return dict_filters[effect_name]

