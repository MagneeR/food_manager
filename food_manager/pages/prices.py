# Prices page
import reflex as rx
from rxconfig import config

from ..template import base_page
from ..constants import Pages, Routes
from ..state import ItemsState, PricesState
from ..components.modals import supermarket_modal
from ..style import ColorPalette, vstack_pages_style

def accordion_item(price_entry) -> rx.Component:
    return rx.accordion.item(
        header=price_entry.supermarket, 
        content=rx.hstack(
            price_entry.price,
            rx.icon("trash-2", _as="button", on_click=PricesState.delete_price(price_entry)),
        ),
        background_color= ColorPalette.BACKGROUND_GREEN.value,
    )

@rx.page(
    route=f"{Routes.PRICE.value}/[item_id]",
    title=Pages.PRICE_LOWER.value,
    on_load=[ItemsState.get_item_detail, PricesState.list_prices],
)
@base_page
def prices() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                f"Precios de {ItemsState.item.item.upper()}",
                size="8"
            ),
            rx.accordion.root(
                rx.foreach(
                    PricesState.prices,
                    accordion_item
                ),
                collapsible=True,
                width="300px",
                type="multiple",
                color_scheme="jade",
                margin_top="32px",
                margin_bottom="16px",
            ),
            supermarket_modal(),
            style=vstack_pages_style
        ),
        id="prices-page",
    )