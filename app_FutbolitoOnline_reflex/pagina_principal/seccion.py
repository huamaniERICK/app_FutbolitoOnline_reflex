import reflex as rx

def seccion():
    return rx.flex(
        rx.box(
            rx.hstack(
                rx.html('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_AfkWlpCMOdxqNWi28h3Zv7pI70mciJiWrQ&s"  width="866" height="100%">')),
                

        ),
        rx.box(
            rx.hstack(
                rx.text("Mis torneos",size="9",style={"font-family":"quesha"}),
                rx.button(
                    "CREAR TORNEOS",
                    color_scheme="blue",
                    on_click=lambda:rx.redirect("/create_page"),
                    # margin_top="40em",
                    width="30%",
                ),
            ),
        ),
    ),

            
    
    
    