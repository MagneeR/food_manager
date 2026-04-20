import reflex as rx

from ..style import modal_button, ColorPalette

# Creating an image carroussel as a reflex component
class ImageCarrousselState(rx.State):
    images = [ "/How.png", "/index.png", "/places.png", "/items.png", "/prices.png", "/shopping.png" ]
    index = 0
    total_length : int
    completed : bool

    async def create(self):
        self.total_length = len(self.images) - 1

    def next_image(self):
        if self.index == self.total_length:
            self.index = 0
            self.completed = True
        else:
            self.index += 1
    
    def previous_image(self):
        if self.index == 0:
            self.index = self.total_length
        else:
            self.index -= 1


def ImageCarroussel() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.desktop_only(
                rx.image(
                    src = ImageCarrousselState.images[ImageCarrousselState.index],
                    height = "400px",
                    width = "400px",
                    border=f"0.8em solid {ColorPalette.ACCENT_ORANGE.value}",
                ),
            ),
            rx.mobile_and_tablet(
                rx.image(
                    src = ImageCarrousselState.images[ImageCarrousselState.index],
                    height = "auto",
                    border=f"0.8em solid {ColorPalette.ACCENT_ORANGE.value}",
                ),
            ),
            rx.flex(
                rx.button(
                    "Anterior",
                    on_click=ImageCarrousselState.previous_image,
                    style=modal_button
                ),
                rx.button(
                    "Siguiente",
                    on_click=ImageCarrousselState.next_image,
                    style=modal_button
                ),
                direction="row",
                spacing="4"
            ),
            direction="column",
            spacing="2",
            align="center"
        ),
        align="center"
    )