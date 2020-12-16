import cv2
import os
from filters import dilateFilter, blurFilter, greyfilter, erodeFilter
import numpy as np
import sys
import re


args = sys.argv
dict_effects = {}
for i in range(0, len(args)):
    arg = args[i]
    if arg == '-i':

        input_directory = args[i + 1]
        # List of files
        files = os.listdir(input_directory)

    if arg == '-o':
        output = args[i + 1]
        print(output)

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

for file in files:
    for key in dict_effects:
        if key == "blur":
            blurFilter.filter(file, int(dict_effects[key]))

        if key == "dilate":
            dilateFilter.filter(file, int(dict_effects[key]))

        if key == "grayscale":
            greyfilter.filter(file)


