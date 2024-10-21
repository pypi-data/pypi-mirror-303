from pathlib import Path

def print_welcome_message():
    """Выводит приветственное сообщение."""
    print("Welcome to Py3D!")

def check_file_exists(filepath):
    """Проверяет, существует ли файл по указанному пути."""
    return Path(filepath).is_file()
