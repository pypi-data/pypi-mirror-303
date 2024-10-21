import os
import shutil


def organize_files(source: str, destination: str, subfolder_only_sort: bool, overwrite_combined_set: set, set_map: dict[str, str]) -> None:
    files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
    moved_files = 0

    for file in files:
        file_extension_type = os.path.splitext(file)[1][1:]
        if not file_extension_type:
            continue

        found_key = None
        if file_extension_type.upper() in overwrite_combined_set:
            found_key = set_map.get(file_extension_type.upper())

        folder_name = (file_extension_type.upper() + "_Files" if not found_key else found_key)

        dest_path = os.path.join(destination, folder_name)
        if not os.path.exists(os.path.join(destination, folder_name)):
            if subfolder_only_sort:
                continue
            os.makedirs(dest_path)

        shutil.move(os.path.join(source, file), dest_path)
        moved_files += 1

        print(f"Moved file {file} from {source} to {dest_path}")

    if moved_files == 0:
        print("No files to be moved were detected")
    else:
        print(f"Completed organizing files. {moved_files} out of {len(files)} detected files moved")