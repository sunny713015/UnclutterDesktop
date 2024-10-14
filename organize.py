import os
import shutil

# Path to the user's desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# List of files to ignore
ignore_files = ['Recycle Bin']
ignore_extensions = ['.py', '.lnk']

# Check if a file is a shortcut or a file that should be ignored
def should_ignore(file_name, extension):
    if file_name in ignore_files:
        return True
    if extension in ignore_extensions:
        return True
    return False

# Create a folder only if it doesn't exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")

# Move files to their respective extension folders
def organize_files():
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        # Skip directories or Recycle Bin
        if os.path.isdir(item_path) or should_ignore(item, None):
            continue
        
        # Get the file extension
        file_name, file_extension = os.path.splitext(item)

        # Skip ignored extensions
        if should_ignore(None, file_extension):
            continue

        # Create folder for the extension
        extension_folder = os.path.join(desktop_path, file_extension[1:].upper() + "_Files")
        create_folder(extension_folder)

        # Move the file to the respective folder
        try:
            shutil.move(item_path, os.path.join(extension_folder, item))
            print(f"Moved {item} to {extension_folder}")
        except Exception as e:
            print(f"Error moving {item}: {e}")

if __name__ == "__main__":
    organize_files()
