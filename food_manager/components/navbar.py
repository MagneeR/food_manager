import reflex as rx

from food_manager.state import MyLocalAuthState

from ..style import navbar_style, ColorPalette
from ..constants import Icons, Routes

def navbar_item_mobile(icon:str, href:str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(
                tag=icon,
                size=30,
                color = ColorPalette.ACCENT_PURPLE.value,
            ),
            height="3.5em",
            text_align="center",
            justify_content="center",
        ),
        href=href,
        underline="none",
    )

def logout() -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(
                tag=Icons.LOGOUT.value,
                size=30,
                color = ColorPalette.ACCENT_PURPLE.value,
            ),
            height="4em",
            text_align="center",
            justify_content="center",
        ),
        on_click=MyLocalAuthState.perform_logout,
        as_="button",
    )

def navbar() -> rx.Component:
    return rx.cond(
        MyLocalAuthState.authenticated_user_info,
        rx.hstack(
            navbar_item_mobile(Icons.HOME.value, Routes.HOME.value ),
            navbar_item_mobile(Icons.PLACES.value, Routes.PLACES.value ),
            navbar_item_mobile(Icons.SHOPPING.value, href=Routes.SHOPPING.value ),
            logout(),
            style=navbar_style
        ),
        rx.hstack(
            navbar_item_mobile(Icons.HOME.value, Routes.HOME.value ),
            style=navbar_style
        ),
    ),