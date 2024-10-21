class ModelGeometry:
    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces

    def get_vertices(self):
        return self.vertices

    def get_faces(self):
        return self.faces

    def scale(self, factor):
        """Масштабирование модели."""
        self.vertices = [[coord * factor for coord in vertex] for vertex in self.vertices]

    def translate(self, dx, dy, dz):
        """Перемещение модели."""
        self.vertices = [[x + dx, y + dy, z + dz] for x, y, z in self.vertices]
