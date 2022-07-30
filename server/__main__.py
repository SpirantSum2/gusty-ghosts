import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Main page of our server, this is not a web-based applications, so should just show some information on usage"""
    return {"message": "This is a server for picphone app (Python Discord Summer Code Jam 2022)"}


if __name__ == '__main__':
    uvicorn.run("__main__:app", host="0.0.0.0", port=5000)
