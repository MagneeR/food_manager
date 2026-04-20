# File to create the base template for all the pages in the app.
from typing import Callable

import reflex as rx

from .components.footer import footer
from .components.navbar import navbar

# Use @base_page decorator to call the base_page function
def base_page(
    page: Callable[[], rx.Component]
) -> rx.Component:
    return rx.box(
        page(),
        footer(),
        navbar(),
        min_height="100dvh",
        id="base-page",
    )