from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def get_root():
    return {
        "message": "Place holder application root"
    }

