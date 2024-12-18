import os
import shutil
import argparse

FILE_TYPES = {
    'documents': ['.doc', '.docx', '.txt', '.rtf'],
    'pdfs': ['.pdf'],
    'pictures': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'movies': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'music': ['.mp3', '.wav', '.aac', '.flac'],
    'tables': ['.xls', '.xlsx', '.csv'],
    'slides': ['.ppt', '.pptx'],
    'compressed': ['.zip', '.tar', '.tar.gz', '.rar', '.7z'],
}

def create_folder(folder_name):
    directory_path = os.path.join(directory, folder_name)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    return directory_path

def move_file_to_folder(file_name, destination_folder):
    target_path = os.path.join(destination_folder, os.path.basename(file_name))
    shutil.move(file_name, target_path)
    print(f"Moved: {file_name} -> {target_path}")

def organize_files():
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            continue

        file_ext = os.path.splitext(item)[1].lower()
        sorted_flag = False

        for category, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                folder = create_folder(category)
                move_file_to_folder(item_path, folder)
                sorted_flag = True
                break

        if not sorted_flag:
            misc_folder = create_folder('miscellaneous')
            move_file_to_folder(item_path, misc_folder)

def main():
    parser = argparse.ArgumentParser(description='Organize files into categories.')
    parser.add_argument('directory', help='Path to the directory with files.')
    args = parser.parse_args()

    global directory
    directory = args.directory

    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    organize_files()
    print("All files have been organized.")

if __name__ == '__main__':
    main()
