# Places page
import reflex as rx
from typing import List

from ..state import ItemsState, PlacesState
from ..models import ItemsModel

from ..template import base_page
from ..constants import Pages, Routes
from ..components.modals import item_modal, no_price_modal
from ..style import add_button_style, common_card_style, vstack_pages_style, modal_button

def item_card(item_entry: ItemsModel) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.text(
                    item_entry.item,
                    size="5"
                ),
                rx.icon(
                    "trash-2",
                    _as="button",
                    on_click=ItemsState.delete_item(item_entry),
                ),
                align_items="inherit",
            ),
            rx.cond(
                item_entry.has_price,
                rx.link(
                    "Ver precios",
                    size="2",
                    href=f"{Routes.PRICE.value}/{item_entry.id}",
                    style=modal_button,
                ),
                no_price_modal(item_entry.id)
            ),
            rx.hstack(
                rx.button(
                    "-",
                    on_click=ItemsState.decrement(item_entry),
                    style=add_button_style
                ),
                rx.text(
                    item_entry.quantity,
                    size="3"
                ),
                rx.button(
                    "+",
                    on_click=ItemsState.increment(item_entry),
                    style=add_button_style
                ),
                spacing="2",
                width="100%",
                align_items="center",
                justify_content="space-evenly"
            ),
            align_items="center",
        ),
        style=common_card_style,
    )

def item_grid() -> rx.Component:
    return rx.grid(
        rx.foreach(
            ItemsState.items,
            item_card
        ),
        columns=ItemsState.items_length,
        width=ItemsState.items_width,
        spacing="2",
    )

@rx.page(
    route=f"{Routes.ITEMS.value}/[place_id]",
    title=Pages.ITEMS.value,
    on_load=[PlacesState.get_place_detail, ItemsState.list_items]
)
@base_page
def items() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                f"COMIDA EN {PlacesState.place.place}",
                size="9",
                width="100%",
            ),
            item_grid(),
            item_modal(),
            style=vstack_pages_style
        ),
        id="items-page",
    )