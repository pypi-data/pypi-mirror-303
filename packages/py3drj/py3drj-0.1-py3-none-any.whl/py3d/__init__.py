# py3d/__init__.py

# Импортируем основные классы и функции
from .core import Model
from .rendering import render_model

__all__ = [
    'Model',
    'render_model',
]

# Определяем метаинформацию о пакете
__version__ = '0.1'
__author__ = 'Alex Repre'
__email__ = 'cblackmidis@gmail.com'
