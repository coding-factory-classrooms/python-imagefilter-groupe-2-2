import configparser


# Read config.ini file


def get_general_settings(ini_file):
    config_object = configparser.ConfigParser()
    config_object.read(ini_file)
    general = config_object["general"]
    return general


def get_input_directory(general_settings):
    input_directory_path = general_settings["input_dir"]
    return input_directory_path + '/'


def get_output_directory(general_settings):
    output_directory_path = general_settings["output_dir"]
    return output_directory_path + '/'


def get_log_file(general_settings):
    log_file = general_settings["log_file"]
    return log_file


def get_filter_dict(ini_file):
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
        try:
            effect_value = int(effect_parameters[1])
            dict_filters[effect_name] = effect_value
        except IndexError as e:
            dict_filters[effect_name] = 0
    return dict_filters


def get_filter_list():
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
