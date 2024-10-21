import os
import configparser
from yasfs.file_organizer import organize_files

def create_default_config(config_file_path) -> bool:
    if not os.path.exists(config_file_path):
        print(f"Config file does not exist at: {config_file_path}, creating config file and exiting")

        config = configparser.ConfigParser()

        # Define default settings
        config['Settings'] = {
            'source': '',
            'destination': '',
            'subfolder_only_sort': 'False',
        }
        config['Overwrite Destinations'] = {
            'audio': 'MP3, WAV, OGG, M4A, FLAC, AIFF, WMA, AAC, GIF'
        }

        # Write comments and the config to the file
        with open(config_file_path, 'w') as configfile:
            configfile.write("[Settings]\n")

            configfile.write("# Takes FilePath as value; determines where files are being read from.\n")
            configfile.write("source: \n")

            configfile.write("# Takes FilePath as value; determines where files get moved to.\n")
            configfile.write("destination: \n\n")

            configfile.write("# Takes bool as value; if True, does not sort files if they have no pre-made destination folder,\n")
            configfile.write("subfolder_only_sort: False\n\n")

            configfile.write("[Overwrite Destinations]\n")
            configfile.write(
                "# Here you can overwrite the sorting process by specifying a folder name to be created (if it does not exist)\n"
                "# and the file extension types that will go into it. The key is case-sensitive, but the items are not.\n"
                "# The format is as follows:\n"
                "# My_Audio_Folder: MP3, WAV, OGG, M4A, FLAC, AIFF, WMA, AAC\n"
                "# Simply repeat this for as many folders and file types as you want.\n"
            )

        return True
    return False

def read_config_file(config_file_path, args) -> None:
    if create_default_config(config_file_path):
        return

    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(config_file_path)

    config_settings = read_config_values(config, args)
    if not config_settings:
        return

    source, destination, subfolder_only_sort, overwrite_combined_set, set_map = config_settings
    organize_files(source, destination, subfolder_only_sort, overwrite_combined_set, set_map)

def read_config_values(config, args) -> list:
    try:
        # Read and validate source and destination
        source = args.source if args.source else config.get('Settings', 'source')
        if source == "":
            raise Exception(f"No provided file path for 'source'")
        if not os.path.exists(source):
            raise Exception(f"Invalid 'source': {source}")

        destination = args.destination if args.destination else config.get('Settings', 'destination')
        if destination == "":
            raise Exception(f"No provided file path for 'destination'")
        if not os.path.exists(destination):
            raise Exception(f"Invalid 'destination': {destination}")

        subfolder_only_sort = args.subfolder_only_sort if True else config.get('Settings', 'subfolder_only_sort')
        if not subfolder_only_sort:
            if subfolder_only_sort == "":
                raise Exception("No value provided for 'subfolder_only_sort'")
            subfolder_only_sort = config.getboolean('Settings', 'subfolder_only_sort')

        overwrite_destinations = {}
        for key in config['Overwrite Destinations']:
            values = config['Overwrite Destinations'][key].split(',')
            overwrite_destinations[key] = [value.strip() for value in values]

        # Preprocess for faster lookup
        overwrite_combined_set = set(item.upper() for arr in overwrite_destinations.values() for item in arr)
        set_map = {item: key for key, values in overwrite_destinations.items() for item in values}

        print(f"Source: {source}")
        print(f"Destination: {destination}")
        print(f"Sort Only If Destination Subfolder Exists: {subfolder_only_sort}\n")
        return [source, destination, subfolder_only_sort, overwrite_combined_set, set_map]
    except ValueError:
        print("Provided value for 'subfolder_only_sort' is not of type bool")
        return []
    except Exception as e:
        print(e)
        return []