from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from tortoise.contrib.fastapi import register_tortoise

from app.routers import user, scrape, root
# from app.utils.config import database_url


# from app.services.recording_scheduler import record


def create_app():  # App creation
    app = FastAPI(
        title="perfect-price API",
        description="Documentation of perfect-price API",
    )

    # CORS handling
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Adding API routers

    # / routes
    app.include_router(
        root.router,
        tags=["root"],
    )

    # /user routes
    app.include_router(
        user.router,
        prefix="/user",
        tags=["user"],
    )

    app.include_router(
        scrape.router,
        prefix="/scrape",
        tags=["scrape"]
    )

    # # Database Registration
    # register_tortoise(
    #     app,
    #     db_url=database_url,
    #     modules={'models': ['app.database.models']},
    #     generate_schemas=True,
    #     add_exception_handlers=True
    # )

    return app
