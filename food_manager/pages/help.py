# Help page
import reflex as rx
from rxconfig import config

from ..template import base_page
from ..constants import Pages, Routes
from ..components.carrousel import ImageCarroussel, ImageCarrousselState
from ..style import vstack_pages_style

@rx.page(
    route=Routes.HELP.value,
    title=Pages.HELP.value,
    on_load=ImageCarrousselState.create
)
@base_page
def help() -> rx.Component:
    return rx.box(
        rx.vstack(
            ImageCarroussel(),
            style=vstack_pages_style
        ),
        id="help-page",
    )