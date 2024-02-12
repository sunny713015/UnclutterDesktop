import os
import shutil

def organize_desktop():
    desktop_path = os.path.expanduser("~/Desktop")
    script_filename = os.path.basename(__file__)  # Get the filename of the script

    # Create a dictionary to store files based on their extensions
    files_by_extension = {}

    # Iterate over all files on the desktop
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        # Check if the path is a file (not a directory) and exclude the script file
        if os.path.isfile(file_path) and filename != script_filename:
            # Extract the file extension
            _, extension = os.path.splitext(filename)

            # Remove the leading dot from the extension
            extension = extension[1:]

            # If the extension is not in the dictionary, create an entry
            if extension not in files_by_extension:
                files_by_extension[extension] = []

            # Append the file to the list of files with the same extension
            files_by_extension[extension].append(file_path)

    # Create folders for each extension and move files accordingly
    for extension, files in files_by_extension.items():
        folder_path = os.path.join(desktop_path, extension)

        # Create the folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Move files to the corresponding folder
        for file_path in files:
            shutil.move(file_path, folder_path)

    print("Desktop organized successfully!")

if __name__ == "__main__":
    organize_desktop()