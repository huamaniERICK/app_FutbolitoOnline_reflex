import reflex as rx

class TextAreaBlur(rx.State):
    text: str = "Futbolito Online"

def index():
    return rx.center(
        rx.h1(
            {
                "style": {
                    "text-align": "center",
                    "margin": "20px 0",
                }
            },
            TextAreaBlur.text
        )
    )

app = rx.App()
app.add_page(index)