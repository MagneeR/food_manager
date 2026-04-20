import reflex as rx
from reflex_local_auth import LoginState

from ..constants import DO_LOGIN, DO_REGISTER
from ..style import form_card_style, auth_form_button, ColorPalette
from ..state import MyRegisterState

def input_width(name, placeholder, **props ) -> rx.Component:
    """Render a 100% width input."""
    return rx.input(
        name=name,
        placeholder=placeholder,
        width="100%",
        **props,
    )

def login_error() -> rx.Component:
    """Render the login error message."""
    return rx.cond(
        LoginState.error_message != "",
        rx.callout(
            LoginState.error_message,
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            width="100%",
        ),
    )

def register_error() -> rx.Component:
    """Render the registration error message."""
    return rx.cond(
        MyRegisterState.error_message != "",
        rx.callout(
            MyRegisterState.error_message,
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            width="100%",
        ),
    )

def register_success() -> rx.Component:
    return rx.callout(
        "Registration successful! Please log in.",
        icon="circle_check",
        color_scheme="green",
        role="alert",
        width="100%",
    ),


def login_form() -> rx.Component:
    """Render the login form."""
    return rx.card(      
        rx.form(
            rx.vstack(
                rx.heading(
                    DO_LOGIN,
                    size="7",
                    align="center",
                    color=ColorPalette.BACKGROUND_GREEN.value,
                ),
                login_error(),
                input_width("username", "Nombre de usuario"),
                input_width("password", "Contraseña", type="password"),
                rx.button(DO_LOGIN, width="100%", style=auth_form_button),
            ),
            on_submit=LoginState.on_submit,
        ),
        style=form_card_style
    )

def register_form() -> rx.Component:
    """Render the register form."""
    return rx.card(      
        rx.form(
            rx.vstack(
                rx.heading(
                    DO_REGISTER,
                    size="8",
                    align="center",
                ),
                register_error(),
                input_width("username", "Nombre de usuario"),
                input_width("password", "Contraseña", type="password"),
                input_width("confirm_password", "Confirmar contraseña", type="password"),
                rx.button(DO_REGISTER, width="100%", style=auth_form_button),
            ),
            on_submit=MyRegisterState.handle_registration_custom,
        ),
        style=form_card_style
    )