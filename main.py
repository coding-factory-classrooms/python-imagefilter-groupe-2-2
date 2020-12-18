import cv2
import os
from filters import dilateFilter, blurFilter, greyfilter, zeTeam
import directories
import sys
import re
import log
import config

# Get the arguments from command line in a list
args = sys.argv

# iterate over the the argument list
for i in range(0, len(args)):
    arg = args[i]

    if arg == '--list-filters':
        # Get the filter list
        config.get_filter_list()


for i in range(0, len(args)):
    arg = args[i]

    if arg == '--config-file':
        dict_effects = {}
        try:
            # Get the config_file from command line
            config_file = args[i+1]
            # Get the general settings from the config file
            general_settings = config.get_general_settings(config_file)

            # Get input and output directory
            input_directory = config.get_input_directory(general_settings)
            output_directory = config.get_output_directory(general_settings)
            # Get the dict effect as keys = filters | values = value of filter
            dict_effects = config.get_filter_dict(config_file)
        except IndexError as e:
            print('You did not enter an input folder')
        try:
            # List of files from an input directory
            files = os.listdir(input_directory)
            directories.create_directory(output_directory)
        except FileNotFoundError as e:
            print(f"Specified directory path cannot be found: {input_directory} ")

    if arg == '-i':
        # Get the input directory
        input_directory = (args[i + 1]+"/")

        try:
            # List of files
            files = os.listdir(input_directory)
        except FileNotFoundError as e:
            print(f"Specified directory path cannot be found: {input_directory} ")

    if arg == '-o':
        # Get the output directory
        output_directory = (args[i + 1] + "/")
        directories.create_directory(output_directory)

    if arg == '--filters':
        # Here we get all the filters with their
        dict_effects = {}
        # Get arguments from command line
        effects = args[i + 1]

        # Create List of entered effects
        list_effects = effects.split('|')

        # iterate on each effect of our effects
        for effect in list_effects:
            effect_parameters = effect.split(':')
            effect_name = effect_parameters[0]

            # Check if the effect is a message. We do this before the regex check to avoid errors
            if effect_name == "message":
                dict_effects[effect_name] = effect_parameters[1]
            else:
                try:
                    # Do a regex check to make sure we give an int
                    if re.match('[\+\-]?[0-9]+', effect_parameters[1]):
                        effect_value = int(effect_parameters[1])

                        # Manage negative error
                        if effect_value < 0:
                            print(f"Expected value for {effect_name} has to be positive (>0), so we changed your value from {effect_value} to {effect_value * -1} ")
                            effect_value *= -1

                        # Manage pair value error
                        if effect_value % 2 == 0:
                            print(f"Expected value for {effect_name} has to be odd, so we changed your value from {effect_value} to {effect_value + 1} ")
                            effect_value += 1

                        # Input values in dict as key = effect_name and value = effect_value
                        dict_effects[effect_name] = effect_value

                    else:
                        print(f'Value : "{effect_parameters[1]}" for {effect_name} is incorrect. A number is required')

            # Handle index out of bond error
                except IndexError as e:
                    dict_effects[effect_name] = 0

try:
    # Iterate on our list of files from the input directory
    for file in files:
        # Manage exceptions such as file is not an image
        try:
            # Get the image
            new_file = cv2.imread(input_directory+file)
            # Get the new file name
            file_name = "new_" + file
            # Create the new file
            cv2.imwrite(output_directory + file_name, new_file)
            # We give the input_path the output directory because this is where we will put the modified images
            input_path = output_directory

            # We iterate on our dict of effects
            for key in dict_effects:
                # If the effect is blur
                if key == "blur":
                    # Apply blue filter
                    blurFilter.filter(file, int(dict_effects[key]), input_path)
                # If the effect is dilate
                if key == "dilate":
                    # Apply dilate filter
                    dilateFilter.filter(file, int(dict_effects[key]), input_path)
                # If the filter is greyscale
                if key == "grayscale":
                    # Apply greyscale
                    greyfilter.filter(file, input_path)
                # If the filter is add message
                if key == "message":
                    # Apply message
                    zeTeam.show_the_team(file, output_directory, dict_effects[key])

        except cv2.error:
            log.wrong_file(file)

except NameError as e:
    print("Enter correct directory")

