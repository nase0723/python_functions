
already_open_files = []

def check_if_the_file_is_closed(files):
    for file in files:
        try:
            f = open(file)
            f.close()
        except PermissionError:
            already_open_files.append(file)