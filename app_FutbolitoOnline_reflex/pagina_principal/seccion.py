import reflex as rx

def seccion():
    return rx.box(
        rx.hstack(
            rx.html('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_AfkWlpCMOdxqNWi28h3Zv7pI70mciJiWrQ&s"  width="866" height="100%">'),
            rx.container(
                rx.flex(
                    rx.vstack(
                        rx.text("Mis torneos",size="9",style={"font-family":"quesha"}),
                        rx.vstack(
                            rx.card("Card 1", size="5",width="630px"),
                            rx.card("Card 2", size="5",width="630px"),
                            rx.card("Card 3", size="5",width="630px"),
                            rx.card("Card 4", size="5",width="630px"),
                            spacing="1",
                        ),
                        rx.button(
                            "CREAR TORNEOS",
                            color_scheme="blue",
                            on_click=lambda:rx.redirect("/create_page"),
                            #margin_top="0em",
                            margin_right="-400px",
                            size="4",
                        ),
                        align="center",
                        justify_content="center",
  
                   ),   
                
                ),
            ),
        ),
    ),
    
    
    

    