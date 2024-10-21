from PIL import Image

def load_texture(texture_file):
    """Загрузка текстуры из файла."""
    try:
        with Image.open(texture_file) as img:
            return img
    except (FileNotFoundError, IOError) as e:
        print(f"Ошибка загрузки текстуры: {e}")
        return None
