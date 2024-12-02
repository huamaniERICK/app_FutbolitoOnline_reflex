import reflex as rx 

def seccion2():
    return rx.box(
        rx.hstack(
            rx.box(
                rx.vstack(
                    rx.card(
                        rx.link("Generalidades",color="blue",size="5"),
                        size="5"),
                    rx.card(
                        rx.link("Participantes", color="blue", size="5"),
                        size="5"),
                    rx.card(
                        rx.link("Clasificacion",color="blue",size="5"),
                        size="5"),
                    rx.card(
                        rx.link("Resultados",color="blue",size="5"),
                        size="5"),
                    spacing="3",
                    
                )
            )      
        )       
    )
    