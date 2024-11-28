import reflex as rx

def seccion():
    return rx.hstack(
        rx.image(src="/football.webp",width="100px",height="auto",border_radius="15px 50px",border="5px solid #555"),
    )