import reflex as rx
import reflex_local_auth
from food_manager.state import MyRegisterState

from ..template import base_page
from ..constants import Routes, DO_REGISTER
from ..components.auth import register_form, register_success
from ..style import vstack_pages_style

@rx.page(
    route=Routes.REGISTER.value,
    title=DO_REGISTER,
)
@base_page
def register() -> rx.Component:
    return rx.box(
        rx.vstack(
            #rx.heading(DO_REGISTER, size="9"),
            rx.cond(
                reflex_local_auth.RegistrationState.success,
                register_success(),
                register_form(),
            ),
            style=vstack_pages_style
        ),
        id="register-page",
    )

