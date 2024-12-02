import reflex as rx

from .encabezado_ajustes import encabezado_ajustes
from .seccion2 import seccion2

def main_ajustes():
    return rx.box(
        encabezado_ajustes(),
        seccion2(),

    )