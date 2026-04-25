from fastapi import FastAPI
from router import router

app = FastAPI(title="Timezone Converter API", version="1.0.0")
app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Добро пожаловать в Timezone Converter API",
        "docs": "/docs",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)