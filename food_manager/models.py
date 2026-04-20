# File to create the different models of the app.
import reflex as rx

from sqlmodel import Field, Relationship
from typing import Optional, List
from reflex_local_auth.user import LocalUser

class PlacesModel(rx.Model, table=True):
    user_id: int = Field(foreign_key="localuser.id")
    place: str

class ItemsModel(rx.Model, table=True):
    user_id: int = Field(foreign_key="localuser.id")
    place_id: int = Field(default=None, foreign_key="placesmodel.id")
    item: str
    quantity: int
    has_price: bool = Field(default=False)

class PricesModel(rx.Model, table=True):
    user_id: int = Field(foreign_key="localuser.id")
    item_id: int = Field(default=None, foreign_key="itemsmodel.id")
    supermarket: str | None
    price: float | None