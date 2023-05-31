import fastapi
from fastapi_chameleon import template
import fastapi_chameleon
import uvicorn

router = fastapi.APIRouter()

@router.get("/")
@template(template_file="index.html")

def index(user: str = "anon"):
    return {
        
        "user_name": "Lili" 
        
    }
    
@router.get("/about")
def about():
    return{}
