# __init__.py
# Importujemy moduł Pybind11
from .uniezgame import (
    dodaj,         # Importujemy funkcję dodającą dwie liczby
    Renderer,      # Importujemy klasę RendererWrapper
    Rect,          # Importujemy klasę Rect
    Input,         # Importujemy klasę Input
    create_window  # Importujemy funkcję tworzącą okno
)

__all__ = [
    'dodaj',
    'Renderer',
    'Rect',
    'Input',
    'create_window'
]
