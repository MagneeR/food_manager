# Constants file
from enum import Enum

# Constants
APP_NAME = 'FOOD MANAGER'
DO_LOGIN = 'Iniciar sesión'
DO_LOGOUT = 'Cerrar sesión'
DO_REGISTER = 'Regístrate'
REGISTRATION_DELAY = 1.5

# Brand
class Brand(Enum):
    IG_NAME = "@flavourstoremember"
    NAME = "Flavours to remember"

# Routes
class Routes(Enum):
    HOME = '/'
    # User authentication
    LOGOUT = '/logout'
    REGISTER = '/register'
    # Pages
    PLACES = '/places'
    ITEMS = '/items'
    CONTACT = '/contact'
    SHOPPING = '/shopping'
    PRICE = '/prices'
    SUPERMARKET = '/supermarket'
    HELP = '/help'

# Pages names
class Pages(Enum):
    HOME = 'Inicio'
    LOGOUT = 'Cerrar sesion'
    PLACES_LOWER = 'Lugares'
    PLACES_UPPER = 'LUGARES'
    ITEMS = 'Comida'
    CONTACT = 'Contacto'
    SHOPPING = 'Compra'
    PRICE_LOWER = 'Precios'
    PRICE_UPPER = 'PRECIOS'
    SUPERMARKET = 'Precios/Supermercado'
    HELP = '¿Cómo funciona?'  

# URLs
class URLs(Enum):
    INSTAGRAM = 'https://www.instagram.com/flavourstoremember/'
    GITHUB = 'https://github.com/magneer'

# Icons
class Icons(Enum):
    INSTAGRAM = "instagram"
    GITHUB = "github"
    HOME = "home"
    PLACES = "refrigerator"
    SHOPPING = "shopping-cart"
    HELP = "circle-help"
    LOGOUT = "log-out"