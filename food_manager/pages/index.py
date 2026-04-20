# Index page
import reflex as rx
from rxconfig import config

from ..template import base_page
from ..constants import Pages, Routes, APP_NAME, DO_REGISTER, Icons
from ..style import Size, ColorPalette, index_vstack_style, base_button, index_card_style, auth_form_button
from ..components.auth import login_form
from ..state import MyLocalAuthState

def index_card(icon:str, title:str, href:str, page:bool) -> rx.Component:
    index_card_info = rx.cond(
        page,
        rx.link(
            rx.hstack(
                rx.icon(icon, color=ColorPalette.ACCENT_PURPLE.value),
                rx.text(
                    title,
                    size="5",
                    color=ColorPalette.ACCENT_PURPLE.value),
            ),
            href=href,
        ),
        rx.link(
            rx.hstack(
                rx.icon(icon, color=ColorPalette.ACCENT_PURPLE.value),
                rx.text(
                    title,
                    size="5",
                    color=ColorPalette.ACCENT_PURPLE.value),
            ),
            on_click=MyLocalAuthState.perform_logout,
            _as="button",
        ),
    )
    return rx.card(
        index_card_info,
        style=index_card_style
    ),

@rx.page(
    route=Routes.HOME.value,
    title=Pages.HOME.value,
)
@base_page
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.cond(
            MyLocalAuthState.authenticated_user_info,
            # Logged view
            rx.vstack(
                rx.heading(f"Hola {MyLocalAuthState.authenticated_user.username}", size="9"),
                rx.grid(
                    index_card(Icons.PLACES.value, Pages.PLACES_LOWER.value, Routes.PLACES.value, True),
                    index_card(Icons.SHOPPING.value, Pages.SHOPPING.value, Routes.SHOPPING.value, True),
                    index_card(Icons.HELP.value, Pages.HELP.value, Routes.HELP.value, True),
                    index_card(Icons.LOGOUT.value, Pages.LOGOUT.value, "", False),
                    columns=rx.breakpoints(initial="1", sm="1", lg="4"),
                    width="75%",
                    spacing="2",
                ),
                style=index_vstack_style,
            ),
            # Unlogged view
            rx.vstack(
                rx.heading(
                    f"Bienvenido a {APP_NAME}!",
                    size="9",
                ),
                rx.box(
                    index_card(Icons.HELP.value, Pages.HELP.value, Routes.HELP.value, True),
                    width="75%",
                    padding_top="16px",
                    padding_bottom="16px",
                ),
                login_form(), 
                rx.button(
                    rx.link(
                        DO_REGISTER,
                        href=Routes.REGISTER.value,
                        font_size=Size.BIG.value,
                    ),
                    width="100%",
                    style=auth_form_button,
                ),
                style=index_vstack_style,
            ),
        ),  
        #min_height="70dvh",
        id="index-page",
    )