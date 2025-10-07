from fastapi import FastAPI

app = FastAPI(title="Kanban TODO API")

@app.get("/")
async def root():
    return {"message": "Hello from Kanban API"}