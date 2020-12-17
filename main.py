import cv2
import os
from filters import dilateFilter, blurFilter, greyfilter, erodeFilter
import directories
import sys
import re


args = sys.argv
dict_effects = {}
for i in range(0, len(args)):
    arg = args[i]
    if arg == '-i':

        input_directory = (args[i + 1]+"/")
        #print(input_directory)
        try:
            # List of files
            files = os.listdir(input_directory)
        except FileNotFoundError as e:
            print(f"Specified directory path cannot be found: {input_directory} ")

    if arg == '-o':
        output_directory = (args[i + 1] + "/")
        directories.create_directory(output_directory)

    if arg == '--filters':
        # Get arguments from command line
        effects = args[i + 1]

        # Create List of entered effects
        list_effects = effects.split('|')

        # iterate on each effect of our effects
        for effect in list_effects:
            effect_parameters = effect.split(':')
            effect_name = effect_parameters[0]

            try:
                if re.match('[0-9]+', effect_parameters[1]):
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

    for file in files:
        try:
            new_file = cv2.imread(input_directory+file)
            cv2.imwrite(output_directory + "new_" + file, new_file)
            input_path = output_directory
            file_name = "new_" + file

        except cv2.error:
            print(f"Your file={file} is not an image")

        for key in dict_effects:
            if key == "blur":
                blurFilter.filter(file_name, int(dict_effects[key]), input_path, output_directory)

            if key == "dilate":
                dilateFilter.filter(file_name, int(dict_effects[key]), input_path, output_directory)

            if key == "grayscale":
                greyfilter.filter(file_name, input_path, output_directory)
except NameError as e:
    print("Enter correct directory")

