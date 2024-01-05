from fastapi import FastAPI
from sqlmodel import SQLModel
SQLModel.mysqlurl = "mysql+pymysql://root:1230@localhost/database1"
import usermodule
# from usermodule import router


app = FastAPI()



app.include_router(usermodule.router, prefix="/api")
