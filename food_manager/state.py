from typing import Optional, Any, List
import asyncio
import sqlalchemy
import sqlmodel
import reflex as rx
import reflex_local_auth

from .constants import REGISTRATION_DELAY, Routes
from .models import PlacesModel, ItemsModel, PricesModel

class MyLocalAuthState(reflex_local_auth.LocalAuthState):
    @rx.var(cache=True)
    def authenticated_user_info(self) -> Optional[reflex_local_auth.LocalUser]:
        if self.authenticated_user.id < 0:
            return
        with rx.session() as session:
            return session.exec(
                sqlmodel.select(reflex_local_auth.LocalUser).where(
                    reflex_local_auth.LocalUser.id == self.authenticated_user.id
                ),
            ).one_or_none()
    
    def perform_logout(self):
        self.do_logout()
        return rx.redirect(Routes.HOME.value)

class MyRegisterState(reflex_local_auth.RegistrationState):  
    def handle_registration_custom(self, form_data: dict[str, Any]):
        """Handle registration form on_submit.

        Set error_message appropriately based on validation results.

        Args:
            form_data: A dict of form fields and values.
        """
        username = form_data["username"]
        password = form_data["password"]
        validation_errors = self._validate_fields(
            username, password, form_data["confirm_password"]
        )
        if validation_errors:
            self.new_user_id = -1
            return validation_errors
        self._register_user(username, password)
        return type(self).successful_registration_custom

    @rx.event
    async def successful_registration_custom(
        self,
    ):
        # Set success and redirect to login page after a brief delay.
        self.error_message = ""
        self.new_user_id = -1
        self.success = True
        yield
        await asyncio.sleep(REGISTRATION_DELAY)
        yield [rx.redirect(Routes.HOME.value), type(self).set_success(False)]

# Places page state
class PlacesState(MyLocalAuthState):
    places: List["PlacesModel"] = []
    place: Optional["PlacesModel"] = None
    places_length: str
    places_width: str

    @rx.var(cache=True)
    def my_place_id(self) -> str :
        return self.router.page.params.get('place_id',"")
    
    def get_place_detail(self):
        if self.my_place_id == "": 
            self.place = None
            return
        with rx.session() as session:
            result = session.exec(
                sqlmodel.select(PlacesModel).where(PlacesModel.id == self.my_place_id)
            ).one_or_none()
        self.place = result
    
    def add_place(self, form_data: dict):
        data = form_data.copy()
        if self.authenticated_user_info.id is not None:
            data["user_id"] = self.authenticated_user_info.id
        #self.form_data = data
        with rx.session() as session:
            db_entry = PlacesModel(
                **data
            )
            session.add(db_entry) # Add to the session
            session.commit() # Insert to the database
            session.refresh(db_entry)
            self.place = db_entry
        return rx.redirect(Routes.PLACES.value)
        
    def list_places(self):
        with rx.session() as session:
            places = session.exec(
                sqlmodel.select(PlacesModel).where(
                    PlacesModel.user_id == self.authenticated_user_info.id)
            ).all()
            self.places = places
        if len(self.places) > 1:
            self.places_length = "2"
            self.places_width = "100%"
        else:
            self.places_length = "1"
            self.places_width = "75%"
    
    def delete_place(self, delete_place_info: Optional["PlacesModel"]):
        with rx.session() as session:
            place = session.exec(
                sqlmodel.select(PlacesModel).where(
                    PlacesModel.id == delete_place_info.id
                )
            ).one_or_none()
            if place is not None:
                items = session.exec(
                    sqlmodel.select(ItemsModel).where(
                        ItemsModel.place_id == delete_place_info.id
                    )
                ).all()
                for item in items:
                    prices = session.exec(
                        sqlmodel.select(PricesModel).where(
                            PricesModel.item_id == item.id
                        )
                    ).all()
                    for price in prices:
                        session.delete(price)
                        session.commit()
                    session.delete(item)
                session.delete(place)
                session.commit()
        return rx.redirect(Routes.PLACES.value)

# Items page state
class ItemsState(PlacesState):
    form_data: dict = {"ItemsModel"}
    items: List["ItemsModel"] = []
    pricing_info: List["ItemsModel"] = []
    item: Optional["ItemsModel"] = None
    items_length: str
    items_width: str

    @rx.var(cache=True)
    def my_item_id(self) -> str :
        return self.router.page.params.get('item_id',"")
    
    def update_db(self, item_detail: dict):
        with rx.session() as session:
            item = session.exec(
                sqlmodel.select(ItemsModel).where(
                    ItemsModel.id == item_detail["id"]
                )
            ).one_or_none()
            if item is None:
                return
            for key, value in item_detail.items():
                setattr(item, key, value)            
            session.add(item)
            session.commit()
            session.refresh(item)
            self.item = item
    
    def add_items(self, form_data: dict):
        data = form_data.copy()
        if self.authenticated_user_info.id is not None:
            data["user_id"] = self.authenticated_user_info.id
        if data["price"] != "":
            # Replace , in price with .
            data["price"] = data["price"].replace(",", ".")
            data["has_price"] = True
        self.form_data = data
        with rx.session() as session:
            db_entry = ItemsModel(
                    **data
            )
            session.add(db_entry) # Add to the session
            session.commit() # Insert to the database
            session.refresh(db_entry)
            self.item = db_entry
        # Map values of pricing info
        if data["price"] != "" and self.authenticated_user_info.id is not None:
            price_data = {
                "user_id": self.authenticated_user_info.id,
                "item_id": self.item.id,
                "supermarket": data["supermarket"],
                "price": data["price"]
            }
            with rx.session() as session:
                prices_db_entry = PricesModel(
                    **price_data
                )
                session.add(prices_db_entry) # Add to the session
                session.commit() # Insert to the database
                session.refresh(prices_db_entry)
        return rx.redirect(f"{Routes.ITEMS.value}/{self.item.place_id}")
        
    def list_items(self):
        with rx.session() as session:
            items = session.exec(
                sqlmodel.select(ItemsModel).where(
                    (ItemsModel.user_id == self.authenticated_user_info.id) &
                    (ItemsModel.place_id == self.my_place_id)
                )
            ).all()
            self.items = items
        if len(self.items) > 1:
            self.items_length = "2"
            self.items_width = "100%"
        else:
            self.items_length = "1"
            self.items_width = "75%"

    def increment(self, item_detail: dict):
        item_detail["quantity"] += 1
        self.update_db(item_detail)
        return rx.redirect(f"{Routes.ITEMS.value}/{self.item.place_id}")

    def decrement(self, item_detail: dict):
        item_detail["quantity"] -= 1
        self.update_db(item_detail)
        return rx.redirect(f"{Routes.ITEMS.value}/{self.item.place_id}")
    
    def get_item_detail(self):
        if self.my_item_id == "": 
            self.item = None
            return
        with rx.session() as session:
            result = session.exec(
                sqlmodel.select(ItemsModel).where(ItemsModel.id == self.my_item_id)
            ).one_or_none()
        self.item = result
    
    def delete_item(self, delete_item_info: Optional["ItemsModel"]):
        with rx.session() as session:
            item = session.exec(
                sqlmodel.select(ItemsModel).where(
                    ItemsModel.id == delete_item_info.id
                )
            ).one_or_none()
            if item is not None:
                prices = session.exec(
                    sqlmodel.select(PricesModel).where(
                        PricesModel.item_id == delete_item_info.id
                    )
                ).all()
                for price in prices:
                    session.delete(price)
                    session.commit()
                session.delete(item)
                session.commit()
        return rx.redirect(f"{Routes.ITEMS.value}/{delete_item_info.place_id}")

# Prices page state
class PricesState(ItemsState):
    prices: List["PricesModel"] = []
    price: Optional["PricesModel"] = None

    def list_prices(self):
        with rx.session() as session:
            prices = session.exec(
                sqlmodel.select(PricesModel).where(
                    (PricesModel.user_id == self.authenticated_user_info.id) &
                    (PricesModel.item_id == self.my_item_id)
                )
            ).all()
            self.prices = prices
    
    def add_supermarket_prices(self, form_data: dict):
        data = form_data.copy()
        if self.authenticated_user_info.id is not None:
            data["user_id"] = self.authenticated_user_info.id
        # Replace , in price with .
        data["price"] = data["price"].replace(",", ".")
        self.form_data = data
        with rx.session() as session:
            db_entry = PricesModel(
                    **data
            )
            session.add(db_entry) # Add to the session
            session.commit() # Insert to the database
            session.refresh(db_entry)
            self.price = db_entry
        # Update item has_price to True
        with rx.session() as session:
            item = session.exec(
                sqlmodel.select(ItemsModel).where(
                    ItemsModel.id == data["item_id"]
                )
            ).one_or_none()
            if item is not None:
                item.has_price = True
                session.add(item)
                session.commit()
        return rx.redirect(f"{Routes.PRICE.value}/{data['item_id']}")
    
    def delete_price(self, delete_price_info: Optional["PricesModel"]):
        with rx.session() as session:
            price = session.exec(
                sqlmodel.select(PricesModel).where(
                    PricesModel.id == delete_price_info.id
                )
            ).one_or_none()
            if price is not None:
                session.delete(price)
                ## Update item has_price to False if there are no more prices for the item
                other_price = session.exec(
                    sqlmodel.select(PricesModel).where(
                        PricesModel.item_id == delete_price_info.item_id
                    )
                ).one_or_none()
                if other_price is None:
                    item = session.exec(
                        sqlmodel.select(ItemsModel).where(
                            ItemsModel.id == delete_price_info.item_id
                        )
                    ).one_or_none()
                    if item is not None:
                        item.has_price = False
                        session.add(item)
            session.commit()
        return rx.redirect(f"{Routes.PRICE.value}/{delete_price_info.item_id}")

# Shopping page state
class ShoppingState(MyLocalAuthState):
    shopping_items: List["ItemsModel"] = []
    shopping_list: List[dict] = []

    def get_shopping_list(self):
        with rx.session() as session:
            shopping_items = session.exec(
                sqlmodel.select(ItemsModel).where(
                    (ItemsModel.user_id == self.authenticated_user_info.id) &
                    (ItemsModel.quantity <= 1)
                )
            ).all()
            self.shopping_items = shopping_items
            self.shopping_list = [
                    {"item": shopping_items.item,
                    "color": "crimson" if shopping_items.quantity == 0 else "orange",
                    "text_decoration": "none" 
                    } for shopping_items in self.shopping_items 
                ]
    
    def item_bought(self, shopping_list_item: dict):
        for shopping_item in self.shopping_list:
            if shopping_item["item"] == shopping_list_item["item"]:
                if shopping_item["text_decoration"] == "none":
                    shopping_item["text_decoration"] = "line-through"
                else:
                    shopping_item["text_decoration"] = "none"