import reflex as rx

def pagina_inicio():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("FutbolitoOnline", size="9", color="orange",style={"font-family":"quesha"}),
                rx.heading("Iniciar Sesión", size="8", color="orange",style={"font-family":"roboto"}),
                rx.input(placeholder="Nombre de usuario o correo electronico",size="3",width="150%"),
                rx.input(placeholder="Contraseña", type_="password",size="3",width="150%"),
                rx.button("Iniciar sesion", color_scheme="grass",size="3",on_click=lambda:rx.redirect("/encabezado")),
                rx.text("¿Olvidaste contraseña? ", color="red", size="2", cursor="pointer"),
                rx.link("¿Eres nuevo? Registrate aquí", color="red", href="/register_page"),
                
                width="100%",
                align_items="center",
                justify_content="center",
            ),
            
            width="460px",
            height="460px",
            padding="50px",
            
            
            
        ),
        background="blue",
        height="100vh",
    )