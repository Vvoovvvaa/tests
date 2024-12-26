import os
import shutil
import argparse


FILE_CATEGORIES = {
    'documents': ['.doc', '.docx', '.txt', '.rtf'],
    'pdfs': ['.pdf'],
    'pictures': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'movies': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'music': ['.mp3', '.wav', '.aac', '.flac'],
    'tables': ['.xls', '.xlsx', '.csv'],
    'slides': ['.ppt', '.pptx'],
    'compressed': ['.zip', '.tar', '.tar.gz', '.rar', '.7z'],
}

def parse_arguments():
    parser = argparse.ArgumentParser(description='Организация файлов по категориям.')
    parser.add_argument('directory', help='Путь к папке с файлами.')
    return parser.parse_args()



def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def move_file(file_path, category_folder):
    shutil.move(file_path, category_folder)
    print(f"Перемещён: {file_path} -> {category_folder}")

def organize_files(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            continue

        file_extension = os.path.splitext(item)[1].lower()  
        file_moved = False

        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_folder = os.path.join(directory, category)
                ensure_folder_exists(category_folder) 
                move_file(item_path, category_folder) 
                file_moved = True
                break

        if not file_moved:
            misc_folder = os.path.join(directory, 'other')
            ensure_folder_exists(misc_folder)
            move_file(item_path, misc_folder)

def main():
    args = parse_arguments()  
    directory = args.directory
    if not os.path.isdir(directory):
        print(f"Ошибка: Папка '{directory}' не существует.")
        return
    organize_files(directory)
    print("Файлы успешно организованы.")


if __name__ == '__main__':
    main()
