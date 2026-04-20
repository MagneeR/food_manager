# Definition of:
# 1. The color palette used in the application
# 2. The different styles used in the application globally and for each component
import reflex as rx
from enum import Enum

## Color Palette
class ColorPalette(Enum):
    BACKGROUND_BLUE ="#1483AB"
    BACKGROUND_GREEN ="#2B8089"
    ACCENT_BLUE ="#7CB6FF"
    ACCENT_PURPLE ="#829DFF"
    ACCENT_ORANGE ="#FEB53D"
    LIGHT_BLUE ="#D5DCFE"

## Sizes for spacing and text
class Size(Enum):
    XSMALL = "0.15em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "1.5em"
    LARGE = "2em"
    XLARGE = "6em"

## Font Family and Weight
class FontFamily(Enum):
    HEADER = "Abril Fatface, serif"
    BODY = "Poppins-Medium, sans-serif"
    FOOTER = "Comfortaa-Medium, sans-serif"

class FontWeight(Enum):
    LIGHT = "300"
    REGULAR = "400"
    MEDIUM = "500"
    BOLD = "700"

## Base style
BASE_STYLE = {
    rx.box: {
        "background_color": ColorPalette.BACKGROUND_BLUE.value,
    },
    rx.heading: {
        "color": ColorPalette.ACCENT_BLUE.value,
        "font_family": FontFamily.HEADER.value,
        "text_align": "center",
    },
    rx.text: { 
        "color": ColorPalette.LIGHT_BLUE.value,
    },
    rx.segmented_control.root : {
        "position":"fixed",
        "right":"0",
        "top":"0",
    },
    rx.link: {
        "color": ColorPalette.LIGHT_BLUE.value,
        "text_decoration": "none",
        "_hover": {
            "color": ColorPalette.LIGHT_BLUE.value,
        },
        "font_family": FontFamily.BODY.value,
        "font_weight": FontWeight.LIGHT.value,
    },
    rx.grid: {
        "padding_top": "32px",
        "padding_bottom": "16px",
    },
}

## Vstack styles
vstack_pages_style = dict(
    spacing="5",
    justify="center",
    padding="48px 16px 16px 16px",
    align_items="center",
)

vstack_shopping_style = dict(
    spacing="5",
    justify="center",
    padding="16px",
    align_items="center",
    width="100%",
    min_height="50vh",
    background_image=f"url({rx.asset('shopping_paper.png')})",
    background_size="auto",
    background_repeat="round",    
)

## Navbar styles
navbar_style = dict(
    background_color = ColorPalette.ACCENT_ORANGE.value,
    width = "100%",
    position = "fixed",
    bottom = "0",
    z_index = "999",
    justify_content = "space-evenly",
    padding_top = "12px",
    padding_left = "16px",
)

## Footer styles
vstack_footer_style_top = dict(
    width="100%",
    text_align="center",
    align_items="center",
    justify_content="center",
    min_height="auto",
    spacing="2"
)

vstack_footer_style_bottom = dict(
    width="100%",
    text_align="center",
    align_items="center",
    justify_content="center",
    min_height="auto",
    margin_bottom="30em",
    spacing="2"
)

footer_text_style_top = dict(
    font_family= FontFamily.FOOTER.value,
)

footer_text_style_bottom = dict(
    font_family= FontFamily.FOOTER.value,
    font_size=Size.MEDIUM.value
)

## Index styles
index_vstack_style = dict(
    spacing="2",
    justify="center",
    padding="48px 16px 16px 16px",
    align_items="center",
)

index_card_style=dict(
    height= "100%",
    padding= Size.SMALL.value,
    border_radius= Size.DEFAULT.value,
    background_color= ColorPalette.ACCENT_ORANGE.value,
    border= f"{Size.XSMALL.value} solid",
    border_color = ColorPalette.ACCENT_PURPLE.value,
    white_space= "normal",
    text_align= "center",
    style={
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": ColorPalette.ACCENT_BLUE.value,
        }
    }
)

## Auth style
form_card_style=dict(
    justify_content="center",
    width="100%",
    background_color= ColorPalette.LIGHT_BLUE.value,
    font_family= FontFamily.FOOTER.value,
)

auth_form_button=dict(
    height= "100%",
    padding= Size.SMALL.value,
    border_radius= Size.DEFAULT.value,
    color = ColorPalette.LIGHT_BLUE.value,
    background_color = ColorPalette.BACKGROUND_GREEN.value,
    border= f"{Size.XSMALL.value} solid",
    border_color = ColorPalette.LIGHT_BLUE.value,
    white_space= "normal",
    text_align= "start",
    font_family= FontFamily.BODY.value,
    font_weight= FontWeight.MEDIUM.value,
    style={
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": ColorPalette.ACCENT_BLUE.value,
        }
    }
)

## Button styles
base_button=dict(
    height= "100%",
    padding= Size.SMALL.value,
    border_radius= Size.DEFAULT.value,
    color = ColorPalette.LIGHT_BLUE.value,
    background_color = ColorPalette.ACCENT_BLUE.value,
    border= f"{Size.XSMALL.value} solid",
    border_color = ColorPalette.BACKGROUND_GREEN.value,
    white_space= "normal",
    text_align= "start",
    font_family= FontFamily.BODY.value,
    font_weight= FontWeight.MEDIUM.value,
    style={
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": ColorPalette.ACCENT_BLUE.value,
        }
    }
)

outline_buttons=dict(
    height= "100%",
    padding= Size.SMALL.value,
    border_radius= Size.DEFAULT.value,
    color = ColorPalette.LIGHT_BLUE.value,
    background_color= "unset",
    border= f"{Size.XSMALL.value} solid",
    border_color = ColorPalette.BACKGROUND_GREEN.value,
    white_space= "normal",
    text_align= "center",
    style={
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": ColorPalette.ACCENT_BLUE.value,
        }
    }
)

add_button_style=dict(
    height= Size.LARGE.value,
    padding_left = "0.85em",
    padding_right = "0.85em",
    padding_top = "0em",
    padding_bottom = "0em",
    border_radius= "4px",
    color = ColorPalette.LIGHT_BLUE.value,
    background_color = ColorPalette.ACCENT_BLUE.value,
    border= f"{Size.XSMALL.value} solid",
    border_color = ColorPalette.BACKGROUND_GREEN.value,
    white_space= "normal",
    text_align= "start",
    style={
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": ColorPalette.ACCENT_BLUE.value,
        }
    }
)

## Card styles
common_card_style=dict(
    height= "100%",
    padding= Size.SMALL.value,
    border_radius= Size.DEFAULT.value,
    color = ColorPalette.LIGHT_BLUE.value,
    background_color= ColorPalette.BACKGROUND_GREEN.value,
    border= f"{Size.XSMALL.value} solid",
    border_color = ColorPalette.ACCENT_BLUE.value,
    white_space= "normal",
    text_align= "center",
    style={
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": ColorPalette.ACCENT_BLUE.value,
        }
    }
)

## Modal styles
modal_button=dict(
    height= "100%",
    padding= Size.SMALL.value,
    border_radius= Size.DEFAULT.value,
    color = ColorPalette.ACCENT_PURPLE.value,
    background_color = ColorPalette.ACCENT_ORANGE.value,
    border= f"{Size.XSMALL.value} solid",
    border_color = ColorPalette.ACCENT_ORANGE.value,
    white_space= "normal",
    text_align= "start",
    font_family= FontFamily.BODY.value,
    font_weight= FontWeight.MEDIUM.value,
    style={
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": ColorPalette.ACCENT_BLUE.value,
        }
    }
)

modal_title_style=dict(
    color= ColorPalette.ACCENT_ORANGE.value,
    font_family= FontFamily.HEADER.value,
    font_weight= FontWeight.BOLD.value,
)

modal_background_style=dict(
    background_color= ColorPalette.ACCENT_PURPLE.value
)

modal_close_button_style=dict(
    background_color= ColorPalette.ACCENT_ORANGE.value,
    color= ColorPalette.ACCENT_PURPLE.value
)