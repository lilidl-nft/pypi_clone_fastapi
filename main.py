import fastapi
import fastapi_chameleon
from fastapi_chameleon import template
import uvicorn

app = fastapi.FastAPI()

fastapi_chameleon.global_init("C:\Users\licdi\Desktop\Python\pypi_clone_fastapi\pypi_clone_fastapi\templates")

@app.get("/")
@template(template_file="index.html")

def index():
    return {
        
        "user_name": "Lili" 
        
        }






if __name__ == "__main__":
    uvicorn.run(app)