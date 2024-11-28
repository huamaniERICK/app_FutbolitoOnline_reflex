import reflex as rx

def pagina_registro():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("FutbolitoOnline",size="9",color="orange", style={"font-family":"quesha"}),
                rx.heading("Crea tu cuenta ", size="8", color="orange",style={"font-family":"roboto"}),
                rx.input(placeholder="Nombre",size="3", width="150%"),
                rx.input(placeholder="Correo electrónico", size="3", width="150%", autocomplete="email"),
                rx.input(placeholder="Contraseña", type_="password", size="3", width="150%"),
                rx.button("Registrarme", color_scheme="red", size="3"),
                spacing="3",
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