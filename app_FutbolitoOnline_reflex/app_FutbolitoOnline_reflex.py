import reflex as rx
from .componentes.pantalla_inicio import login_page
from .componentes.pantalla_registro import register_page

def index ()->rx.components:
    return rx.center(
        rx.box(
            rx.text(
                "Crea tu primer torneo ideal con tus propias ideas",
                size="8",
                weight="bold",
                color="blue",
                margin_top="-4em",
                margin_bottom="4em",
                style={"font-family":"roboto"}
            ),
            rx.vstack(
                rx.button(
                    "INICIAR SESION",
                    size="3",
                    weight="bold",
                    color_scheme="grass",
                    width="100%",
                    on_click=lambda: rx.redirect("/login_page"),
                    border_radius="20px",
                
                ),
                rx.button(
                    "REGISTRATE", 
                    size="3",
                    weight="bold",
                    color_scheme="ruby",
                    width="100%",
                    on_click=lambda: rx.redirect("/register_page"),
                    border_radius="20px",
                    ),
                spacing="4",
            ),
        ),
        height="100vh",
        
        
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(login_page, route="/login_page")
app.add_page(register_page, route="/register_page")


# rx.button(
      
#             "Decrement",
#             color_scheme="ruby",
#             on_click=State.decrement,
#         ),
#         rx.heading(State.count, font_size="2em"),
#         rx.button(
#             "Increment",
#             color_scheme="grass",
#             on_click=State.increment,
#         ),
#         spacing="4",
#     )