# Footer component to include in the template
import reflex as rx

from ..constants import APP_NAME, Icons, URLs, Brand
from ..style import ( 
    vstack_footer_style_top,
    vstack_footer_style_bottom,
    footer_text_style_top,
    footer_text_style_bottom,
    FontFamily,
    FontWeight,
    ColorPalette,
    Size
)

def social_link(
    icon: str,
    text: str,
    href: str,
    text_size: str = "16px"
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text.strong(
                text,
                style={"font_family": FontFamily.FOOTER.value,
                       "font_size": text_size}
            ),
            text_align="center",
            justify_content="center",
        ),
        href=href,
        is_external=True,
    )

def footer() -> rx.Component:
    desktop_child = rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(f"© {APP_NAME} 2024"),
                social_link(Icons.GITHUB.value, "Designed by MagneeR", URLs.GITHUB.value),
                style=vstack_footer_style_top,
            ),
            rx.vstack(
                rx.text("¿Quieres ideas para recetas? Puedes visitar nuestro perfil de Instagram:"),
                social_link(Icons.INSTAGRAM.value, Brand.IG_NAME.value, URLs.INSTAGRAM.value),
                style=vstack_footer_style_top,
            ),
        )
    )

    mobile_child = rx.box(
        rx.vstack(
            rx.vstack(
                rx.text(
                    "¿Quieres ideas para recetas?",
                    style=footer_text_style_top
                ),
                rx.text(
                    "Puedes visitar nuestro perfil de Instagram:",
                    style=footer_text_style_top
                ),
                social_link(Icons.INSTAGRAM.value, Brand.IG_NAME.value, URLs.INSTAGRAM.value),
                style=vstack_footer_style_top,
                spacing="1"
            ),
            rx.vstack(
                rx.text(
                    f"© {APP_NAME} 2024",
                    style=footer_text_style_bottom
                ),
                social_link(Icons.GITHUB.value, "Designed by MagneeR", URLs.GITHUB.value, Size.MEDIUM.value),
                style=vstack_footer_style_bottom,
                spacing="1"
            ),
            spacing="1"
        )
    )
    return rx.box(
        rx.desktop_only(desktop_child),
        rx.mobile_and_tablet(mobile_child),
    )