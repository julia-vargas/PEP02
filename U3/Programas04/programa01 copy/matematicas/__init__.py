# Para que lo interprete como un paquete importable

# 1. Código de inicialización y metadatos del paquete
VERSION = "1.0.0"
print(f"[INFO] Paquete 'matematicas' v{VERSION} inicializado.")

# 2. Exponer submódulos y funciones clave directamente en el paquete
from . import operaciones
from . import figuras
from . import conversiones

from .figuras import area_circulo
from .conversiones import a_entero

# 3. Controlar qué se exporta al usar 'from matematicas import *'
__all__ = ["operaciones", "figuras", "conversiones", "area_circulo", "a_entero", "VERSION"]