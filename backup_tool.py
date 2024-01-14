import shutil
import os
import datetime
import sys


def backup_folder(source_folder, backup_location):
    # Creates a timestamp for the backup folder
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Creates the backup folder with timestamp
    backup_folder_name = f"backup_{timestamp}"
    backup_folder_path = os.path.join(backup_location, backup_folder_name)
    os.makedirs(backup_folder_path)

    # Copies all of the contents of the source folder to the backup folder
    source_folder_contents = os.listdir(source_folder)
    for item in source_folder_contents:
        source_item_path = os.path.join(source_folder, item)
        backup_item_path = os.path.join(backup_folder_path, item)
        if os.path.isdir(source_item_path):
            shutil.copytree(source_item_path, backup_item_path)
        else:
            shutil.copy2(source_item_path, backup_item_path)

    print(f"Backup created successfully at: {backup_folder_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_folder> <backup_location>")
        sys.exit(1)

    source_folder_path = sys.argv[1]
    backup_location_path = sys.argv[2]

    backup_folder(source_folder_path, backup_location_path)
