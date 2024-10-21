# py3d/models/__init__.py

# Импортируем функции и классы для работы с 3D-геометрией и текстурами
from .geometry import ModelGeometry
from .textures import load_texture

__all__ = [
    'ModelGeometry',
    'load_texture',
]

# Определяем метаинформацию о подмодуле
__version__ = '0.1'
