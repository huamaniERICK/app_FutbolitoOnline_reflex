import reflex as rx 

def seccion2():
    return rx.box(
        rx.box(
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Generalidades", value="tab1"),
                    rx.tabs.trigger("Participantes", value="tab2"),
                    rx.tabs.trigger("Clasificacion", value="tab3"),
                    rx.tabs.trigger("Resultados", value="tab4"),
                ),
                rx.tabs.content(
                    rx.box(
                        rx.center(
                            rx.vstack(
                                rx.text("Nombre del torneo",size="7",style={"font-family":"quesha"}),
                                rx.hstack(
                                    rx.input(placeholder="Coloca un nombre",width="40em",id="coloca un nombre"),
                                    rx.button("Cambiar",on_click=rx.set_value("coloca un nombre","")),
                                    margin_top="-1em",
                                    margin_bottom="2em",
                                ),
                                rx.text("Ubicacion",size="7",style={"font-family":"quesha"}),
                                rx.hstack(
                                    rx.input(placeholder="Ingresa una ubicacion...",width="40em",id="Ingresa una ubicacion..."),
                                    rx.button("Cambiar",on_click=rx.set_value("Ingresa una ubicacion..","")),
                                    margin_top="-1em",
                                    margin_bottom="2em",
                                ),
                                rx.text("Fecha del torneo",size="7",style={"font-family":"quesha"}),
                                rx.hstack(
                                    rx.input(placeholder="DD/MM/AA",width="40em",id="DD/MM/AA"),
                                    rx.button("Cambiar",on_click=rx.set_value("DD/MM/AA","")),
                                ),
                                margin_top="2em",
                            ),
                        ),
                    ),
                    value="tab1",
                ),
                rx.tabs.content(
                    rx.text("item on tab 2"),
                    value="tab2",
                ),
                rx.tabs.content(
                    rx.box(
                        rx.center(
                            rx.vstack(
                                rx.text("Elige la clasificacion del torneo",size="7",style={"font-family":"quesha"},margin_left="11em"),
                                rx.hstack(
                                    rx.text("Etapa grupal",size="5",style={"font-family":"arial black"},margin_right="8em"),
                                    rx.text("Etapa grupal y Etapa Eliminatoria",size="5",style={"font-family":"arial black"},margin_right="8em"),
                                    rx.text("Etapa Eliminatoria",size="5",style={"font-family":"arial black"}),
                                    margin_top="3em",
                                ),
                            ),
                            margin_top="2em",
                        ),
                    ),
                    value="tab3",
                ),
                rx.tabs.content(
                    rx.text("item on tab 4"),
                    value="tab4",
                ),
                default_value="tab1",
                orientation="vertical",
            ),
        ),
    ),
      
            