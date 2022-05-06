from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from routes import auth ,matatu, user
from auth import google_auth


app = FastAPI(title="Matatu Shifter Backend")

origins = ["*"]


app.add_middleware(SessionMiddleware, secret_key="secret")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/static', StaticFiles(directory="../frontend/build", html = True), name = "frontend")

app.include_router(google_auth.router)
app.include_router(auth.router)
app.include_router(matatu.router)
app.include_router(user.router)






















