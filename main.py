import fastapi
import fastapi_chameleon
import uvicorn

from views import home
from views import account
from views import packages

app = fastapi.FastAPI()

fastapi_chameleon.global_init(r"C:\Users\licdi\Desktop\Python\pypi_clone_fastapi\templates")

app.include_router(home.router)
app.include_router(account.router)
app.include_router(packages.router)



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)