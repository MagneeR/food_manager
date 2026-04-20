# Modal components for specific pages
import reflex as rx

from ..style import (
    modal_button,
    modal_title_style,
    modal_background_style,
    modal_close_button_style,
)
from ..state import PlacesState, ItemsState, PricesState

def place_modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.box(
                rx.button(
                    "Añadir lugar",
                    style=modal_button
                    )
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Añade un nuevo lugar",
                style=modal_title_style
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        name="place",
                        placeholder="Nombre del lugar",
                        required=True,
                        margin_bottom="16px"
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Añadir",
                                size="3",
                                type="submit",
                                style=modal_close_button_style
                            ),
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                size="3",
                                style=modal_close_button_style
                            ),
                        ),
                        spacing="2",
                    ),
                    direction="column",
                    spacing="3",
                ),
                on_submit=PlacesState.add_place,
                reset_on_submit=False,
            ),
            style=modal_background_style
        ),
    )

def item_modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.box(
                rx.button(
                    "Añadir comida",
                    style=modal_button
                )
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Añade nueva comida",
                style=modal_title_style
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        type="hidden",
                        name="place_id",
                        value=PlacesState.place.id,
                        display="none",
                    ),
                    rx.input(
                        name="item",
                        placeholder="Nombre de la comida",
                        required=True,
                    ),
                    rx.input(
                        name="quantity",
                        placeholder="Cantidad",
                        required=True,
                    ),
                    rx.input(
                        name="supermarket",
                        placeholder="Supermercado",
                        required=False,
                    ),
                    rx.input(
                        name="price",
                        placeholder="Precio",
                        required=False,
                        type="number",
                        step="0.01",
                        margin_bottom="16px"
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Añadir",
                                size="3",
                                type="submit",
                                style=modal_close_button_style
                            ),
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                size="3",
                                style=modal_close_button_style
                            ),
                        ),
                        spacing="2",
                    ),
                    direction="column",
                    spacing="2",
                ),
                on_submit=ItemsState.add_items,
                reset_on_submit=False,
            ),
            style=modal_background_style
        ),
    )

def supermarket_modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.box(
                rx.button(
                    "Añadir precios de supermercado",
                    style=modal_button
                )
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Añade nuevo precio de supermercado",
                style=modal_title_style
            ),
            rx.form(
                rx.flex(
                    rx.box(
                        rx.input(
                            type="hidden",
                            name="item_id",
                            value=PricesState.my_item_id,
                        ),
                        display="none",
                    ),
                    rx.input(
                        name="supermarket",
                        placeholder="Supermercado",
                        required=True,
                    ),
                    rx.input(
                        name="price",
                        placeholder="Precio",
                        required=True,
                        margin_bottom="16px"
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.box(
                                rx.button(
                                    "Añadir",
                                    size="3",
                                    type="submit",
                                    style=modal_close_button_style
                                )
                            ),
                        ),
                        rx.dialog.close(
                            rx.box(
                                rx.button(
                                    "Cancelar",
                                    size="3",
                                    style=modal_close_button_style
                                ),
                            ),
                        ),
                        spacing="2",
                    ),
                    direction="column",
                    spacing="2",
                ),
                on_submit=PricesState.add_supermarket_prices,
                reset_on_submit=False
            ),
            style=modal_background_style
        ),
    )

def no_price_modal(item_id: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.box(
                rx.button(
                    "Sin precio",
                    style=modal_button
                )
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Añade nuevo precio de supermercado",
                style=modal_title_style
            ),
            rx.form(
                rx.flex(
                    rx.box(
                        rx.input(
                            type="hidden",
                            name="item_id",
                            value=item_id,
                        ),
                        display="none",
                    ),
                    rx.input(
                        name="supermarket",
                        placeholder="Supermercado",
                        required=True,
                    ),
                    rx.input(
                        name="price",
                        placeholder="Precio",
                        required=True,
                        margin_bottom="16px"
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.box(
                                rx.button(
                                    "Añadir",
                                    size="3",
                                    type="submit",
                                    style=modal_close_button_style
                                )
                            ),
                        ),
                        rx.dialog.close(
                            rx.box(
                                rx.button(
                                    "Cancelar",
                                    size="3",
                                    style=modal_close_button_style
                                ),
                            ),
                        ),
                        spacing="2",
                    ),
                    direction="column",
                    spacing="2",
                ),
                on_submit=PricesState.add_supermarket_prices,
                reset_on_submit=False
            ),
            style=modal_background_style
        ),
    )