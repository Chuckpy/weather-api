from fastapi import FastAPI
from weather.routes import weather_router
from fastapi.middleware.cors import CORSMiddleware
from db import models
from db.session import engine




def get_application()-> FastAPI:
    '''This method should give all main application properly configured'''

    main_app = FastAPI()

    models.Base.metadata.create_all(bind=engine)

    # including new routes to main app
    main_app.include_router(weather_router)
    #CORS Middleware
    main_app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    return main_app

app = get_application()
