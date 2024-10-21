import numpy as np

class Model:
    def __init__(self, filename):
        self.filename = filename
        self.vertices = []
        self.faces = []
        self.load_model()

    def load_model(self):
        """Загрузка модели из файла."""
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('v '):
                        try:
                            self.vertices.append([float(val) for val in line.split()[1:]])
                        except ValueError:
                            print(f"Ошибка в строке вершин: {line}")
                    elif line.startswith('f '):
                        try:
                            self.faces.append([int(val.split('/')[0]) - 1 for val in line.split()[1:]])
                        except (ValueError, IndexError):
                            print(f"Ошибка в строке граней: {line}")
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден.")
        except IOError as e:
            print(f"Ошибка при чтении файла {self.filename}: {e}")

    def get_vertices(self):
        return np.array(self.vertices)

    def get_faces(self):
        # Используем dtype=object для работы с неравномерными полигонами
        return np.array(self.faces, dtype=object)
