import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/")
def index():
    return "Test"

uvicorn.run(app)