import reflex as rx

def create_page():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("Nuevo Torneo", size="8", color="black"),
                rx.text("Puedes cambiar todos los datos posteriormente",size="1",),
                rx.input(placeholder="Nombre del torneo",size="3",color="blue",width="75%"),
                rx.input(placeholder="Contraseña", type_="password",size="3",width="75%"),
                
                width="100%",
                align_items="center",
                justify_content="center",
            ),
            width="450px",
            height="600px",
            padding="50px",
            background="white",
            box_shadow="0px 4px 10px rgba(0, 0, 0, 0.25)",
        ),
        background="blue",
        height="100vh",
        
        
    )