from decouple import config
import reflex as rx

DATABASE_URL = config("DATABASE_URL")
# In cors_allowed_origins, add the URL of frontend application
config = rx.Config(
    app_name="food_manager",
    #cors_allowed_origins=[
    #    "http://localhost:3000",
    #],
    db_url=DATABASE_URL,
    plugins=[
        rx.plugins.SitemapPlugin()
    ],
    tailwind=None,
    show_built_with_reflex=False
)