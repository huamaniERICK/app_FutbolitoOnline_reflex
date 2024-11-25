import reflex as rx
import requests as rq

@rx.page(route="/login", title="login")
def login () -> rx.Component:
    return rx.section(
        rx.image(src='/futbol y copa.png', width="300px", border_radius="15px 50px"),
    )