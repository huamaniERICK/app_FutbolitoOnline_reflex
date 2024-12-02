import reflex as rx 

def encabezado_ajustes():
    return rx.hstack(
        rx.avatar(src="/icono.png", fallback="RX", size="6"),
        rx.text("FutbolitoOnline",size="8",color="orange",style={"font-family":"quesha"},),
        rx.spacer(),
        rx.button("IDIOMA",width="10%",color_scheme="ruby",margin_right="10px",on_click=lambda:rx.redirect("/")),
        rx.button("CUENTA",width="10%",color_scheme="ruby",margin_right="10px",on_click=lambda:rx.redirect("/")),
        rx.button("MIS TORNEOS",width="10%",color_scheme="ruby",margin_right="10px",on_click=lambda:rx.redirect("/")),
        rx.button("BUSCAR TORNEOS",width="10%",color_scheme="ruby",margin_right="70px",on_click=lambda:rx.redirect("/")),
        background="blue",
        align="center"

    )