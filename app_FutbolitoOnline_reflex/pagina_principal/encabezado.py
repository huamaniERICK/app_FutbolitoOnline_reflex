import reflex as rx

def encabezado():
    return rx.hstack(
        rx.avatar(src="/icono.png", fallback="RX", size="6"),
        rx.text("FutbolitoOnline",size="8",color="orange",style={"font-family":"quesha"},),
        rx.spacer(),
        rx.button("IDIOMA",color_scheme="ruby"),
        rx.button("CUENTA",color_scheme="ruby",margin_right="70px"),
        rx.button("CREAR TORNEO",color_scheme="green",margin_right="60px",on_click=lambda:rx.redirect("/create_page")),
    
        background="blue",
        align="center",
    ),