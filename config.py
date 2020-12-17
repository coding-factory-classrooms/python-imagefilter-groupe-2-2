import configparser

#Read config.ini file
config_object = configparser.ConfigParser()
config_object.read("imagefilter.ini")

general = config_object["general"]

print(general["input_dir"])
