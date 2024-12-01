import reflex as rx

from .pagina_agregacion.main_ajustes import main_ajustes
from .componentes.pantalla_creacion import create_page
from .pagina_principal.main import main
from .componentes.pantalla_inicio import pagina_inicio
from .componentes.pantalla_registro import pagina_registro

def index ()->rx.components:
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("Bienvenido a nuestra app",size="8",color="orange",style={"font-family":"quesha"}),
                rx.text("FutbolitoOnline",size="9",color="orange",style={"font-family":"quesha"}),
                spacing="3",
                width="100%",
                margin_top="-6em",
                align_items="center",
                justify_content="center",
                ),
            rx.html('<img src="https://png.pngtree.com/png-clipart/20210905/original/pngtree-football-european-cup-match-football-match-png-image_6696366.jpg" alt="Imagen de fútbol y copa" width="300" height="200">',width="100%",aling_items="center"),
            rx.spacer(height="50px"),
            rx.vstack(
                rx.button("INICIAR SESION",size="3",weight="bold",color_scheme="grass",width="100%",on_click=lambda: rx.redirect("/login_page"),border_radius="20px",),
                rx.button("REGISTRATE", size="3",weight="bold",color_scheme="ruby",width="100%",on_click=lambda: rx.redirect("/register_page"),border_radius="20px"),  
                spacing="3",
                width="100%",
                ),
            
            
        # width="460px",
        # height="460px",
        # padding="50px",
        # align_items="center",
        # justify_content="center",   
            
        ),
        
        height="100vh",
        background="blue",
        align_items="center",
        #justify_content="center",
        
    ),

app = rx.App()
app.add_page(index, route="/")
app.add_page(pagina_inicio, route="/login_page")
app.add_page(pagina_registro, route="/register_page")
app.add_page(main, route="/main")
app.add_page(create_page,route="/create_page")
app.add_page(main_ajustes, route="/main_ajustes")




