import reflex as rx
from .encabezado import encabezado
from .seccion import seccion

def main():
    return rx.box(
        encabezado(),
        seccion(),
        
    
    )
