import reflex as rx 

def seccion2():
    return rx.box(
        rx.box(
            rx.vstack(
                rx.link(
                    "Generalidades",
                    color="black",
                    size="5",
                    margin_top="3em",
                    
                ),
                rx.link(
                    "Participantes",
                    color="black",
                    size="5",
                    
                ),
                rx.link(
                    "Clasificacion",
                    color="black",
                    size="5",
                    
                ),
                rx.link(
                    "Resultados",
                    color="black",
                    size="5",
                    
                ),
                
                align_items="center",
                justify_content="center",
                spacing="9",
                style={"font-family":"quesha"},
            
            ),
            background="#0fc3f0",
            width="10%",
            height="89vh",
            
        
        
        ),
    rx.box(
        rx.center(
            rx.vstack(
                rx.text("Nombre del torneo",size="5",margin_top="-32em",align="center"),
                rx.hstack(
                    rx.input(id="input1",width="450px"),
                    rx.button("Cancelar", on_click=rx.set_value("input1",""),),
                ),
            ),
            
        ),
        
    ),

    ),
        