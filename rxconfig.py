#from decouple import config
import os
from dotenv import load_dotenv
import reflex as rx

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
# In cors_allowed_origins, add the URL of frontend application
config = rx.Config(
    app_name="food_manager",
    #cors_allowed_origins=[
    #    "http://localhost:3000",
    #],
    api_url="https://foodmanager.up.railway.app:8000",
    db_url=DATABASE_URL,
    plugins=[
        rx.plugins.SitemapPlugin()
    ],
    tailwind=None,
    show_built_with_reflex=False
)