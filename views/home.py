import fastapi
from fastapi_chameleon import template
import fastapi_chameleon
import uvicorn

router = fastapi.APIRouter()

@router.get("/")
@template(template_file="home/index.pt")

def index(user: str = "anon"):
    return {
        
        "user_name": "Lili" 
        
    }
    
@router.get("/about")
@template()
def about():
    return{}
