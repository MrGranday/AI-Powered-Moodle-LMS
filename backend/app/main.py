from fastapi import FastAPI
from app.auth import routes as auth_routes
from app.users import routes as user_routes

app = FastAPI(
    title="AI-Enhanced Learning Management Platform",
    description="A lightweight AI-powered LMS prototype.",
    version="0.1.0",
)

app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])


@app.get("/")
async def root():
    return {"message": "Welcome to the AI-Enhanced Learning Management Platform API"}
