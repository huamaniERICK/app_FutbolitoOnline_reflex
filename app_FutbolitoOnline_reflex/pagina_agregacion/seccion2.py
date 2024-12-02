import reflex as rx 

def seccion2():
    return rx.box(
        rx.hstack(
            rx.box(
                rx.tabs.root(

                    rx.tabs.list(
                        rx.tabs.trigger("Generalidades", value="Generalidades"),
                        rx.tabs.trigger("Participacion", value="Participacion"),
                        rx.tabs.trigger("Clasificacion", value="Clasificacion"),
                        rx.tabs.trigger("Resultados", value="Resultados"),
                        
                    ),
                    rx.tabs.content(
                        rx.center(
                            rx.text("NOMBRE DEL TORNEO"),
                        ),
                        value="Generalidades",
                    ),
                    rx.tabs.content(
                        rx.box(
                            rx.hstack(

                            ),
                            background_color="white",
                            border_radius="20px",
                            width="350px",
                            height="100px",
                            padding="300px",
                            box_shadow="0px 3px 10px rgba(0, 0, 0, 0.50)",
                        ),
                        value="Participacion",
                    ),
                    default_value="tab1",
                    orientation="vertical",
                )
                    #     on_change=SegmentedState.setvar("control"),
                    #     value=SegmentedState.control,     
                    # ),
                    # rx.card(
                    #     rx.text(SegmentedState.control,align="left"),
                    #     rx.text(SegmentedState.control,align="left"),
                    #     rx.text(SegmentedState.control,align="left"),
                    #     width="100%",
                    # )
                    
            )
        )      
    )       
    
    