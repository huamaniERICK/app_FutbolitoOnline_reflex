import reflex as rx

def create_page():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("Nuevo Torneo", size="8", color="black",style={"font-family":"quesha"}),
                rx.text("Puedes cambiar todos los datos posteriormente",size="3",),
                rx.text("NOMBRE", size="2", color="black", margin_right="250px", style={"font-family":"cooper black"},margin_top="2em"),
                rx.input(placeholder="Nombre del torneo",size="3",color="blue",width="95%",margin_top="-1em"),
                rx.text("FECHA", size="2", color="black", margin_right="250px", style={"font-family":"cooper black"},margin_top="1em"),
                rx.input(placeholder="DD/MM/AA",size="3",width="95%",margin_top="-1em"),
                rx.text("HORA",size="2", color="black", margin_right="250px", style={"font-family":"cooper black"},margin_top="1em"),
                rx.input(placeholder="HH:MM:SS",size="3",width="95",margin_top="-1em"),
                rx.hstack(
                    rx.button("CANCELAR",color_scheme="ruby",on_click=lambda:rx.redirect("/main")),
                    rx.button("SIGUIENTE",color_scheme="grass",margin_right="70px",on_click=lambda:rx.redirect("/main_ajustes")),
                    margin_top="9em",
                    margin_right="-260px",
                ),
                
                
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