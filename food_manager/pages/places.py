# Places page
import reflex as rx
from typing import List

from food_manager.models import PlacesModel

from ..template import base_page
from ..constants import Pages, Routes
from ..components.modals import place_modal
from ..style import common_card_style, vstack_pages_style
from ..state import PlacesState

def place_card(place_entry : PlacesModel) -> rx.Component:
    return rx.card(
        rx.link(
            rx.text(place_entry.place, size="5"),
            href=f"{Routes.ITEMS.value}/{place_entry.id}",
        ),
        rx.hstack(
            rx.icon(
                "trash-2",
                _as="button",
                on_click=PlacesState.delete_place(place_entry)
            ),
            justify_content="flex-end",
        ),
        style=common_card_style
    )

def place_grid() -> rx.Component:
    return rx.grid(
        rx.foreach(
            PlacesState.places,
            place_card
        ),
        columns=PlacesState.places_length,
        width=PlacesState.places_width,
        spacing="2",
    )

@rx.page(
    route=Routes.PLACES.value,
    title=Pages.PLACES_LOWER.value,
    on_load=PlacesState.list_places
)
@base_page
def places() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(Pages.PLACES_UPPER.value, size="9"),
            place_grid(),
            place_modal(),
            style=vstack_pages_style
        ),
        id="places-page",
    )