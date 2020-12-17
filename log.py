from datetime import datetime


# log action in the log.txt file and also print it in the console
def log_filter(file_name, filter_name):
    """ write a message in the console and the log.txt file with the action we do

    :param file_name: the name of the file we want to modify
    :param filter_name: the name of the effect we want to apply
    """

    # we're taking the today date
    now = datetime.now()
    # we choose the date display
    timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
    # printing action in the console
    print(f"{timestamp} the {file_name} file has been modified by {filter_name} effects")
    # printing action in the log.txt file
    with open("log.txt", "a") as f:
        f.write(f"{timestamp} the {file_name} file has been modified by {filter_name} effects\n")


# log error in the log.txt file and also print it in the console
def log_error(filter_name, file_name):
    """ write an error message in the console and the log.txt file with the action we wanted to do

    :param filter_name: the name of the file we wanted to modify
    :param file_name: the name of the effect we wanted to apply
    """

    # we're taking the today date
    now = datetime.now()
    # we choose the date display
    timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
    # printing error in the console
    print(f"{timestamp} Your input value was not referenced so, cannot apply {filter_name} filter on {file_name}\n")
    # printing error in the log.txt file
    with open("log.txt", "a") as f:
        f.write(
            f"{timestamp} Your input value was not referenced so, cannot apply {filter_name} filter on {file_name}\n")


def directory_created(output):
    # we're taking the today date
    now = datetime.now()
    # we choose the date display
    timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
    # printing action in the console
    print(f"{timestamp} Successfully created the directory {output}\n")
    # printing action in the log.txt file
    with open("log.txt", "a") as f:
        f.write(f"{timestamp} Successfully created the directory {output}\n")


def directory_failed(output):
    # we're taking the today date
    now = datetime.now()
    # we choose the date display
    timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
    # printing action in the console
    print(f"{timestamp} Creation of the directory {output} failed.\n")
    # printing action in the log.txt file
    with open("log.txt", "a") as f:
        f.write(f"{timestamp} Creation of the directory {output} failed.\n")


# to clean the log.txt file
def log_clean():
    with open("log.txt", "w") as f:
        f.write(f" ")
