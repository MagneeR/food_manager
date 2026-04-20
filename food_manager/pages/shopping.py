# Shopping page
import reflex as rx
from rxconfig import config

from ..template import base_page
from ..constants import Pages, Routes
from ..state import ShoppingState
from ..style import vstack_pages_style, vstack_shopping_style

def shopping_items(shopping_list) -> rx.Component:
    return rx.list_item(
        rx.checkbox(
            rx.text(
               shopping_list["item"],
               color = shopping_list["color"],
               size="5",
               text_decoration=shopping_list["text_decoration"],
            ),
            size="3",
            on_change=ShoppingState.item_bought(shopping_list),
        ),
    )

@rx.page(
    route=Routes.SHOPPING.value,
    title=Pages.SHOPPING.value,
    on_load=ShoppingState.get_shopping_list,
)
@base_page
def shopping() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Lista de la compra", size="9"),
            rx.vstack(
                rx.list(
                    rx.foreach(
                        ShoppingState.shopping_list,
                        shopping_items
                    ),
                ),
                style=vstack_shopping_style,
            ),
            style=vstack_pages_style,
        ),
        id="shopping-page",
    )

"""
New idea for shopping list
When clicking on the button that creates get_item, the item dissapears using the method finish_item
from typing import List


class ListState(rx.State):
    items: List[str] = ["Write Code", "Sleep", "Have Fun"]
    new_item: str

    @rx.event
    def set_new_item(self, new_item: str):
        self.new_item = new_item

    @rx.event
    def add_item(self):
        self.items += [self.new_item]

    def finish_item(self, item: str):
        self.items = [i for i in self.items if i != item]


def get_item(item):
    return rx.list.item(
        rx.hstack(
            rx.button(
                on_click=lambda: ListState.finish_item(item),
                height="1.5em",
                background_color="white",
                border="1px solid blue",
            ),
            rx.text(item, font_size="1.25em"),
        ),
    )


def todo_example():
    return rx.vstack(
        rx.heading("Todos"),
        rx.input(
            on_blur=ListState.set_new_item, placeholder="Add a todo...", bg="white"
        ),
        rx.button("Add", on_click=ListState.add_item, bg="white"),
        rx.divider(),
        rx.list.ordered(
            rx.foreach(
                ListState.items,
                get_item,
            ),
        ),
        bg="#ededed",
        padding="1em",
        border_radius="0.5em",
        shadow="lg",
    )
"""